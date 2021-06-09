from PyQt5 import QtCore, QtWidgets,uic,QtGui
try: from .resources.filepaths import ui 
except: from resources.filepaths import ui 

def format(color, style=''):
    """
    Return a QTextCharFormat with the given attributes.
    """
    _color = QtGui.QColor()
    if type(color) is not str:
        _color.setRgb(color[0], color[1], color[2])
    else:
        _color.setNamedColor(color)

    _format = QtGui.QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QtGui.QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format


# Syntax styles that can be shared by all languages

STYLES = {
    'isa': format([34,34,127]),
    'register': format([206, 103, 16], 'bold'),
    'brace': format('darkGray'),
    'label': format('orange', 'bold'),
    'linenum': format('blue'),
    'string': format([20, 110, 100]),
    'string2': format([30, 120, 110]),
    'comment': format([128, 128, 128]),
    'self': format([150, 85, 140], 'italic'),
    'numbers': format([100, 150, 190]),
}


class MIPS_Highlighter(QtGui.QSyntaxHighlighter):
    """Syntax highlighter for the Python language.
    """
    # Python isas


    isa = [
        'lui', 'addi?u?' , 'andi?', 'b(eq|ne)',
        'j(al|r)?', 'l(bu|hu|l|ui|w|b|h)', 'ori?','nor',
        'slti?u?', 's(r|l)l', 's(b|c|h|w)' , 'subu?', 'multu?',
        'mf(hi|lo|c0)', 'divu?', 'sra',
        'syscall', 'ktext', 'text', 'data', 'kdata','globl','global'
        ]

    # Python registers
    registers = [
        "\\$(0|at|sp|gp|fp|ra)", 
        "\\$(a|v|t|s|k)[0-9]", 
        "\\$[0-3]?[0-9]"
    ]

    # Python braces
    braces = [
        '\{', '\}', '\(', '\)', '\[', '\]',
    ]

    def __init__(self, document):
        QtGui.QSyntaxHighlighter.__init__(self, document)

        # Multi-line strings (expression, flag, style)
        # FIXME: The triple-quotes in these two lines will mess up the
        # syntax highlighting from this point onward
        self.tri_single = (QtCore.QRegExp("'''"), 1, STYLES['string2'])
        self.tri_double = (QtCore.QRegExp('"""'), 2, STYLES['string2'])

        rules = []


        # All other rules
        rules += [

            # Double-quoted string, possibly containing escape sequences
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),
            # Single-quoted string, possibly containing escape sequences
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, STYLES['string']),

            # 'def' followed by an identifier
            (r'[a-zA-Z0-9]*:', 0, STYLES['label']),

            # From '#' until a newline

            # Numeric literals
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers']),
            
            (r'#[^\n]*', 0, STYLES['comment']),
            (r'line [0-9]+', 0, STYLES['linenum']),
        ]
        # Keyword, register, and brace rules
        rules += [(r'\b%s\b' % w, 0, STYLES['isa'])
                  for w in MIPS_Highlighter.isa]
        rules += [(r'%s' % o, 0, STYLES['register'])
                  for o in MIPS_Highlighter.registers]
        rules += [(r'%s' % b, 0, STYLES['brace'])
                  for b in MIPS_Highlighter.braces]

        # Build a QRegExp for each pattern
        self.rules = [(QtCore.QRegExp(pat), index, fmt)
                      for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text.
        """
        # Do other syntax formatting
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        # Do multi-line strings
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)

    def match_multiline(self, text, delimiter, in_state, style):
        """Do highlighting of multi-line strings. ``delimiter`` should be a
        ``QRegExp`` for triple-single-quotes or triple-double-quotes, and
        ``in_state`` should be a unique integer to represent the corresponding
        state changes when inside those strings. Returns True if we're still
        inside a multi-line string when this function is finished.
        """
        # If inside triple-single quotes, start at 0
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        # Otherwise, look for the delimiter on this line
        else:
            start = delimiter.indexIn(text)
            # Move past this match
            add = delimiter.matchedLength()

        # As long as there's a delimiter match on this line...
        while start >= 0:
            # Look for the ending delimiter
            end = delimiter.indexIn(text, start + add)
            # Ending delimiter on this line?
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            # No; multi-line string
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            # Apply formatting
            self.setFormat(start, length, style)
            # Look for the next match
            start = delimiter.indexIn(text, start + length)

        # Return True if still inside a multi-line string, False otherwise
        if self.currentBlockState() == in_state:
            return True
        else:
            return False

class Header(QtWidgets.QWidget):
    def __init__(self,title):
        super(QtWidgets.QWidget, self).__init__() 
        self.setObjectName("header")
        self.resize(335, 30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        lay = QtWidgets.QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        frame=QtWidgets.QFrame()
        lay.addWidget(frame)

        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 30))
        self.setMaximumSize(QtCore.QSize(16777215, 30))
        self.horizontalLayout = QtWidgets.QHBoxLayout(frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Title = QtWidgets.QLabel(self,text=title)
        self.Title.setObjectName("Title")
        self.horizontalLayout.addWidget(self.Title)
        self.saveBtn = QtWidgets.QToolButton(self, text = "Save File")
        self.saveBtn.setObjectName("saveBtn")
        self.saveBtn.setVisible(False)
        self.horizontalLayout.addWidget(self.saveBtn)
        self.popoutBtn = QtWidgets.QToolButton(self)
        self.popoutBtn.setObjectName("popoutBtn")
        self.horizontalLayout.addWidget(self.popoutBtn)
        self.closeBtn = QtWidgets.QToolButton(self)
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout.addWidget(self.closeBtn)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Title.setText(_translate("header", self.Title.text()))
        self.popoutBtn.setText(_translate("header", "--"))
        self.closeBtn.setText(_translate("header", "X"))
class ResultsWindow(QtWidgets.QDockWidget):
    textBox:QtWidgets.QTextEdit
    horizontalScrollBar:QtWidgets.QScrollBar
    verticalScrollBar:QtWidgets.QScrollBar
    lineNum:QtWidgets.QTextEdit
    scrollArea:QtWidgets.QScrollArea
    borderLine:QtCore.QLine
    dividerLine:QtCore.QLine
    header:Header
    def __init__(self, title, parent, text=None):
        super(QtWidgets.QDockWidget, self).__init__(parent) 
        uic.loadUi(ui.resultswindow, self)
        self.setWindowTitle(title)
        self.header=Header(title)
        self.header.setStyleSheet("QFrame,QLabel{background-color:rgb(200,200,200)}")
        self.header.closeBtn.pressed.connect(self.close)
        self.header.popoutBtn.pressed.connect(self.popout)
        self.setTitleBarWidget(self.header)
        #self.textBox.textChanged.connect(self.updateScrollBars)
        self.verticalScrollBar=self.textBox.verticalScrollBar()
        self.horizontalScrollBar=self.textBox.horizontalScrollBar()
        self.lineNum.setVerticalScrollBar(self.verticalScrollBar)
        self.lineNum.setAlignment(QtCore.Qt.AlignRight)
       # self.verticalScrollBar.sliderMoved.connect(self.verticalMovement)
        self.isClosed=True
        self.dialog=None
        self.header.saveBtn.pressed.connect(self.SaveContents)

    @property
    def Title(self):
        return self.header.Title.text()
    @Title.setter
    def Title(self,value):
        self.header.Title.setText(value)
    
    def closeEvent(self, i):
        self.isClosed=True
        i.accept()
    
    def show(self):
        self.isClosed=False
        super().show()
    
    def canShow(self):
        return (self.isClosed==False)
    
    def popout(self):
        self.setFloating(not self.isFloating())    
    def verticalMovement(self) : 
        self.lineNum.verticalScrollBar().setValue(self.verticalScrollBar.value())
    
    def SaveContents(self, DefaultSuffix='*', NameFilters=['Everything (*)']):
        #savedest=QtWidgets.QFileDialog.getSaveFileName(self,"Save Settings as",self.lastSaveLocation,"*.json")
        if self.dialog is None : return
        
        if self.dialog.exec_() == QtWidgets.QDialog.Accepted:
            saveDest=self.dialog.selectedFiles()[0]
            with open(saveDest,'w') as sd: sd.write(self.textBox.toPlainText())
        else:
            return
        

    def CanSave(self,canSave:bool, DefaultSuffix='', NameFilters=['Everything (*)']):
        self.header.saveBtn.setVisible(canSave)
        
        self.dialog = QtWidgets.QFileDialog()
        self.dialog.setFilter(self.dialog.filter() | QtCore.QDir.Hidden)
        self.dialog.setDefaultSuffix(DefaultSuffix)
        self.dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        self.dialog.setNameFilters(NameFilters)

    def SpimSyntax(self):
        self.highlighter=MIPS_Highlighter(self.textBox.document())
 
    #def resizevent(self, event): 
#        self.scrollArea.setMinimumWidth(self.width())
#        self.scrollArea.setMaximumWidth(self.width())
#        self.scrollArea.setMinimumHeight(self.height())
#        self.scrollArea.setMaximumHeight(self.height())

    def setText(self,text): self.textBox.setText(text)    
    def setContents(self,text,showLineNumbers=False):
        text=text.split('\n')
        data=""
        nums=""
        self.isUsed=True
        i=1
        nl='\n'
        for line in text:
            if showLineNumbers:
                nums+=str(i)+nl
                i=i+1
            data+=line+nl
        self.textBox.setText(data)
        if showLineNumbers: self.lineNum.setText(nums)
        else: self.lineNum.hide()
        self.show()
        return True
    def displayFile(self,filepath, showLineNumbers=False):
        data=""
        nums=""
        try:
            with open(filepath,'r') as f: 
                flist=f.readlines()
        except FileNotFoundError: 
            self.hide()
            self.isUsed=False
            return False

        self.isUsed=True
        i=1
        nl='\n'
        for line in flist:
            if showLineNumbers:
                nums+=str(i)+nl
                i=i+1
            data+=line
        self.textBox.setText(data)
        if showLineNumbers:
            self.lineNum.setText(nums)
        else: self.lineNum.hide()
        self.show()
        return True



