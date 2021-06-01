from PyQt5 import QtCore, QtGui, QtWidgets
from enum import Flag
try: from .resources.filepaths import Icons
except: from filepaths import Icons
class CollapsibleBox(QtWidgets.QWidget):
    ExpandCollapse_finished=QtCore.pyqtSignal()
    def __init__(self, title="", parent=None, *buttons):
        parent:CollapsibleBox
        self.parent:CollapsibleBox
        super(CollapsibleBox, self).__init__()
        self.parent=parent
        self.title=title
        lay = QtWidgets.QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        frame=QtWidgets.QFrame(self)
        frame.setObjectName("CollapsibleBox")
        lay.addWidget(frame)

        self.toggle_button = QtWidgets.QToolButton( text=title, checkable=True, checked=False)
        self.toggle_button.setObjectName("toggle_button")
        self.toggle_button.setStyleSheet("QToolButton#toggle_button { border: None; }")
        #self.toggle_button.setStyleSheet("background-color: rgb(255, 200, 200);")
        self.toggle_button.setToolButtonStyle( QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setMaximumWidth(100000)
        
        #if index is None: self.toggle_button.setMinimumHeight(20)
        #else: self.toggle_button.setMinimumHeight(30)
        self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)

        lay1 =QtWidgets.QHBoxLayout()
        lay1.setSpacing(8)
        lay1.setContentsMargins(0,0,0,0)
        lay1.addWidget(self.toggle_button)
        self.Buttons = buttons
        for button in self.Buttons: 
            button.setStyleSheet("QToolButton#toggle_button { border: None; }")
            lay1.addWidget(button)
            button.hide()
        self.lay1=lay1
        self.toggle_animation = QtCore.QParallelAnimationGroup(self)

        self.content_area = QtWidgets.QScrollArea( maximumHeight=0, minimumHeight=0)
        self.content_area.setObjectName("content_area")
        self.content_area.setSizePolicy( QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.content_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content_area.setLayout(QtWidgets.QVBoxLayout())
        self.content_area.setContentsMargins(0, 0, 0, 0)
        self.content_area.layout().addStretch()
        self.content_height=0
        
        lay = QtWidgets.QVBoxLayout(frame)
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
        for button in self.Buttons:
            if button is not None:
                (button.show() if self._isOpen else button.hide())
        
        if type(self.parent) is CollapsibleBox: 
            if self.isClosed : self.parent.content_height = self.parent.content_height - self.content_height 
            self.updateAnimation()
            if self.isOpen : self.parent.content_height = self.parent.content_height + self.content_height

    def setBackgroundColor(self,color): self.setStyleSheet("QFrame#CollapsibleBox,QToolButton#toggle_button,QToolButton#toggle_button,QToolButton#toggle_button,QScrollArea#content_area {background-color: %s}"%color)

    def toggle_animation_finished(self):
        if self.parent is not None: self.parent.updateAnimation()
        self.ExpandCollapse_finished.emit()
    
    def toggleState(self,expand):
        """Toggles the Boxes open/close state
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

    def getContents(self):
        lay = self.content_area.layout()
        items = [lay.itemAt(i).widget() for i in range(lay.count()) if lay.itemAt(i).widget() is not None]
        return items
        
    def height(self):
        if self.isOpen: return self.collapsed_height+self.content_height
        else: return self.collapsed_height
    
    def updateHeight(self,widget:QtWidgets.QWidget, Forward=True,addi=0):
        lay:QtWidgets.QVBoxLayout
        lay=self.content_area.layout()

        if self.content_height<lay.spacing()*2: addi = lay.spacing()*2

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

    

