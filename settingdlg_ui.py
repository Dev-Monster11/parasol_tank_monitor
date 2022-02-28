# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingdlg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_SettingDlg(object):
    def setupUi(self, SettingDlg):
        if not SettingDlg.objectName():
            SettingDlg.setObjectName(u"SettingDlg")
        SettingDlg.resize(904, 649)
        SettingDlg.setStyleSheet(u"QWidget{\n"
"	font-size: 30px;\n"
"}")
        self.gridLayoutWidget = QWidget(SettingDlg)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(80, 430, 431, 208))
        self.generalLayout = QGridLayout(self.gridLayoutWidget)
        self.generalLayout.setObjectName(u"generalLayout")
        self.generalLayout.setContentsMargins(10, 10, 10, 10)
        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.generalLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.generalLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.generalLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.generalLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.generalLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.generalLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.generalLayout.addWidget(self.pushButton, 3, 1, 1, 1)

        self.gridLayoutWidget_2 = QWidget(SettingDlg)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(540, 100, 331, 271))
        self.tankLayout = QGridLayout(self.gridLayoutWidget_2)
        self.tankLayout.setObjectName(u"tankLayout")
        self.tankLayout.setContentsMargins(10, 30, 10, 10)
        self.comboBox = QComboBox(self.gridLayoutWidget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.tankLayout.addWidget(self.comboBox, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.gridLayoutWidget_2)
        self.groupBox.setObjectName(u"groupBox")

        self.tankLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.gridLayoutWidget_3 = QWidget(SettingDlg)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(620, 410, 383, 80))
        self.settingLayout = QGridLayout(self.gridLayoutWidget_3)
        self.settingLayout.setObjectName(u"settingLayout")
        self.settingLayout.setContentsMargins(10, 10, 10, 10)
        self.checkBox = QCheckBox(self.gridLayoutWidget_3)
        self.checkBox.setObjectName(u"checkBox")

        self.settingLayout.addWidget(self.checkBox, 0, 0, 1, 1)

        self.gridLayoutWidget_4 = QWidget(SettingDlg)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(550, 510, 160, 86))
        self.mainLayout = QGridLayout(self.gridLayoutWidget_4)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.tabWidget = QTabWidget(self.gridLayoutWidget_4)
        self.tabWidget.setObjectName(u"tabWidget")
        self.generalTab = QWidget()
        self.generalTab.setObjectName(u"generalTab")
        self.tabWidget.addTab(self.generalTab, "")
        self.tankTab = QWidget()
        self.tankTab.setObjectName(u"tankTab")
        self.tabWidget.addTab(self.tankTab, "")

        self.mainLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(SettingDlg)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SettingDlg)
    # setupUi

    def retranslateUi(self, SettingDlg):
        SettingDlg.setWindowTitle(QCoreApplication.translate("SettingDlg", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("SettingDlg", u"WiFi Password", None))
        self.label_3.setText(QCoreApplication.translate("SettingDlg", u"Machine Password", None))
        self.label.setText(QCoreApplication.translate("SettingDlg", u"WiFi Name", None))
        self.pushButton.setText(QCoreApplication.translate("SettingDlg", u"Apply", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("SettingDlg", u"Anolyte Only", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("SettingDlg", u"Analyte & Catholyte", None))

        self.groupBox.setTitle(QCoreApplication.translate("SettingDlg", u"Settings", None))
        self.checkBox.setText(QCoreApplication.translate("SettingDlg", u"External Over Flow Tank?", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generalTab), QCoreApplication.translate("SettingDlg", u"General", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tankTab), QCoreApplication.translate("SettingDlg", u"Tank", None))
    # retranslateUi

