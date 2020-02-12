# -*- coding: utf-8 -*-
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRunnable, pyqtSlot, pyqtSignal, QObject, QThread, QThreadPool
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import time
import random
import requests
import json
import time
import re
import datetime
import sys
from functools import partial
def nowINFOMAIN():
    now = datetime.datetime.now()
    prefix = str(' - [ID:MAIN/INFO] -')
    result = now.strftime("%X") + prefix
    return result
def nowERRORMAIN():
    now = datetime.datetime.now()
    prefix = str(' - [ID:MAIN/ERROR] -')
    result = now.strftime("%X") + prefix
    return result

########################################################################BLOCK 1 - Code begin###########################################################################

class Ui_DropBot(object):
    SizeRangeInit = np.arange(3.5, 15, 0.5)
    SizeRange = []
    for item in SizeRangeInit:
        item = str(format(item, '.10g')) + ' US'
        SizeRange.append(item)
    LocalVars = locals()
    def setupUi(self, DropBot):
        global LogOutput
        DropBot.setObjectName("DropBot")
        DropBot.resize(1300, 793)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DropBot.sizePolicy().hasHeightForWidth())
        DropBot.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 151))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 100, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 151))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 100, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 151))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 80, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        DropBot.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(DropBot)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftLayout = QtWidgets.QVBoxLayout()
        self.leftLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.leftLayout.setSpacing(6)
        self.leftLayout.setObjectName("leftLayout")
        self.DropBotLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DropBotLabel.setFont(font)
        self.DropBotLabel.setStyleSheet("font: 25pt \"Ubuntu\";")
        self.DropBotLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DropBotLabel.setObjectName("DropBotLabel")
        self.leftLayout.addWidget(self.DropBotLabel)
        self.GridButtonsLayout = QtWidgets.QGridLayout()
        self.GridButtonsLayout.setContentsMargins(-1, 0, -1, 0)
        self.GridButtonsLayout.setSpacing(0)
        self.GridButtonsLayout.setObjectName("GridButtonsLayout")
        self.TextLabelLayout = QtWidgets.QVBoxLayout()
        self.TextLabelLayout.setObjectName("TextLabelLayout")
        self.ProfileLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProfileLabel.sizePolicy().hasHeightForWidth())
        self.ProfileLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ProfileLabel.setFont(font)
        self.ProfileLabel.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.ProfileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ProfileLabel.setObjectName("ProfileLabel")
        self.TextLabelLayout.addWidget(self.ProfileLabel)
        self.ModelLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ModelLabel.sizePolicy().hasHeightForWidth())
        self.ModelLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ModelLabel.setFont(font)
        self.ModelLabel.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.ModelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ModelLabel.setObjectName("ModelLabel")
        self.TextLabelLayout.addWidget(self.ModelLabel)
        self.SizeLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SizeLabel.sizePolicy().hasHeightForWidth())
        self.SizeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.SizeLabel.setFont(font)
        self.SizeLabel.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.SizeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SizeLabel.setObjectName("SizeLabel")
        self.TextLabelLayout.addWidget(self.SizeLabel)
        self.TaskCountLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TaskCountLabel.sizePolicy().hasHeightForWidth())
        self.TaskCountLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.TaskCountLabel.setFont(font)
        self.TaskCountLabel.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.TaskCountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TaskCountLabel.setObjectName("TaskCountLabel")
        self.TextLabelLayout.addWidget(self.TaskCountLabel)
        self.ProxyConfigLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProxyConfigLabel.sizePolicy().hasHeightForWidth())
        self.ProxyConfigLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ProxyConfigLabel.setFont(font)
        self.ProxyConfigLabel.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.ProxyConfigLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ProxyConfigLabel.setObjectName("ProxyConfigLabel")
        self.TextLabelLayout.addWidget(self.ProxyConfigLabel)
        self.GridButtonsLayout.addLayout(self.TextLabelLayout, 0, 0, 1, 1)
        self.LeftButtonsLayout = QtWidgets.QVBoxLayout()
        self.LeftButtonsLayout.setObjectName("LeftButtonsLayout")
        self.ProfileButtonsLayout = QtWidgets.QHBoxLayout()
        self.ProfileButtonsLayout.setContentsMargins(70, 20, 10, 20)
        self.ProfileButtonsLayout.setObjectName("ProfileButtonsLayout")
        self.ProfileComboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProfileComboBox.sizePolicy().hasHeightForWidth())
        self.ProfileComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.ProfileComboBox.setFont(font)
        self.ProfileComboBox.setStyleSheet("")
        self.ProfileComboBox.setIconSize(QtCore.QSize(16, 16))
        self.ProfileComboBox.setFrame(True)
        self.ProfileComboBox.setObjectName("ProfileComboBox")
        self.ProfileButtonsLayout.addWidget(self.ProfileComboBox)
        self.EditProfile = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EditProfile.sizePolicy().hasHeightForWidth())
        self.EditProfile.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.EditProfile.setFont(font)
        self.EditProfile.setStyleSheet("margin-left:10; border-radius: ")
        self.EditProfile.setObjectName("EditProfile")
        self.ProfileButtonsLayout.addWidget(self.EditProfile)
        self.LeftButtonsLayout.addLayout(self.ProfileButtonsLayout)
        self.ModelLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ModelLineEdit.sizePolicy().hasHeightForWidth())
        self.ModelLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.ModelLineEdit.setFont(font)
        self.ModelLineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ModelLineEdit.setToolTip("")
        self.ModelLineEdit.setStyleSheet(".QLineEdit {margin-left:70; margin-top:20; margin-bottom:20; margin-right:60;}")
        self.ModelLineEdit.setObjectName("ModelLineEdit")
        self.LeftButtonsLayout.addWidget(self.ModelLineEdit)
        self.SizeButtonsLayout = QtWidgets.QHBoxLayout()
        self.SizeButtonsLayout.setContentsMargins(70, 20, 10, 20)
        self.SizeButtonsLayout.setObjectName("SizeButtonsLayout")
        self.SizeComboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SizeComboBox.sizePolicy().hasHeightForWidth())
        self.SizeComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.SizeComboBox.setFont(font)
        self.SizeComboBox.setStyleSheet("")
        self.SizeComboBox.setIconSize(QtCore.QSize(16, 16))
        self.SizeComboBox.setFrame(True)
        self.SizeComboBox.setObjectName("SizeComboBox")
        self.SizeComboBox.addItems(self.SizeRange)
        self.SizeButtonsLayout.addWidget(self.SizeComboBox)
        self.EditSize = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EditSize.sizePolicy().hasHeightForWidth())
        self.EditSize.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.EditSize.setFont(font)
        self.EditSize.setStyleSheet("margin-left:10; border-radius: ")
        self.EditSize.setObjectName("EditSize")
        self.SizeButtonsLayout.addWidget(self.EditSize)
        self.LeftButtonsLayout.addLayout(self.SizeButtonsLayout)
        self.TaskCountLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TaskCountLineEdit.sizePolicy().hasHeightForWidth())
        self.TaskCountLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.TaskCountLineEdit.setFont(font)
        self.TaskCountLineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.TaskCountLineEdit.setToolTip("")
        self.TaskCountLineEdit.setStyleSheet(".QLineEdit {margin-left:70; margin-top:20; margin-bottom:20; margin-right:60;}")
        self.TaskCountLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.TaskCountLineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.TaskCountLineEdit.setClearButtonEnabled(False)
        self.TaskCountLineEdit.setObjectName("TaskCountLineEdit")
        self.onlyInt = QtGui.QIntValidator()
        self.TaskCountLineEdit.setValidator(self.onlyInt)
        self.LeftButtonsLayout.addWidget(self.TaskCountLineEdit)
        self.ProxyConfigLayout = QtWidgets.QHBoxLayout()
        self.ProxyConfigLayout.setContentsMargins(70, 20, 10, 20)
        self.ProxyConfigLayout.setObjectName("ProxyConfigLayout")
        self.ProxyConfigComboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProxyConfigComboBox.sizePolicy().hasHeightForWidth())
        self.ProxyConfigComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.ProxyConfigComboBox.setFont(font)
        self.ProxyConfigComboBox.setAutoFillBackground(False)
        self.ProxyConfigComboBox.setStyleSheet("")
        self.ProxyConfigComboBox.setIconSize(QtCore.QSize(16, 16))
        self.ProxyConfigComboBox.setFrame(True)
        self.ProxyConfigComboBox.setObjectName("ProxyConfigComboBox")
        self.ProxyConfigLayout.addWidget(self.ProxyConfigComboBox)
        self.ProxyConfigEdit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProxyConfigEdit.sizePolicy().hasHeightForWidth())
        self.ProxyConfigEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.ProxyConfigEdit.setFont(font)
        self.ProxyConfigEdit.setStyleSheet("margin-left:10; border-radius: ")
        self.ProxyConfigEdit.setObjectName("ProxyConfigEdit")
        self.ProxyConfigLayout.addWidget(self.ProxyConfigEdit)
        self.LeftButtonsLayout.addLayout(self.ProxyConfigLayout)
        self.GridButtonsLayout.addLayout(self.LeftButtonsLayout, 0, 1, 1, 1)
        self.leftLayout.addLayout(self.GridButtonsLayout)
        self.LeftDownLayout = QtWidgets.QVBoxLayout()
        self.LeftDownLayout.setObjectName("LeftDownLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.CreateTaskButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateTaskButton.sizePolicy().hasHeightForWidth())
        self.CreateTaskButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CreateTaskButton.setFont(font)
        self.CreateTaskButton.setStyleSheet("margin-left: 150; margin-right:150; margin-top: 5; margin-bottom: 5; height: 40px; padding-left: 15px; padding-right:15px;")
        self.CreateTaskButton.setObjectName("CreateTaskButton")
        self.horizontalLayout_2.addWidget(self.CreateTaskButton)
        self.LeftDownLayout.addLayout(self.horizontalLayout_2)
        self.LogOutput = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LogOutput.sizePolicy().hasHeightForWidth())
        self.LogOutput.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 100, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 100, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 80, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.LogOutput.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(8)
        self.LogOutput.setFont(font)
        self.LogOutput.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LogOutput.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.LogOutput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LogOutput.setAutoFillBackground(True)
        self.LogOutput.setStyleSheet("")
        self.LogOutput.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LogOutput.setLineWidth(0)
        self.LogOutput.setDocumentTitle("")
        self.LogOutput.setUndoRedoEnabled(False)
        self.LogOutput.setReadOnly(True)
        self.LogOutput.setObjectName("LogOutput")
        self.LeftDownLayout.addWidget(self.LogOutput)
        self.leftLayout.addLayout(self.LeftDownLayout)
        self.horizontalLayout.addLayout(self.leftLayout)
        self.RightLayout = QtWidgets.QVBoxLayout()
        self.RightLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.RightLayout.setObjectName("RightLayout")
        self.TaskManagerLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TaskManagerLabel.sizePolicy().hasHeightForWidth())
        self.TaskManagerLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.TaskManagerLabel.setFont(font)
        self.TaskManagerLabel.setStyleSheet("font: 25pt \"Ubuntu\";")
        self.TaskManagerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TaskManagerLabel.setObjectName("TaskManagerLabel")
        self.RightLayout.addWidget(self.TaskManagerLabel)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ID0 = QtWidgets.QLabel(self.centralwidget)
        self.ID0.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ID0.sizePolicy().hasHeightForWidth())
        self.ID0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.ID0.setFont(font)
        self.ID0.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ID0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ID0.setAlignment(QtCore.Qt.AlignCenter)
        self.ID0.setObjectName("ID0")
        self.horizontalLayout_4.addWidget(self.ID0)
        self.PROXY0 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PROXY0.sizePolicy().hasHeightForWidth())
        self.PROXY0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.PROXY0.setFont(font)
        self.PROXY0.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.PROXY0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PROXY0.setAlignment(QtCore.Qt.AlignCenter)
        self.PROXY0.setObjectName("PROXY0")
        self.horizontalLayout_4.addWidget(self.PROXY0)
        self.SIZE0 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SIZE0.sizePolicy().hasHeightForWidth())
        self.SIZE0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.SIZE0.setFont(font)
        self.SIZE0.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.SIZE0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SIZE0.setAlignment(QtCore.Qt.AlignCenter)
        self.SIZE0.setObjectName("SIZE0")
        self.horizontalLayout_4.addWidget(self.SIZE0)
        self.MODEL0 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MODEL0.sizePolicy().hasHeightForWidth())
        self.MODEL0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.MODEL0.setFont(font)
        self.MODEL0.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.MODEL0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MODEL0.setAlignment(QtCore.Qt.AlignCenter)
        self.MODEL0.setObjectName("MODEL0")
        self.horizontalLayout_4.addWidget(self.MODEL0)
        self.SITE0 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SITE0.sizePolicy().hasHeightForWidth())
        self.SITE0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.SITE0.setFont(font)
        self.SITE0.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.SITE0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SITE0.setStyleSheet("height:32px;")
        self.SITE0.setAlignment(QtCore.Qt.AlignCenter)
        self.SITE0.setObjectName("SITE0")
        self.horizontalLayout_4.addWidget(self.SITE0)
        self.STATUS0 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STATUS0.sizePolicy().hasHeightForWidth())
        self.STATUS0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.STATUS0.setFont(font)
        self.STATUS0.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.STATUS0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.STATUS0.setAlignment(QtCore.Qt.AlignCenter)
        self.STATUS0.setObjectName("STATUS0")
        self.horizontalLayout_4.addWidget(self.STATUS0)
        self.REMOVE0 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.REMOVE0.sizePolicy().hasHeightForWidth())
        self.REMOVE0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.REMOVE0.setFont(font)
        self.REMOVE0.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.REMOVE0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.REMOVE0.setAlignment(QtCore.Qt.AlignCenter)
        self.REMOVE0.setObjectName("REMOVE0")
        self.horizontalLayout_4.addWidget(self.REMOVE0)
        self.RightLayout.addLayout(self.horizontalLayout_4)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet(".QScrollArea {border: 0.5px solid #32414B; border-radius: 20%;}\n"
".QPushButton{height: 24px; width: 24px; background-color: rgb(228, 70, 70); background-image: url(bin.png);\n"
"border: 1px solid rgb(228, 70, 70);\n"
"margin-left: 10px; margin-right: auto;\n"
"border-radius: 15px;\n"
"background-repeat:no-repeat;\n"
"background-position:center;}\n"
".QPushButton:hover {\n"
"border: 2px solid white;\n"
"}\n"
".QLabel {font: 10pt \"Ubuntu\";}\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setAlignment(QtCore.Qt.AlignTop)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.RightLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.RightLayout)
        DropBot.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(DropBot)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1300, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTheme = QtWidgets.QMenu(self.menuBar)
        self.menuTheme.setObjectName("menuTheme")
        self.menuTheme_2 = QtWidgets.QMenu(self.menuTheme)
        self.menuTheme_2.setObjectName("menuTheme_2")
        DropBot.setMenuBar(self.menuBar)
        self.actionWebsite = QtWidgets.QAction(DropBot)
        self.actionWebsite.setObjectName("actionWebsite")
        self.actionEdit_profile = QtWidgets.QAction(DropBot)
        self.actionEdit_profile.setObjectName("actionEdit_profile")
        self.actionEdit_size_list = QtWidgets.QAction(DropBot)
        self.actionEdit_size_list.setObjectName("actionEdit_size_list")
        self.actionProxy_checker = QtWidgets.QAction(DropBot)
        self.actionProxy_checker.setObjectName("actionProxy_checker")
        self.actionEdit_proxy_config = QtWidgets.QAction(DropBot)
        self.actionEdit_proxy_config.setObjectName("actionEdit_proxy_config")
        self.actionDark = QtWidgets.QAction(DropBot)
        self.actionDark.setObjectName("actionDark")
        self.actionLight = QtWidgets.QAction(DropBot)
        self.actionLight.setObjectName("actionLight")
        self.menuFile.addAction(self.actionEdit_profile)
        self.menuFile.addAction(self.actionEdit_size_list)
        self.menuFile.addAction(self.actionProxy_checker)
        self.menuFile.addAction(self.actionEdit_proxy_config)
        self.menuHelp.addAction(self.actionWebsite)
        self.menuTheme_2.addAction(self.actionDark)
        self.menuTheme_2.addAction(self.actionLight)
        self.menuTheme.addAction(self.menuTheme_2.menuAction())
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTheme.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(DropBot)
        QtCore.QMetaObject.connectSlotsByName(DropBot)

    def retranslateUi(self, DropBot):
        _translate = QtCore.QCoreApplication.translate
        DropBot.setWindowTitle(_translate("DropBot", "DropBot"))
        self.DropBotLabel.setText(_translate("DropBot", "DropBot Settings"))
        self.ProfileLabel.setText(_translate("DropBot", "Profile:"))
        self.ModelLabel.setText(_translate("DropBot", "Model:"))
        self.SizeLabel.setText(_translate("DropBot", "Size:"))
        self.TaskCountLabel.setText(_translate("DropBot", "Task count:"))
        self.ProxyConfigLabel.setText(_translate("DropBot", "Proxy config:"))
        self.EditProfile.setText(_translate("DropBot", "   Edit   "))
        self.EditSize.setText(_translate("DropBot", "   Help   "))
        self.EditSize.clicked.connect(self.SizeHelp)
        self.EditProfile.clicked.connect(self.profileedit)
        self.ProxyConfigEdit.setText(_translate("DropBot", "   Edit   "))
        self.ProxyConfigEdit.clicked.connect(self.ProxyConfig)
        self.CreateTaskButton.setText(_translate("DropBot", "ADD TASK"))
        self.CreateTaskButton.clicked.connect(self.AddTaskToFile)
        self.LogOutput.setHtml(_translate("DropBot", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\';\"><br /></p></body></html>"))
        self.TaskManagerLabel.setText(_translate("DropBot", "Task Manager"))
        self.PROXY0.setText(_translate("DropBot", "PROXY"))
        self.SITE0.setText(_translate("DropBot", "SITE"))
        self.ID0.setText(_translate("DropBot", "   ID"))
        self.MODEL0.setText(_translate("DropBot", "MODEL"))
        self.REMOVE0.setText(_translate("DropBot", " "))
        self.SIZE0.setText(_translate("DropBot", "SIZE"))
        self.STATUS0.setText(_translate("DropBot", "STATUS"))
        self.menuFile.setTitle(_translate("DropBot", "File"))
        self.menuHelp.setTitle(_translate("DropBot", "Help"))
        self.menuTheme.setTitle(_translate("DropBot", "Settings"))
        self.menuTheme_2.setTitle(_translate("DropBot", "Theme"))
        self.actionWebsite.setText(_translate("DropBot", "Website"))
        self.actionEdit_profile.setText(_translate("DropBot", "Edit profile"))
        self.actionEdit_profile.triggered.connect(self.profileedit)
        self.actionEdit_size_list.setText(_translate("DropBot", "International size chart"))
        self.actionEdit_size_list.triggered.connect(self.SizeHelp)
        self.actionProxy_checker.setText(_translate("DropBot", "Proxy checker"))
        self.actionEdit_proxy_config.setText(_translate("DropBot", "Edit proxy config"))
        self.actionDark.setText(_translate("DropBot", "Dark"))
        self.actionLight.setText(_translate("DropBot", "Light"))
        self.ProxyConfigComboBox.addItem('None')
        
        ########################################################################BLOCK 2###########################################################################

    def loadSave(self):
        try:
            file = open('save.json', 'r', encoding='utf-8').read()
        except:
            log = nowERRORMAIN() + ' Save file not found, creating new one...'
            self.LogOutput.append(log)
            open('save.json', 'w', encoding='utf-8').close()
            data = open('save.json', 'r', encoding='utf-8')
            file = data.read()
            data.close()
        else:
            log = nowINFOMAIN() + ' Save file founded, loading profiles.'
            self.LogOutput.append(log)
        try:
            jsondata = json.loads(file, encoding = 'utf-8')
            jsondata['Tasks']
            jsondata['Profiles']
            jsondata['ProxyConfigs']
        except:
            file = open("save.json", "r+", encoding='utf-8')
            json.dump({'Profiles': [], 'Tasks' : [], 'ProxyConfigs' : []}, file)
            try:
                jsondata = json.loads(file.read(), encoding='utf-8')
                jsondata['Tasks']
                jsondata['Profiles']
                jsondata['ProxyConfigs']
            except:
                file.close()
                open('save.json', 'w', encoding='utf-8').close()
                file = open("save.json", "r+", encoding='utf-8')
                json.dump({'Profiles': [], 'Tasks' : [], 'ProxyConfigs' : []}, file)
                file.close()
                self.LogOutput.clear()
                log = nowERRORMAIN() + ' Save file corrupted, creating new one...'
                self.LogOutput.append(log)
                self.loadSave()
            file.close()
        else:
            if file == '{"Profiles": [], "Tasks" : [], "ProxyConfigs" : []}':
                log = nowERRORMAIN() + ' No profiles founded, please, create a new one.'
                self.LogOutput.append(log)
            else:
                try:
                    profilenames = []
                    for dicts in jsondata['Profiles']:
                        profilenames.append(dicts['profilename'])
                        if dicts['profilename'] == '':
                            open('save.json', 'w', encoding='utf-8').close()
                            file = open("save.json", "r+", encoding='utf-8')
                            json.dump({'Profiles': [], 'Tasks' : [], 'ProxyConfigs' : []}, file)
                            file.close()
                            self.LogOutput.clear()
                            log = nowERRORMAIN() + ' Save file corrupted, creating new one...'
                            self.LogOutput.append(log)
                            self.loadSave()
                    self.ProfileComboBox.clear()
                    self.ProfileComboBox.addItems(profilenames)
                    log = nowINFOMAIN() + ' Profiles succesefully updated!'
                    self.LogOutput.append(log)
                    proxyprofilenames = []
                    for dicts in jsondata['ProxyConfigs']:
                        proxyprofilenames.append(dicts['profilename'])
                        if dicts['profilename'] == '':
                            open('save.json', 'w', encoding='utf-8').close()
                            file = open("save.json", "r+", encoding='utf-8')
                            json.dump({'Profiles': [], 'Tasks' : [], 'ProxyConfigs' : []}, file)
                            file.close()
                            self.LogOutput.clear()
                            log = nowERRORMAIN() + ' Save file corrupted, creating new one...'
                            self.LogOutput.append(log)
                            self.loadSave()
                    proxyprofilenames.append('None')
                    self.ProxyConfigComboBox.clear()
                    self.ProxyConfigComboBox.addItems(proxyprofilenames)
                    self.rldTasks()
                except Exception as e:
                    print(e)
                    open('save.json', 'w', encoding='utf-8').close()
                    file = open("save.json", "r+", encoding='utf-8')
                    json.dump({'Profiles': [], 'Tasks' : [], 'ProxyConfigs' : []}, file)
                    file.close()
                    self.LogOutput.clear()
                    log = nowERRORMAIN() + ' Save file corrupted, creating new one...'
                    self.LogOutput.append(log)
                    self.loadSave()
    def resetProfiles(self):
        self.ProfileComboBox.clear()
    def profileedit(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_ProfileManager()
        dialog.ui.setupUi(dialog)
        dialog.ui.Save.clicked.connect(self.loadSave)
        dialog.ui.Reset.clicked.connect(self.loadSave)
        dialog.ui.Reset.clicked.connect(self.resetProfiles)
        dialog.setWindowIcon(QtGui.QIcon('icon2.png'))
        dialog.exec_()
        dialog.show()
    def authDialog(self):
        global authform
        global threadpool
        threadpool = QThreadPool()
        threadpool.setMaxThreadCount(2)
        print("Multithreading with maximum %d threads" % threadpool.maxThreadCount())
        authform = QtWidgets.QDialog()
        authform.ui = Ui_authform()
        authform.ui.setupUi(authform)
        authform.setWindowIcon(QtGui.QIcon('icon2.png'))
        authform.show()
        authform.ui.checkConnection()
    def SizeHelp(self):
        sizeHelp = QtWidgets.QDialog()
        sizeHelp.ui = Ui_SizeChart()
        sizeHelp.ui.setupUi(sizeHelp)
        sizeHelp.setWindowIcon(QtGui.QIcon('icon2.png'))
        sizeHelp.exec_()
        sizeHelp.show()
    def ProxyConfig(self):
        proxyConfig = QtWidgets.QDialog()
        proxyConfig.ui = Ui_ProxyConfig()
        proxyConfig.ui.setupUi(proxyConfig)
        proxyConfig.setWindowIcon(QtGui.QIcon('icon2.png'))
        proxyConfig.ui.pushButton.clicked.connect(self.loadSave)
        proxyConfig.exec_()
        proxyConfig.show()
    def RemoveTask(self, ID):
        LocalVars = locals()
        file = open('save.json','r', encoding='utf-8')
        jsondata = json.loads(file.read(), encoding='utf-8')
        file.close()
        log = nowINFOMAIN() + ' Removing task with ID ' + ID + ' from task manager' 
        self.LogOutput.append(log)
        LAYOUT_NAME = 'THREAD' + ID
        def deleteItems(layout):
            if layout is not None:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                       widget.deleteLater()
                    else:
                        deleteItems(item.layout())
        deleteItems(self.LocalVars[LAYOUT_NAME])
        try:
            file = open('save.json', 'r', encoding='utf-8')
            jsondata = json.loads(file.read(), encoding='utf-8')
            file.close()
        except:
            self.loadSave()
        iteration = 0
        for task in jsondata['Tasks']:
            if task['taskID'] == ID:
                del jsondata['Tasks'][iteration]
                file = open('save.json', 'w')
                json.dump(jsondata, file, indent=4, ensure_ascii=False)
            else:
                iteration += 1
    def unfill(self):
        def deleteItems(layout):
            if layout is not None:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                       widget.deleteLater()
                    else:
                        deleteItems(item.layout())
        deleteItems(self.verticalLayout_2)
        
        ########################################################################BLOCK 3###########################################################################

    def AddTaskToFile(self):
        LocalVars = locals()
        file = open('save.json', 'r', encoding='utf-8')
        try:
            jsondata = json.loads(file.read(), encoding='utf-8')
        except:
            self.loadSave()
        currentProfile = self.ProfileComboBox.currentText()
        currentProxyProfile = self.ProxyConfigComboBox.currentText()
        if currentProfile != '':
            for profile in jsondata['Profiles']:
                if profile['profilename'] == currentProfile:
                    model = self.ModelLineEdit.text()
                    if model != '':
                        site = 'adidas.com'
                        size = self.SizeComboBox.currentText()###STAGE 3 PROCEED####################################################################
                        taskCount = self.TaskCountLineEdit.text()
                        if taskCount != '':
                            try:
                                int(taskCount)
                            except:
                                self.TaskCountLineEdit.clear()
                            else:
                                taskCount = int(taskCount)
                                if taskCount != 0:
                                    if self.ProxyConfigComboBox.currentText() == 'None':
                                        proxyUsage = False
                                    else:
                                        proxyUsage = True
                                        proxyConfig = self.ProxyConfigComboBox.currentText()
                                    #ADD TASK STAGE
                                    file = open('save.json', 'r')
                                    jsondata = json.loads(file.read(), encoding='utf-8')
                                    file.close()
                                    try:
                                        profileData = jsondata['Profiles']
                                        currentTasks = jsondata['Tasks']
                                        proxyData = jsondata['ProxyConfigs']
                                        if proxyUsage == True:
                                            for dict in proxyData:
                                                if dict['profilename'] == currentProxyProfile:
                                                    proxyData = dict
                                        for dict in profileData:
                                            if dict['profilename'] == currentProfile:
                                                profileData = dict
                                    except:
                                        self.loadSave()
                                    else:
                                    #try:
                                        if currentTasks != []:
                                            currentID = int(currentTasks[::-1][0]['taskID'])
                                        else:
                                            currentID = 0
                                        if proxyUsage == True:
                                            proxyTasksCounter = 0
                                            for items in jsondata['Tasks']:
                                                    if items['currentProxy'] != None and currentProxyProfile == items['proxyprofile']:
                                                        proxyTasksCounter += 1
                                        for ID in list(range(currentID, currentID + taskCount)):
                                            ID += 1
                                            if proxyUsage == True:
                                                if proxyTasksCounter < len(proxyData['proxyList']):
                                                    print('FLAG TRUE2')
                                                    data = {'taskID': str(ID), 'model': model, 'proxyprofile': currentProxyProfile, 'currentProxy': proxyData['proxyList'][proxyTasksCounter - 1], 'size' : size, 'site': site, 'status' : 'Created'}
                                                    proxyTasksCounter += 1
                                                else:
                                                    data = {'taskID': str(ID), 'model': model, 'proxyprofile': 'None', 'currentProxy': 'None', 'size' : size, 'site': site, 'status' : 'Created'}
                                            else:
                                                data = {'taskID': str(ID), 'model': model, 'proxyprofile': 'None', 'currentProxy': 'None', 'size' : size, 'site': site, 'status' : 'Created'}
                                            data.update(profileData)
                                            jsondata['Tasks'].append(data)
                                        file = open('save.json', 'r+', encoding='utf-8')
                                        json.dump(jsondata, file, indent=4, ensure_ascii=False)
                                        file.close()
                                    #except Exception as e:
                                    #        print(e)
                                    #        self.loadSave()
                                    #        self.AddTaskToFile()
                                    #    else:
                                        self.rldTasks()
    def rldTasks(self):
        self.unfill()
        try:
            file = open('save.json','r', encoding='utf-8')
            jsondata = json.loads(file.read(), encoding='utf-8')
            file.close()
            for dict in jsondata['Tasks']:
                ID = 'ID' + str(dict['taskID']) 
                IDint = str(dict['taskID'])
                #THREAD IDENTIFY
                THREAD = 'THREAD' + str(dict['taskID'])
                #PROXY IDENTIFY
                if str(dict['currentProxy']) == 'None':
                    ProxyValue = '    -None-    '
                else:
                    ProxyValue = str(dict['currentProxy'])
                PROXY = 'PROXY' + str(dict['taskID'])
                #SIZE IDENTIFY
                SIZE = 'SIZE' + str(dict['taskID'])
                SizeValue = str(dict['size'])
                #MODEL IDENTIFY
                MODEL = 'MODEL' + str(dict['taskID'])
                modelValue = str(dict['model'])
                #SITE IDENTIFY LAST LABEL LocalVars[SITE]
                SITE = 'SITE' + str(dict['taskID'])
                siteValue = str(dict['site'])
                #STATUS *CHANGEBLE*
                STATUS = 'STATUS' + str(dict['taskID'])
                statusValue = str(dict['status'])
                #REMOVE TASK BUTTON
                REMOVE = 'REMOVE' + str(dict['taskID'])
                self.LocalVars[THREAD] = QtWidgets.QHBoxLayout()
                self.LocalVars[THREAD].setObjectName(THREAD)
                self.LocalVars[ID] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.LocalVars[ID].sizePolicy().hasHeightForWidth())
                self.LocalVars[ID].setSizePolicy(sizePolicy)
                self.LocalVars[ID].setContextMenuPolicy(QtCore.Qt.NoContextMenu)
                self.LocalVars[ID].setLayoutDirection(QtCore.Qt.LeftToRight)
                self.LocalVars[ID].setStyleSheet("")
                self.LocalVars[ID].setAlignment(QtCore.Qt.AlignCenter)
                self.LocalVars[ID].setObjectName(str(ID))
                IDIndex = '[' + str(dict['taskID']) + ']'
                self.LocalVars[ID].setText(IDIndex)
                self.LocalVars[THREAD].addWidget(self.LocalVars[ID])
                self.LocalVars[PROXY] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.LocalVars[PROXY].sizePolicy().hasHeightForWidth())
                self.LocalVars[PROXY].setSizePolicy(sizePolicy)
                self.LocalVars[PROXY].setContextMenuPolicy(QtCore.Qt.NoContextMenu)
                self.LocalVars[PROXY].setLayoutDirection(QtCore.Qt.LeftToRight)
                self.LocalVars[PROXY].setStyleSheet("")
                self.LocalVars[PROXY].setAlignment(QtCore.Qt.AlignCenter)
                self.LocalVars[PROXY].setObjectName(PROXY)
                self.LocalVars[PROXY].setText(ProxyValue)
                self.LocalVars[THREAD].addWidget(self.LocalVars[PROXY])
                self.LocalVars[SIZE] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.LocalVars[SIZE].sizePolicy().hasHeightForWidth())
                self.LocalVars[SIZE].setSizePolicy(sizePolicy)
                self.LocalVars[SIZE].setContextMenuPolicy(QtCore.Qt.NoContextMenu)
                self.LocalVars[SIZE].setLayoutDirection(QtCore.Qt.LeftToRight)
                self.LocalVars[SIZE].setStyleSheet("")
                self.LocalVars[SIZE].setAlignment(QtCore.Qt.AlignCenter)
                self.LocalVars[SIZE].setObjectName(str(SIZE))
                self.LocalVars[SIZE].setText(SizeValue)
                self.LocalVars[THREAD].addWidget(self.LocalVars[SIZE])
                self.LocalVars[MODEL] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.LocalVars[MODEL].sizePolicy().hasHeightForWidth())
                self.LocalVars[MODEL].setSizePolicy(sizePolicy)
                self.LocalVars[MODEL].setContextMenuPolicy(QtCore.Qt.NoContextMenu)
                self.LocalVars[MODEL].setLayoutDirection(QtCore.Qt.LeftToRight)
                self.LocalVars[MODEL].setStyleSheet("")
                self.LocalVars[MODEL].setAlignment(QtCore.Qt.AlignCenter)
                self.LocalVars[MODEL].setObjectName(str(MODEL))
                self.LocalVars[MODEL].setText(modelValue)
                self.LocalVars[THREAD].addWidget(self.LocalVars[MODEL])
                self.LocalVars[SITE] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.LocalVars[SITE].sizePolicy().hasHeightForWidth())
                self.LocalVars[SITE].setSizePolicy(sizePolicy)
                self.LocalVars[SITE].setContextMenuPolicy(QtCore.Qt.NoContextMenu)
                self.LocalVars[SITE].setLayoutDirection(QtCore.Qt.LeftToRight)
                self.LocalVars[SITE].setStyleSheet("")
                self.LocalVars[SITE].setAlignment(QtCore.Qt.AlignCenter)
                self.LocalVars[SITE].setObjectName(SITE)
                self.LocalVars[SITE].setText(siteValue)
                self.LocalVars[THREAD].addWidget(self.LocalVars[SITE])
                self.LocalVars[STATUS] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.LocalVars[STATUS].sizePolicy().hasHeightForWidth())
                self.LocalVars[STATUS].setSizePolicy(sizePolicy)
                self.LocalVars[STATUS].setContextMenuPolicy(QtCore.Qt.NoContextMenu)
                self.LocalVars[STATUS].setLayoutDirection(QtCore.Qt.LeftToRight)
                self.LocalVars[STATUS].setStyleSheet("")
                self.LocalVars[STATUS].setAlignment(QtCore.Qt.AlignCenter)
                self.LocalVars[STATUS].setObjectName(STATUS)
                self.LocalVars[STATUS].setText(str(statusValue))
                self.LocalVars[THREAD].addWidget(self.LocalVars[STATUS])
                self.LocalVars[REMOVE] = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.LocalVars[REMOVE].setEnabled(True)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.LocalVars[REMOVE].sizePolicy().hasHeightForWidth())
                self.LocalVars[REMOVE].setSizePolicy(sizePolicy)
                self.LocalVars[REMOVE].setContextMenuPolicy(QtCore.Qt.NoContextMenu)
                self.LocalVars[REMOVE].setLayoutDirection(QtCore.Qt.LeftToRight)
                self.LocalVars[REMOVE].setStyleSheet("")
                self.LocalVars[REMOVE].setText(str(dict['taskID']))
                self.LocalVars[REMOVE].setStyleSheet("color: transparent;")
                self.LocalVars[REMOVE].setObjectName(REMOVE)
                self.LocalVars[THREAD].addWidget(self.LocalVars[REMOVE])
                self.LocalVars[REMOVE].clicked.connect(partial(self.RemoveTask, IDint))
                self.verticalLayout_2.addLayout(self.LocalVars[THREAD])
                self.LocalVars[THREAD].setAlignment(QtCore.Qt.AlignTop)
        except Exception as e:
            print(e)
            open('save.json', 'w', encoding='utf-8').close()
            self.loadSave()

