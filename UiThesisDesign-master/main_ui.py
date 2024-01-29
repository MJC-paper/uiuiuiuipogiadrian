# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1103, 707)
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setMinimumSize(QtCore.QSize(65, 0))
        self.icon_only_widget.setMaximumSize(QtCore.QSize(65, 16777215))
        self.icon_only_widget.setStyleSheet(" background-color: #FEF6E4;\n"
"  \n"
"")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout.setContentsMargins(10, 20, 10, 50)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.icon_only_Acc = QtWidgets.QLabel(self.icon_only_widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.icon_only_Acc.setFont(font)
        self.icon_only_Acc.setObjectName("icon_only_Acc")
        self.verticalLayout.addWidget(self.icon_only_Acc)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.dashboardbutton_2 = QtWidgets.QPushButton(self.icon_only_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashboardbutton_2.sizePolicy().hasHeightForWidth())
        self.dashboardbutton_2.setSizePolicy(sizePolicy)
        self.dashboardbutton_2.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.dashboardbutton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboardbutton_2.setIcon(icon)
        self.dashboardbutton_2.setCheckable(True)
        self.dashboardbutton_2.setAutoExclusive(True)
        self.dashboardbutton_2.setObjectName("dashboardbutton_2")
        self.verticalLayout.addWidget(self.dashboardbutton_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.infobutton_2 = QtWidgets.QPushButton(self.icon_only_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infobutton_2.sizePolicy().hasHeightForWidth())
        self.infobutton_2.setSizePolicy(sizePolicy)
        self.infobutton_2.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.infobutton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icon/icons8-about-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infobutton_2.setIcon(icon1)
        self.infobutton_2.setCheckable(True)
        self.infobutton_2.setAutoExclusive(True)
        self.infobutton_2.setObjectName("infobutton_2")
        self.verticalLayout.addWidget(self.infobutton_2)
        self.exitbutton_2 = QtWidgets.QPushButton(self.icon_only_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbutton_2.sizePolicy().hasHeightForWidth())
        self.exitbutton_2.setSizePolicy(sizePolicy)
        self.exitbutton_2.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.exitbutton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icon/icons8-exit-35.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitbutton_2.setIcon(icon2)
        self.exitbutton_2.setCheckable(True)
        self.exitbutton_2.setAutoExclusive(True)
        self.exitbutton_2.setObjectName("exitbutton_2")
        self.verticalLayout.addWidget(self.exitbutton_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.icons_details_widget = QtWidgets.QWidget(self.centralwidget)
        self.icons_details_widget.setMinimumSize(QtCore.QSize(130, 150))
        self.icons_details_widget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.icons_details_widget.setStyleSheet(" background-color: #FEF6E4;\n"
"  \n"
"")
        self.icons_details_widget.setObjectName("icons_details_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icons_details_widget)
        self.verticalLayout_3.setContentsMargins(5, -1, 5, 35)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.icon_Acc = QtWidgets.QLabel(self.icons_details_widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.icon_Acc.setFont(font)
        self.icon_Acc.setText("")
        self.icon_Acc.setPixmap(QtGui.QPixmap(":/icons/icon/logo.png"))
        self.icon_Acc.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_Acc.setObjectName("icon_Acc")
        self.verticalLayout_3.addWidget(self.icon_Acc)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.dashboardbutton = QtWidgets.QPushButton(self.icons_details_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashboardbutton.sizePolicy().hasHeightForWidth())
        self.dashboardbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dashboardbutton.setFont(font)
        self.dashboardbutton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dashboardbutton.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.dashboardbutton.setIcon(icon)
        self.dashboardbutton.setCheckable(True)
        self.dashboardbutton.setAutoRepeat(False)
        self.dashboardbutton.setAutoExclusive(True)
        self.dashboardbutton.setObjectName("dashboardbutton")
        self.verticalLayout_3.addWidget(self.dashboardbutton)
        spacerItem4 = QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.infobutton = QtWidgets.QPushButton(self.icons_details_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infobutton.sizePolicy().hasHeightForWidth())
        self.infobutton.setSizePolicy(sizePolicy)
        self.infobutton.setMinimumSize(QtCore.QSize(0, 0))
        self.infobutton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.infobutton.setFont(font)
        self.infobutton.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.infobutton.setIcon(icon1)
        self.infobutton.setCheckable(True)
        self.infobutton.setAutoExclusive(True)
        self.infobutton.setObjectName("infobutton")
        self.verticalLayout_3.addWidget(self.infobutton)
        self.exitbutton = QtWidgets.QPushButton(self.icons_details_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbutton.sizePolicy().hasHeightForWidth())
        self.exitbutton.setSizePolicy(sizePolicy)
        self.exitbutton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.exitbutton.setFont(font)
        self.exitbutton.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.exitbutton.setIcon(icon2)
        self.exitbutton.setCheckable(True)
        self.exitbutton.setAutoExclusive(True)
        self.exitbutton.setObjectName("exitbutton")
        self.verticalLayout_3.addWidget(self.exitbutton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.gridLayout.addWidget(self.icons_details_widget, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.topWidget = QtWidgets.QWidget(self.widget)
        self.topWidget.setStyleSheet("")
        self.topWidget.setObjectName("topWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_10 = QtWidgets.QPushButton(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icon/backward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout.addWidget(self.pushButton_10)
        spacerItem6 = QtWidgets.QSpacerItem(413, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.label_2 = QtWidgets.QLabel(self.topWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.gridLayout_2.addWidget(self.topWidget, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.stackedWidget.setStyleSheet("QWidget {\n"
"    background: qlineargradient(spread:pad, x2:1, y1:1, x1:1, y1:2, stop:0 #FEF6E4, stop:1 #ffffff);\n"
"    border: 1px solid black;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.dasboardpage = QtWidgets.QWidget()
        self.dasboardpage.setObjectName("dasboardpage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dasboardpage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.aircon = QtWidgets.QWidget(self.dasboardpage)
        self.aircon.setMinimumSize(QtCore.QSize(240, 200))
        self.aircon.setMaximumSize(QtCore.QSize(240, 200))
        self.aircon.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #000000; \n"
"border-radius: 5px;\n"
"")
        self.aircon.setObjectName("aircon")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.aircon)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ac_image = QtWidgets.QLabel(self.aircon)
        self.ac_image.setText("")
        self.ac_image.setPixmap(QtGui.QPixmap(":/icons/icon/Ac.png"))
        self.ac_image.setAlignment(QtCore.Qt.AlignCenter)
        self.ac_image.setObjectName("ac_image")
        self.horizontalLayout_2.addWidget(self.ac_image)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.ac_on = QtWidgets.QLabel(self.aircon)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ac_on.setFont(font)
        self.ac_on.setAlignment(QtCore.Qt.AlignCenter)
        self.ac_on.setObjectName("ac_on")
        self.verticalLayout_6.addWidget(self.ac_on)
        self.ac_off = QtWidgets.QLabel(self.aircon)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ac_off.setFont(font)
        self.ac_off.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.ac_off.setAlignment(QtCore.Qt.AlignCenter)
        self.ac_off.setObjectName("ac_off")
        self.verticalLayout_6.addWidget(self.ac_off)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.gridLayout_3.addWidget(self.aircon, 1, 1, 1, 1)
        self.door = QtWidgets.QWidget(self.dasboardpage)
        self.door.setMinimumSize(QtCore.QSize(240, 200))
        self.door.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #000000; \n"
"border-radius: 5px;\n"
"")
        self.door.setObjectName("door")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.door)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.door)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icons/icon/door.png"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.door)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.label_10 = QtWidgets.QLabel(self.door)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.gridLayout_3.addWidget(self.door, 3, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.dasboardpage)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border-radius: 11px; ")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)
        self.lights = QtWidgets.QWidget(self.dasboardpage)
        self.lights.setMinimumSize(QtCore.QSize(240, 200))
        self.lights.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #000000; \n"
"border-radius: 5px;\n"
"")
        self.lights.setObjectName("lights")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.lights)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.lights)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/icons/icon/light.png"))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.lights)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.lights)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout_3.addWidget(self.lights, 3, 0, 1, 1)
        self.powerconsumption = QtWidgets.QWidget(self.dasboardpage)
        self.powerconsumption.setMinimumSize(QtCore.QSize(240, 200))
        self.powerconsumption.setMaximumSize(QtCore.QSize(240, 200))
        self.powerconsumption.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #000000; \n"
"border-radius: 5px;\n"
"")
        self.powerconsumption.setObjectName("powerconsumption")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.powerconsumption)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.powerconsumption)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/icons/icon/Pc.png"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.tableView = QtWidgets.QTableView(self.powerconsumption)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_8.addWidget(self.tableView)
        self.gridLayout_3.addWidget(self.powerconsumption, 3, 2, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.electricfan = QtWidgets.QWidget(self.dasboardpage)
        self.electricfan.setMinimumSize(QtCore.QSize(240, 200))
        self.electricfan.setMaximumSize(QtCore.QSize(240, 200))
        self.electricfan.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #000000; \n"
"border-radius: 5px;\n"
"")
        self.electricfan.setObjectName("electricfan")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.electricfan)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.electricfan)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/icon/icons8-fan-50.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.electricfan)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_14 = QtWidgets.QLabel(self.electricfan)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_14.addWidget(self.electricfan)
        self.gridLayout_3.addLayout(self.horizontalLayout_14, 1, 2, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.dasboardpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(20, 20))
        self.widget_2.setMaximumSize(QtCore.QSize(400, 60))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_19 = QtWidgets.QLabel(self.widget_2)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_9.addWidget(self.label_19, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget_2)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_9.addWidget(self.label_20, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget_2)
        self.label_17.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout_9.addWidget(self.label_17, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget_2)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout_9.addWidget(self.label_16, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_2, 0, 1, 1, 1)
        self.dashboard = QtWidgets.QWidget(self.dasboardpage)
        self.dashboard.setMinimumSize(QtCore.QSize(240, 200))
        self.dashboard.setMaximumSize(QtCore.QSize(240, 200))
        self.dashboard.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #000000; \n"
