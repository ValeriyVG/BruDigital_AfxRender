# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\RnD\17_AxF_Render\project\gui\mainWindowUI.ui'
#
# Created: Fri Dec 21 14:25:28 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BruDigital_AXFrender(object):
    def setupUi(self, BruDigital_AXFrender):
        BruDigital_AXFrender.setObjectName("BruDigital_AXFrender")
        BruDigital_AXFrender.resize(1028, 705)
        self.centralwidget = QtGui.QWidget(BruDigital_AXFrender)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SecretButtonLayOut = QtGui.QHBoxLayout()
        self.SecretButtonLayOut.setObjectName("SecretButtonLayOut")
        self.SecretButton = QtGui.QPushButton(self.centralwidget)
        self.SecretButton.setMaximumSize(QtCore.QSize(15, 15))
        self.SecretButton.setCheckable(True)
        self.SecretButton.setObjectName("SecretButton")
        self.SecretButtonLayOut.addWidget(self.SecretButton)
        self.SecretButtonLine = QtGui.QFrame(self.centralwidget)
        self.SecretButtonLine.setFrameShape(QtGui.QFrame.HLine)
        self.SecretButtonLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.SecretButtonLine.setObjectName("SecretButtonLine")
        self.SecretButtonLayOut.addWidget(self.SecretButtonLine)
        self.verticalLayout.addLayout(self.SecretButtonLayOut)
        self.MaxFileName = QtGui.QLineEdit(self.centralwidget)
        self.MaxFileName.setObjectName("MaxFileName")
        self.verticalLayout.addWidget(self.MaxFileName)
        self.manRenderLayOut = QtGui.QHBoxLayout()
        self.manRenderLayOut.setContentsMargins(-1, 0, -1, -1)
        self.manRenderLayOut.setObjectName("manRenderLayOut")
        self.manRenderChb = QtGui.QCheckBox(self.centralwidget)
        self.manRenderChb.setObjectName("manRenderChb")
        self.manRenderLayOut.addWidget(self.manRenderChb)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.manRenderLayOut.addItem(spacerItem)
        self.verticalLayout.addLayout(self.manRenderLayOut)
        self.RenderPassLine = QtGui.QFrame(self.centralwidget)
        self.RenderPassLine.setFrameShape(QtGui.QFrame.HLine)
        self.RenderPassLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.RenderPassLine.setObjectName("RenderPassLine")
        self.verticalLayout.addWidget(self.RenderPassLine)
        self.RenderPassLabel = QtGui.QLabel(self.centralwidget)
        self.RenderPassLabel.setMaximumSize(QtCore.QSize(100, 30))
        self.RenderPassLabel.setObjectName("RenderPassLabel")
        self.verticalLayout.addWidget(self.RenderPassLabel)
        self.RenderPassCommonLayOut = QtGui.QHBoxLayout()
        self.RenderPassCommonLayOut.setContentsMargins(-1, 0, -1, -1)
        self.RenderPassCommonLayOut.setObjectName("RenderPassCommonLayOut")
        self.RenderPassLayOut = QtGui.QGridLayout()
        self.RenderPassLayOut.setObjectName("RenderPassLayOut")
        self.RenderPassCommonLayOut.addLayout(self.RenderPassLayOut)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.RenderPassCommonLayOut.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.RenderPassCommonLayOut)
        self.AxfFileLine = QtGui.QFrame(self.centralwidget)
        self.AxfFileLine.setFrameShape(QtGui.QFrame.HLine)
        self.AxfFileLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.AxfFileLine.setObjectName("AxfFileLine")
        self.verticalLayout.addWidget(self.AxfFileLine)
        self.AxfFileLabel = QtGui.QLabel(self.centralwidget)
        self.AxfFileLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.AxfFileLabel.setObjectName("AxfFileLabel")
        self.verticalLayout.addWidget(self.AxfFileLabel)
        self.AxfFileList = QtGui.QListWidget(self.centralwidget)
        self.AxfFileList.setObjectName("AxfFileList")
        self.verticalLayout.addWidget(self.AxfFileList)
        self.StartRenderLayOut = QtGui.QHBoxLayout()
        self.StartRenderLayOut.setContentsMargins(-1, 0, -1, -1)
        self.StartRenderLayOut.setObjectName("StartRenderLayOut")
        self.AxfFileNumLabel = QtGui.QLabel(self.centralwidget)
        self.AxfFileNumLabel.setObjectName("AxfFileNumLabel")
        self.StartRenderLayOut.addWidget(self.AxfFileNumLabel)
        self.AxfFileNumLabel_2 = QtGui.QLabel(self.centralwidget)
        self.AxfFileNumLabel_2.setText("")
        self.AxfFileNumLabel_2.setObjectName("AxfFileNumLabel_2")
        self.StartRenderLayOut.addWidget(self.AxfFileNumLabel_2)
        self.AxfFileClearButton = QtGui.QPushButton(self.centralwidget)
        self.AxfFileClearButton.setObjectName("AxfFileClearButton")
        self.StartRenderLayOut.addWidget(self.AxfFileClearButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.StartRenderLayOut.addItem(spacerItem2)
        self.StartRenderButton = QtGui.QPushButton(self.centralwidget)
        self.StartRenderButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.StartRenderButton.setObjectName("StartRenderButton")
        self.StartRenderLayOut.addWidget(self.StartRenderButton)
        self.verticalLayout.addLayout(self.StartRenderLayOut)
        BruDigital_AXFrender.setCentralWidget(self.centralwidget)

        self.retranslateUi(BruDigital_AXFrender)
        QtCore.QMetaObject.connectSlotsByName(BruDigital_AXFrender)

    def retranslateUi(self, BruDigital_AXFrender):
        BruDigital_AXFrender.setWindowTitle(QtGui.QApplication.translate("BruDigital_AXFrender", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.SecretButton.setText(QtGui.QApplication.translate("BruDigital_AXFrender", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.manRenderChb.setText(QtGui.QApplication.translate("BruDigital_AXFrender", "Manual Render", None, QtGui.QApplication.UnicodeUTF8))
        self.RenderPassLabel.setText(QtGui.QApplication.translate("BruDigital_AXFrender", "Render Passes", None, QtGui.QApplication.UnicodeUTF8))
        self.AxfFileLabel.setText(QtGui.QApplication.translate("BruDigital_AXFrender", "AXF Files", None, QtGui.QApplication.UnicodeUTF8))
        self.AxfFileNumLabel.setText(QtGui.QApplication.translate("BruDigital_AXFrender", "0 SKUs in the list", None, QtGui.QApplication.UnicodeUTF8))
        self.AxfFileClearButton.setText(QtGui.QApplication.translate("BruDigital_AXFrender", "Clear List", None, QtGui.QApplication.UnicodeUTF8))
        self.StartRenderButton.setText(QtGui.QApplication.translate("BruDigital_AXFrender", "Start render", None, QtGui.QApplication.UnicodeUTF8))

