
from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtCore import QTimer, QSize, Qt
from PySide2.QtGui import QPixmap
import qtawesome as qta
import numpy as np
import pyqtgraph as pg

from settingdlg_ui import Ui_SettingDlg



class SettingDlg(QDialog):
    def __init__(self, parent=None):
        super(SettingDlg, self).__init__(parent)
        self.ui = Ui_SettingDlg()
        self.ui.setupUi(self)
        self.setLayout(self.ui.mainLayout)
        self.resize(QSize(640, 480))
        self.setLayout(self.ui.mainLayout)
        self.ui.generalTab.setLayout(self.ui.generalLayout)
        self.ui.tankTab.setLayout(self.ui.tankLayout)
        self.ui.tabWidget.setTabIcon(0, qta.icon('fa5.flag', color='teal'))
        self.ui.tabWidget.setTabIcon(1, qta.icon('fa5.flag', color='teal'))
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)