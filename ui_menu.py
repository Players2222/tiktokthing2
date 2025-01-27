# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Main_menu(object):
    def setupUi(self, Main_menu):
        if not Main_menu.objectName():
            Main_menu.setObjectName(u"Main_menu")
        Main_menu.resize(310, 280)
        self.StartB = QPushButton(Main_menu)
        self.StartB.setObjectName(u"StartB")
        self.StartB.setGeometry(QRect(20, 210, 271, 51))
        self.ScriptList = QComboBox(Main_menu)
        self.ScriptList.setObjectName(u"ScriptList")
        self.ScriptList.setGeometry(QRect(20, 50, 271, 28))
        self.VideoList = QComboBox(Main_menu)
        self.VideoList.setObjectName(u"VideoList")
        self.VideoList.setGeometry(QRect(20, 130, 271, 28))
        self.ScriptL = QLabel(Main_menu)
        self.ScriptL.setObjectName(u"ScriptL")
        self.ScriptL.setGeometry(QRect(20, 10, 271, 31))
        self.ScriptL.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.VideoL = QLabel(Main_menu)
        self.VideoL.setObjectName(u"VideoL")
        self.VideoL.setGeometry(QRect(20, 90, 271, 31))
        self.VideoL.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Main_menu)

        QMetaObject.connectSlotsByName(Main_menu)
    # setupUi

    def retranslateUi(self, Main_menu):
        Main_menu.setWindowTitle(QCoreApplication.translate("Main_menu", u"Main_menu", None))
        self.StartB.setText(QCoreApplication.translate("Main_menu", u"Start", None))
        self.ScriptL.setText(QCoreApplication.translate("Main_menu", u"SCRIPT", None))
        self.VideoL.setText(QCoreApplication.translate("Main_menu", u"VIDEO", None))
    # retranslateUi

