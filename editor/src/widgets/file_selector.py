# -*- coding: utf-8 -*-
'''
File Selector widget.
'''
from PySide.QtCore import *
from PySide.QtGui import *


class FileSelectorWidget(QWidget):
    

    def __init__(self, parent=None, path=None):
        super(FileSelectorWidget, self).__init__(parent)
        # Init size
        #self.setMinimumSize(1000, 400)
        # Model
        self._init_model()
        # Initialize UI items
        self._create_ui()
        # Initialize layout
        self._create_layout()
        # Connections
        self._create_connections()
        # Initialize FS view
        self.set_root_path(path)


    def _init_model(self):
        self._model = QFileSystemModel(self)


    def _create_ui(self):
        # Tree View file system
        self._fs_view = QTreeView(self)
        self._fs_view.setModel(self._model)
        self._fs_view.setMinimumSize(500, 300)
        # Resizing columns policy
        header = self._fs_view.header()
        # First column with all space available
        header.setResizeMode(0, QHeaderView.Stretch)
        # Other fit to content
        header.setResizeMode(1, QHeaderView.ResizeToContents)
        header.setResizeMode(2, QHeaderView.ResizeToContents)
        header.setResizeMode(3, QHeaderView.ResizeToContents)
        # -- Sorting headers
        self._fs_view.setSortingEnabled(True)
        self._fs_view.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        # Buttons
        self._btn_add = QPushButton(">", self)
        # List View Widget for selected items
        self._selected_items_view = QListWidget(self)
            

    def _create_layout(self):
        # Main layout
        main_layout = QHBoxLayout()
        # Add View
        main_layout.addWidget(self._fs_view)
        # Buttons layout
        btn_layout = QVBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self._btn_add)
        btn_layout.addStretch()
        main_layout.addLayout(btn_layout)
        # Add selectied items list
        main_layout.addWidget(self._selected_items_view)
        # Set the layout
        self.setLayout(main_layout)


    def _create_connections(self):
        self._btn_add.clicked.connect(self._add_current_item_in_selection)

        
    def set_root_path(self, path=None):
        if path is None:
            path = QDir.currentPath()
        self._model.setRootPath(path)
        self._fs_view.setRootIndex(self._model.index(self._model.rootPath()))
        
        
    def get_root_path(self):
        return self._model.rootPath()
    
    def _get_relative_path(self, file_path):
        split_items = file_path.split(self.get_root_path())
        return split_items[-1]


    def _add_current_item_in_selection(self):
        list_indexes = self._fs_view.selectedIndexes()
        # If no selection -> return
        if not list_indexes:
            return
        index = list_indexes[0]
        # If not file -> return
        if self._model.isDir(index):
            return
        # Get relative file path
        file_path = self._model.filePath(index)
        # Create and add item
        item = QListWidgetItem(self._get_relative_path(file_path))
        self._selected_items_view.addItem(item)
