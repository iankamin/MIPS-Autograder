# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from typing import List, Tuple
from PyQt5 import QtCore, QtGui, QtWidgets
from copy import deepcopy
from time import sleep
from .collapsibleBox import CollapsibleBox
from .RowTypes import *
from .utilities import set_Test,settings

class Test(QtWidgets.QWidget): 
    def __init__(self,index,parent,TopRow=None,isSkelton=False): 
        self._index=index
        self.isSkeleton=isSkelton
        super(QtWidgets.QWidget, self).__init__()
        self.setObjectName("Test")
        self.parent=parent
        if TopRow is None or TopRow.TestName.text()=="": 
            self._name= "Sample" if isSkelton else "Test"
        else: self._name = TopRow.TestName.text()
        self.TopRow=TopRow
        self.setupUi()
        self.index=index

    @property
    def name(self): return self._name
    @name.setter
    def name(self,s):
        if s == "": self._name = "Test"
        else: self._name=s
        self.HidingBox.toggle_button.setText("{:0>2} - {}".format(self.index,self.name))
    def setName(self,s): self.name=s
    
    @property
    def index(self): return self._index
    @index.setter
    def index(self,i):
        self._index=i
        self.HidingBox.toggle_button.setText("{:0>2} - {}".format(self.index,self.name))
        if i%2: self.setBackgroundColor("rgb(245, 245, 255)")
        else:   self.setBackgroundColor("rgb(230, 230, 255)")
    
    @property
    def title(self): return "{:0>2} - {}".format(self.index,self.name)
    def addButton(self,connectFunc, text):
        text=" " + text
        button = QtWidgets.QToolButton(text=text)
        icon = QtGui.QIcon(QtGui.QPixmap(Icons.add2))
        button.setIcon(icon)
        button.setToolButtonStyle( QtCore.Qt.ToolButtonTextBesideIcon)
        button.setFixedWidth(130)
        button.pressed.connect(connectFunc)
        return button
    def copyButton(self):
        button = QtWidgets.QToolButton()
        icon = QtGui.QIcon(QtGui.QPixmap(Icons.copy))
        button.setIcon(icon)
        button.setToolButtonStyle( QtCore.Qt.ToolButtonIconOnly)
        button.setFixedWidth(50)
        button.pressed.connect(self.Copy) 
        return button
    def deleteButton(self):
        button = QtWidgets.QToolButton()
        icon = QtGui.QIcon(QtGui.QPixmap(Icons.delete))
        button.setIcon(icon)
        button.setToolButtonStyle( QtCore.Qt.ToolButtonIconOnly)
        button.setFixedWidth(50)
        button.pressed.connect(self.deleteSelf)
        return button

    def setupUi(self):
        self.setObjectName("test") 
        self.setMinimumWidth(650)
        self.verticalLayout = QtWidgets.QVBoxLayout(self) 
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setSpacing(0)
        if self.TopRow is None: self.TopRow=TestTopRow()
        if self.isSkeleton: self.TopRow.hide()
        
        self.HidingBox=CollapsibleBox("%s - %s"%(self.name,self.index),None, self.copyButton(),self.deleteButton() )
        self.HidingBox.lay1.setContentsMargins(0,0,10,0)
        
        self.setBackgroundColor= self.HidingBox.setBackgroundColor
        self.setStyleSheet=self.HidingBox.setStyleSheet
        self.styleSheet=self.HidingBox.styleSheet
        
        self.HidingBox.content_area.layout().setContentsMargins(20,0,10,0)
        self.HidingBox.toggle_button.setMinimumHeight(30)
        
        self.verticalLayout.addWidget(self.HidingBox)

        self.TopRow.TestName.textChanged.connect(self.setName)
        if not self.isSkeleton: self.HidingBox.addWidget(self.TopRow)
        if not self.isSkeleton: 
            self.allUserInput  = CollapsibleBox("User Input"       ,self.HidingBox, self.addButton(connectFunc=lambda: self.addRow(UserInputRow), text="User Input"))
        self.DataInput         = CollapsibleBox("Data Input"       ,self.HidingBox, self.addButton(connectFunc=lambda: self.addRow(DataRow     ), text="Data") )
        self.InputRegisters    = CollapsibleBox("Input Registers"  ,self.HidingBox, self.addButton(connectFunc=lambda: self.addRow(RegisterRow ), text="Register"))
        if not self.isSkeleton: 
            self.Outputs       = CollapsibleBox("Output Registers" ,self.HidingBox, self.addButton(connectFunc=lambda: self.addRow(OutputRow   ), text="Output"))
        
        self.verticalLayout.addStretch()
        self.retranslateUi() 

    def deleteSelf(self): self.parent.deleteTest(self)

    def validateEmpty(self) -> Tuple[bool,str,List[Row]]:
        out=''

        # ensure program has INPUTS
        items = []
        items = items + self.allUserInput.getContents()
        items = items + self.DataInput.getContents()
        items = items + self.InputRegisters.getContents()
        v1=True
        if len(items)==0:
            out+="(WARNING) \n - {title} has no inputs".format(title=self.title)
            self.ExpandAndCollapseAll(expand=True)
            v1=False

        # ensure program has OUPUTS
        v2=True
        itemsO = self.Outputs.getContents()
        if len(itemsO)==0:
            out+="(WARNING) \n - {title} has no outputs".format(title=self.title)
            self.ExpandAndCollapseAll(expand=True)
            v2= False
        items=items+itemsO
        return (v1 and v2), out, items

    def validate(self) -> Tuple[bool,str]:
        _,outputString,items=self.validateEmpty()
        #verify that every input and output is filled in completely
        blankBoxes=True    
        for item in items:
            blankBoxes = item.validate() and blankBoxes
        if not blankBoxes:
            outputString+="\n - {title} has empty textboxs".format(title=self.title)
            self.ExpandAndCollapseAll(expand=True)
        
        return blankBoxes,outputString

    def validRow(self,item) -> bool:
        if item is UserInputRow: return True
        if item is OutputRow: return True
        if item is RegisterRow: return True
        if item is DataRow: return True
        return False
    
    def ExpandAndCollapseAll(self,expand):
        toggleAll_animation = QtCore.QParallelAnimationGroup(self)

        toggleAll_animation.setDirection(
            QtCore.QAbstractAnimation.Forward if expand else QtCore.QAbstractAnimation.Backward)

        if self.HidingBox.isOpen: hbox_ch=self.HidingBox.content_height
        else: hbox_ch=0
        
        if not expand: #Hiding box need to be first when collapsing and last when Expanding
            for anim in self.ExpandAndCollapseAll_AnimationSet(self.HidingBox,expand): toggleAll_animation.addAnimation(anim)

        for anim in self.ExpandAndCollapseAll_AnimationSet(self.DataInput,expand): toggleAll_animation.addAnimation(anim)
        for anim in self.ExpandAndCollapseAll_AnimationSet(self.InputRegisters,expand): toggleAll_animation.addAnimation(anim)
        if not self.isSkeleton:
            for anim in self.ExpandAndCollapseAll_AnimationSet(self.allUserInput,expand): toggleAll_animation.addAnimation(anim)
            for anim in self.ExpandAndCollapseAll_AnimationSet(self.Outputs,expand): toggleAll_animation.addAnimation(anim)
        self.DataInput.isOpen=expand
        self.InputRegisters.isOpen=expand
        if not self.isSkeleton:
            self.allUserInput.isOpen=expand
            self.Outputs.isOpen=expand

        if expand: 
            for anim in self.ExpandAndCollapseAll_AnimationSet(self.HidingBox,expand, override=self.HidingBox.isOpen, startHeightOffset=hbox_ch): 
                toggleAll_animation.addAnimation(anim)
        
        self.HidingBox.isOpen=expand
        
        toggleAll_animation.start()
        
        self.HidingBox.updateAnimation(0, self.HidingBox.content_height)

    def ExpandAndCollapseAll_AnimationSet(self, box:CollapsibleBox, expand, dur=0, override=False, startHeightOffset=0):
        if not override:
            if box.isClosed and not expand: return
            if box.isOpen and expand: return

        if dur<=0: dur=box.animationDuration
        anim = QtCore.QPropertyAnimation(box, b"minimumHeight")
        anim.setDuration(dur)
        anim.setStartValue(box.collapsed_height + startHeightOffset)
        anim.setEndValue(box.collapsed_height + box.content_height )
        yield anim

        anim = QtCore.QPropertyAnimation(box, b"maximumHeight")
        anim.setDuration(dur)
        anim.setStartValue(box.collapsed_height + startHeightOffset)
        anim.setEndValue(box.collapsed_height + box.content_height )
        yield anim
        
        anim = QtCore.QPropertyAnimation(box.content_area, b"maximumHeight")
        anim.setDuration(dur)
        anim.setStartValue(0 + startHeightOffset)
        anim.setEndValue(box.content_height )
        yield anim
    

    #TODO make the add user input button work
    def addRow(self,rowType,row=None,**kwargs):
        row:Row
        if rowType is None and row is None: raise Exception("either row or rowType must be defined")
        if row is not None: rowType=type(row)
        
        if rowType is UserInputRow:  destination=self.allUserInput
        elif rowType is DataRow:     destination=self.DataInput
        elif rowType is RegisterRow: destination=self.InputRegisters
        elif rowType is OutputRow:   destination=self.Outputs
        else: raise Exception("unusable type %s"%rowType)
        
        if row is None: row=rowType(parent=destination,**kwargs)
        else: row.parent = destination
        row.Deleted.connect(self.rowDeleted)
        return row
   
    def rowDeleted(self, row,box): box.updateHeight(row,Forward=False)
    
    def Copy(self):
        newTest = deepcopy(self)
        self.parent.addTest(newTest)

    def retranslateUi(self): pass
    
    def convertToSettingsTest(self,setting:settings): 
        """Converts The GUI Layout of a Test to the version needed to run the Autograder

        Args:
            setting (settings): The Settings File to Store this test
        """
        test_setting=set_Test(parent=setting)
        test_setting.head_init(**self.TopRow.GetKwargs())
        
        if not self.isSkeleton: self.setJSONKwargs( setFunction=test_setting.AddUserInput, layout=self.allUserInput.content_area.layout(), allowedtype=UserInputRow)
        self.setJSONKwargs( setFunction=test_setting.AddMemInput, layout=self.DataInput.content_area.layout(), allowedtype=DataRow)
        self.setJSONKwargs( setFunction=test_setting.AddRegInput, layout=self.InputRegisters.content_area.layout(), allowedtype=RegisterRow)
        if not self.isSkeleton: self.setJSONKwargs( setFunction=test_setting.AddOutput, layout=self.Outputs.content_area.layout(), allowedtype=OutputRow)
        
        return test_setting
        
    def setJSONKwargs(self, setFunction, layout:QtWidgets.QLayout, allowedtype:type):
        """ Used to convert each row to a settings.Test row

        Args:
            setFunction (method): The function belonging to each type in the layout
            layout (QtWidgets.QLayout): the layout to parse through
            allowedtype (type): The type of Widget with the layout 
        """
        items = [layout.itemAt(i).widget() for i in range(layout.count()) ]
        for item in items: 
            if type(item) is not allowedtype: continue
            setFunction(**item.getKwargs())
        return
         
    def __deepcopy__(self,_):
        topRow=self.TopRow.copy()
        copy = Test(index=self.index,parent=self.parent,TopRow=topRow,isSkelton=self.isSkeleton)
        
        if not self.isSkeleton: 
            lay=self.allUserInput.content_area.layout()
            items = [lay.itemAt(i).widget() for i in range(lay.count()) ]
            for item in items: 
                i=type(item)
                if i is not UserInputRow: continue
                copy.addRow(UserInputRow, row=item.copy())
        
        lay=self.DataInput.content_area.layout()
        items = [lay.itemAt(i).widget() for i in range(lay.count()) ]
        for item in items: 
            i=type(item)
            if i is not DataRow: continue
            copy.addRow(DataRow, item.copy())
        
        lay=self.InputRegisters.content_area.layout()
        items = [lay.itemAt(i).widget() for i in range(lay.count()) ]
        for item in items: 
            i=type(item)
            if i is not RegisterRow: continue
            copy.addRow(RegisterRow, item.copy())


        if not self.isSkeleton: 
            lay=self.Outputs.content_area.layout()
            items = [lay.itemAt(i).widget() for i in range(lay.count()) ]
            for item in items: 
                i=type(item)
                if i is not OutputRow: continue
                copy.addRow(OutputRow, item.copy())
            

        return copy