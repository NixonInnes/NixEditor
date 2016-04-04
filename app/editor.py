#!/usr/bin/env python3

import sys
from PySide import QtGui, QtCore


class Editor(QtGui.QMainWindow):

    def __init__(self):
        super().__init__()
        self.fname = ''
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle('NixEditor')
        self.center()

        self.editor = QtGui.QTextEdit()
        self.setCentralWidget(self.editor)

        self.statusbar = self.statusBar()
        menubar = self.menuBar()
        self.filemenu = menubar.addMenu('&File')
        self.helpmenu = menubar.addMenu('&Help')
        self.add_actions()

        self.show()
        self.statusbar.showMessage('Ready')

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def add_actions(self):
        do_fopen = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        do_fopen.setShortcut('Ctrl+O')
        do_fopen.setStatusTip('Open file')
        do_fopen.triggered.connect(self.fopenDialog)
        self.filemenu.addAction(do_fopen)

        do_fsave = QtGui.QAction(QtGui.QIcon('save.png'), 'Save', self)
        do_fsave.setShortcut('Ctrl+S')
        do_fsave.setStatusTip('Save file')
        do_fsave.triggered.connect(self.fsaveDialog)
        self.filemenu.addAction(do_fsave)

        do_exit = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        do_exit.setShortcut('Ctrl+Q')
        do_exit.setStatusTip('Exit application')
        do_exit.triggered.connect(self.close)
        self.filemenu.addAction(do_exit)


    def fopenDialog(self):
        self.fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        with open(self.fname, 'r') as file:
            self.editor.setText(file.read())
        self.statusbar.showMessage('Opened %s' % self.fname)

    def fsaveDialog(self):
        if not self.fname:
            self.fname, _ = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        with open(self.fname, 'wt') as file:
            file.write(self.editor.toPlainText())
        self.statusbar.showMessage('Saved %s' % self.fname)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure you want to Quit?",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


