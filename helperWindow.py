from PyQt5.QtWidgets import *

import helperWindow_ui


class HelperWindow(QMainWindow, helperWindow_ui.Ui_HelperWindow):
    def __init__(self, parent=None):
        super(HelperWindow, self).__init__(parent)
        self.setupUi(self)
