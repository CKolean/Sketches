from PySide2 import QtCore
from PySide2.QtGui import QPalette, QColor
from PySide2 import QtWidgets


class SpotterDialog(QtWidgets.QDialog):
    # using super to combine my init with parent class init
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Spotter")
        self.setMinimumWidth(500)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.set_colors()
        self.create_widgets()
        self.create_layouts()
    def set_colors(self):
        self.setStyleSheet("color:rgb(219, 212, 204);"
                           "background-color: rgb(36, 36, 36);"
                           "selection-color: red;"
                           "label-color: orange;")
        #self.setStyleSheet("Window,QLineEdit,QPushButton { background-color: rgb(36, 36, 36) }")
        self.setAutoFillBackground(True)

    def create_widgets(self):
        self.searchBtn = QtWidgets.QPushButton("Search!")
        self.searchBtn.setStyleSheet("font: bold 14px")
        self.input = QtWidgets.QLineEdit()
        self.output = QtWidgets.QLabel("thing")

        self.resultTable = QtWidgets.QTableWidget()
        self.resultTable.setColumnCount(3)
        self.resultTable.setRowCount(3)
        self.resultTable.setColumnWidth(0, 300)
        self.resultTable.setStyleSheet("color: white;"
                        "background-color: rgb(36, 36, 36)"
                        "selection-color: rgb(36, 36, 36)"
                        "selection-background-color: black;")
        self.resultTableHeader = self.resultTable.horizontalHeader()
        self.resultTableHeader.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.resultTable.setHorizontalHeaderLabels(["Name", "Hits", "Time"])

    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        button_layout = QtWidgets.QVBoxLayout(self)
        button_layout.addStretch()

        button_layout.addWidget(self.searchBtn)
        button_layout.addWidget(self.input)

        table_layout = QtWidgets.QVBoxLayout(self)
        button_layout.addWidget(self.resultTable)

        main_layout.addLayout(button_layout)
        main_layout.addLayout(table_layout)
        main_layout.addWidget(self.output)



