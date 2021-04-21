from PyQt5 import QtCore, QtGui, QtWidgets

class CollapsibleBox(QtWidgets.QWidget):
    def __init__(self, title="", parent=None):
        parent:CollapsibleBox
        self.parent:CollapsibleBox
        super(CollapsibleBox, self).__init__()
        self.parent=parent
        self.title=title
        self.toggle_button = QtWidgets.QToolButton(
            text=title, checkable=True, checked=False
        )
        self.toggle_button.setStyleSheet("QToolButton { border: None; }")
        #self.toggle_button.setStyleSheet("background-color: rgb(255, 200, 200);")
        self.toggle_button.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon
        )
        self.toggle_button.setMaximumWidth(100000)
        self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)

        self.toggle_animation = QtCore.QParallelAnimationGroup(self)

        self.content_area = QtWidgets.QScrollArea(
            maximumHeight=0, minimumHeight=0
        )
        self.content_area.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        self.content_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content_area.setLayout(QtWidgets.QVBoxLayout())
        self.content_area.setStyleSheet("background-color: rgb(200, 200, 255);")
        self.content_area.layout().addStretch(255)
        self.content_area.setContentsMargins(0, 0, 0, 0)
        self.content_height=self.content_area.layout().spacing()*2

        lay = QtWidgets.QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.toggle_button)
        lay.addWidget(self.content_area) 

        self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self, b"minimumHeight"))
        self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self, b"maximumHeight"))
        self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self.content_area, b"maximumHeight"))

        self.collapsed_height=self.sizeHint().height() - self.content_area.maximumHeight()
        self.isOpen = False

        if type(parent) is CollapsibleBox:
            self.parent.addWidget(self)
            self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self.parent, b"minimumHeight"))
            self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self.parent, b"maximumHeight"))
            self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self.parent.content_area, b"maximumHeight"))
            self.toggle_animation.finished.connect(self.toggle_animation_finished)
    
    def toggle_animation_finished(self):
        self.parent.updateAnimation()

    @QtCore.pyqtSlot()
    def on_pressed(self):
        self.isOpen= not(self.isOpen)
        
        self.toggle_button.setArrowType(
            QtCore.Qt.DownArrow if self.isOpen else QtCore.Qt.RightArrow
        )
        
        self.toggle_animation.setDirection(
            QtCore.QAbstractAnimation.Forward
            if self.isOpen
            else QtCore.QAbstractAnimation.Backward
        )
        
        if type(self.parent) is CollapsibleBox: 
            if not(self.isOpen) : self.parent.content_height = self.parent.content_height - self.content_height 
            self.updateAnimation()
            if (self.isOpen) : self.parent.content_height = self.parent.content_height + self.content_height
        
        
        if self.content_area.layout().count()>0: self.toggle_animation.start()

    def setContentLayout(self, layout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)
        self.collapsed_height = (
            self.sizeHint().height() - self.content_area.maximumHeight()
        )
        self.content_height = self.content_area.layout().sizeHint().height()
        self.updateAnimation()

    def updateAnimation(self,startValue=0,EndValue=None):
        if EndValue is None: EndValue=self.content_height
        dur=150
        for i in range(0,2):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(dur)
            animation.setStartValue(self.collapsed_height+startValue)
            animation.setEndValue(self.collapsed_height + EndValue)
        
        content_animation = self.toggle_animation.animationAt(2)
        content_animation.setDuration(dur)
        content_animation.setStartValue(startValue)
        content_animation.setEndValue(EndValue)

        if not(type(self.parent) is CollapsibleBox): return
            
        for i in range(3,5):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(dur)
            animation.setStartValue(self.parent.content_height+self.parent.collapsed_height)
            animation.setEndValue(self.parent.content_height+self.parent.collapsed_height+EndValue)
        
        content_animation = self.toggle_animation.animationAt(5)
        content_animation.setDuration(dur)
        content_animation.setStartValue(self.parent.content_height)
        content_animation.setEndValue(self.parent.content_height+EndValue)
        

    def addWidget(self,widget:QtWidgets.QWidget):
        lay=self.content_area.layout()
        lay.insertWidget(lay.count()-1,widget)
        self.updateHeight(widget)

    def height(self):
        if self.isOpen: return self.collapsed_height+self.content_height
        else: return self.collapsed_height
    
    def updateHeight(self,widget:QtWidgets.QWidget, Forward=True):
        if type(self.parent) is CollapsibleBox and self.parent.isOpen:
            self.parent.updateHeight(widget,Forward)
        
        if type(widget) is CollapsibleBox: i = widget.height()
        else: i=widget.sizeHint().height()
        if Forward: direction = 1
        else: direction=-1

        self.content_height+=direction*(i+self.content_area.layout().spacing())
        self.updateAnimation()
        if self.isOpen:
            self.setMaximumHeight(self.content_height+self.collapsed_height)
            self.setMinimumHeight(self.content_height+self.collapsed_height)
            self.content_area.setMaximumHeight(self.content_height)

    

