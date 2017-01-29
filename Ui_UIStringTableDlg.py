# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\githubs\pyqtexcel2lua\UIStringTableDlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(677, 344)
        Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 12, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 91, 16))
        self.label_2.setObjectName("label_2")
        self.mExcelPath = QtWidgets.QLineEdit(Dialog)
        self.mExcelPath.setGeometry(QtCore.QRect(120, 10, 461, 20))
        self.mExcelPath.setObjectName("mExcelPath")
        self.mOutputPath = QtWidgets.QLineEdit(Dialog)
        self.mOutputPath.setGeometry(QtCore.QRect(120, 50, 461, 20))
        self.mOutputPath.setObjectName("mOutputPath")
        self.mBroseExcelBtn = QtWidgets.QPushButton(Dialog)
        self.mBroseExcelBtn.setGeometry(QtCore.QRect(590, 10, 75, 23))
        self.mBroseExcelBtn.setObjectName("mBroseExcelBtn")
        self.mLuaPathBtn = QtWidgets.QPushButton(Dialog)
        self.mLuaPathBtn.setGeometry(QtCore.QRect(590, 50, 75, 23))
        self.mLuaPathBtn.setObjectName("mLuaPathBtn")
        self.mOutputBtn = QtWidgets.QPushButton(Dialog)
        self.mOutputBtn.setGeometry(QtCore.QRect(590, 100, 75, 23))
        self.mOutputBtn.setObjectName("mOutputBtn")
        self.mStateTipTxt = QtWidgets.QLabel(Dialog)
        self.mStateTipTxt.setGeometry(QtCore.QRect(30, 90, 54, 12))
        self.mStateTipTxt.setText("")
        self.mStateTipTxt.setObjectName("mStateTipTxt")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Excel文件路径："))
        self.label_2.setText(_translate("Dialog", "输出文件路径："))
        self.mBroseExcelBtn.setText(_translate("Dialog", "浏览"))
        self.mLuaPathBtn.setText(_translate("Dialog", "浏览"))
        self.mOutputBtn.setText(_translate("Dialog", "输出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

