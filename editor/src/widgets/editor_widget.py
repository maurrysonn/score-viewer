# -*- coding: utf-8 -*-
'''
Main widget of application. 
'''

from PySide.QtGui import * 
from widgets.file_selector import FileSelectorWidget
from widgets.options_viewer_widget import OptionsViewerWidget


class EditorWidget(QWidget):
    
    def __init__(self, parent=None):
        super(EditorWidget, self).__init__(parent)
        # Create UI
        self._create_ui()
        # Create layout
        self._create_layout()
        # Initialize
        
    def _create_ui(self):
        self._file_selector = FileSelectorWidget(self)
        self._options_viewer = OptionsViewerWidget(self)
        
    
    def _create_layout(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self._file_selector)
        main_layout.addWidget(self._options_viewer)
        self.setLayout(main_layout)
        
    def set_root_path(self, path=None):
        self._file_selector.set_root_path(path)
        