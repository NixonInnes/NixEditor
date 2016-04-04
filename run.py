import sys
from PySide.QtGui import QApplication
from app.editor import Editor

def main():
    app = QApplication(sys.argv)
    ex = Editor()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()