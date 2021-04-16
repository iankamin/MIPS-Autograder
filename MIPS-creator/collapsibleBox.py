from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets


class CollapsibleBox(QtWidgets.QWidget):
    def __init__(self, title="", parent=None):
        parent:CollapsibleBox
        super(CollapsibleBox, self).__init__()
        self.parent=parent
        self.toggle_button = QtWidgets.QToolButton(
            text=title, checkable=True, checked=False
        )
        self.toggle_button.setStyleSheet("QToolButton { border: None; }")
        self.toggle_button.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon
        )
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

        lay = QtWidgets.QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.toggle_button)
        lay.addWidget(self.content_area)

        self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self, b"minimumHeight"))
        self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self, b"maximumHeight"))
        self.toggle_animation.addAnimation( QtCore.QPropertyAnimation(self.content_area, b"maximumHeight"))
        self.checked = True
        if type(parent) is CollapsibleBox:
            self.parent.addWidget(self)
            self.toggle_animation.finished.connect(self.parent.updateAnimation)

    @QtCore.pyqtSlot()
    def on_pressed(self):
        self.checked = not(self.checked)
        i=self.checked
        i=i
        self.toggle_button.setArrowType(
            QtCore.Qt.DownArrow if not self.checked else QtCore.Qt.RightArrow
        )
        self.toggle_animation.setDirection(
            QtCore.QAbstractAnimation.Forward
            if not self.checked
            else QtCore.QAbstractAnimation.Backward
        )
        if type(self.parent) is CollapsibleBox:
            self.parentExpandAnimation()
        if self.content_area.layout().count()>0: 
            self.toggle_animation.start()

    def setContentLayout(self, layout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)
        self.collapsed_height = (
            self.sizeHint().height() - self.content_area.maximumHeight()
        )
        self.content_height = layout.sizeHint().height()
        self.updateAnimation()

    def updateAnimation(self,startValue=0,EndValue=None):
        if EndValue is None: EndValue=self.content_height
        
        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(500)
            animation.setStartValue(self.collapsed_height+startValue)
            animation.setEndValue(self.collapsed_height + EndValue)

        content_animation = self.toggle_animation.animationAt(
            self.toggle_animation.animationCount() - 1
        )
        content_animation.setDuration(500)
        content_animation.setStartValue(startValue)
        content_animation.setEndValue(EndValue)


    def parentExpandAnimation(self):
        parent:CollapsibleBox
        dir = 1 if not self.checked else -1
        parent=self.parent
        
        p_orig_content_height = parent.content_height
        p_orig_direction = parent.toggle_animation.direction()
        
        parent.content_height = p_orig_content_height+dir*self.content_height
        parent.toggle_animation.setDirection(self.toggle_animation.direction())
        
        p_new_content_height=parent.content_height
        p_new_direction = parent.toggle_animation.direction()
        parent.updateAnimation(p_orig_content_height+self.collapsed_height+parent.collapsed_height, parent.content_height)
        parent.toggle_animation.start()

        parent.toggle_animation.setDirection(p_orig_direction)



        pass


    def addWidget(self,widget):
        lay=self.content_area.layout()
        lay.insertWidget(lay.count()-1,widget)
        self.setContentLayout(self.content_area.layout())