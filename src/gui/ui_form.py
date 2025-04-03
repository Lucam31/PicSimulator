# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 30, 348, 191))
        self.MEM = QVBoxLayout(self.verticalLayoutWidget)
        self.MEM.setSpacing(0)
        self.MEM.setObjectName(u"MEM")
        self.MEM.setContentsMargins(0, 0, 0, 0)
        self.MEM_LINE0 = QHBoxLayout()
        self.MEM_LINE0.setSpacing(0)
        self.MEM_LINE0.setObjectName(u"MEM_LINE0")
        self.hcorner = QLineEdit(self.verticalLayoutWidget)
        self.hcorner.setObjectName(u"hcorner")
        self.hcorner.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.hcorner)

        self.h0 = QLineEdit(self.verticalLayoutWidget)
        self.h0.setObjectName(u"h0")
        self.h0.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h0)

        self.h1 = QLineEdit(self.verticalLayoutWidget)
        self.h1.setObjectName(u"h1")
        self.h1.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h1)

        self.h2 = QLineEdit(self.verticalLayoutWidget)
        self.h2.setObjectName(u"h2")
        self.h2.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h2)

        self.h3 = QLineEdit(self.verticalLayoutWidget)
        self.h3.setObjectName(u"h3")
        self.h3.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h3)

        self.h4 = QLineEdit(self.verticalLayoutWidget)
        self.h4.setObjectName(u"h4")
        self.h4.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h4)

        self.h5 = QLineEdit(self.verticalLayoutWidget)
        self.h5.setObjectName(u"h5")
        self.h5.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h5)

        self.h6 = QLineEdit(self.verticalLayoutWidget)
        self.h6.setObjectName(u"h6")
        self.h6.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h6)

        self.h7 = QLineEdit(self.verticalLayoutWidget)
        self.h7.setObjectName(u"h7")
        self.h7.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h7)


        self.MEM.addLayout(self.MEM_LINE0)

        self.MEM_LINE1 = QHBoxLayout()
        self.MEM_LINE1.setSpacing(0)
        self.MEM_LINE1.setObjectName(u"MEM_LINE1")
        self.index0 = QLineEdit(self.verticalLayoutWidget)
        self.index0.setObjectName(u"index0")
        self.index0.setReadOnly(True)

        self.MEM_LINE1.addWidget(self.index0)

        self.h0_2 = QLineEdit(self.verticalLayoutWidget)
        self.h0_2.setObjectName(u"h0_2")
        self.h0_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h0_2)

        self.h1_2 = QLineEdit(self.verticalLayoutWidget)
        self.h1_2.setObjectName(u"h1_2")
        self.h1_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h1_2)

        self.h2_2 = QLineEdit(self.verticalLayoutWidget)
        self.h2_2.setObjectName(u"h2_2")
        self.h2_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h2_2)

        self.h3_2 = QLineEdit(self.verticalLayoutWidget)
        self.h3_2.setObjectName(u"h3_2")
        self.h3_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h3_2)

        self.h4_2 = QLineEdit(self.verticalLayoutWidget)
        self.h4_2.setObjectName(u"h4_2")
        self.h4_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h4_2)

        self.h5_2 = QLineEdit(self.verticalLayoutWidget)
        self.h5_2.setObjectName(u"h5_2")
        self.h5_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h5_2)

        self.h6_2 = QLineEdit(self.verticalLayoutWidget)
        self.h6_2.setObjectName(u"h6_2")
        self.h6_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h6_2)

        self.h7_2 = QLineEdit(self.verticalLayoutWidget)
        self.h7_2.setObjectName(u"h7_2")
        self.h7_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h7_2)


        self.MEM.addLayout(self.MEM_LINE1)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(400, 330, 259, 189))
        self.MEM_LINE1_2 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.MEM_LINE1_2.setSpacing(0)
        self.MEM_LINE1_2.setObjectName(u"MEM_LINE1_2")
        self.MEM_LINE1_2.setContentsMargins(0, 0, 0, 0)
        self.index0_2 = QLineEdit(self.horizontalLayoutWidget_3)
        self.index0_2.setObjectName(u"index0_2")
        self.index0_2.setReadOnly(True)

        self.MEM_LINE1_2.addWidget(self.index0_2)

        self.h0_3 = QLineEdit(self.horizontalLayoutWidget_3)
        self.h0_3.setObjectName(u"h0_3")
        self.h0_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h0_3)

        self.h1_3 = QLineEdit(self.horizontalLayoutWidget_3)
        self.h1_3.setObjectName(u"h1_3")
        self.h1_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h1_3)

        self.h2_3 = QLineEdit(self.horizontalLayoutWidget_3)
        self.h2_3.setObjectName(u"h2_3")
        self.h2_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h2_3)

        self.h3_3 = QLineEdit(self.horizontalLayoutWidget_3)
        self.h3_3.setObjectName(u"h3_3")
        self.h3_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h3_3)

        self.h4_3 = QLineEdit(self.horizontalLayoutWidget_3)
        self.h4_3.setObjectName(u"h4_3")
        self.h4_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h4_3)

        self.h5_3 = QLineEdit(self.horizontalLayoutWidget_3)
        self.h5_3.setObjectName(u"h5_3")
        self.h5_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h5_3)

        self.h6_3 = QLineEdit(self.horizontalLayoutWidget_3)
        self.h6_3.setObjectName(u"h6_3")
        self.h6_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h6_3)

        self.h7_3 = QLineEdit(self.horizontalLayoutWidget_3)
        self.h7_3.setObjectName(u"h7_3")
        self.h7_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h7_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.h0.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.h1.setText(QCoreApplication.translate("MainWindow", u"01", None))
        self.h2.setText(QCoreApplication.translate("MainWindow", u"02", None))
        self.h3.setText(QCoreApplication.translate("MainWindow", u"03", None))
        self.h4.setText(QCoreApplication.translate("MainWindow", u"04", None))
        self.h5.setText(QCoreApplication.translate("MainWindow", u"05", None))
        self.h6.setText(QCoreApplication.translate("MainWindow", u"06", None))
        self.h7.setText(QCoreApplication.translate("MainWindow", u"07", None))
        self.index0.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.h0_2.setText("")
        self.h1_2.setText("")
        self.h2_2.setText("")
        self.h3_2.setText("")
        self.h4_2.setText("")
        self.h5_2.setText("")
        self.h6_2.setText("")
        self.h7_2.setText("")
        self.index0_2.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.h0_3.setText("")
        self.h1_3.setText("")
        self.h2_3.setText("")
        self.h3_3.setText("")
        self.h4_3.setText("")
        self.h5_3.setText("")
        self.h6_3.setText("")
        self.h7_3.setText("")
    # retranslateUi

