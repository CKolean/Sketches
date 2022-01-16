from PySide2 import QtCore
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

    def show_text(self,text):
        self.output.setText(text)
    def do_search(self):
        results = []
        list = os.scandir("C:/Users/Thuule//Documents/maya/scripts")
        for entry in list:
            if entry.is_dir() or entry.is_file():
                results.append(entry)
        list.close()
        self.show_text(str(results))

    def create_connections(self):
        self.searchBtn.clicked.connect(self.do_search)
spotter = QApplication([])
spotter.setStyle('Fusion')

window = app()
window.show()
spotter.exec_()