"border-radius: 5px;\n"
"")
        self.dashboard.setObjectName("dashboard")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.dashboard)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.people_mage = QtWidgets.QLabel(self.dashboard)
        self.people_mage.setText("")
        self.people_mage.setPixmap(QtGui.QPixmap(":/icons/icon/people.png"))
        self.people_mage.setAlignment(QtCore.Qt.AlignCenter)
        self.people_mage.setObjectName("people_mage")
        self.horizontalLayout_6.addWidget(self.people_mage)
        self.lcdNumber = QtWidgets.QLCDNumber(self.dashboard)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 26.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_6.addWidget(self.lcdNumber)
        self.gridLayout_3.addWidget(self.dashboard, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.dasboardpage)
        self.infopage = QtWidgets.QWidget()
        self.infopage.setObjectName("infopage")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.infopage)
        self.gridLayout_13.setContentsMargins(0, 20, 0, 20)
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setVerticalSpacing(20)
        self.gridLayout_13.setObjectName("gridLayout_13")
        spacerItem8 = QtWidgets.QSpacerItem(173, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem8, 0, 1, 1, 1)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_26 = QtWidgets.QLabel(self.infopage)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_16.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.infopage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_16.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.infopage)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_16.addWidget(self.label_28)
        self.horizontalLayout_19.addLayout(self.verticalLayout_16)
        self.verticalLayout_17.addLayout(self.horizontalLayout_19)
        self.gridLayout_13.addLayout(self.verticalLayout_17, 4, 2, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(174, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem9, 4, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem10, 2, 5, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(181, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem11, 0, 3, 1, 2)
        spacerItem12 = QtWidgets.QSpacerItem(173, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem12, 4, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem13, 2, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.infopage)
        self.label_22.setMinimumSize(QtCore.QSize(300, 0))
        self.label_22.setMaximumSize(QtCore.QSize(250, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_13.addWidget(self.label_22, 0, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.infopage)
        self.textBrowser.setMaximumSize(QtCore.QSize(1500, 1500))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_13.addWidget(self.textBrowser, 1, 1, 3, 4)
        self.stackedWidget.addWidget(self.infopage)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.dashboardbutton_2.toggled['bool'].connect(self.dashboardbutton.setChecked) # type: ignore
        self.infobutton_2.toggled['bool'].connect(self.infobutton.setChecked) # type: ignore
        self.exitbutton_2.toggled['bool'].connect(self.exitbutton.setChecked) # type: ignore
        self.dashboardbutton.toggled['bool'].connect(self.dashboardbutton_2.setChecked) # type: ignore
        self.infobutton.toggled['bool'].connect(self.infobutton_2.setChecked) # type: ignore
        self.exitbutton.toggled['bool'].connect(self.exitbutton_2.setChecked) # type: ignore
        self.exitbutton.clicked.connect(MainWindow.close) # type: ignore
        self.exitbutton_2.clicked.connect(MainWindow.close) # type: ignore
        self.pushButton_10.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.pushButton_10.toggled['bool'].connect(self.icons_details_widget.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.icon_only_Acc.setText(_translate("MainWindow", "ACC"))
        self.dashboardbutton.setText(_translate("MainWindow", "  Dashboard"))
        self.infobutton.setText(_translate("MainWindow", "   Info"))
        self.exitbutton.setText(_translate("MainWindow", "Exit"))
        self.label_2.setText(_translate("MainWindow", "Adaptive Classroom Control"))
        self.ac_on.setText(_translate("MainWindow", "1"))
        self.ac_off.setText(_translate("MainWindow", "1"))
        self.label_15.setText(_translate("MainWindow", "2"))
        self.label_10.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "Dashboard"))
        self.label_5.setText(_translate("MainWindow", "1"))
        self.label_8.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "2"))
        self.label_14.setText(_translate("MainWindow", "3"))
        self.label_19.setText(_translate("MainWindow", "White = On"))
        self.label_20.setText(_translate("MainWindow", "Red = Off"))
        self.label_26.setText(_translate("MainWindow", "Version 1.0\n"
" Developers & Researchers"))
        self.label_27.setText(_translate("MainWindow", "Aquino, Marc Adrian\n"
"Carilla, Tristan Paul\n"
"Cerezo, Mario\n"
"Sagun, Argielyn Mae\n"
"Ungos, Warren"))
        self.label_28.setText(_translate("MainWindow", "Develop in November 2023"))
        self.label_22.setText(_translate("MainWindow", "About ACC"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Adaptive Classroom Control(ACC)</span><span style=\" font-size:20pt;\">: Utilize YOLO Algorithm for Human Detection, Temperature Control and Electrical EnergyConservation</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Adaptive Classroom Control (ACC), also known as ACC, is a cutting-edge system designed to create a smarter and more efficient classroom environment. ACC seamlessly integrates with various devices, such as air conditioners, electric fans, and lights, to dynamically respond to the presence of people and the temperature inside the room. The goal is to optimize energy usage and create a comfortable learning space.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Future DevelopmentsWe are committed to enhancing ACC to meet the evolving needs of educational environments. Planned future developments include:Integration with Smart Devices: Extend compatibility to include more smart devices for a fully connected classroom experience.Customization Options: Allow users to customize ACC settings to align with specific preferences and classroom requirements.</span></p></body></html>"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
