# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helperWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelperWindow(object):
    def setupUi(self, HelperWindow):
        HelperWindow.setObjectName("HelperWindow")
        HelperWindow.resize(837, 727)
        self.centralwidget = QtWidgets.QWidget(HelperWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        HelperWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelperWindow)
        QtCore.QMetaObject.connectSlotsByName(HelperWindow)

    def retranslateUi(self, HelperWindow):
        _translate = QtCore.QCoreApplication.translate
        HelperWindow.setWindowTitle(_translate("HelperWindow", "Active Contours Helper Window"))

