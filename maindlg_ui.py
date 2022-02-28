# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maindlg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainDlg(object):
    def setupUi(self, MainDlg):
        if not MainDlg.objectName():
            MainDlg.setObjectName(u"MainDlg")
        MainDlg.resize(1076, 936)
        MainDlg.setStyleSheet(u"QWidget{\n"
"	font-size: 30px;\n"
"}")
        self.gridLayoutWidget = QWidget(MainDlg)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 190, 456, 211))
        self.mainLayout = QGridLayout(self.gridLayoutWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.headerLayout.addWidget(self.label)

        self.btnSetting = QPushButton(self.gridLayoutWidget)
        self.btnSetting.setObjectName(u"btnSetting")

        self.headerLayout.addWidget(self.btnSetting)

        self.btnCalibration = QPushButton(self.gridLayoutWidget)
        self.btnCalibration.setObjectName(u"btnCalibration")

        self.headerLayout.addWidget(self.btnCalibration)


        self.mainLayout.addLayout(self.headerLayout, 0, 0, 1, 1)

        self.contentLayout = QGridLayout()
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(10, 10, 10, 10)

        self.mainLayout.addLayout(self.contentLayout, 1, 0, 1, 1)


        self.retranslateUi(MainDlg)

        QMetaObject.connectSlotsByName(MainDlg)
    # setupUi

    def retranslateUi(self, MainDlg):
        MainDlg.setWindowTitle(QCoreApplication.translate("MainDlg", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("MainDlg", u"Logo", None))
        self.btnSetting.setText(QCoreApplication.translate("MainDlg", u"Settings", None))
        self.btnCalibration.setText(QCoreApplication.translate("MainDlg", u"Calibration", None))
    # retranslateUi

