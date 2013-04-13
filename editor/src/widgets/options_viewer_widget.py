# -*- coding: utf-8 -*-
'''
Options viewer widget.
'''
from PySide.QtGui import *


class OptionsViewerWidget(QWidget):
    
    def __init__(self, parent=None):
        super(OptionsViewerWidget, self).__init__(parent)
        # Initialize UI items
        self._create_ui()
        # Initialize layout
        self._create_layout()
        
             
    def _create_ui(self):
        # Label example content
        self._label = QLabel(self)
        self._label.setText("OptionsViewerWidget content.")
    
    
    def _create_layout(self):
        # Main layout
        main_layout = QHBoxLayout(self)
        # Add label
        main_layout.addWidget(self._label)
        # Set the layout
        self.setLayout(main_layout)