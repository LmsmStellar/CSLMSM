# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Management.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 1001, 531))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 360, 480, 71))
        self.tableWidget_3.setMaximumSize(QtCore.QSize(1000, 200))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(0, 230, 162, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(7)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(0, 150, 971, 71))
        self.tableWidget.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(0, 120, 112, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_6.setGeometry(QtCore.QRect(0, 250, 480, 71))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(10, 340, 44, 16))
        self.label_9.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(7)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(530, 320, 136, 28))
        self.label_10.setMaximumSize(QtCore.QSize(10000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_4.setGeometry(QtCore.QRect(510, 360, 479, 71))
        self.tableWidget_4.setMaximumSize(QtCore.QSize(1000, 200))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2.setGeometry(QtCore.QRect(136, 37, 100, 20))
        self.comboBox_2.setMaximumSize(QtCore.QSize(200, 20))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(2, 2, 128, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(136, 2, 107, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(2, 37, 100, 20))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 20))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(253, 37, 100, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(253, 2, 58, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(620, 10, 100, 20))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(200, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(400, 10, 171, 21))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(0, 90, 100, 20))
        self.comboBox_3.setMaximumSize(QtCore.QSize(200, 20))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(130, 60, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(250, 60, 26, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(0, 60, 103, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 90, 100, 20))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(200, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 40, 89, 36))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_4.setGeometry(QtCore.QRect(136, 90, 100, 20))
        self.comboBox_4.setMaximumSize(QtCore.QSize(200, 20))
        self.comboBox_4.setObjectName("comboBox_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 50, 83, 36))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 240, 75, 50))
        self.pushButton_4.setMinimumSize(QtCore.QSize(75, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(530, 240, 117, 50))
        self.pushButton_5.setMinimumSize(QtCore.QSize(75, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_5.setGeometry(QtCore.QRect(570, 20, 321, 175))
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 175))
        self.groupBox_5.setObjectName("groupBox_5")
        self.comboBox_14 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_14.setGeometry(QtCore.QRect(11, 97, 86, 30))
        self.comboBox_14.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_14.setObjectName("comboBox_14")
        self.label_20 = QtWidgets.QLabel(self.groupBox_5)
        self.label_20.setGeometry(QtCore.QRect(11, 77, 111, 16))
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(self.groupBox_5)
        self.label_22.setGeometry(QtCore.QRect(128, 77, 88, 16))
        self.label_22.setObjectName("label_22")
        self.comboBox_16 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_16.setGeometry(QtCore.QRect(222, 46, 86, 20))
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_15 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_15.setGeometry(QtCore.QRect(128, 97, 86, 30))
        self.comboBox_15.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_13 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_13.setGeometry(QtCore.QRect(128, 41, 86, 30))
        self.comboBox_13.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_13.setObjectName("comboBox_13")
        self.label_19 = QtWidgets.QLabel(self.groupBox_5)
        self.label_19.setGeometry(QtCore.QRect(11, 21, 72, 16))
        self.label_19.setObjectName("label_19")
        self.label_23 = QtWidgets.QLabel(self.groupBox_5)
        self.label_23.setGeometry(QtCore.QRect(222, 21, 85, 16))
        self.label_23.setObjectName("label_23")
        self.label_21 = QtWidgets.QLabel(self.groupBox_5)
        self.label_21.setGeometry(QtCore.QRect(128, 21, 57, 16))
        self.label_21.setObjectName("label_21")
        self.comboBox_12 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_12.setGeometry(QtCore.QRect(11, 41, 86, 30))
        self.comboBox_12.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_12.setObjectName("comboBox_12")
        self.widget = QtWidgets.QWidget(self.tab_4)
        self.widget.setGeometry(QtCore.QRect(50, 360, 77, 54))
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_5.addWidget(self.pushButton_6, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_5.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 110, 481, 91))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayoutWidget_13 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(10, 20, 463, 41))
        self.gridLayoutWidget_13.setObjectName("gridLayoutWidget_13")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.comboBox_10 = QtWidgets.QComboBox(self.gridLayoutWidget_13)
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout_18.addWidget(self.comboBox_10, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_13)
        self.label_17.setObjectName("label_17")
        self.gridLayout_18.addWidget(self.label_17, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_13)
        self.label_16.setObjectName("label_16")
        self.gridLayout_18.addWidget(self.label_16, 0, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_13)
        self.label_18.setObjectName("label_18")
        self.gridLayout_18.addWidget(self.label_18, 0, 0, 1, 1)
        self.comboBox_11 = QtWidgets.QComboBox(self.gridLayoutWidget_13)
        self.comboBox_11.setObjectName("comboBox_11")
        self.gridLayout_18.addWidget(self.comboBox_11, 1, 2, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.gridLayoutWidget_13)
        self.comboBox_9.setObjectName("comboBox_9")
        self.gridLayout_18.addWidget(self.comboBox_9, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 121, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 67, 16))
        self.label_12.setObjectName("label_12")
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_6.setGeometry(QtCore.QRect(10, 40, 86, 20))
        self.comboBox_6.setObjectName("comboBox_6")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 210, 191, 51))
        self.groupBox_6.setObjectName("groupBox_6")
        self.comboBox_17 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_17.setGeometry(QtCore.QRect(10, 20, 86, 20))
        self.comboBox_17.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox_17.setObjectName("comboBox_17")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 10, 121, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(11, 21, 77, 16))
        self.label_15.setObjectName("label_15")
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_7.setGeometry(QtCore.QRect(10, 40, 86, 20))
        self.comboBox_7.setObjectName("comboBox_7")
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(440, 20, 111, 91))
        self.groupBox.setObjectName("groupBox")
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setGeometry(QtCore.QRect(11, 21, 26, 16))
        self.label_26.setObjectName("label_26")
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_8.setGeometry(QtCore.QRect(10, 50, 86, 20))
        self.comboBox_8.setObjectName("comboBox_8")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_8.setGeometry(QtCore.QRect(500, 200, 301, 41))
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_25 = QtWidgets.QLabel(self.groupBox_8)
        self.label_25.setGeometry(QtCore.QRect(11, 21, 149, 16))
        self.label_25.setObjectName("label_25")
        self.comboBox_19 = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_19.setGeometry(QtCore.QRect(170, 20, 86, 20))
        self.comboBox_19.setObjectName("comboBox_19")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_7.setGeometry(QtCore.QRect(200, 210, 181, 81))
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_24 = QtWidgets.QLabel(self.groupBox_7)
        self.label_24.setGeometry(QtCore.QRect(11, 21, 114, 16))
        self.label_24.setObjectName("label_24")
        self.comboBox_18 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_18.setGeometry(QtCore.QRect(10, 50, 86, 20))
        self.comboBox_18.setObjectName("comboBox_18")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_9.setGeometry(QtCore.QRect(390, 250, 577, 300))
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_9)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 541, 181))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget_4)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_6.addWidget(self.listWidget, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 0, 2, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.gridLayoutWidget_4)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_6.addWidget(self.tableWidget_2, 1, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.comboBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_10.addWidget(self.comboBox_5, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_14.setObjectName("label_14")
        self.gridLayout_10.addWidget(self.label_14, 0, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_10.addWidget(self.pushButton_8, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_10, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "New or modified or removed uers"))
        self.label_7.setText(_translate("MainWindow", "List of users"))
        self.label_9.setText(_translate("MainWindow", "Users rights"))
        self.label_10.setText(_translate("MainWindow", "Administrators"))
        self.label.setText(_translate("MainWindow", "Organization"))
        self.label_2.setText(_translate("MainWindow", "User Name"))
        self.label_3.setText(_translate("MainWindow", "E-mail"))
        self.pushButton.setText(_translate("MainWindow", "New Password"))
        self.label_5.setText(_translate("MainWindow", "Last Name"))
        self.label_6.setText(_translate("MainWindow", "Tel"))
        self.label_4.setText(_translate("MainWindow", "First Name"))
        self.pushButton_2.setText(_translate("MainWindow", "Validate"))
        self.pushButton_3.setText(_translate("MainWindow", "Remove"))
        self.pushButton_4.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_5.setText(_translate("MainWindow", "DB transfer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "User management"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Create an instrumentation"))
        self.label_20.setText(_translate("MainWindow", "Insect ejector reference"))
        self.label_22.setText(_translate("MainWindow", "Camera reference"))
        self.label_19.setText(_translate("MainWindow", "Tank reference"))
        self.label_23.setText(_translate("MainWindow", "Acquisition system"))
        self.label_21.setText(_translate("MainWindow", "Sensor type"))
        self.pushButton_6.setText(_translate("MainWindow", "DB transfer"))
        self.pushButton_7.setText(_translate("MainWindow", "Cancel"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Create a test means"))
        self.label_17.setText(_translate("MainWindow", "Test means name"))
        self.label_16.setText(_translate("MainWindow", "Serial number"))
        self.label_18.setText(_translate("MainWindow", "Test means type"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Creating a coating"))
        self.label_12.setText(_translate("MainWindow", "Coating name"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Create teams for A/C &WT tests"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Create a detergent"))
        self.label_15.setText(_translate("MainWindow", "Detergent name"))
        self.groupBox.setTitle(_translate("MainWindow", "Insect autorization"))
        self.label_26.setText(_translate("MainWindow", "Insect"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Create an intrinsic value"))
        self.label_25.setText(_translate("MainWindow", "Name of an intrinsic value type"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Create a test point type"))
        self.label_24.setText(_translate("MainWindow", "Name of test point type"))
        self.groupBox_9.setTitle(_translate("MainWindow", "User rights"))
        self.label_13.setText(_translate("MainWindow", "Other users"))
        self.label_14.setText(_translate("MainWindow", "Rights"))
        self.pushButton_8.setText(_translate("MainWindow", "Validate"))
        self.label_11.setText(_translate("MainWindow", "Authorized users"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "User\'s allocation"))
