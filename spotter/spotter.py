from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import os

# it's good practice to have ui as it's own module
import spotter_ui as sui


# needed for windows
class app(sui.SpotterDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.name = "none"
        self.create_connections()

    def show_text(self, text):
        self.output.setText(text)

    def do_search(self,path):
        results = []
        list = os.scandir(path)
        for index, entry in enumerate(list):
            if entry.is_dir() or entry.is_file():
                item = QTableWidgetItem(str(entry))
                count = self.resultTable.rowCount()
                self.resultTable.setRowCount(count+1)
                self.resultTable.setItem(index,0,item)
        list.close()
    def add_item(self):
        self.resultTable.setItem(0,0, QTableWidgetItem("thing"))

    def create_connections(self):
        self.searchBtn.clicked.connect(self.do_search())


spotter = QApplication([])
spotter.setStyle('Fusion')

window = app()
window.show()
spotter.exec_()
