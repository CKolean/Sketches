from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
# it's good practice to have ui as it's own module
import spotter_ui as sui
# needed for windows
spotter = QApplication([])
spotter.setStyle('Fusion')

window = sui.SpotterDialog()
window.show()
spotter.exec_()
