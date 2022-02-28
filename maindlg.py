
from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtCore import QTimer, QSize, Qt
from PySide2.QtGui import QPixmap
import qtawesome as qta
import numpy as np
import pyqtgraph as pg

from maindlg_ui import Ui_MainDlg
from settingdlg import SettingDlg
from db import DB

class MainDlg(QDialog):
    def __init__(self, parent=None):
        super(MainDlg, self).__init__(parent)
        self.ui = Ui_MainDlg()
        self.ui.setupUi(self)
        self.setLayout(self.ui.mainLayout)
        pg.setConfigOptions(antialias=True)
        colors = [(56, 173, 107), (60, 132, 167), (235, 136, 23), (123, 127, 140)]
        self.legends = []
        self.pw = []
        self.line = []

        for i in range(4):
            self.pw.append(pg.PlotWidget())
            self.pw[i].showGrid(x=True, y=True)
            self.legends.append(pg.LegendItem())
            self.legends[i].setParentItem(self.pw[i].graphicsItem())
            for j in range(4):
                temp = self.pw[i].plot(np.random.normal(size=100), pen=colors[j])
                self.legends[i].addItem(temp, 'Tank')
        self.ui.contentLayout.addWidget(self.pw[0], 0, 0)
        self.ui.contentLayout.addWidget(self.pw[1], 0, 1)
        self.ui.contentLayout.addWidget(self.pw[2], 1, 0)
        self.ui.contentLayout.addWidget(self.pw[3], 1, 1)
        # logoImg = QPixmap("./logo_merge.png").scaled(60, 60, Qt.KeepAspectRatio)
        logoImg = QPixmap("./logo_merge.png")
        # logoSize = logoImg.size()
        self.ui.label.setPixmap(logoImg)

        # brandImg = QPixmap("./brand.png").scaledToHeight(logoImg.height())
        # # logoSize = logoImg.size()
        # self.ui.label_2.setPixmap(brandImg)

        self.ui.btnSetting.setIcon(qta.icon('fa.cogs', color='teal'))
        self.ui.btnCalibration.setIcon(qta.icon('fa5s.blind', color='teal'))
        self.ui.btnSetting.setIconSize(QSize(32, 32))
        self.ui.btnCalibration.setIconSize(QSize(32, 32))

        self.settingdlg = SettingDlg(self)

        self.ui.btnSetting.clicked.connect(self.btnSettings_clicked)
        self.ui.btnCalibration.clicked.connect(self.btnCalibration_clicked)
        # pw1 = pg.PlotWidget()
        # pw1.showGrid(x=True, y=True)
        # self.leveldata = np.random.normal(size=(1))

        # self.tank0_level = pw1.plot(pen=(56, 173, 107), name="tank0")
        # tank1_level = pw1.plot(np.random.normal(size=100), pen=(60, 132, 167), name="tank1")
        # tank2_level = pw1.plot(np.random.normal(size=100), pen=(235, 136, 23), name="tank2")
        # tank3_level = pw1.plot(np.random.normal(size=100), pen=(123, 127, 140), name="tank3")
        # pw2 = pg.PlotWidget()
        # pw2.plot([1,2,3,4])

        # pw3 = pg.PlotWidget()
        # pw3.plot([1,2,3,4])
        # pw4 = pg.PlotWidget()
        # pw4.plot([1,2,3,4])

        # self.ui.contentLayout.addWidget(pw1, 0, 0)
        # self.ui.contentLayout.addWidget(pw2, 0, 1)
        # self.ui.contentLayout.addWidget(pw3, 1, 0)
        # self.ui.contentLayout.addWidget(pw4, 1, 1)
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.update)
        # self.timer.start(5000)
        # legend = pg.LegendItem((80,60), offset=(70,20))
        # legend.setParentItem(pw1.graphicsItem())
        # legend.addItem(self.tank0_level, 'Tank0')
        # self.ptr = 0
    def update(self):
        self.tank0_level.setData(self.leveldata[self.ptr%10])
        if self.ptr == 0:
            self.tank0_level.enableAutoRange('xy', False)
        self.ptr += 1
    def btnSettings_clicked(self):

        self.settingdlg.exec()
    def btnCalibration_clicked(self):

        a = DB()
        a.insertDemo((1, 1.4, 1.4, 80, 1.5, 50, '2021-02-02 01:01:01'))