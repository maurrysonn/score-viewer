# -*- coding: utf-8 -*-
# Import PySide classes
from PySide.QtCore import *
from PySide.QtGui import *
from widgets.editor_widget import EditorWidget
import sys


def main():
    
    # Create a Qt application
    app = QApplication(sys.argv)
    # Create Main Editor Widget
    editor = EditorWidget()
    editor.show()
    # Enter Qt application main loop
    app.exec_()
    sys.exit()
    

if __name__ == "__main__":
    main()
