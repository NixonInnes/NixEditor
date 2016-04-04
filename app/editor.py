#!/usr/bin/env python3

from PySide import QtGui, QtCore


class Editor(QtGui.QMainWindow):

    def __init__(self):
        super().__init__()
        self.fname = ''
        self.changesSaved = False
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle('NixEditor')
        self.center()

        self.editor = QtGui.QPlainTextEdit()
        self.editor.textChanged.connect(self.changed)

        self.setCentralWidget(self.editor)

        self.statusbar = self.statusBar()

        self.initMenubar()
        self.initActions()

        self.show()
        self.statusbar.showMessage('Ready')

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


    def initMenubar(self):
        menubar = self.menuBar()
        self.filemenu = menubar.addMenu('&File')
        self.helpmenu = menubar.addMenu('&Help')

    def initActions(self):
        do_fnew = QtGui.QAction(QtGui.QIcon('icons/new.png'), '&New', self)
        do_fnew.setShortcut('Ctrl+N')
        do_fnew.setStatusTip('New file')
        do_fnew.triggered.connect(self.fnew)
        self.filemenu.addAction(do_fnew)

        do_fopen = QtGui.QAction(QtGui.QIcon('icons/open.png'), '&Open', self)
        do_fopen.setShortcut('Ctrl+O')
        do_fopen.setStatusTip('Open file')
        do_fopen.triggered.connect(self.fopen)
        self.filemenu.addAction(do_fopen)

        do_fsave = QtGui.QAction(QtGui.QIcon('icons/save.png'), '&Save', self)
        do_fsave.setShortcut('Ctrl+S')
        do_fsave.setStatusTip('Save file')
        do_fsave.triggered.connect(self.fsave)
        self.filemenu.addAction(do_fsave)

        do_exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        do_exit.setShortcut('Ctrl+Q')
        do_exit.setStatusTip('Exit application')
        do_exit.triggered.connect(self.close)
        self.filemenu.addAction(do_exit)

    def changed(self):
        self.changesSaved = False

    def fnew(self):
        # TODO: write new file function
        pass

    def fopen(self):
        self.fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        with open(self.fname, 'r') as file:
            self.editor.setText(file.read())
        self.statusbar.showMessage('Opened %s' % self.fname)

    def fsave(self):
        if not self.fname:
            self.fname, _ = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        if self.fname:
            with open(self.fname, 'wt') as file:
                file.write(self.editor.toPlainText())
            self.changesSaved = True
            self.statusbar.showMessage('Saved %s' % self.fname)

    def closeEvent(self, event):
        if self.changesSaved:
            event.accept()
        else:
            reply = QtGui.QMessageBox.question(self, 'Message',
                                               "Are you sure you want to Quit without saving?",
                                               QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                               QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                event.accept()
            else:
                self.fsave()


