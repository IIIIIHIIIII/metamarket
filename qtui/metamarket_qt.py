#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metamarket_qt.ui'
#
# Created: Mon Jun 22 22:10:24 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 557)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabwidget = QtGui.QTabWidget(self.centralwidget)
        self.tabwidget.setObjectName(_fromUtf8("tabwidget"))
        self.chan_tab = QtGui.QWidget()
        self.chan_tab.setObjectName(_fromUtf8("chan_tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.chan_tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.chan_groupbox = QtGui.QGroupBox(self.chan_tab)
        self.chan_groupbox.setObjectName(_fromUtf8("chan_groupbox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.chan_groupbox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.chan_list = QtGui.QListWidget(self.chan_groupbox)
        self.chan_list.setObjectName(_fromUtf8("chan_list"))
        self.verticalLayout.addWidget(self.chan_list)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.chan_send_button = QtGui.QPushButton(self.chan_groupbox)
        self.chan_send_button.setObjectName(_fromUtf8("chan_send_button"))
        self.horizontalLayout.addWidget(self.chan_send_button)
        self.chan_view_button = QtGui.QPushButton(self.chan_groupbox)
        self.chan_view_button.setObjectName(_fromUtf8("chan_view_button"))
        self.horizontalLayout.addWidget(self.chan_view_button)
        self.chan_delete_button = QtGui.QPushButton(self.chan_groupbox)
        self.chan_delete_button.setObjectName(_fromUtf8("chan_delete_button"))
        self.horizontalLayout.addWidget(self.chan_delete_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.chan_groupbox, 1, 0, 1, 1)
        self.tabwidget.addTab(self.chan_tab, _fromUtf8(""))
        self.market_tab = QtGui.QWidget()
        self.market_tab.setObjectName(_fromUtf8("market_tab"))
        self.gridLayout_7 = QtGui.QGridLayout(self.market_tab)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.market_groupbox = QtGui.QGroupBox(self.market_tab)
        self.market_groupbox.setObjectName(_fromUtf8("market_groupbox"))
        self.gridLayout_6 = QtGui.QGridLayout(self.market_groupbox)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.market_table = QtGui.QTableWidget(self.market_groupbox)
        self.market_table.setObjectName(_fromUtf8("market_table"))
        self.market_table.setColumnCount(2)
        self.market_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.market_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.market_table.setHorizontalHeaderItem(1, item)
        self.market_table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.market_table)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.market_import_button = QtGui.QPushButton(self.market_groupbox)
        self.market_import_button.setObjectName(_fromUtf8("market_import_button"))
        self.horizontalLayout_3.addWidget(self.market_import_button)
        self.market_view_button = QtGui.QPushButton(self.market_groupbox)
        self.market_view_button.setObjectName(_fromUtf8("market_view_button"))
        self.horizontalLayout_3.addWidget(self.market_view_button)
        self.market_delete_button = QtGui.QPushButton(self.market_groupbox)
        self.market_delete_button.setObjectName(_fromUtf8("market_delete_button"))
        self.horizontalLayout_3.addWidget(self.market_delete_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.market_groupbox, 0, 0, 1, 1)
        self.tabwidget.addTab(self.market_tab, _fromUtf8(""))
        self.offer_tab = QtGui.QWidget()
        self.offer_tab.setObjectName(_fromUtf8("offer_tab"))
        self.gridLayout_12 = QtGui.QGridLayout(self.offer_tab)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.offer_groupbox = QtGui.QGroupBox(self.offer_tab)
        self.offer_groupbox.setObjectName(_fromUtf8("offer_groupbox"))
        self.gridLayout_11 = QtGui.QGridLayout(self.offer_groupbox)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.offer_mkt_combobox = QtGui.QComboBox(self.offer_groupbox)
        self.offer_mkt_combobox.setObjectName(_fromUtf8("offer_mkt_combobox"))
        self.horizontalLayout_6.addWidget(self.offer_mkt_combobox)
        self.offer_search_lineedit = QtGui.QLineEdit(self.offer_groupbox)
        self.offer_search_lineedit.setObjectName(_fromUtf8("offer_search_lineedit"))
        self.horizontalLayout_6.addWidget(self.offer_search_lineedit)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.offer_tablewidget = QtGui.QTableWidget(self.offer_groupbox)
        self.offer_tablewidget.setObjectName(_fromUtf8("offer_tablewidget"))
        self.offer_tablewidget.setColumnCount(4)
        self.offer_tablewidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.offer_tablewidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.offer_tablewidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.offer_tablewidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.offer_tablewidget.setHorizontalHeaderItem(3, item)
        self.offer_tablewidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_7.addWidget(self.offer_tablewidget)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.offer_order_button = QtGui.QPushButton(self.offer_groupbox)
        self.offer_order_button.setObjectName(_fromUtf8("offer_order_button"))
        self.horizontalLayout_7.addWidget(self.offer_order_button)
        self.offer_view_button = QtGui.QPushButton(self.offer_groupbox)
        self.offer_view_button.setObjectName(_fromUtf8("offer_view_button"))
        self.horizontalLayout_7.addWidget(self.offer_view_button)
        self.offer_delete_button = QtGui.QPushButton(self.offer_groupbox)
        self.offer_delete_button.setObjectName(_fromUtf8("offer_delete_button"))
        self.horizontalLayout_7.addWidget(self.offer_delete_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.gridLayout_11.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.offer_groupbox, 0, 0, 1, 1)
        self.tabwidget.addTab(self.offer_tab, _fromUtf8(""))
        self.order_tab = QtGui.QWidget()
        self.order_tab.setObjectName(_fromUtf8("order_tab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.order_tab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.order_groupbox = QtGui.QGroupBox(self.order_tab)
        self.order_groupbox.setObjectName(_fromUtf8("order_groupbox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.order_groupbox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.orders_table = QtGui.QTableWidget(self.order_groupbox)
        self.orders_table.setObjectName(_fromUtf8("orders_table"))
        self.orders_table.setColumnCount(5)
        self.orders_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(4, item)
        self.orders_table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.orders_table)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.order_process_button = QtGui.QPushButton(self.order_groupbox)
        self.order_process_button.setObjectName(_fromUtf8("order_process_button"))
        self.horizontalLayout_2.addWidget(self.order_process_button)
        self.order_view_button = QtGui.QPushButton(self.order_groupbox)
        self.order_view_button.setObjectName(_fromUtf8("order_view_button"))
        self.horizontalLayout_2.addWidget(self.order_view_button)
        self.order_cancel_button = QtGui.QPushButton(self.order_groupbox)
        self.order_cancel_button.setObjectName(_fromUtf8("order_cancel_button"))
        self.horizontalLayout_2.addWidget(self.order_cancel_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.order_groupbox, 0, 0, 1, 1)
        self.tabwidget.addTab(self.order_tab, _fromUtf8(""))
        self.ident_tab = QtGui.QWidget()
        self.ident_tab.setObjectName(_fromUtf8("ident_tab"))
        self.gridLayout_10 = QtGui.QGridLayout(self.ident_tab)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.ident_myid_groupbox = QtGui.QGroupBox(self.ident_tab)
        self.ident_myid_groupbox.setObjectName(_fromUtf8("ident_myid_groupbox"))
        self.gridLayout_9 = QtGui.QGridLayout(self.ident_myid_groupbox)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.ident_myid_label = QtGui.QLabel(self.ident_myid_groupbox)
        self.ident_myid_label.setObjectName(_fromUtf8("ident_myid_label"))
        self.verticalLayout_5.addWidget(self.ident_myid_label)
        self.ident_btcaddr_label = QtGui.QLabel(self.ident_myid_groupbox)
        self.ident_btcaddr_label.setObjectName(_fromUtf8("ident_btcaddr_label"))
        self.verticalLayout_5.addWidget(self.ident_btcaddr_label)
        self.ident_bmaddr_label = QtGui.QLabel(self.ident_myid_groupbox)
        self.ident_bmaddr_label.setObjectName(_fromUtf8("ident_bmaddr_label"))
        self.verticalLayout_5.addWidget(self.ident_bmaddr_label)
        self.gridLayout_9.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.ident_myid_groupbox)
        self.ident_groupbox = QtGui.QGroupBox(self.ident_tab)
        self.ident_groupbox.setObjectName(_fromUtf8("ident_groupbox"))
        self.gridLayout_8 = QtGui.QGridLayout(self.ident_groupbox)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.ident_market_combobox = QtGui.QComboBox(self.ident_groupbox)
        self.ident_market_combobox.setObjectName(_fromUtf8("ident_market_combobox"))
        self.horizontalLayout_5.addWidget(self.ident_market_combobox)
        self.ident_search_lineedit = QtGui.QLineEdit(self.ident_groupbox)
        self.ident_search_lineedit.setObjectName(_fromUtf8("ident_search_lineedit"))
        self.horizontalLayout_5.addWidget(self.ident_search_lineedit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.ident_table = QtGui.QTableWidget(self.ident_groupbox)
        self.ident_table.setObjectName(_fromUtf8("ident_table"))
        self.ident_table.setColumnCount(3)
        self.ident_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.ident_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.ident_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.ident_table.setHorizontalHeaderItem(2, item)
        self.ident_table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.ident_table)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.ident_reg_button = QtGui.QPushButton(self.ident_groupbox)
        self.ident_reg_button.setObjectName(_fromUtf8("ident_reg_button"))
        self.horizontalLayout_4.addWidget(self.ident_reg_button)
        self.ident_view_button = QtGui.QPushButton(self.ident_groupbox)
        self.ident_view_button.setObjectName(_fromUtf8("ident_view_button"))
        self.horizontalLayout_4.addWidget(self.ident_view_button)
        self.ident_burn_button = QtGui.QPushButton(self.ident_groupbox)
        self.ident_burn_button.setObjectName(_fromUtf8("ident_burn_button"))
        self.horizontalLayout_4.addWidget(self.ident_burn_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout_8.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.ident_groupbox)
        self.gridLayout_10.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.tabwidget.addTab(self.ident_tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabwidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionLogin = QtGui.QAction(MainWindow)
        self.actionLogin.setObjectName(_fromUtf8("actionLogin"))
        self.menuFile.addAction(self.actionLogin)
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "METAmarket-Qt", None))
        self.chan_groupbox.setTitle(_translate("MainWindow", "Channel: METAMARKET", None))
        self.chan_send_button.setText(_translate("MainWindow", "Send Message", None))
        self.chan_view_button.setText(_translate("MainWindow", "View Message", None))
        self.chan_delete_button.setText(_translate("MainWindow", "Delete Message", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.chan_tab), _translate("MainWindow", "Channel", None))
        self.market_groupbox.setTitle(_translate("MainWindow", "Available Markets:", None))
        item = self.market_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.market_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description", None))
        self.market_import_button.setText(_translate("MainWindow", "Import Market", None))
        self.market_view_button.setText(_translate("MainWindow", "View Market", None))
        self.market_delete_button.setText(_translate("MainWindow", "Delete Market", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.market_tab), _translate("MainWindow", "Markets", None))
        self.offer_groupbox.setTitle(_translate("MainWindow", "Available Offers: Market Name", None))
        self.offer_search_lineedit.setText(_translate("MainWindow", "Search", None))
        item = self.offer_tablewidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.offer_tablewidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Locale", None))
        item = self.offer_tablewidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Amount", None))
        item = self.offer_tablewidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price", None))
        self.offer_order_button.setText(_translate("MainWindow", "Order", None))
        self.offer_view_button.setText(_translate("MainWindow", "View Offer", None))
        self.offer_delete_button.setText(_translate("MainWindow", "Delete Offer", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.offer_tab), _translate("MainWindow", "Offers", None))
        self.order_groupbox.setTitle(_translate("MainWindow", "My Orders:", None))
        item = self.orders_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Status", None))
        item = self.orders_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.orders_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Locale", None))
        item = self.orders_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount", None))
        item = self.orders_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Price", None))
        self.order_process_button.setText(_translate("MainWindow", "Process", None))
        self.order_view_button.setText(_translate("MainWindow", "View Offer", None))
        self.order_cancel_button.setText(_translate("MainWindow", "Cancel Order", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.order_tab), _translate("MainWindow", "Orders", None))
        self.ident_myid_groupbox.setTitle(_translate("MainWindow", "My Identity:", None))
        self.ident_myid_label.setText(_translate("MainWindow", "ID Hash: ", None))
        self.ident_btcaddr_label.setText(_translate("MainWindow", "BTC Address: ", None))
        self.ident_bmaddr_label.setText(_translate("MainWindow", "BM Address: ", None))
        self.ident_groupbox.setTitle(_translate("MainWindow", "Known Identities:", None))
        self.ident_search_lineedit.setText(_translate("MainWindow", "Search", None))
        item = self.ident_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.ident_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Rep Score", None))
        item = self.ident_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ID", None))
        self.ident_reg_button.setText(_translate("MainWindow", "Register My Identity", None))
        self.ident_view_button.setText(_translate("MainWindow", "View Identity", None))
        self.ident_burn_button.setText(_translate("MainWindow", "BURN BTC", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.ident_tab), _translate("MainWindow", "Identities", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionLogin.setText(_translate("MainWindow", "Login", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

