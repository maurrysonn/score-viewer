# -*- coding: utf-8 -*-
'''
File Selector widget.
'''
from PySide.QtGui import *


class FileSelectorWidget(QWidget):
    
    def __init__(self, parent=None):
        super(FileSelectorWidget, self).__init__(parent)
        # Initialize UI items
        self._create_ui()
        # Initialize layout
        self._create_layout()
        
             
    def _create_ui(self):
        # Label example content
        self._label = QLabel(self)
        self._label.setText("FileSelectorWidget content.")
    
    
    def _create_layout(self):
        # Main layout
        main_layout = QHBoxLayout(self)
        # Add label
        main_layout.addWidget(self._label)
        # Set the layout
        self.setLayout(main_layout)