# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 631)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 780, 611))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.ipLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.ipLabel.setFont(font)
        self.ipLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ipLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ipLabel.setObjectName("ipLabel")
        self.gridLayout.addWidget(self.ipLabel, 0, 0, 1, 1)
        self.locationLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.locationLabel.setFont(font)
        self.locationLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.locationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.locationLabel.setObjectName("locationLabel")
        self.gridLayout.addWidget(self.locationLabel, 0, 2, 1, 1)
        self.typeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.typeLabel.setFont(font)
        self.typeLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.typeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.typeLabel.setObjectName("typeLabel")
        self.gridLayout.addWidget(self.typeLabel, 0, 4, 1, 1)
        self.delayLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.delayLabel.setFont(font)
        self.delayLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.delayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.delayLabel.setObjectName("delayLabel")
        self.gridLayout.addWidget(self.delayLabel, 0, 3, 1, 1)
        self.portLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.portLabel.setFont(font)
        self.portLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.portLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.portLabel.setObjectName("portLabel")
        self.gridLayout.addWidget(self.portLabel, 0, 1, 1, 1)
        self.ipList = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.ipList.setStyleSheet("border: 0px;")
        self.ipList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ipList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ipList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ipList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ipList.setProperty("showDropIndicator", False)
        self.ipList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.ipList.setAlternatingRowColors(True)
        self.ipList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ipList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ipList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.ipList.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ipList.setMovement(QtWidgets.QListView.Static)
        self.ipList.setFlow(QtWidgets.QListView.TopToBottom)
        self.ipList.setProperty("isWrapping", False)
        self.ipList.setResizeMode(QtWidgets.QListView.Adjust)
        self.ipList.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.ipList.setViewMode(QtWidgets.QListView.ListMode)
        self.ipList.setUniformItemSizes(False)
        self.ipList.setWordWrap(False)
        self.ipList.setSelectionRectVisible(True)
        self.ipList.setObjectName("ipList")
        self.gridLayout.addWidget(self.ipList, 1, 0, 1, 1)
        self.ipList_19 = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.ipList_19.setStyleSheet("border: 0px;")
        self.ipList_19.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ipList_19.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ipList_19.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ipList_19.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ipList_19.setProperty("showDropIndicator", False)
        self.ipList_19.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.ipList_19.setAlternatingRowColors(True)
        self.ipList_19.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ipList_19.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ipList_19.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.ipList_19.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ipList_19.setMovement(QtWidgets.QListView.Static)
        self.ipList_19.setFlow(QtWidgets.QListView.TopToBottom)
        self.ipList_19.setProperty("isWrapping", False)
        self.ipList_19.setResizeMode(QtWidgets.QListView.Adjust)
        self.ipList_19.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.ipList_19.setViewMode(QtWidgets.QListView.ListMode)
        self.ipList_19.setUniformItemSizes(False)
        self.ipList_19.setWordWrap(False)
        self.ipList_19.setSelectionRectVisible(True)
        self.ipList_19.setObjectName("ipList_19")
        self.gridLayout.addWidget(self.ipList_19, 1, 1, 1, 1)
        self.ipList_18 = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.ipList_18.setStyleSheet("border: 0px;")
        self.ipList_18.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ipList_18.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ipList_18.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ipList_18.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ipList_18.setProperty("showDropIndicator", False)
        self.ipList_18.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.ipList_18.setAlternatingRowColors(True)
        self.ipList_18.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ipList_18.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ipList_18.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.ipList_18.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ipList_18.setMovement(QtWidgets.QListView.Static)
        self.ipList_18.setFlow(QtWidgets.QListView.TopToBottom)
        self.ipList_18.setProperty("isWrapping", False)
        self.ipList_18.setResizeMode(QtWidgets.QListView.Adjust)
        self.ipList_18.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.ipList_18.setViewMode(QtWidgets.QListView.ListMode)
        self.ipList_18.setUniformItemSizes(False)
        self.ipList_18.setWordWrap(False)
        self.ipList_18.setSelectionRectVisible(True)
        self.ipList_18.setObjectName("ipList_18")
        self.gridLayout.addWidget(self.ipList_18, 1, 2, 1, 1)
        self.ipList_17 = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.ipList_17.setStyleSheet("border: 0px;")
        self.ipList_17.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ipList_17.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ipList_17.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ipList_17.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ipList_17.setProperty("showDropIndicator", False)
        self.ipList_17.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.ipList_17.setAlternatingRowColors(True)
        self.ipList_17.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ipList_17.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ipList_17.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.ipList_17.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ipList_17.setMovement(QtWidgets.QListView.Static)
        self.ipList_17.setFlow(QtWidgets.QListView.TopToBottom)
        self.ipList_17.setProperty("isWrapping", False)
        self.ipList_17.setResizeMode(QtWidgets.QListView.Adjust)
        self.ipList_17.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.ipList_17.setViewMode(QtWidgets.QListView.ListMode)
        self.ipList_17.setUniformItemSizes(False)
        self.ipList_17.setWordWrap(False)
        self.ipList_17.setSelectionRectVisible(True)
        self.ipList_17.setObjectName("ipList_17")
        self.gridLayout.addWidget(self.ipList_17, 1, 4, 1, 1)
        self.ipList_16 = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.ipList_16.setStyleSheet("border: 0px;")
        self.ipList_16.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ipList_16.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ipList_16.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ipList_16.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ipList_16.setProperty("showDropIndicator", False)
        self.ipList_16.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.ipList_16.setAlternatingRowColors(True)
        self.ipList_16.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ipList_16.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ipList_16.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.ipList_16.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ipList_16.setMovement(QtWidgets.QListView.Static)
        self.ipList_16.setFlow(QtWidgets.QListView.TopToBottom)
        self.ipList_16.setProperty("isWrapping", False)
        self.ipList_16.setResizeMode(QtWidgets.QListView.Adjust)
        self.ipList_16.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.ipList_16.setViewMode(QtWidgets.QListView.ListMode)
        self.ipList_16.setUniformItemSizes(False)
        self.ipList_16.setWordWrap(False)
        self.ipList_16.setSelectionRectVisible(True)
        self.ipList_16.setObjectName("ipList_16")
        self.gridLayout.addWidget(self.ipList_16, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)

        self.listwidgets = [self.ipList, self.ipList_16,self.ipList_17,self.ipList_18,self.ipList_19]
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        for item in self.listwidgets:
            itemlist = [str(val) for val in range(0,200)]
            print(itemlist)
            item.addItems(itemlist)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ipLabel.setText(_translate("Dialog", "IP adress "))
        self.locationLabel.setText(_translate("Dialog", "Country, City "))
        self.typeLabel.setText(_translate("Dialog", "Type "))
        self.delayLabel.setText(_translate("Dialog", "Delay "))
        self.portLabel.setText(_translate("Dialog", "Port "))
        self.ipList.setSortingEnabled(False)
        self.ipList_19.setSortingEnabled(False)
        self.ipList_18.setSortingEnabled(False)
        self.ipList_17.setSortingEnabled(False)
        self.ipList_16.setSortingEnabled(False)
        # connet the scroll bar signle to our slot
        self.ipList.verticalScrollBar().valueChanged.connect(self.__chnge_position)
        self.ipList_16.verticalScrollBar().valueChanged.connect(self.__chnge_position)
        self.ipList_17.verticalScrollBar().valueChanged.connect(self.__chnge_position)
        self.ipList_18.verticalScrollBar().valueChanged.connect(self.__chnge_position)
        self.ipList_19.verticalScrollBar().valueChanged.connect(self.__chnge_position)
    def __chnge_position(self,index):
        #slot to change the scroll bar  position of all table
        self.ipList.verticalScrollBar().setValue(index)
        self.ipList_16.verticalScrollBar().setValue(index)
        self.ipList_17.verticalScrollBar().setValue(index)
        self.ipList_18.verticalScrollBar().setValue(index)
        self.ipList_19.verticalScrollBar().setValue(index)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())