# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_coordtransform.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Coordtransform(object):
    def setupUi(self, Coordtransform):
        Coordtransform.setObjectName("Coordtransform")
        Coordtransform.resize(525, 615)
        self.OK = QtWidgets.QDialogButtonBox(Coordtransform)
        self.OK.setGeometry(QtCore.QRect(342, 580, 171, 32))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.OK.setFont(font)
        self.OK.setOrientation(QtCore.Qt.Horizontal)
        self.OK.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.OK.setObjectName("OK")
        self.X = QtWidgets.QLineEdit(Coordtransform)
        self.X.setGeometry(QtCore.QRect(10, 140, 113, 27))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.X.setFont(font)
        self.X.setObjectName("X")
        self.Y = QtWidgets.QLineEdit(Coordtransform)
        self.Y.setGeometry(QtCore.QRect(140, 140, 113, 27))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.Y.setFont(font)
        self.Y.setObjectName("Y")
        self.results = QtWidgets.QTextBrowser(Coordtransform)
        self.results.setGeometry(QtCore.QRect(10, 400, 501, 141))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.results.setFont(font)
        self.results.setObjectName("results")
        self.label = QtWidgets.QLabel(Coordtransform)
        self.label.setGeometry(QtCore.QRect(10, 100, 281, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Coordtransform)
        self.label_2.setGeometry(QtCore.QRect(44, 120, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Coordtransform)
        self.label_3.setGeometry(QtCore.QRect(176, 120, 41, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.transform = QtWidgets.QPushButton(Coordtransform)
        self.transform.setGeometry(QtCore.QRect(400, 140, 97, 27))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.transform.setFont(font)
        self.transform.setObjectName("transform")
        self.label_6 = QtWidgets.QLabel(Coordtransform)
        self.label_6.setGeometry(QtCore.QRect(20, 380, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.clear = QtWidgets.QPushButton(Coordtransform)
        self.clear.setGeometry(QtCore.QRect(280, 140, 97, 27))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setItalic(False)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.label_8 = QtWidgets.QLabel(Coordtransform)
        self.label_8.setGeometry(QtCore.QRect(110, 10, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(Coordtransform)
        self.line.setGeometry(QtCore.QRect(6, 90, 511, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_7 = QtWidgets.QLabel(Coordtransform)
        self.label_7.setGeometry(QtCore.QRect(10, 250, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(Coordtransform)
        self.label_10.setGeometry(QtCore.QRect(10, 316, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Coordtransform)
        self.label_11.setGeometry(QtCore.QRect(178, 554, 21, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Coordtransform)
        self.label_12.setGeometry(QtCore.QRect(355, 553, 21, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Coordtransform)
        self.label_13.setGeometry(QtCore.QRect(10, 546, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.inputproj4 = QtWidgets.QTextBrowser(Coordtransform)
        self.inputproj4.setGeometry(QtCore.QRect(10, 270, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.inputproj4.setFont(font)
        self.inputproj4.setObjectName("inputproj4")
        self.outputproj4 = QtWidgets.QTextBrowser(Coordtransform)
        self.outputproj4.setGeometry(QtCore.QRect(10, 336, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.outputproj4.setFont(font)
        self.outputproj4.setObjectName("outputproj4")
        self.trfX = QtWidgets.QTextBrowser(Coordtransform)
        self.trfX.setGeometry(QtCore.QRect(210, 546, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.trfX.setFont(font)
        self.trfX.setObjectName("trfX")
        self.trfY = QtWidgets.QTextBrowser(Coordtransform)
        self.trfY.setGeometry(QtCore.QRect(380, 546, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.trfY.setFont(font)
        self.trfY.setObjectName("trfY")
        self.mQgsProjectionSelectionWidgetINPUT = gui.QgsProjectionSelectionWidget(Coordtransform)
        self.mQgsProjectionSelectionWidgetINPUT.setGeometry(QtCore.QRect(100, 177, 391, 27))
        self.mQgsProjectionSelectionWidgetINPUT.setObjectName("mQgsProjectionSelectionWidgetINPUT")
        self.mQgsProjectionSelectionWidgetOUTPUT = gui.QgsProjectionSelectionWidget(Coordtransform)
        self.mQgsProjectionSelectionWidgetOUTPUT.setGeometry(QtCore.QRect(100, 217, 391, 27))
        self.mQgsProjectionSelectionWidgetOUTPUT.setObjectName("mQgsProjectionSelectionWidgetOUTPUT")
        self.label_14 = QtWidgets.QLabel(Coordtransform)
        self.label_14.setGeometry(QtCore.QRect(10, 180, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Coordtransform)
        self.label_15.setGeometry(QtCore.QRect(10, 220, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setItalic(False)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")

        self.retranslateUi(Coordtransform)
        self.OK.accepted.connect(Coordtransform.accept) # type: ignore
        self.OK.rejected.connect(Coordtransform.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Coordtransform)

    def retranslateUi(self, Coordtransform):
        _translate = QtCore.QCoreApplication.translate
        Coordtransform.setWindowTitle(_translate("Coordtransform", "Coordtransform"))
        self.label.setText(_translate("Coordtransform", "USAGE: Input x, y and epsg/user defined values"))
        self.label_2.setText(_translate("Coordtransform", "X / lon"))
        self.label_3.setText(_translate("Coordtransform", "Y / lat"))
        self.transform.setText(_translate("Coordtransform", "Transform"))
        self.label_6.setText(_translate("Coordtransform", "RESULTS"))
        self.clear.setText(_translate("Coordtransform", "Clear"))
        self.label_8.setText(_translate("Coordtransform", "X,Y point coordtransform\n"
" Copyright (C) 2018 Giuseppe De Marco\n"
"www.d2gis.com\n"
"Modifications Jacques Beilin\n"
"ENSG 2024"))
        self.label_7.setText(_translate("Coordtransform", "INPUT EPSG/USER To PROJ4"))
        self.label_10.setText(_translate("Coordtransform", "OUTPUT EPSG/USER To PROJ4"))
        self.label_11.setText(_translate("Coordtransform", "X"))
        self.label_12.setText(_translate("Coordtransform", "Y"))
        self.label_13.setText(_translate("Coordtransform", "TRANSFORMED \n"
"COORDINATES"))
        self.label_14.setText(_translate("Coordtransform", "INPUT CRS"))
        self.label_15.setText(_translate("Coordtransform", "OUTPUT CRS"))
from qgis import gui
