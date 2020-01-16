# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_authform(object):
    def setupUi(self, authform):
        authform.setObjectName("authform")
        authform.resize(237, 157)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        authform.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(authform)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(authform)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.serverStatus = QtWidgets.QLabel(authform)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.serverStatus.setFont(font)
        self.serverStatus.setStyleSheet("color:green;")
        self.serverStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.serverStatus.setObjectName("serverStatus")
        self.horizontalLayout_2.addWidget(self.serverStatus)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(authform)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(authform)
        self.password.setStyleSheet("width: 150px;")
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.login = QtWidgets.QLineEdit(authform)
        self.login.setStyleSheet("width: 150px;")
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(authform)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.submit = QtWidgets.QPushButton(authform)
        self.submit.setObjectName("submit")
        self.horizontalLayout.addWidget(self.submit)
        self.cancel = QtWidgets.QPushButton(authform)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(authform)
        QtCore.QMetaObject.connectSlotsByName(authform)

    def retranslateUi(self, authform):
        _translate = QtCore.QCoreApplication.translate
        authform.setWindowTitle(_translate("authform", "Authorizing to server"))
        self.label.setText(_translate("authform", "Please authorize to server."))
        self.serverStatus.setText(_translate("authform", "Server is now ONLINE"))
        self.label_3.setText(_translate("authform", "Password"))
        self.label_2.setText(_translate("authform", "Login"))
        self.submit.setText(_translate("authform", "   Submit   "))
        self.cancel.setText(_translate("authform", "   Cancel   "))


if __name__ == "__main__":
    import sys
    import qdarkstyle
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    authform = QtWidgets.QDialog()
    ui = Ui_authform()
    ui.setupUi(authform)
    authform.show()
    sys.exit(app.exec_())