###########################################################PROFILE MANAGER#####################################################################################################################

########################################################################BLOCK 4###########################################################################


class Ui_ProfileManager(object):
    def setupUi(self, ProfileManager):
        ProfileManager.setObjectName("ProfileManager")
        ProfileManager.resize(514, 796)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProfileManager.sizePolicy().hasHeightForWidth())
        ProfileManager.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        ProfileManager.setPalette(palette)
        ProfileManager.setStyleSheet("")
        ProfileManager.setWindowFilePath("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ProfileManager)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet("font: 750 25pt \"Ubuntu\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.profilename = QtWidgets.QLineEdit(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profilename.sizePolicy().hasHeightForWidth())
        self.profilename.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.profilename.setFont(font)
        self.profilename.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.profilename.setStyleSheet("")
        self.profilename.setInputMask("")
        self.profilename.setText("")
        self.profilename.setFrame(True)
        self.profilename.setCursorPosition(0)
        self.profilename.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.profilename.setPlaceholderText("")
        self.profilename.setObjectName("profilename")
        self.profilename.setMaxLength(15)
        regexp = QtCore.QRegExp('[a-zA-Z0-9]+')
        validator = QtGui.QRegExpValidator(regexp)
        self.profilename.setValidator(validator)
        self.verticalLayout_3.addWidget(self.profilename)
        self.firstname = QtWidgets.QLineEdit(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstname.sizePolicy().hasHeightForWidth())
        self.firstname.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.firstname.setFont(font)
        self.firstname.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.firstname.setStyleSheet("")
        self.firstname.setInputMask("")
        self.firstname.setText("")
        self.firstname.setFrame(True)
        self.firstname.setCursorPosition(0)
        self.firstname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.firstname.setPlaceholderText("")
        self.firstname.setObjectName("firstname")
        self.verticalLayout_3.addWidget(self.firstname)
        self.lastname = QtWidgets.QLineEdit(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastname.sizePolicy().hasHeightForWidth())
        self.lastname.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.lastname.setFont(font)
        self.lastname.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lastname.setStyleSheet("")
        self.lastname.setInputMask("")
        self.lastname.setText("")
        self.lastname.setFrame(True)
        self.lastname.setCursorPosition(0)
        self.lastname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lastname.setPlaceholderText("")
        self.lastname.setObjectName("lastname")
        self.verticalLayout_3.addWidget(self.lastname)
        self.email = QtWidgets.QLineEdit(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email.sizePolicy().hasHeightForWidth())
        self.email.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.email.setFont(font)
        self.email.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.email.setStyleSheet("")
        self.email.setInputMask("")
        self.email.setText("")
        self.email.setFrame(True)
        self.email.setCursorPosition(0)
        self.email.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.email.setPlaceholderText("")
        self.email.setObjectName("email")
        self.verticalLayout_3.addWidget(self.email)
        self.telephone = QtWidgets.QLineEdit(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.telephone.sizePolicy().hasHeightForWidth())
        self.telephone.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.telephone.setFont(font)
        self.telephone.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.telephone.setStyleSheet("")
        self.telephone.setInputMask("")
        self.telephone.setText("")
        self.telephone.setFrame(True)
        self.telephone.setCursorPosition(0)
        self.telephone.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.telephone.setPlaceholderText("")
        self.telephone.setObjectName("telephone")
        self.verticalLayout_3.addWidget(self.telephone)
        self.address = QtWidgets.QLineEdit(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.address.sizePolicy().hasHeightForWidth())
        self.address.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.address.setFont(font)
        self.address.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.address.setStyleSheet("")
        self.address.setInputMask("")
        self.address.setText("")
        self.address.setFrame(True)
        self.address.setCursorPosition(0)
        self.address.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.address.setPlaceholderText("")
        self.address.setObjectName("address")
        self.verticalLayout_3.addWidget(self.address)
        self.house = QtWidgets.QLineEdit(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house.sizePolicy().hasHeightForWidth())
        self.house.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.house.setFont(font)
        self.house.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.house.setStyleSheet("")
        self.house.setInputMask("")
        self.house.setText("")
        self.house.setFrame(True)
        self.house.setCursorPosition(0)
        self.house.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.house.setPlaceholderText("")
        self.house.setObjectName("house")
        self.verticalLayout_3.addWidget(self.house)
        self.apartament = QtWidgets.QLineEdit(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apartament.sizePolicy().hasHeightForWidth())
        self.apartament.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.apartament.setFont(font)
        self.apartament.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.apartament.setStyleSheet("")
        self.apartament.setInputMask("")
        self.apartament.setText("")
        self.apartament.setFrame(True)
        self.apartament.setCursorPosition(0)
        self.apartament.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.apartament.setPlaceholderText("")
        self.apartament.setObjectName("apartament")
        self.verticalLayout_3.addWidget(self.apartament)
        self.city = QtWidgets.QLineEdit(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city.sizePolicy().hasHeightForWidth())
        self.city.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.city.setFont(font)
        self.city.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.city.setStyleSheet("")
        self.city.setInputMask("")
        self.city.setText("")
        self.city.setFrame(True)
        self.city.setCursorPosition(0)
        self.city.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.city.setPlaceholderText("")
        self.city.setObjectName("city")
        self.verticalLayout_3.addWidget(self.city)
        self.zipcode = QtWidgets.QLineEdit(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zipcode.sizePolicy().hasHeightForWidth())
        self.zipcode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.zipcode.setFont(font)
        self.zipcode.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.zipcode.setStyleSheet("")
        self.zipcode.setInputMask("")
        self.zipcode.setText("")
        self.zipcode.setFrame(True)
        self.zipcode.setCursorPosition(0)
        self.zipcode.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.zipcode.setPlaceholderText("")
        self.zipcode.setObjectName("zipcode")
        self.verticalLayout_3.addWidget(self.zipcode)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_17 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_5.addWidget(self.label_17)
        self.label_16 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.label_15 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.label_13 = QtWidgets.QLabel(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.number = QtWidgets.QLineEdit(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number.sizePolicy().hasHeightForWidth())
        self.number.setSizePolicy(sizePolicy)
        self.number.setStyleSheet("height: 20px;")
        self.number.setObjectName("number")
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.number.setFont(font)
        self.verticalLayout_4.addWidget(self.number)
        self.owner = QtWidgets.QLineEdit(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.owner.sizePolicy().hasHeightForWidth())
        self.owner.setSizePolicy(sizePolicy)
        self.owner.setStyleSheet("height: 20px;")
        self.owner.setObjectName("owner")
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.owner.setFont(font)
        self.verticalLayout_4.addWidget(self.owner)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.month = QtWidgets.QComboBox(ProfileManager)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.month.setFont(font)
        self.month.setStyleSheet("")
        self.month.setObjectName("month")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.horizontalLayout_3.addWidget(self.month)
        self.year = QtWidgets.QComboBox(ProfileManager)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.year.setFont(font)
        self.year.setStyleSheet("")
        self.year.setObjectName("year")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.horizontalLayout_3.addWidget(self.year)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(ProfileManager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("height: 20px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Reset = QtWidgets.QPushButton(ProfileManager, default=False, autoDefault=False)
        self.Reset.setStyleSheet("")
        self.Reset.setObjectName("Reset")
        self.horizontalLayout_4.addWidget(self.Reset)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Save = QtWidgets.QPushButton(ProfileManager)
        self.Save.setObjectName("Save")
        self.horizontalLayout_5.addWidget(self.Save)
        self.Cancel = QtWidgets.QPushButton(ProfileManager, default=False, autoDefault=False)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout_5.addWidget(self.Cancel)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(ProfileManager)
        QtCore.QMetaObject.connectSlotsByName(ProfileManager)

    def retranslateUi(self, ProfileManager):
        _translate = QtCore.QCoreApplication.translate
        ProfileManager.setWindowTitle(_translate("ProfileManager", "Profile manager"))
        self.label_7.setText(_translate("ProfileManager", "Profile Edit"))
        self.label_2.setText(_translate("ProfileManager", "Profile name:"))
        self.label_4.setText(_translate("ProfileManager", "First name:"))
        self.label_3.setText(_translate("ProfileManager", "Last name:"))
        self.label_5.setText(_translate("ProfileManager", "Email:"))
        self.label_6.setText(_translate("ProfileManager", "Telephone:"))
        self.label_8.setText(_translate("ProfileManager", "Adress:"))
        self.label_9.setText(_translate("ProfileManager", "House number:"))
        self.label_10.setText(_translate("ProfileManager", "Apartament number:"))
        self.label_11.setText(_translate("ProfileManager", "City:"))
        self.label_12.setText(_translate("ProfileManager", "Zipcode:"))
        self.label_17.setText(_translate("ProfileManager", "Card number:"))
        self.label_16.setText(_translate("ProfileManager", "Card owner:"))
        self.label_15.setText(_translate("ProfileManager", "Expiring month/ year: "))
        self.label_13.setText(_translate("ProfileManager", "CVC/CVV2 Code:"))
        self.month.setItemText(0, _translate("ProfileManager", "01"))
        self.month.setItemText(1, _translate("ProfileManager", "02"))
        self.month.setItemText(2, _translate("ProfileManager", "03"))
        self.month.setItemText(3, _translate("ProfileManager", "04"))
        self.month.setItemText(4, _translate("ProfileManager", "05"))
        self.month.setItemText(5, _translate("ProfileManager", "06"))
        self.month.setItemText(6, _translate("ProfileManager", "07"))
        self.month.setItemText(7, _translate("ProfileManager", "08"))
        self.month.setItemText(8, _translate("ProfileManager", "09"))
        self.month.setItemText(9, _translate("ProfileManager", "10"))
        self.month.setItemText(10, _translate("ProfileManager", "11"))
        self.month.setItemText(11, _translate("ProfileManager", "12"))
        self.year.setItemText(0, _translate("ProfileManager", "2020"))
        self.year.setItemText(1, _translate("ProfileManager", "2021"))
        self.year.setItemText(2, _translate("ProfileManager", "2022"))
        self.year.setItemText(3, _translate("ProfileManager", "2023"))
        self.year.setItemText(4, _translate("ProfileManager", "2024"))
        self.year.setItemText(5, _translate("ProfileManager", "2025"))
        self.year.setItemText(6, _translate("ProfileManager", "2026"))
        self.year.setItemText(7, _translate("ProfileManager", "2027"))
        self.year.setItemText(8, _translate("ProfileManager", "2028"))
        self.year.setItemText(9, _translate("ProfileManager", "2029"))
        self.year.setItemText(10, _translate("ProfileManager", "2030"))
        self.Reset.setText(_translate("ProfileManager", "   Reset all profiles and tasks   "))
        self.Reset.clicked.connect(self.resetSettings)
        self.Save.setText(_translate("ProfileManager", "   Save   "))
        self.Save.setEnabled(False)
        self.Save.clicked.connect(self.saveProfile)
        self.Cancel.setText(_translate("ProfileManager", "   Cancel   "))
        self.Cancel.clicked.connect(ProfileManager.accept)
        self.profilename.textChanged.connect(self.checkText)
        self.firstname.textChanged.connect(self.checkText)
        self.lastname.textChanged.connect(self.checkText)
        self.email.textChanged.connect(self.checkText)
        self.telephone.textChanged.connect(self.checkText)
        self.address.textChanged.connect(self.checkText)
        self.apartament.textChanged.connect(self.checkText)
        self.house.textChanged.connect(self.checkText)
        self.city.textChanged.connect(self.checkText)
        self.zipcode.textChanged.connect(self.checkText)
        self.number.textChanged.connect(self.checkText)
        self.owner.textChanged.connect(self.checkText)
        self.lineEdit_2.textChanged.connect(self.checkText)
        
        ########################################################################BLOCK 5###########################################################################

    def resetSettings(self):
        self.profilename.clear()
        self.firstname.clear()
        self.lastname.clear()
        self.email.clear()
        self.telephone.clear()
        self.address.clear()
        self.apartament.clear()
        self.house.clear()
        self.city.clear()
        self.zipcode.clear()
        self.number.clear()
        self.owner.clear()
        self.lineEdit_2.clear()
        self.month.setCurrentIndex(0)
        self.year.setCurrentIndex(0)
        try:
            open('save.json', 'w', encoding='utf-8').close()
        except Exception as e:
            print(e)
    def checkText(self):
        self.label_2.setStyleSheet('')
        fields = []
        fields.append(self.profilename.text())
        fields.append(self.firstname.text())
        fields.append(self.lastname.text())
        fields.append(self.email.text())
        fields.append(self.telephone.text())
        fields.append(self.address.text())
        fields.append(self.apartament.text())
        fields.append(self.house.text())
        fields.append(self.city.text())
        fields.append(self.zipcode.text())
        fields.append(self.number.text())
        fields.append(self.owner.text())
        fields.append(self.lineEdit_2.text())
        err = False
        for field in fields:
            if field == '':
                err = True
        if err != True:
            self.Save.setEnabled(True)
        else:
            self.Save.setEnabled(False)
    def saveProfile(self, ProfileManager):
        try:
           field1 = self.profilename.text()
           field2 = self.firstname.text()
           field3 = self.lastname.text()
           field4 = self.email.text()
           field5 = self.telephone.text()
           field6 = self.address.text()
           field7 = self.apartament.text()
           field8 = self.house.text()
           field9 = self.city.text()
           field10 = self.zipcode.text()
           field11 = self.number.text()
           field12 = self.owner.text()
           field13 = str(self.month.currentText())
           field14 = str(self.year.currentText())
           field15 = self.lineEdit_2.text()

           data = {'profilename': field1, 'firstname': field2, 'lastname': field3, 'email': field4, 'telephone': field5, 'address': field6, 'apartament': field7, 'housenum':field8, 'city':field9, 'zipcode':field10, 'cardnum':field11, 'cardowner':field12, 'month':field13, 'year':field14, 'cvc':field15}
        except Exception as e:
            print(e)
        #Check json syntax and file existance
        try:
            f = open("save.json", "r", encoding='utf-8').read()
            json.loads(f)
        except Exception as e:
            f = open("save.json", "w", encoding='utf-8')
            json.dump({'Profiles': [], 'Tasks': []}, f, ensure_ascii=False)
            f.close()
            print(e)
        try:
            write_file = open("save.json", "r+", encoding='utf-8')
            jsondata = json.loads(write_file.read())
            err = False
            if jsondata['Profiles'] != []:
                for profile in jsondata['Profiles']:
                    try:
                        if profile['profilename'] == data['profilename']:
                            err = True
                    except:
                        err = False
            else:
                err = False
            if err == False:
                jsondata['Profiles'].append(data)
                write_file.close()
                open('save.json', 'w', encoding='utf-8').close()
                write_file = open("save.json", "r+", encoding='utf-8')
                json.dump(jsondata, write_file, indent=4, ensure_ascii=False)
                self.profilename.clear()
                self.firstname.clear()
                self.lastname.clear()
                self.email.clear()
                self.telephone.clear()
                self.address.clear()
                self.apartament.clear()
                self.house.clear()
                self.city.clear()
                self.zipcode.clear()
                self.number.clear()
                self.owner.clear()
                self.lineEdit_2.clear()
                self.month.setCurrentIndex(0)
                self.year.setCurrentIndex(0)
                write_file.close()
            else:
                self.profilename.clear()
                self.label_2.setStyleSheet('color:red;')
        except Exception as e:
            print(e)



########################################################################BLOCK 6###########################################################################

class Ui_authform(object):
    def startAuth(self):
        if not self.worker2Thread.isRunning():
            self.worker2Thread.start()


    def setupUi(self, authform):
        authform.setObjectName("authform")
        authform.resize(377, 215)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        authform.setFont(font)
        authform.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(authform)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(authform)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.AuthorizeFormTab = QtWidgets.QWidget()
        self.AuthorizeFormTab.setObjectName("AuthorizeFormTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.AuthorizeFormTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.AuthorizeFormTab)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(self.AuthorizeFormTab)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 185, 21);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.AuthorizeFormTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.login = QtWidgets.QLineEdit(self.AuthorizeFormTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.login.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.login.setStyleSheet("width: 100px;")
        self.login.setObjectName("login")
        regexp = QtCore.QRegExp('[a-zA-Z0-9_@.]+')
        validator = QtGui.QRegExpValidator(regexp)
        self.login.setValidator(validator)
        self.login.textEdited.connect(self.checkText)
        self.gridLayout.addWidget(self.login, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.AuthorizeFormTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.AuthorizeFormTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.password.setStyleSheet("width: 100px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.password.textEdited.connect(self.checkText)
        self.gridLayout.addWidget(self.password, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.submit = QtWidgets.QPushButton(self.AuthorizeFormTab)
        self.submit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.submit.setObjectName("submit")
        self.horizontalLayout.addWidget(self.submit)
        self.cancel = QtWidgets.QPushButton(self.AuthorizeFormTab)
        self.cancel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.AuthorizeFormTab, "")
        self.ServerStatusTab = QtWidgets.QWidget()
        self.ServerStatusTab.setObjectName("ServerStatusTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ServerStatusTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.ServerStatusTab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.ServerStatusTab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.ServerStatusTab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.server2Status = QtWidgets.QLabel(self.ServerStatusTab)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.server2Status.setFont(font)
        self.server2Status.setStyleSheet("color: rgb(255, 185, 21);")
        self.server2Status.setObjectName("server2Status")
        self.gridLayout_2.addWidget(self.server2Status, 1, 2, 1, 1)
        self.server1Status = QtWidgets.QLabel(self.ServerStatusTab)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.server1Status.setFont(font)
        self.server1Status.setStyleSheet("color: rgb(255, 185, 21);")
        self.server1Status.setObjectName("server1Status")
        self.gridLayout_2.addWidget(self.server1Status, 0, 2, 1, 1)
        self.server3Status = QtWidgets.QLabel(self.ServerStatusTab)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.server3Status.setFont(font)
        self.server3Status.setStyleSheet("color: rgb(255, 185, 21);")
        self.server3Status.setObjectName("server3Status")
        self.gridLayout_2.addWidget(self.server3Status, 2, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(self.ServerStatusTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.ServerStatusTab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(authform)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(authform)

    def retranslateUi(self, authform):
        _translate = QtCore.QCoreApplication.translate
        authform.setWindowTitle(_translate("authform", "DropBot Authorizing"))
        self.label.setText(_translate("authform", "Please authorize to DropBot.site"))
        self.label_7.setText(_translate("authform", "   Loading...   "))
        self.label_3.setText(_translate("authform", "Password"))
        self.label_2.setText(_translate("authform", "Login"))
        self.submit.setText(_translate("authform", "Submit"))
        self.submit.setEnabled(False)
        self.submit.clicked.connect(self.disableSubmit)





        self.worker2Thread = QThread()
        self.worker2 = Worker2()
        self.worker2.moveToThread(self.worker2Thread)
        # Connecting signals
        self.submit.clicked.connect(self.startAuth)
        self.worker2.request.connect(self.authClient)
        self.worker2.stopped.connect(self.worker2Thread.quit)
        self.worker2Thread.started.connect(self.worker2.run)





        self.cancel.setText(_translate("authform", "Cancel"))
        self.cancel.clicked.connect(self.Buttonexit)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AuthorizeFormTab), _translate("authform", "Auth"))
        self.label_4.setText(_translate("authform", "   API Server   "))
        self.label_5.setText(_translate("authform", "   DropBot Server   "))
        self.label_6.setText(_translate("authform", "   API Google   "))
        self.server2Status.setText(_translate("authform", "Loading.."))
        self.server1Status.setText(_translate("authform", "Loading.."))
        self.server3Status.setText(_translate("authform", "Loading.."))
        self.pushButton.setText(_translate("authform", "Update"))
        self.pushButton.clicked.connect(self.checkConnection)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ServerStatusTab), _translate("authform", "Servers status"))
    
    ########################################################################BLOCK 7###########################################################################
    def disableSubmit(self):
        self.submit.setEnabled(False)
    def checkText(self):
        loginField = self.login.text()
        passwordField = self.password.text()
        if loginField != '' and passwordField != '' and 'ONLINE' in self.label_7.text():
            self.submit.setEnabled(True)
        else:
            self.submit.setEnabled(False)

    def Buttonexit(self):
        sys.exit()
    def authClient(self, data):
        try:

            data = json.loads(data, encoding='utf-8')
        except Exception as e:
            print(e)
            self.label_7.setText("   FATAL API ERROR   ")
            self.label_7.setStyleSheet('color:red')
            self.checkText()
        else:
            print('Reading response...')
            if data['name'] != None:
                print('API returned code 200 - success')
                global name
                name = str(data['name'])
                message = 'Welcome back, ' + name
                authform.ui.label.setText(message)
                authform.ui.label.setStyleSheet('color: green;')
                app.processEvents()
                time.sleep(0.5)
                print('Authentication completed succesefully.')
                authform.ui.authSuccess()
            else:
                print('API returned code 403 - fail')
                print('Authentication failed.')
                authform.ui.login.clear()
                authform.ui.password.clear()
                authform.ui.label.setText('Incorrect login or password')
                authform.ui.label.setStyleSheet('color: red;')
                app.processEvents()
                authform.ui.checkConnection()

########################################################################BLOCK 8###########################################################################

    def checkConnection(self):
        self.worker1 = Worker1()
        threadpool.start(self.worker1)
    def authSuccess(self):
        DropBot.setWindowTitle('DropBot | Logged as {} ({})'.format(name, loginArg))
        authform.accept()
        DropBot.show()
        log = nowINFOMAIN() + ' Auth for ' + name + ' was succesefull' 
        ui.LogOutput.append(log)


########################################################################BLOCK 9###########################################################################

class Ui_SizeChart(object):
    def setupUi(self, SizeChart):
        SizeChart.setObjectName("SizeChart")
        SizeChart.resize(823, 685)
        SizeChart.setMinimumSize(QtCore.QSize(823, 685))
        SizeChart.setMaximumSize(QtCore.QSize(823, 685))
        self.verticalLayout = QtWidgets.QVBoxLayout(SizeChart)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(SizeChart)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(SizeChart)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(SizeChart)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SizeChart)
        QtCore.QMetaObject.connectSlotsByName(SizeChart)

    def retranslateUi(self, SizeChart):
        _translate = QtCore.QCoreApplication.translate
        SizeChart.setWindowTitle(_translate("SizeChart", "Dialog"))
        self.label.setText(_translate("SizeChart", "International shoe convertion chart"))
        self.textBrowser.setHtml(_translate("SizeChart", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\';\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt;\">Adult Mens and Womens Shoe Size Conversion Table<br /></span><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#ff6600;\">M/W indicates Men\'s or Women\'s Sizes. Other systems are for either gender.</span></p>\n"
"<table border=\"2\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" align=\"center\" cellspacing=\"0\" cellpadding=\"4\">\n"
"<tr>\n"
"<td colspan=\"2\" bgcolor=\"#ffcc66\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#0000ff; background-color:#ffcc66;\">System</span></p></td>\n"
"<td colspan=\"16\" bgcolor=\"#ffcc66\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#0000ff; background-color:#ffcc66;\">Sizes</span></p></td>\n"
"<td colspan=\"2\" bgcolor=\"#ffcc66\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#0000ff; background-color:#ffcc66;\">System</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"2\" bgcolor=\"#ffffcc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffcc;\">Europe</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">35</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">35½</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">36</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">37</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">37½</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">38</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">38½</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">39</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">40</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">41</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">42</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">43</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">44</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">45</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">46½</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">48½</span></p></td>\n"
"<td colspan=\"2\" bgcolor=\"#ffffcc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffcc;\">Europe</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"2\" bgcolor=\"#ccccff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ccccff;\">Mexico</span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\"> </span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\"> </span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\"> </span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\"> </span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\"> </span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\">4.5</span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\">5</span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\">5.5</span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\">6</span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\">6.5</span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\">7</span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\">7.5</span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\">9</span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\">10</span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\">11</span></p></td>\n"
"<td bgcolor=\"#ccccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccccff;\">12.5</span></p></td>\n"
"<td colspan=\"2\" bgcolor=\"#ccccff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ccccff;\">Mexico</span></p></td></tr>\n"
"<tr>\n"
"<td rowspan=\"2\" bgcolor=\"#ffccff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffccff;\">Japan</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffccff;\">M</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">21.5</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">22</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">22.5</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">23</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">23.5</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">24</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">24.5</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">25</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">25.5</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">26</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">26.5</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">27.5</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">28.5</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">29.5</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">30.5</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffccff;\">31.5</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffccff;\">Japan</span></p></td>\n"
"<td bgcolor=\"#ffccff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffccff;\">M</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">W</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">21</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">21.5</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">22</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">22.5</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">23</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">23.5</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">24</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">24.5</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">25</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">25.5</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">26</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">27</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">28</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">29</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">30</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">31</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Japan</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">W</span></p></td></tr>\n"
"<tr>\n"
"<td rowspan=\"2\" bgcolor=\"#ffcc99\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffcc99;\">U.K.</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffcc99;\">M</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">3</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">3½</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">4</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">4½</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">5</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">5½</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">6</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">6½</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">7</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">7½</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">8</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">8½</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">10</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">11</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">12</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcc99;\">13½</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffcc99;\">U.K.</span></p></td>\n"
"<td bgcolor=\"#ffcc99\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffcc99;\">M</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">W</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">2½</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">3</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">3½</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">4</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">4½</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">5</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">5½</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">6</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">6½</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">7</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">7½</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">8</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">9½</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">10½</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">11½</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">13</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">U.K.</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">W</span></p></td></tr>\n"
"<tr>\n"
"<td rowspan=\"2\" bgcolor=\"#ffffcc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffcc;\">Australia</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffcc;\">M</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">3</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">3½</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">4</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">4½</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">5</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">5½</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">6</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">6½</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">7</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">7½</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">8</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">8½</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">10</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">11</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">12</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">13½</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffcc;\">Australia</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffcc;\">M</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#cccccc;\">W</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">3½</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">4</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">4½</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">5</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">5½</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">6</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">6½</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">7</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">7½</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">8</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">8½</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">9</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">10½</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">11½</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">12½</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#cccccc;\">14</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#cccccc;\">Australia</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#cccccc;\">W</span></p></td></tr>\n"
"<tr>\n"
"<td rowspan=\"2\" bgcolor=\"#9999cc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#9999cc;\">U.S. &amp; Canada</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#9999cc;\">M</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">3½</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">4</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">4½</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">5</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">5½</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">6</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">6½</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">7</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">7½</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">8</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">8½</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">9</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">10½</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">11½</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">12½</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#9999cc;\">14</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#9999cc;\">U.S. &amp; Canada</span></p></td>\n"
"<td bgcolor=\"#9999cc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#9999cc;\">M</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ccffcc;\">W</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">5</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">5½</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">6</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">6½</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">7</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">7½</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">8</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">8½</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">9</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">9½</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">10</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">10.5</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">12</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">13</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">14</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccffcc;\">15.5</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ccffcc;\">U.S. &amp; Canada</span></p></td>\n"
"<td bgcolor=\"#ccffcc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ccffcc;\">W</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ccff99;\">Russia &amp; Ukraine *</span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ccff99;\">W</span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\">33½</span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\">34</span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\"> </span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\">35</span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\"> </span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\">36</span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\"> </span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\">37</span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\"> </span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\">38</span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\"> </span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\">39</span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\"> </span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\"> </span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\"> </span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ccff99;\"> </span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ccff99;\">Russia &amp; Ukraine</span></p></td>\n"
"<td bgcolor=\"#ccff99\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ccff99;\">W</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"2\" bgcolor=\"#ffffff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Korea</span><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000;\"> (mm.)</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">228</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">231</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">235</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">238</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">241</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">245</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">248</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">251</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">254</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">257</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">260</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">267</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">273</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">279</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">286</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">292</span></p></td>\n"
"<td colspan=\"2\" bgcolor=\"#ffffff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Korea</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"2\" bgcolor=\"#ffcccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffcccc;\">Inches</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">9</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">9</span><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000;\">1/8</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">9¼</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">9</span><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000;\">3/8</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">9½</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">9</span><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000;\">5/8</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">9¾</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">9</span><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000;\">7/8</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">10</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">10</span><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000;\">1/8</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">10¼</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">10½</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">10¾</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">11</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">11¼</span></p></td>\n"
"<td bgcolor=\"#ffcccc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffcccc;\">11½</span></p></td>\n"
"<td colspan=\"2\" bgcolor=\"#ffcccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffcccc;\">Inches</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"2\" bgcolor=\"#ffffcc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffcc;\">Centimeters</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">22.8</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">23.1</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">23.5</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">23.8</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">24.1</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">24.5</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">24.8</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">25.1</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">25.4</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">25.7</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">26</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">26.7</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">27.3</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">27.9</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">28.6</span></p></td>\n"
"<td bgcolor=\"#ffffcc\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffcc;\">29.2</span></p></td>\n"
"<td colspan=\"2\" bgcolor=\"#ffffcc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffcc;\">Centimeters</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"2\" bgcolor=\"#ffffff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Mondopoint</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">228</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">231</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">235</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">238</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">241</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">245</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">248</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">251</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">254</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">257</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">260</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">267</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">273</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">279</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">286</span></p></td>\n"
"<td bgcolor=\"#ffffff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; color:#000000; background-color:#ffffff;\">292</span></p></td>\n"
"<td colspan=\"2\" bgcolor=\"#ffffff\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Mondopoint</span></p></td></tr></table></body></html>"))
        self.pushButton.setText(_translate("SizeChart", "Cancel"))
        self.pushButton.clicked.connect(SizeChart.accept)
        
        ########################################################################BLOCK 10 - Stage 01###########################################################################

class Ui_ProxyConfig(object):
    def setupUi(self, ProxyConfig):
        ProxyConfig.setObjectName("ProxyConfig")
        ProxyConfig.resize(822, 520)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProxyConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ProxyConfig)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.SeparatorLabel = QtWidgets.QLabel(ProxyConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SeparatorLabel.sizePolicy().hasHeightForWidth())
        self.SeparatorLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.SeparatorLabel.setFont(font)
        self.SeparatorLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.SeparatorLabel.setStyleSheet("margin-top: 15px; margin-bottom: auto;")
        self.SeparatorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SeparatorLabel.setObjectName("SeparatorLabel")
        self.gridLayout.addWidget(self.SeparatorLabel, 1, 0, 1, 1)
        self.SeparatorComboBox = QtWidgets.QComboBox(ProxyConfig)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.SeparatorComboBox.setFont(font)
        self.SeparatorComboBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.SeparatorComboBox.setStyleSheet("")
        self.SeparatorComboBox.setObjectName("SeparatorComboBox")
        self.SeparatorComboBox.addItem("")
        self.SeparatorComboBox.addItem("")
        self.SeparatorComboBox.addItem("")
        self.SeparatorComboBox.addItem("")
        self.gridLayout.addWidget(self.SeparatorComboBox, 1, 2, 1, 1)
        self.ProxyTypeLabel = QtWidgets.QLabel(ProxyConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProxyTypeLabel.sizePolicy().hasHeightForWidth())
        self.ProxyTypeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.ProxyTypeLabel.setFont(font)
        self.ProxyTypeLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ProxyTypeLabel.setStyleSheet("margin-top: 15px; margin-bottom: auto;")
        self.ProxyTypeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ProxyTypeLabel.setObjectName("ProxyTypeLabel")
        self.gridLayout.addWidget(self.ProxyTypeLabel, 2, 0, 1, 1)
        self.ProfileName = QtWidgets.QLineEdit(ProxyConfig)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.ProfileName.setFont(font)
        self.ProfileName.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ProfileName.setStyleSheet("")
        self.ProfileName.setObjectName("ProfileName")
        self.gridLayout.addWidget(self.ProfileName, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.ProxyTypeComboBox = QtWidgets.QComboBox(ProxyConfig)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.ProxyTypeComboBox.setFont(font)
        self.ProxyTypeComboBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ProxyTypeComboBox.setStyleSheet("")
        self.ProxyTypeComboBox.setObjectName("ProxyTypeComboBox")
        self.ProxyTypeComboBox.addItem("")
        self.ProxyTypeComboBox.addItem("")
        self.gridLayout.addWidget(self.ProxyTypeComboBox, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.ProfileNameLabel = QtWidgets.QLabel(ProxyConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProfileNameLabel.sizePolicy().hasHeightForWidth())
        self.ProfileNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.ProfileNameLabel.setFont(font)
        self.ProfileNameLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ProfileNameLabel.setStyleSheet("margin-top: 15px; margin-bottom: auto;")
        self.ProfileNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ProfileNameLabel.setObjectName("ProfileNameLabel")
        self.gridLayout.addWidget(self.ProfileNameLabel, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.pushButton = QtWidgets.QPushButton(ProxyConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("margin-left: 120; margin-right:120; margin-top: 5; margin-bottom: 5; height: 40px; padding-left: 15px; padding-right:15px;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.LogOutput = QtWidgets.QTextEdit(ProxyConfig)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.LogOutput.setFont(font)
        self.LogOutput.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LogOutput.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.LogOutput.setToolTipDuration(0)
        self.LogOutput.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.LogOutput.setObjectName("LogOutput")
        self.verticalLayout_3.addWidget(self.LogOutput)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(ProxyConfig)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.ProxyInput = QtWidgets.QTextBrowser(ProxyConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProxyInput.sizePolicy().hasHeightForWidth())
        self.ProxyInput.setSizePolicy(sizePolicy)
        self.ProxyInput.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ProxyInput.setUndoRedoEnabled(True)
        self.ProxyInput.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.ProxyInput.setObjectName("ProxyInput")
        self.verticalLayout_2.addWidget(self.ProxyInput)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.cancel = QtWidgets.QPushButton(ProxyConfig)
class Ui_ProxyConfig(object):
    def setupUi(self, ProxyConfig):
        ProxyConfig.setObjectName("ProxyConfig")
        ProxyConfig.resize(822, 520)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProxyConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ProxyConfig)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.SeparatorLabel = QtWidgets.QLabel(ProxyConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SeparatorLabel.sizePolicy().hasHeightForWidth())
        self.SeparatorLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.SeparatorLabel.setFont(font)
        self.SeparatorLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.SeparatorLabel.setStyleSheet("margin-top: 15px; margin-bottom: auto;")
        self.SeparatorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SeparatorLabel.setObjectName("SeparatorLabel")
        self.gridLayout.addWidget(self.SeparatorLabel, 1, 0, 1, 1)
        self.SeparatorComboBox = QtWidgets.QComboBox(ProxyConfig)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.SeparatorComboBox.setFont(font)
        self.SeparatorComboBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.SeparatorComboBox.setStyleSheet("")
        self.SeparatorComboBox.setObjectName("SeparatorComboBox")
        self.SeparatorComboBox.addItem("")
        self.gridLayout.addWidget(self.SeparatorComboBox, 1, 2, 1, 1)
        self.ProxyTypeLabel = QtWidgets.QLabel(ProxyConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProxyTypeLabel.sizePolicy().hasHeightForWidth())
        self.ProxyTypeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.ProxyTypeLabel.setFont(font)
        self.ProxyTypeLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ProxyTypeLabel.setStyleSheet("margin-top: 15px; margin-bottom: auto;")
        self.ProxyTypeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ProxyTypeLabel.setObjectName("ProxyTypeLabel")
        self.gridLayout.addWidget(self.ProxyTypeLabel, 2, 0, 1, 1)
        self.ProfileName = QtWidgets.QLineEdit(ProxyConfig)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.ProfileName.setFont(font)
        self.ProfileName.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ProfileName.setStyleSheet("")
        self.ProfileName.setObjectName("ProfileName")
        self.ProfileName.setMaxLength(15)
        regexp = QtCore.QRegExp('[a-zA-Z0-9]+')
        validator = QtGui.QRegExpValidator(regexp)
        self.ProfileName.setValidator(validator)
        self.gridLayout.addWidget(self.ProfileName, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.ProxyTypeComboBox = QtWidgets.QComboBox(ProxyConfig)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.ProxyTypeComboBox.setFont(font)
        self.ProxyTypeComboBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ProxyTypeComboBox.setStyleSheet("")
        self.ProxyTypeComboBox.setObjectName("ProxyTypeComboBox")
        self.ProxyTypeComboBox.addItem("")
        self.gridLayout.addWidget(self.ProxyTypeComboBox, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.ProfileNameLabel = QtWidgets.QLabel(ProxyConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProfileNameLabel.sizePolicy().hasHeightForWidth())
        self.ProfileNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.ProfileNameLabel.setFont(font)
        self.ProfileNameLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ProfileNameLabel.setStyleSheet("margin-top: 15px; margin-bottom: auto;")
        self.ProfileNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ProfileNameLabel.setObjectName("ProfileNameLabel")
        self.gridLayout.addWidget(self.ProfileNameLabel, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.pushButton = QtWidgets.QPushButton(ProxyConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("margin-left: 120; margin-right:120; margin-top: 5; margin-bottom: 5; height: 40px; padding-left: 15px; padding-right:15px;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.LogOutput = QtWidgets.QTextEdit(ProxyConfig)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.LogOutput.setFont(font)
        self.LogOutput.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LogOutput.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.LogOutput.setToolTipDuration(0)
        self.LogOutput.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.LogOutput.setObjectName("LogOutput")
        self.verticalLayout_3.addWidget(self.LogOutput)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(ProxyConfig)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.ProxyInput = QtWidgets.QTextEdit(ProxyConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProxyInput.sizePolicy().hasHeightForWidth())
        self.ProxyInput.setSizePolicy(sizePolicy)
        self.ProxyInput.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ProxyInput.setUndoRedoEnabled(True)
        self.ProxyInput.setStyleSheet('color: white;')
        self.ProxyInput.setObjectName("ProxyInput")
        self.ProxyInput.setAcceptRichText(False)
        self.verticalLayout_2.addWidget(self.ProxyInput)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.cancel = QtWidgets.QPushButton(ProxyConfig)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ProxyConfig)
        QtCore.QMetaObject.connectSlotsByName(ProxyConfig)

    def retranslateUi(self, ProxyConfig):
        _translate = QtCore.QCoreApplication.translate
        ProxyConfig.setWindowTitle(_translate("ProxyConfig", "Proxy config"))
        self.label.setText(_translate("ProxyConfig", "Proxy config"))
        self.SeparatorLabel.setText(_translate("ProxyConfig", "Separator"))
        self.SeparatorComboBox.setItemText(0, _translate("ProxyConfig", "(Default) String"))
        self.ProxyTypeLabel.setText(_translate("ProxyConfig", "Proxy type"))
        self.ProxyTypeComboBox.setItemText(0, _translate("ProxyConfig", "PROXY:PORT"))
        self.ProfileNameLabel.setText(_translate("ProxyConfig", "Profile name"))
        self.ProfileName.textEdited.connect(self.checkText)
        self.pushButton.setText(_translate("ProxyConfig", "Add proxy profile"))
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.saveProxyProfile)
        self.label_2.setText(_translate("ProxyConfig", "Please enter your proxies here:"))
        self.cancel.setText(_translate("ProxyConfig", "   Cancel   "))
        self.cancel.clicked.connect(ProxyConfig.accept)
    def checkText(self):
        text = self.ProfileName.text()
        if text != '' and text != 'None':
            self.pushButton.setEnabled(True)
            self.ProfileNameLabel.setStyleSheet('')
        else:
            self.pushButton.setEnabled(False)
    def saveProxyProfile(self, ProxyConfig):
        write_file = open("save.json", "r+", encoding='utf-8')
        jsondata = json.loads(write_file.read())
        err = False
        if jsondata['ProxyConfigs'] != []:
            for ProxyProfileName in jsondata['ProxyConfigs']:
                try:
                    if ProxyProfileName['profilename'] == self.ProfileName.text():
                        self.ProfileName.clear()
                        self.ProfileNameLabel.setStyleSheet('color:red;')
                        self.checkText()
                        err = True
                except:
                    err = False
        if err == False:
            self.pushButton.setEnabled(False)
            currentSeparator = self.SeparatorComboBox.currentText()
            if currentSeparator == '(Default) String':
                currentSeparator = '\n'
            try:
                profilename = self.ProfileName.text()
                currentInputProxy = str(self.ProxyInput.toPlainText())
                proxyType = self.ProxyTypeComboBox.currentText()
                currentProxyListUnproceed = re.split(currentSeparator, currentInputProxy)
                currentProxyList = []
                if proxyType == "PROXY:PORT":
                    proxyType = 'noauth'
                    for item in currentProxyListUnproceed:
                        if item != '':
                            currentItem = re.search(r'(\d{1,3}\.){3}\d{1,3}:(\d+)', item)
                            if currentItem == None:
                                err = True
                            else:
                                currentProxyList.append(currentItem.group(0))
                    if err == True:
                        log = nowERRORMAIN() + ' Parsing error occured. Check accuracy.'
                        self.LogOutput.append(log)
                    else:
                        log = nowINFOMAIN() + ' Parsing succesefull!'
                        self.LogOutput.append(log)
                    data = {'profilename': profilename, 'proxytype': proxyType, 'proxyList': currentProxyList}
            except Exception as e:
                print(e)
            #Check json syntax and file existance
            if err == False:
                try:
                    f = open("save.json", "r", encoding='utf-8').read()
                    json.loads(f)
                except Exception as e:
                    f = open("save.json", "w", encoding='utf-8')
                    log = nowERRORMAIN() + ' Save file corrupted, creating a new one...'
                    self.LogOutput.append(log)
                    json.dump({'Profiles': [], 'Tasks': [], 'ProxyConfigs': []}, f, ensure_ascii=False)
                    f.close()
                    print(e)
                try:
                    write_file = open("save.json", "r+", encoding='utf-8')
                    jsondata = json.loads(write_file.read())
                    err = False
                    if jsondata['ProxyConfigs'] != []:
                        for ProxyProfileName in jsondata['ProxyConfigs']:
                            try:
                                if ProxyProfileName['profilename'] == data['profilename']:
                                    err = True
                            except:
                                err = False
                    else:
                        err = False
                    if err == False:
                        jsondata['ProxyConfigs'].append(data)
                        write_file.close()
                        open('save.json', 'w', encoding='utf-8').close()
                        write_file = open("save.json", "r+", encoding='utf-8')
                        json.dump(jsondata, write_file, indent=4, ensure_ascii=False)
                        log = nowINFOMAIN() + ' Save file succesefully updated!'
                        self.LogOutput.append(log)
                        self.ProfileName.clear()
                        self.ProxyInput.clear()
                        self.SeparatorComboBox.setCurrentIndex(0)
                        self.ProxyTypeComboBox.setCurrentIndex(0)
                        write_file.close()
                    else:
                        self.ProfileName.clear()
                        self.ProfileNameLabel.setStyleSheet('color:red;')
                except Exception as e:
                    log = nowERRORMAIN() + ' Unknown error occured'
                    self.LogOutput.append(log)
                    self.ProfileName.clear()
            self.checkText()
class Worker1(QRunnable):
    '''
    Worker thread
    '''
    def __init__(self):
        super(Worker1, self).__init__()

        # Store constructor arguments (re-used for processing)

    @pyqtSlot()
    def run(self):
        self.setAutoDelete(True)
        authform.ui.pushButton.setEnabled(False)
        authform.ui.submit.setEnabled(False)
        app.processEvents()
        authform.ui.server1Status.setStyleSheet("color: rgb(255, 185, 21);")
        authform.ui.server2Status.setStyleSheet("color: rgb(255, 185, 21);")
        authform.ui.server3Status.setStyleSheet("color: rgb(255, 185, 21);")
        authform.ui.server1Status.setText('Loading...') 
        authform.ui.server2Status.setText('Loading...')   
        authform.ui.server3Status.setText('Loading...')
        authform.ui.label_7.setText('   Loading...   ')
        authform.ui.label_7.setStyleSheet("color: rgb(255, 185, 21);")
        app.processEvents()
        url1 = 'https://api.dropbot.site/auth/index.html'
        url2 = 'https://server224.hosting.reg.ru/'
        url3 = 'https://sheets.google.com'
        err = 0
        try:
            req = requests.get(url1)
        except:
            err = 1
            authform.ui.server1Status.setStyleSheet("color: red;")
            authform.ui.server1Status.setText('OFFLINE')
            app.processEvents()
        else:
            if req.status_code != requests.codes.ok:
                err = 1
                authform.ui.server1Status.setStyleSheet("color: red;")
                errtext = 'OFFLINE (CODE ' + str(req.status_code) + ')'
                authform.ui.server1Status.setText(errtext)  
                app.processEvents()
            else: 
                authform.ui.server1Status.setStyleSheet("color: green;")
                authform.ui.server1Status.setText('ONLINE')
                app.processEvents()
        try:
            req = requests.get(url2)
        except:
            err = 1
            authform.ui.server2Status.setStyleSheet("color: red;")
            authform.ui.server2Status.setText('OFFLINE')     
            app.processEvents()
        else:
            if req.status_code != requests.codes.ok:
                err = 1
                authform.ui.server2Status.setStyleSheet("color: red;")
                errtext = 'OFFLINE (CODE ' + str(req.status_code) + ')'
                authform.ui.server2Status.setText(errtext)
                app.processEvents()
            else:
                authform.ui.server2Status.setStyleSheet("color: green;")
                authform.ui.server2Status.setText('ONLINE') 
                app.processEvents()            
        try:
            req = requests.get(url3)
        except:
            err = 1
            authform.ui.server3Status.setStyleSheet("color: red;")
            authform.ui.server3Status.setText('OFFLINE')
            app.processEvents()
        else:
            if req.status_code != requests.codes.ok:
                err = 1
                authform.ui.server3Status.setStyleSheet("color: red;")
                errtext = 'OFFLINE (CODE ' + str(req.status_code) + ')'
                authform.ui.server3Status.setText(errtext)
                app.processEvents()
            else:
                authform.ui.server3Status.setStyleSheet("color: green;")
                authform.ui.server3Status.setText('ONLINE')
        if err == 1:
            authform.ui.label_7.setStyleSheet("color: red;")
            authform.ui.label_7.setText('   OFFLINE   ')
            app.processEvents()
        else:
            authform.ui.label_7.setStyleSheet("color: green;")
            authform.ui.label_7.setText('   ONLINE   ')
            app.processEvents()
        authform.ui.pushButton.setEnabled(True)
        authform.ui.checkText()

class Worker2(QObject):
    '''
    Class intended to be used in a separate thread to generate numbers and send
    them to another thread.
    '''

    request = pyqtSignal(str)
    stopped = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

    def run(self):
        '''
        Count from 0 to 99 and emit each value to the GUI thread to display.
        '''
        global loginArg
        authform.ui.pushButton.setEnabled(False)
        authform.ui.label.setStyleSheet("color: rgb(255, 185, 21);")
        authform.ui.label.setText('Loading...') 
        apiUrl = 'https://api.dropbot.site/'
        loginArg = authform.ui.login.text()
        passwordArg = authform.ui.password.text()
        finalUrl = apiUrl + '?' + 'login=' + loginArg + '&' + 'password=' + passwordArg
        print('Sending request...')
        req = requests.get(finalUrl)
        print('Request sended')
        data = req.text
        self.request.emit(str(data))
        self.stopped.emit()





if __name__ == "__main__":
    def dark():
        import qdarkstyle
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        log = nowINFOMAIN() + ' Switched to dark theme.'
        ui.LogOutput.append(log)
    def light():
        from PyQt5.QtCore import QFile, QTextStream
        import breeze_resources
        file = QFile(":/light.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        app.setStyleSheet(stream.readAll())
        log = nowINFOMAIN() +  'Switched to light theme.'
        ui.LogOutput.append(log)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DropBot = QtWidgets.QMainWindow()
    ui = Ui_DropBot()
    ui.setupUi(DropBot)
    DropBot.setWindowIcon(QtGui.QIcon('icon2.png'))
    dark()
    QtGui.QFontDatabase.addApplicationFont("Ubuntu-R.ttf")
    log = nowINFOMAIN() + ' DropBot initializing.'
    ui.LogOutput.append(log)
    ui.actionDark.triggered.connect(dark)
    ui.actionLight.triggered.connect(light)
    DropBot.hide()
    log = nowINFOMAIN() + ' DropBot succesefully initialized!'
    ui.LogOutput.append(log)
    ui.loadSave()
    ui.authDialog()
    sys.exit(app.exec_())