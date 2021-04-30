from PyQt5 import QtCore, QtGui, QtWidgets
from enum import Flag
class CollapsibleBox(QtWidgets.QWidget):
    ExpandCollapse_finished=QtCore.pyqtSignal()
    def __init__(self, title="", parent=None, btnFunction=None, btnText="Add New",index= None):
        parent:CollapsibleBox
        self.parent:CollapsibleBox
        super(CollapsibleBox, self).__init__()
        self.indexUpdated(index)
        self.parent=parent
        self.title=title
        self.toggle_button = QtWidgets.QToolButton(
            text=title, checkable=True, checked=False
        )
        self.setObjectName("%s-%s"%(self.title,index or " "))
        self.toggle_button.setStyleSheet("QToolButton { border: None; }")
        #self.toggle_button.setStyleSheet("background-color: rgb(255, 200, 200);")
        self.toggle_button.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon
        )
        self.toggle_button.setMaximumWidth(100000)
        if index is None: self.toggle_button.setMinimumHeight(20)
        else: self.toggle_button.setMinimumHeight(30)
        self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)

        if btnFunction is not None:
            btnText="  "+btnText
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("ui_files/Icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.AddButton = QtWidgets.QPushButton(text=btnText)
            self.AddButton.setMaximumWidth(90)
            self.AddButton.setIcon(icon)
            self.AddButton.pressed.connect(btnFunction)
            self.AddButton.hide()
        else: 
            self.AddButton = None

        lay1 =QtWidgets.QHBoxLayout()
        lay1.setSpacing(0)
        lay1.setContentsMargins(0, 0, 0, 0)
        lay1.addWidget(self.toggle_button)
        if btnFunction is not None: lay1.addWidget(self.AddButton) 

        self.toggle_animation = QtCore.QParallelAnimationGroup(self)

        self.content_area = QtWidgets.QScrollArea(
            maximumHeight=0, minimumHeight=0
        )
        self.content_area.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        self.content_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content_area.setLayout(QtWidgets.QVBoxLayout())
        self.content_area.setContentsMargins(0, 0, 0, 0)
        self.content_area.layout().addStretch()
        self.content_height=0
        
        lay = QtWidgets.QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addLayout(lay1)
        lay.addWidget(self.content_area) 

        self.animationDuration=150
        self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self, b"minimumHeight"))
        self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self, b"maximumHeight"))
        self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self.content_area, b"maximumHeight"))

        self.collapsed_height=self.sizeHint().height() - self.content_area.maximumHeight()
        self._isOpen = False
        self.setContentsMargins(0,0,0,0)
        self.toggle_animation.finished.connect(self.toggle_animation_finished)
        if type(parent) is CollapsibleBox:
            self.parent.addWidget(self)
            self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self.parent, b"minimumHeight"))
            self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self.parent, b"maximumHeight"))
            self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self.parent.content_area, b"maximumHeight"))
        #TODO signals sneed to be defined in seperate class i think

    @property
    def isClosed(self): return not(self.isOpen)
    @isClosed.setter
    def isClosed(self,val:bool): self.isOpen=not(val)
    
    @property
    def isOpen(self): return (self._isOpen)
    @isOpen.setter
    def isOpen(self,val:bool): 
        if self._isOpen == val: return
        self._isOpen=val
        self.toggle_button.setChecked(val)
        self.toggle_button.setArrowType(
            QtCore.Qt.DownArrow if self._isOpen else QtCore.Qt.RightArrow
        )
        self.toggle_animation.setDirection(
            QtCore.QAbstractAnimation.Forward
            if self._isOpen
            else QtCore.QAbstractAnimation.Backward
        )
        if self.AddButton is not None:
            if self._isOpen: self.AddButton.show()
            else:           self.AddButton.hide()
        
        if type(self.parent) is CollapsibleBox: 
            if self.isClosed : self.parent.content_height = self.parent.content_height - self.content_height 
            self.updateAnimation()
            if self.isOpen : self.parent.content_height = self.parent.content_height + self.content_height



    def indexUpdated(self,index):
        if index is not None: 
            if index %2: self.setStyleSheet("background-color: rgb(215, 215, 255)")
            else:        self.setStyleSheet("background-color: rgb(230, 230, 255)")
    
    def toggle_animation_finished(self):
        if self.parent is not None: self.parent.updateAnimation()
        self.ExpandCollapse_finished.emit()
    
    def toggleState(self,expand):
        """[summary]

        Args:
            expand (bool): True is box must expand False if box must collapse
        """
        collapse=not(expand)
        if self.isOpen and expand: return
        if (not self.isOpen) and collapse: return
        self.toggle_button.click()

    @QtCore.pyqtSlot()
    def on_pressed(self):
        self.isOpen= not(self.isOpen)
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


        None
    def updateAnimation(self,startValue=0,EndValue=None):
        if EndValue is None: EndValue=self.content_height
        dur=self.animationDuration
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
    
    def updateHeight(self,widget:QtWidgets.QWidget, Forward=True,addi=0):
        lay:QtWidgets.QVBoxLayout
        lay=self.content_area.layout()

        if self.content_height<lay.spacing()*2: 
            addi=lay.spacing()*2

        direction = 1 if Forward else -1
        self.content_height += direction*(widget.height()+lay.spacing())
        self.content_height += addi
        
        if self.content_height<=lay.spacing()*2: 
            addi=-self.content_height
            self.content_height=0
        
        if type(self.parent) is CollapsibleBox and self.parent.isOpen:
            self.parent.updateHeight(widget,Forward,addi)

        

        self.updateAnimation()
        if self.isOpen:
            self.setMaximumHeight(self.content_height+self.collapsed_height)
            self.setMinimumHeight(self.content_height+self.collapsed_height)
            self.content_area.setMaximumHeight(self.content_height)

    

