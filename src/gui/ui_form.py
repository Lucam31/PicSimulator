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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 280, 761))
        self.MEM = QVBoxLayout(self.verticalLayoutWidget)
        self.MEM.setSpacing(0)
        self.MEM.setObjectName(u"MEM")
        self.MEM.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.MEM.setContentsMargins(0, 0, 0, 0)
        self.MEM_LINE0 = QHBoxLayout()
        self.MEM_LINE0.setSpacing(0)
        self.MEM_LINE0.setObjectName(u"MEM_LINE0")
        self.hcorner = QLineEdit(self.verticalLayoutWidget)
        self.hcorner.setObjectName(u"hcorner")
        self.hcorner.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hcorner.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.hcorner)

        self.h0 = QLineEdit(self.verticalLayoutWidget)
        self.h0.setObjectName(u"h0")
        self.h0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h0)

        self.h1 = QLineEdit(self.verticalLayoutWidget)
        self.h1.setObjectName(u"h1")
        self.h1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h1)

        self.h2 = QLineEdit(self.verticalLayoutWidget)
        self.h2.setObjectName(u"h2")
        self.h2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h2)

        self.h3 = QLineEdit(self.verticalLayoutWidget)
        self.h3.setObjectName(u"h3")
        self.h3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h3)

        self.h4 = QLineEdit(self.verticalLayoutWidget)
        self.h4.setObjectName(u"h4")
        self.h4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h4)

        self.h5 = QLineEdit(self.verticalLayoutWidget)
        self.h5.setObjectName(u"h5")
        self.h5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h5)

        self.h6 = QLineEdit(self.verticalLayoutWidget)
        self.h6.setObjectName(u"h6")
        self.h6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h6)

        self.h7 = QLineEdit(self.verticalLayoutWidget)
        self.h7.setObjectName(u"h7")
        self.h7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7.setReadOnly(True)

        self.MEM_LINE0.addWidget(self.h7)


        self.MEM.addLayout(self.MEM_LINE0)

        self.MEM_LINE1 = QHBoxLayout()
        self.MEM_LINE1.setSpacing(0)
        self.MEM_LINE1.setObjectName(u"MEM_LINE1")
        self.index0 = QLineEdit(self.verticalLayoutWidget)
        self.index0.setObjectName(u"index0")
        self.index0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0.setReadOnly(True)

        self.MEM_LINE1.addWidget(self.index0)

        self.h0_2 = QLineEdit(self.verticalLayoutWidget)
        self.h0_2.setObjectName(u"h0_2")
        self.h0_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h0_2)

        self.h1_2 = QLineEdit(self.verticalLayoutWidget)
        self.h1_2.setObjectName(u"h1_2")
        self.h1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h1_2)

        self.h2_2 = QLineEdit(self.verticalLayoutWidget)
        self.h2_2.setObjectName(u"h2_2")
        self.h2_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h2_2)

        self.h3_2 = QLineEdit(self.verticalLayoutWidget)
        self.h3_2.setObjectName(u"h3_2")
        self.h3_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h3_2)

        self.h4_2 = QLineEdit(self.verticalLayoutWidget)
        self.h4_2.setObjectName(u"h4_2")
        self.h4_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h4_2)

        self.h5_2 = QLineEdit(self.verticalLayoutWidget)
        self.h5_2.setObjectName(u"h5_2")
        self.h5_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h5_2)

        self.h6_2 = QLineEdit(self.verticalLayoutWidget)
        self.h6_2.setObjectName(u"h6_2")
        self.h6_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h6_2)

        self.h7_2 = QLineEdit(self.verticalLayoutWidget)
        self.h7_2.setObjectName(u"h7_2")
        self.h7_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_2.setReadOnly(False)

        self.MEM_LINE1.addWidget(self.h7_2)


        self.MEM.addLayout(self.MEM_LINE1)

        self.MEM_LINE1_2 = QHBoxLayout()
        self.MEM_LINE1_2.setSpacing(0)
        self.MEM_LINE1_2.setObjectName(u"MEM_LINE1_2")
        self.index0_2 = QLineEdit(self.verticalLayoutWidget)
        self.index0_2.setObjectName(u"index0_2")
        self.index0_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_2.setReadOnly(True)

        self.MEM_LINE1_2.addWidget(self.index0_2)

        self.h0_3 = QLineEdit(self.verticalLayoutWidget)
        self.h0_3.setObjectName(u"h0_3")
        self.h0_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h0_3)

        self.h1_3 = QLineEdit(self.verticalLayoutWidget)
        self.h1_3.setObjectName(u"h1_3")
        self.h1_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h1_3)

        self.h2_3 = QLineEdit(self.verticalLayoutWidget)
        self.h2_3.setObjectName(u"h2_3")
        self.h2_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h2_3)

        self.h3_3 = QLineEdit(self.verticalLayoutWidget)
        self.h3_3.setObjectName(u"h3_3")
        self.h3_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h3_3)

        self.h4_3 = QLineEdit(self.verticalLayoutWidget)
        self.h4_3.setObjectName(u"h4_3")
        self.h4_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h4_3)

        self.h5_3 = QLineEdit(self.verticalLayoutWidget)
        self.h5_3.setObjectName(u"h5_3")
        self.h5_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h5_3)

        self.h6_3 = QLineEdit(self.verticalLayoutWidget)
        self.h6_3.setObjectName(u"h6_3")
        self.h6_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h6_3)

        self.h7_3 = QLineEdit(self.verticalLayoutWidget)
        self.h7_3.setObjectName(u"h7_3")
        self.h7_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_3.setReadOnly(False)

        self.MEM_LINE1_2.addWidget(self.h7_3)


        self.MEM.addLayout(self.MEM_LINE1_2)

        self.MEM_LINE1_3 = QHBoxLayout()
        self.MEM_LINE1_3.setSpacing(0)
        self.MEM_LINE1_3.setObjectName(u"MEM_LINE1_3")
        self.index0_3 = QLineEdit(self.verticalLayoutWidget)
        self.index0_3.setObjectName(u"index0_3")
        self.index0_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_3.setReadOnly(True)

        self.MEM_LINE1_3.addWidget(self.index0_3)

        self.h0_4 = QLineEdit(self.verticalLayoutWidget)
        self.h0_4.setObjectName(u"h0_4")
        self.h0_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_4.setReadOnly(False)

        self.MEM_LINE1_3.addWidget(self.h0_4)

        self.h1_4 = QLineEdit(self.verticalLayoutWidget)
        self.h1_4.setObjectName(u"h1_4")
        self.h1_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_4.setReadOnly(False)

        self.MEM_LINE1_3.addWidget(self.h1_4)

        self.h2_4 = QLineEdit(self.verticalLayoutWidget)
        self.h2_4.setObjectName(u"h2_4")
        self.h2_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_4.setReadOnly(False)

        self.MEM_LINE1_3.addWidget(self.h2_4)

        self.h3_4 = QLineEdit(self.verticalLayoutWidget)
        self.h3_4.setObjectName(u"h3_4")
        self.h3_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_4.setReadOnly(False)

        self.MEM_LINE1_3.addWidget(self.h3_4)

        self.h4_4 = QLineEdit(self.verticalLayoutWidget)
        self.h4_4.setObjectName(u"h4_4")
        self.h4_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_4.setReadOnly(False)

        self.MEM_LINE1_3.addWidget(self.h4_4)

        self.h5_4 = QLineEdit(self.verticalLayoutWidget)
        self.h5_4.setObjectName(u"h5_4")
        self.h5_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_4.setReadOnly(False)

        self.MEM_LINE1_3.addWidget(self.h5_4)

        self.h6_4 = QLineEdit(self.verticalLayoutWidget)
        self.h6_4.setObjectName(u"h6_4")
        self.h6_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_4.setReadOnly(False)

        self.MEM_LINE1_3.addWidget(self.h6_4)

        self.h7_4 = QLineEdit(self.verticalLayoutWidget)
        self.h7_4.setObjectName(u"h7_4")
        self.h7_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_4.setReadOnly(False)

        self.MEM_LINE1_3.addWidget(self.h7_4)


        self.MEM.addLayout(self.MEM_LINE1_3)

        self.MEM_LINE1_4 = QHBoxLayout()
        self.MEM_LINE1_4.setSpacing(0)
        self.MEM_LINE1_4.setObjectName(u"MEM_LINE1_4")
        self.index0_4 = QLineEdit(self.verticalLayoutWidget)
        self.index0_4.setObjectName(u"index0_4")
        self.index0_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_4.setReadOnly(True)

        self.MEM_LINE1_4.addWidget(self.index0_4)

        self.h0_5 = QLineEdit(self.verticalLayoutWidget)
        self.h0_5.setObjectName(u"h0_5")
        self.h0_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_5.setReadOnly(False)

        self.MEM_LINE1_4.addWidget(self.h0_5)

        self.h1_5 = QLineEdit(self.verticalLayoutWidget)
        self.h1_5.setObjectName(u"h1_5")
        self.h1_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_5.setReadOnly(False)

        self.MEM_LINE1_4.addWidget(self.h1_5)

        self.h2_5 = QLineEdit(self.verticalLayoutWidget)
        self.h2_5.setObjectName(u"h2_5")
        self.h2_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_5.setReadOnly(False)

        self.MEM_LINE1_4.addWidget(self.h2_5)

        self.h3_5 = QLineEdit(self.verticalLayoutWidget)
        self.h3_5.setObjectName(u"h3_5")
        self.h3_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_5.setReadOnly(False)

        self.MEM_LINE1_4.addWidget(self.h3_5)

        self.h4_5 = QLineEdit(self.verticalLayoutWidget)
        self.h4_5.setObjectName(u"h4_5")
        self.h4_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_5.setReadOnly(False)

        self.MEM_LINE1_4.addWidget(self.h4_5)

        self.h5_5 = QLineEdit(self.verticalLayoutWidget)
        self.h5_5.setObjectName(u"h5_5")
        self.h5_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_5.setReadOnly(False)

        self.MEM_LINE1_4.addWidget(self.h5_5)

        self.h6_5 = QLineEdit(self.verticalLayoutWidget)
        self.h6_5.setObjectName(u"h6_5")
        self.h6_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_5.setReadOnly(False)

        self.MEM_LINE1_4.addWidget(self.h6_5)

        self.h7_5 = QLineEdit(self.verticalLayoutWidget)
        self.h7_5.setObjectName(u"h7_5")
        self.h7_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_5.setReadOnly(False)

        self.MEM_LINE1_4.addWidget(self.h7_5)


        self.MEM.addLayout(self.MEM_LINE1_4)

        self.MEM_LINE1_5 = QHBoxLayout()
        self.MEM_LINE1_5.setSpacing(0)
        self.MEM_LINE1_5.setObjectName(u"MEM_LINE1_5")
        self.index0_5 = QLineEdit(self.verticalLayoutWidget)
        self.index0_5.setObjectName(u"index0_5")
        self.index0_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_5.setReadOnly(True)

        self.MEM_LINE1_5.addWidget(self.index0_5)

        self.h0_6 = QLineEdit(self.verticalLayoutWidget)
        self.h0_6.setObjectName(u"h0_6")
        self.h0_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_6.setReadOnly(False)

        self.MEM_LINE1_5.addWidget(self.h0_6)

        self.h1_6 = QLineEdit(self.verticalLayoutWidget)
        self.h1_6.setObjectName(u"h1_6")
        self.h1_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_6.setReadOnly(False)

        self.MEM_LINE1_5.addWidget(self.h1_6)

        self.h2_6 = QLineEdit(self.verticalLayoutWidget)
        self.h2_6.setObjectName(u"h2_6")
        self.h2_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_6.setReadOnly(False)

        self.MEM_LINE1_5.addWidget(self.h2_6)

        self.h3_6 = QLineEdit(self.verticalLayoutWidget)
        self.h3_6.setObjectName(u"h3_6")
        self.h3_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_6.setReadOnly(False)

        self.MEM_LINE1_5.addWidget(self.h3_6)

        self.h4_6 = QLineEdit(self.verticalLayoutWidget)
        self.h4_6.setObjectName(u"h4_6")
        self.h4_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_6.setReadOnly(False)

        self.MEM_LINE1_5.addWidget(self.h4_6)

        self.h5_6 = QLineEdit(self.verticalLayoutWidget)
        self.h5_6.setObjectName(u"h5_6")
        self.h5_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_6.setReadOnly(False)

        self.MEM_LINE1_5.addWidget(self.h5_6)

        self.h6_6 = QLineEdit(self.verticalLayoutWidget)
        self.h6_6.setObjectName(u"h6_6")
        self.h6_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_6.setReadOnly(False)

        self.MEM_LINE1_5.addWidget(self.h6_6)

        self.h7_6 = QLineEdit(self.verticalLayoutWidget)
        self.h7_6.setObjectName(u"h7_6")
        self.h7_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_6.setReadOnly(False)

        self.MEM_LINE1_5.addWidget(self.h7_6)


        self.MEM.addLayout(self.MEM_LINE1_5)

        self.MEM_LINE1_6 = QHBoxLayout()
        self.MEM_LINE1_6.setSpacing(0)
        self.MEM_LINE1_6.setObjectName(u"MEM_LINE1_6")
        self.index0_6 = QLineEdit(self.verticalLayoutWidget)
        self.index0_6.setObjectName(u"index0_6")
        self.index0_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_6.setReadOnly(True)

        self.MEM_LINE1_6.addWidget(self.index0_6)

        self.h0_7 = QLineEdit(self.verticalLayoutWidget)
        self.h0_7.setObjectName(u"h0_7")
        self.h0_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_7.setReadOnly(False)

        self.MEM_LINE1_6.addWidget(self.h0_7)

        self.h1_7 = QLineEdit(self.verticalLayoutWidget)
        self.h1_7.setObjectName(u"h1_7")
        self.h1_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_7.setReadOnly(False)

        self.MEM_LINE1_6.addWidget(self.h1_7)

        self.h2_7 = QLineEdit(self.verticalLayoutWidget)
        self.h2_7.setObjectName(u"h2_7")
        self.h2_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_7.setReadOnly(False)

        self.MEM_LINE1_6.addWidget(self.h2_7)

        self.h3_7 = QLineEdit(self.verticalLayoutWidget)
        self.h3_7.setObjectName(u"h3_7")
        self.h3_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_7.setReadOnly(False)

        self.MEM_LINE1_6.addWidget(self.h3_7)

        self.h4_7 = QLineEdit(self.verticalLayoutWidget)
        self.h4_7.setObjectName(u"h4_7")
        self.h4_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_7.setReadOnly(False)

        self.MEM_LINE1_6.addWidget(self.h4_7)

        self.h5_7 = QLineEdit(self.verticalLayoutWidget)
        self.h5_7.setObjectName(u"h5_7")
        self.h5_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_7.setReadOnly(False)

        self.MEM_LINE1_6.addWidget(self.h5_7)

        self.h6_7 = QLineEdit(self.verticalLayoutWidget)
        self.h6_7.setObjectName(u"h6_7")
        self.h6_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_7.setReadOnly(False)

        self.MEM_LINE1_6.addWidget(self.h6_7)

        self.h7_7 = QLineEdit(self.verticalLayoutWidget)
        self.h7_7.setObjectName(u"h7_7")
        self.h7_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_7.setReadOnly(False)

        self.MEM_LINE1_6.addWidget(self.h7_7)


        self.MEM.addLayout(self.MEM_LINE1_6)

        self.MEM_LINE1_7 = QHBoxLayout()
        self.MEM_LINE1_7.setSpacing(0)
        self.MEM_LINE1_7.setObjectName(u"MEM_LINE1_7")
        self.index0_7 = QLineEdit(self.verticalLayoutWidget)
        self.index0_7.setObjectName(u"index0_7")
        self.index0_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_7.setReadOnly(True)

        self.MEM_LINE1_7.addWidget(self.index0_7)

        self.h0_8 = QLineEdit(self.verticalLayoutWidget)
        self.h0_8.setObjectName(u"h0_8")
        self.h0_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_8.setReadOnly(False)

        self.MEM_LINE1_7.addWidget(self.h0_8)

        self.h1_8 = QLineEdit(self.verticalLayoutWidget)
        self.h1_8.setObjectName(u"h1_8")
        self.h1_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_8.setReadOnly(False)

        self.MEM_LINE1_7.addWidget(self.h1_8)

        self.h2_8 = QLineEdit(self.verticalLayoutWidget)
        self.h2_8.setObjectName(u"h2_8")
        self.h2_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_8.setReadOnly(False)

        self.MEM_LINE1_7.addWidget(self.h2_8)

        self.h3_8 = QLineEdit(self.verticalLayoutWidget)
        self.h3_8.setObjectName(u"h3_8")
        self.h3_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_8.setReadOnly(False)

        self.MEM_LINE1_7.addWidget(self.h3_8)

        self.h4_8 = QLineEdit(self.verticalLayoutWidget)
        self.h4_8.setObjectName(u"h4_8")
        self.h4_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_8.setReadOnly(False)

        self.MEM_LINE1_7.addWidget(self.h4_8)

        self.h5_8 = QLineEdit(self.verticalLayoutWidget)
        self.h5_8.setObjectName(u"h5_8")
        self.h5_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_8.setReadOnly(False)

        self.MEM_LINE1_7.addWidget(self.h5_8)

        self.h6_8 = QLineEdit(self.verticalLayoutWidget)
        self.h6_8.setObjectName(u"h6_8")
        self.h6_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_8.setReadOnly(False)

        self.MEM_LINE1_7.addWidget(self.h6_8)

        self.h7_8 = QLineEdit(self.verticalLayoutWidget)
        self.h7_8.setObjectName(u"h7_8")
        self.h7_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_8.setReadOnly(False)

        self.MEM_LINE1_7.addWidget(self.h7_8)


        self.MEM.addLayout(self.MEM_LINE1_7)

        self.MEM_LINE1_8 = QHBoxLayout()
        self.MEM_LINE1_8.setSpacing(0)
        self.MEM_LINE1_8.setObjectName(u"MEM_LINE1_8")
        self.index0_8 = QLineEdit(self.verticalLayoutWidget)
        self.index0_8.setObjectName(u"index0_8")
        self.index0_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_8.setReadOnly(True)

        self.MEM_LINE1_8.addWidget(self.index0_8)

        self.h0_9 = QLineEdit(self.verticalLayoutWidget)
        self.h0_9.setObjectName(u"h0_9")
        self.h0_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_9.setReadOnly(False)

        self.MEM_LINE1_8.addWidget(self.h0_9)

        self.h1_9 = QLineEdit(self.verticalLayoutWidget)
        self.h1_9.setObjectName(u"h1_9")
        self.h1_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_9.setReadOnly(False)

        self.MEM_LINE1_8.addWidget(self.h1_9)

        self.h2_9 = QLineEdit(self.verticalLayoutWidget)
        self.h2_9.setObjectName(u"h2_9")
        self.h2_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_9.setReadOnly(False)

        self.MEM_LINE1_8.addWidget(self.h2_9)

        self.h3_9 = QLineEdit(self.verticalLayoutWidget)
        self.h3_9.setObjectName(u"h3_9")
        self.h3_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_9.setReadOnly(False)

        self.MEM_LINE1_8.addWidget(self.h3_9)

        self.h4_9 = QLineEdit(self.verticalLayoutWidget)
        self.h4_9.setObjectName(u"h4_9")
        self.h4_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_9.setReadOnly(False)

        self.MEM_LINE1_8.addWidget(self.h4_9)

        self.h5_9 = QLineEdit(self.verticalLayoutWidget)
        self.h5_9.setObjectName(u"h5_9")
        self.h5_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_9.setReadOnly(False)

        self.MEM_LINE1_8.addWidget(self.h5_9)

        self.h6_9 = QLineEdit(self.verticalLayoutWidget)
        self.h6_9.setObjectName(u"h6_9")
        self.h6_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_9.setReadOnly(False)

        self.MEM_LINE1_8.addWidget(self.h6_9)

        self.h7_9 = QLineEdit(self.verticalLayoutWidget)
        self.h7_9.setObjectName(u"h7_9")
        self.h7_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_9.setReadOnly(False)

        self.MEM_LINE1_8.addWidget(self.h7_9)


        self.MEM.addLayout(self.MEM_LINE1_8)

        self.MEM_LINE1_9 = QHBoxLayout()
        self.MEM_LINE1_9.setSpacing(0)
        self.MEM_LINE1_9.setObjectName(u"MEM_LINE1_9")
        self.index0_9 = QLineEdit(self.verticalLayoutWidget)
        self.index0_9.setObjectName(u"index0_9")
        self.index0_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_9.setReadOnly(True)

        self.MEM_LINE1_9.addWidget(self.index0_9)

        self.h0_10 = QLineEdit(self.verticalLayoutWidget)
        self.h0_10.setObjectName(u"h0_10")
        self.h0_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_10.setReadOnly(False)

        self.MEM_LINE1_9.addWidget(self.h0_10)

        self.h1_10 = QLineEdit(self.verticalLayoutWidget)
        self.h1_10.setObjectName(u"h1_10")
        self.h1_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_10.setReadOnly(False)

        self.MEM_LINE1_9.addWidget(self.h1_10)

        self.h2_10 = QLineEdit(self.verticalLayoutWidget)
        self.h2_10.setObjectName(u"h2_10")
        self.h2_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_10.setReadOnly(False)

        self.MEM_LINE1_9.addWidget(self.h2_10)

        self.h3_10 = QLineEdit(self.verticalLayoutWidget)
        self.h3_10.setObjectName(u"h3_10")
        self.h3_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_10.setReadOnly(False)

        self.MEM_LINE1_9.addWidget(self.h3_10)

        self.h4_10 = QLineEdit(self.verticalLayoutWidget)
        self.h4_10.setObjectName(u"h4_10")
        self.h4_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_10.setReadOnly(False)

        self.MEM_LINE1_9.addWidget(self.h4_10)

        self.h5_10 = QLineEdit(self.verticalLayoutWidget)
        self.h5_10.setObjectName(u"h5_10")
        self.h5_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_10.setReadOnly(False)

        self.MEM_LINE1_9.addWidget(self.h5_10)

        self.h6_10 = QLineEdit(self.verticalLayoutWidget)
        self.h6_10.setObjectName(u"h6_10")
        self.h6_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_10.setReadOnly(False)

        self.MEM_LINE1_9.addWidget(self.h6_10)

        self.h7_10 = QLineEdit(self.verticalLayoutWidget)
        self.h7_10.setObjectName(u"h7_10")
        self.h7_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_10.setReadOnly(False)

        self.MEM_LINE1_9.addWidget(self.h7_10)


        self.MEM.addLayout(self.MEM_LINE1_9)

        self.MEM_LINE1_10 = QHBoxLayout()
        self.MEM_LINE1_10.setSpacing(0)
        self.MEM_LINE1_10.setObjectName(u"MEM_LINE1_10")
        self.index0_10 = QLineEdit(self.verticalLayoutWidget)
        self.index0_10.setObjectName(u"index0_10")
        self.index0_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_10.setReadOnly(True)

        self.MEM_LINE1_10.addWidget(self.index0_10)

        self.h0_11 = QLineEdit(self.verticalLayoutWidget)
        self.h0_11.setObjectName(u"h0_11")
        self.h0_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_11.setReadOnly(False)

        self.MEM_LINE1_10.addWidget(self.h0_11)

        self.h1_11 = QLineEdit(self.verticalLayoutWidget)
        self.h1_11.setObjectName(u"h1_11")
        self.h1_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_11.setReadOnly(False)

        self.MEM_LINE1_10.addWidget(self.h1_11)

        self.h2_11 = QLineEdit(self.verticalLayoutWidget)
        self.h2_11.setObjectName(u"h2_11")
        self.h2_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_11.setReadOnly(False)

        self.MEM_LINE1_10.addWidget(self.h2_11)

        self.h3_11 = QLineEdit(self.verticalLayoutWidget)
        self.h3_11.setObjectName(u"h3_11")
        self.h3_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_11.setReadOnly(False)

        self.MEM_LINE1_10.addWidget(self.h3_11)

        self.h4_11 = QLineEdit(self.verticalLayoutWidget)
        self.h4_11.setObjectName(u"h4_11")
        self.h4_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_11.setReadOnly(False)

        self.MEM_LINE1_10.addWidget(self.h4_11)

        self.h5_11 = QLineEdit(self.verticalLayoutWidget)
        self.h5_11.setObjectName(u"h5_11")
        self.h5_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_11.setReadOnly(False)

        self.MEM_LINE1_10.addWidget(self.h5_11)

        self.h6_11 = QLineEdit(self.verticalLayoutWidget)
        self.h6_11.setObjectName(u"h6_11")
        self.h6_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_11.setReadOnly(False)

        self.MEM_LINE1_10.addWidget(self.h6_11)

        self.h7_11 = QLineEdit(self.verticalLayoutWidget)
        self.h7_11.setObjectName(u"h7_11")
        self.h7_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_11.setReadOnly(False)

        self.MEM_LINE1_10.addWidget(self.h7_11)


        self.MEM.addLayout(self.MEM_LINE1_10)

        self.MEM_LINE1_12 = QHBoxLayout()
        self.MEM_LINE1_12.setSpacing(0)
        self.MEM_LINE1_12.setObjectName(u"MEM_LINE1_12")
        self.index0_12 = QLineEdit(self.verticalLayoutWidget)
        self.index0_12.setObjectName(u"index0_12")
        self.index0_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_12.setReadOnly(True)

        self.MEM_LINE1_12.addWidget(self.index0_12)

        self.h0_13 = QLineEdit(self.verticalLayoutWidget)
        self.h0_13.setObjectName(u"h0_13")
        self.h0_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_13.setReadOnly(False)

        self.MEM_LINE1_12.addWidget(self.h0_13)

        self.h1_13 = QLineEdit(self.verticalLayoutWidget)
        self.h1_13.setObjectName(u"h1_13")
        self.h1_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_13.setReadOnly(False)

        self.MEM_LINE1_12.addWidget(self.h1_13)

        self.h2_13 = QLineEdit(self.verticalLayoutWidget)
        self.h2_13.setObjectName(u"h2_13")
        self.h2_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_13.setReadOnly(False)

        self.MEM_LINE1_12.addWidget(self.h2_13)

        self.h3_13 = QLineEdit(self.verticalLayoutWidget)
        self.h3_13.setObjectName(u"h3_13")
        self.h3_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_13.setReadOnly(False)

        self.MEM_LINE1_12.addWidget(self.h3_13)

        self.h4_13 = QLineEdit(self.verticalLayoutWidget)
        self.h4_13.setObjectName(u"h4_13")
        self.h4_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_13.setReadOnly(False)

        self.MEM_LINE1_12.addWidget(self.h4_13)

        self.h5_13 = QLineEdit(self.verticalLayoutWidget)
        self.h5_13.setObjectName(u"h5_13")
        self.h5_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_13.setReadOnly(False)

        self.MEM_LINE1_12.addWidget(self.h5_13)

        self.h6_13 = QLineEdit(self.verticalLayoutWidget)
        self.h6_13.setObjectName(u"h6_13")
        self.h6_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_13.setReadOnly(False)

        self.MEM_LINE1_12.addWidget(self.h6_13)

        self.h7_13 = QLineEdit(self.verticalLayoutWidget)
        self.h7_13.setObjectName(u"h7_13")
        self.h7_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_13.setReadOnly(False)

        self.MEM_LINE1_12.addWidget(self.h7_13)


        self.MEM.addLayout(self.MEM_LINE1_12)

        self.MEM_LINE1_13 = QHBoxLayout()
        self.MEM_LINE1_13.setSpacing(0)
        self.MEM_LINE1_13.setObjectName(u"MEM_LINE1_13")
        self.index0_13 = QLineEdit(self.verticalLayoutWidget)
        self.index0_13.setObjectName(u"index0_13")
        self.index0_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_13.setReadOnly(True)

        self.MEM_LINE1_13.addWidget(self.index0_13)

        self.h0_14 = QLineEdit(self.verticalLayoutWidget)
        self.h0_14.setObjectName(u"h0_14")
        self.h0_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_14.setReadOnly(False)

        self.MEM_LINE1_13.addWidget(self.h0_14)

        self.h1_14 = QLineEdit(self.verticalLayoutWidget)
        self.h1_14.setObjectName(u"h1_14")
        self.h1_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_14.setReadOnly(False)

        self.MEM_LINE1_13.addWidget(self.h1_14)

        self.h2_14 = QLineEdit(self.verticalLayoutWidget)
        self.h2_14.setObjectName(u"h2_14")
        self.h2_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_14.setReadOnly(False)

        self.MEM_LINE1_13.addWidget(self.h2_14)

        self.h3_14 = QLineEdit(self.verticalLayoutWidget)
        self.h3_14.setObjectName(u"h3_14")
        self.h3_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_14.setReadOnly(False)

        self.MEM_LINE1_13.addWidget(self.h3_14)

        self.h4_14 = QLineEdit(self.verticalLayoutWidget)
        self.h4_14.setObjectName(u"h4_14")
        self.h4_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_14.setReadOnly(False)

        self.MEM_LINE1_13.addWidget(self.h4_14)

        self.h5_14 = QLineEdit(self.verticalLayoutWidget)
        self.h5_14.setObjectName(u"h5_14")
        self.h5_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_14.setReadOnly(False)

        self.MEM_LINE1_13.addWidget(self.h5_14)

        self.h6_14 = QLineEdit(self.verticalLayoutWidget)
        self.h6_14.setObjectName(u"h6_14")
        self.h6_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_14.setReadOnly(False)

        self.MEM_LINE1_13.addWidget(self.h6_14)

        self.h7_14 = QLineEdit(self.verticalLayoutWidget)
        self.h7_14.setObjectName(u"h7_14")
        self.h7_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_14.setReadOnly(False)

        self.MEM_LINE1_13.addWidget(self.h7_14)


        self.MEM.addLayout(self.MEM_LINE1_13)

        self.MEM_LINE1_14 = QHBoxLayout()
        self.MEM_LINE1_14.setSpacing(0)
        self.MEM_LINE1_14.setObjectName(u"MEM_LINE1_14")
        self.index0_14 = QLineEdit(self.verticalLayoutWidget)
        self.index0_14.setObjectName(u"index0_14")
        self.index0_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_14.setReadOnly(True)

        self.MEM_LINE1_14.addWidget(self.index0_14)

        self.h0_15 = QLineEdit(self.verticalLayoutWidget)
        self.h0_15.setObjectName(u"h0_15")
        self.h0_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_15.setReadOnly(False)

        self.MEM_LINE1_14.addWidget(self.h0_15)

        self.h1_15 = QLineEdit(self.verticalLayoutWidget)
        self.h1_15.setObjectName(u"h1_15")
        self.h1_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_15.setReadOnly(False)

        self.MEM_LINE1_14.addWidget(self.h1_15)

        self.h2_15 = QLineEdit(self.verticalLayoutWidget)
        self.h2_15.setObjectName(u"h2_15")
        self.h2_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_15.setReadOnly(False)

        self.MEM_LINE1_14.addWidget(self.h2_15)

        self.h3_15 = QLineEdit(self.verticalLayoutWidget)
        self.h3_15.setObjectName(u"h3_15")
        self.h3_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_15.setReadOnly(False)

        self.MEM_LINE1_14.addWidget(self.h3_15)

        self.h4_15 = QLineEdit(self.verticalLayoutWidget)
        self.h4_15.setObjectName(u"h4_15")
        self.h4_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_15.setReadOnly(False)

        self.MEM_LINE1_14.addWidget(self.h4_15)

        self.h5_15 = QLineEdit(self.verticalLayoutWidget)
        self.h5_15.setObjectName(u"h5_15")
        self.h5_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_15.setReadOnly(False)

        self.MEM_LINE1_14.addWidget(self.h5_15)

        self.h6_15 = QLineEdit(self.verticalLayoutWidget)
        self.h6_15.setObjectName(u"h6_15")
        self.h6_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_15.setReadOnly(False)

        self.MEM_LINE1_14.addWidget(self.h6_15)

        self.h7_15 = QLineEdit(self.verticalLayoutWidget)
        self.h7_15.setObjectName(u"h7_15")
        self.h7_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_15.setReadOnly(False)

        self.MEM_LINE1_14.addWidget(self.h7_15)


        self.MEM.addLayout(self.MEM_LINE1_14)

        self.MEM_LINE1_15 = QHBoxLayout()
        self.MEM_LINE1_15.setSpacing(0)
        self.MEM_LINE1_15.setObjectName(u"MEM_LINE1_15")
        self.index0_15 = QLineEdit(self.verticalLayoutWidget)
        self.index0_15.setObjectName(u"index0_15")
        self.index0_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_15.setReadOnly(True)

        self.MEM_LINE1_15.addWidget(self.index0_15)

        self.h0_16 = QLineEdit(self.verticalLayoutWidget)
        self.h0_16.setObjectName(u"h0_16")
        self.h0_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_16.setReadOnly(False)

        self.MEM_LINE1_15.addWidget(self.h0_16)

        self.h1_16 = QLineEdit(self.verticalLayoutWidget)
        self.h1_16.setObjectName(u"h1_16")
        self.h1_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_16.setReadOnly(False)

        self.MEM_LINE1_15.addWidget(self.h1_16)

        self.h2_16 = QLineEdit(self.verticalLayoutWidget)
        self.h2_16.setObjectName(u"h2_16")
        self.h2_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_16.setReadOnly(False)

        self.MEM_LINE1_15.addWidget(self.h2_16)

        self.h3_16 = QLineEdit(self.verticalLayoutWidget)
        self.h3_16.setObjectName(u"h3_16")
        self.h3_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_16.setReadOnly(False)

        self.MEM_LINE1_15.addWidget(self.h3_16)

        self.h4_16 = QLineEdit(self.verticalLayoutWidget)
        self.h4_16.setObjectName(u"h4_16")
        self.h4_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_16.setReadOnly(False)

        self.MEM_LINE1_15.addWidget(self.h4_16)

        self.h5_16 = QLineEdit(self.verticalLayoutWidget)
        self.h5_16.setObjectName(u"h5_16")
        self.h5_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_16.setReadOnly(False)

        self.MEM_LINE1_15.addWidget(self.h5_16)

        self.h6_16 = QLineEdit(self.verticalLayoutWidget)
        self.h6_16.setObjectName(u"h6_16")
        self.h6_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_16.setReadOnly(False)

        self.MEM_LINE1_15.addWidget(self.h6_16)

        self.h7_16 = QLineEdit(self.verticalLayoutWidget)
        self.h7_16.setObjectName(u"h7_16")
        self.h7_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_16.setReadOnly(False)

        self.MEM_LINE1_15.addWidget(self.h7_16)


        self.MEM.addLayout(self.MEM_LINE1_15)

        self.MEM_LINE1_16 = QHBoxLayout()
        self.MEM_LINE1_16.setSpacing(0)
        self.MEM_LINE1_16.setObjectName(u"MEM_LINE1_16")
        self.index0_16 = QLineEdit(self.verticalLayoutWidget)
        self.index0_16.setObjectName(u"index0_16")
        self.index0_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_16.setReadOnly(True)

        self.MEM_LINE1_16.addWidget(self.index0_16)

        self.h0_17 = QLineEdit(self.verticalLayoutWidget)
        self.h0_17.setObjectName(u"h0_17")
        self.h0_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_17.setReadOnly(False)

        self.MEM_LINE1_16.addWidget(self.h0_17)

        self.h1_17 = QLineEdit(self.verticalLayoutWidget)
        self.h1_17.setObjectName(u"h1_17")
        self.h1_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_17.setReadOnly(False)

        self.MEM_LINE1_16.addWidget(self.h1_17)

        self.h2_17 = QLineEdit(self.verticalLayoutWidget)
        self.h2_17.setObjectName(u"h2_17")
        self.h2_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_17.setReadOnly(False)

        self.MEM_LINE1_16.addWidget(self.h2_17)

        self.h3_17 = QLineEdit(self.verticalLayoutWidget)
        self.h3_17.setObjectName(u"h3_17")
        self.h3_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_17.setReadOnly(False)

        self.MEM_LINE1_16.addWidget(self.h3_17)

        self.h4_17 = QLineEdit(self.verticalLayoutWidget)
        self.h4_17.setObjectName(u"h4_17")
        self.h4_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_17.setReadOnly(False)

        self.MEM_LINE1_16.addWidget(self.h4_17)

        self.h5_17 = QLineEdit(self.verticalLayoutWidget)
        self.h5_17.setObjectName(u"h5_17")
        self.h5_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_17.setReadOnly(False)

        self.MEM_LINE1_16.addWidget(self.h5_17)

        self.h6_17 = QLineEdit(self.verticalLayoutWidget)
        self.h6_17.setObjectName(u"h6_17")
        self.h6_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_17.setReadOnly(False)

        self.MEM_LINE1_16.addWidget(self.h6_17)

        self.h7_17 = QLineEdit(self.verticalLayoutWidget)
        self.h7_17.setObjectName(u"h7_17")
        self.h7_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_17.setReadOnly(False)

        self.MEM_LINE1_16.addWidget(self.h7_17)


        self.MEM.addLayout(self.MEM_LINE1_16)

        self.MEM_LINE1_17 = QHBoxLayout()
        self.MEM_LINE1_17.setSpacing(0)
        self.MEM_LINE1_17.setObjectName(u"MEM_LINE1_17")
        self.index0_17 = QLineEdit(self.verticalLayoutWidget)
        self.index0_17.setObjectName(u"index0_17")
        self.index0_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_17.setReadOnly(True)

        self.MEM_LINE1_17.addWidget(self.index0_17)

        self.h0_18 = QLineEdit(self.verticalLayoutWidget)
        self.h0_18.setObjectName(u"h0_18")
        self.h0_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_18.setReadOnly(False)

        self.MEM_LINE1_17.addWidget(self.h0_18)

        self.h1_18 = QLineEdit(self.verticalLayoutWidget)
        self.h1_18.setObjectName(u"h1_18")
        self.h1_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_18.setReadOnly(False)

        self.MEM_LINE1_17.addWidget(self.h1_18)

        self.h2_18 = QLineEdit(self.verticalLayoutWidget)
        self.h2_18.setObjectName(u"h2_18")
        self.h2_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_18.setReadOnly(False)

        self.MEM_LINE1_17.addWidget(self.h2_18)

        self.h3_18 = QLineEdit(self.verticalLayoutWidget)
        self.h3_18.setObjectName(u"h3_18")
        self.h3_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_18.setReadOnly(False)

        self.MEM_LINE1_17.addWidget(self.h3_18)

        self.h4_18 = QLineEdit(self.verticalLayoutWidget)
        self.h4_18.setObjectName(u"h4_18")
        self.h4_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_18.setReadOnly(False)

        self.MEM_LINE1_17.addWidget(self.h4_18)

        self.h5_18 = QLineEdit(self.verticalLayoutWidget)
        self.h5_18.setObjectName(u"h5_18")
        self.h5_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_18.setReadOnly(False)

        self.MEM_LINE1_17.addWidget(self.h5_18)

        self.h6_18 = QLineEdit(self.verticalLayoutWidget)
        self.h6_18.setObjectName(u"h6_18")
        self.h6_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_18.setReadOnly(False)

        self.MEM_LINE1_17.addWidget(self.h6_18)

        self.h7_18 = QLineEdit(self.verticalLayoutWidget)
        self.h7_18.setObjectName(u"h7_18")
        self.h7_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_18.setReadOnly(False)

        self.MEM_LINE1_17.addWidget(self.h7_18)


        self.MEM.addLayout(self.MEM_LINE1_17)

        self.MEM_LINE1_18 = QHBoxLayout()
        self.MEM_LINE1_18.setSpacing(0)
        self.MEM_LINE1_18.setObjectName(u"MEM_LINE1_18")
        self.index0_18 = QLineEdit(self.verticalLayoutWidget)
        self.index0_18.setObjectName(u"index0_18")
        self.index0_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_18.setReadOnly(True)

        self.MEM_LINE1_18.addWidget(self.index0_18)

        self.h0_19 = QLineEdit(self.verticalLayoutWidget)
        self.h0_19.setObjectName(u"h0_19")
        self.h0_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_19.setReadOnly(False)

        self.MEM_LINE1_18.addWidget(self.h0_19)

        self.h1_19 = QLineEdit(self.verticalLayoutWidget)
        self.h1_19.setObjectName(u"h1_19")
        self.h1_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_19.setReadOnly(False)

        self.MEM_LINE1_18.addWidget(self.h1_19)

        self.h2_19 = QLineEdit(self.verticalLayoutWidget)
        self.h2_19.setObjectName(u"h2_19")
        self.h2_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_19.setReadOnly(False)

        self.MEM_LINE1_18.addWidget(self.h2_19)

        self.h3_19 = QLineEdit(self.verticalLayoutWidget)
        self.h3_19.setObjectName(u"h3_19")
        self.h3_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_19.setReadOnly(False)

        self.MEM_LINE1_18.addWidget(self.h3_19)

        self.h4_19 = QLineEdit(self.verticalLayoutWidget)
        self.h4_19.setObjectName(u"h4_19")
        self.h4_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_19.setReadOnly(False)

        self.MEM_LINE1_18.addWidget(self.h4_19)

        self.h5_19 = QLineEdit(self.verticalLayoutWidget)
        self.h5_19.setObjectName(u"h5_19")
        self.h5_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_19.setReadOnly(False)

        self.MEM_LINE1_18.addWidget(self.h5_19)

        self.h6_19 = QLineEdit(self.verticalLayoutWidget)
        self.h6_19.setObjectName(u"h6_19")
        self.h6_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_19.setReadOnly(False)

        self.MEM_LINE1_18.addWidget(self.h6_19)

        self.h7_19 = QLineEdit(self.verticalLayoutWidget)
        self.h7_19.setObjectName(u"h7_19")
        self.h7_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_19.setReadOnly(False)

        self.MEM_LINE1_18.addWidget(self.h7_19)


        self.MEM.addLayout(self.MEM_LINE1_18)

        self.MEM_LINE1_19 = QHBoxLayout()
        self.MEM_LINE1_19.setSpacing(0)
        self.MEM_LINE1_19.setObjectName(u"MEM_LINE1_19")
        self.index0_19 = QLineEdit(self.verticalLayoutWidget)
        self.index0_19.setObjectName(u"index0_19")
        self.index0_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_19.setReadOnly(True)

        self.MEM_LINE1_19.addWidget(self.index0_19)

        self.h0_20 = QLineEdit(self.verticalLayoutWidget)
        self.h0_20.setObjectName(u"h0_20")
        self.h0_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_20.setReadOnly(False)

        self.MEM_LINE1_19.addWidget(self.h0_20)

        self.h1_20 = QLineEdit(self.verticalLayoutWidget)
        self.h1_20.setObjectName(u"h1_20")
        self.h1_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_20.setReadOnly(False)

        self.MEM_LINE1_19.addWidget(self.h1_20)

        self.h2_20 = QLineEdit(self.verticalLayoutWidget)
        self.h2_20.setObjectName(u"h2_20")
        self.h2_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_20.setReadOnly(False)

        self.MEM_LINE1_19.addWidget(self.h2_20)

        self.h3_20 = QLineEdit(self.verticalLayoutWidget)
        self.h3_20.setObjectName(u"h3_20")
        self.h3_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_20.setReadOnly(False)

        self.MEM_LINE1_19.addWidget(self.h3_20)

        self.h4_20 = QLineEdit(self.verticalLayoutWidget)
        self.h4_20.setObjectName(u"h4_20")
        self.h4_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_20.setReadOnly(False)

        self.MEM_LINE1_19.addWidget(self.h4_20)

        self.h5_20 = QLineEdit(self.verticalLayoutWidget)
        self.h5_20.setObjectName(u"h5_20")
        self.h5_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_20.setReadOnly(False)

        self.MEM_LINE1_19.addWidget(self.h5_20)

        self.h6_20 = QLineEdit(self.verticalLayoutWidget)
        self.h6_20.setObjectName(u"h6_20")
        self.h6_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_20.setReadOnly(False)

        self.MEM_LINE1_19.addWidget(self.h6_20)

        self.h7_20 = QLineEdit(self.verticalLayoutWidget)
        self.h7_20.setObjectName(u"h7_20")
        self.h7_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_20.setReadOnly(False)

        self.MEM_LINE1_19.addWidget(self.h7_20)


        self.MEM.addLayout(self.MEM_LINE1_19)

        self.MEM_LINE1_20 = QHBoxLayout()
        self.MEM_LINE1_20.setSpacing(0)
        self.MEM_LINE1_20.setObjectName(u"MEM_LINE1_20")
        self.index0_20 = QLineEdit(self.verticalLayoutWidget)
        self.index0_20.setObjectName(u"index0_20")
        self.index0_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_20.setReadOnly(True)

        self.MEM_LINE1_20.addWidget(self.index0_20)

        self.h0_21 = QLineEdit(self.verticalLayoutWidget)
        self.h0_21.setObjectName(u"h0_21")
        self.h0_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_21.setReadOnly(False)

        self.MEM_LINE1_20.addWidget(self.h0_21)

        self.h1_21 = QLineEdit(self.verticalLayoutWidget)
        self.h1_21.setObjectName(u"h1_21")
        self.h1_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_21.setReadOnly(False)

        self.MEM_LINE1_20.addWidget(self.h1_21)

        self.h2_21 = QLineEdit(self.verticalLayoutWidget)
        self.h2_21.setObjectName(u"h2_21")
        self.h2_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_21.setReadOnly(False)

        self.MEM_LINE1_20.addWidget(self.h2_21)

        self.h3_21 = QLineEdit(self.verticalLayoutWidget)
        self.h3_21.setObjectName(u"h3_21")
        self.h3_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_21.setReadOnly(False)

        self.MEM_LINE1_20.addWidget(self.h3_21)

        self.h4_21 = QLineEdit(self.verticalLayoutWidget)
        self.h4_21.setObjectName(u"h4_21")
        self.h4_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_21.setReadOnly(False)

        self.MEM_LINE1_20.addWidget(self.h4_21)

        self.h5_21 = QLineEdit(self.verticalLayoutWidget)
        self.h5_21.setObjectName(u"h5_21")
        self.h5_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_21.setReadOnly(False)

        self.MEM_LINE1_20.addWidget(self.h5_21)

        self.h6_21 = QLineEdit(self.verticalLayoutWidget)
        self.h6_21.setObjectName(u"h6_21")
        self.h6_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_21.setReadOnly(False)

        self.MEM_LINE1_20.addWidget(self.h6_21)

        self.h7_21 = QLineEdit(self.verticalLayoutWidget)
        self.h7_21.setObjectName(u"h7_21")
        self.h7_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_21.setReadOnly(False)

        self.MEM_LINE1_20.addWidget(self.h7_21)


        self.MEM.addLayout(self.MEM_LINE1_20)

        self.MEM_LINE1_21 = QHBoxLayout()
        self.MEM_LINE1_21.setSpacing(0)
        self.MEM_LINE1_21.setObjectName(u"MEM_LINE1_21")
        self.index0_21 = QLineEdit(self.verticalLayoutWidget)
        self.index0_21.setObjectName(u"index0_21")
        self.index0_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_21.setReadOnly(True)

        self.MEM_LINE1_21.addWidget(self.index0_21)

        self.h0_22 = QLineEdit(self.verticalLayoutWidget)
        self.h0_22.setObjectName(u"h0_22")
        self.h0_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_22.setReadOnly(False)

        self.MEM_LINE1_21.addWidget(self.h0_22)

        self.h1_22 = QLineEdit(self.verticalLayoutWidget)
        self.h1_22.setObjectName(u"h1_22")
        self.h1_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_22.setReadOnly(False)

        self.MEM_LINE1_21.addWidget(self.h1_22)

        self.h2_22 = QLineEdit(self.verticalLayoutWidget)
        self.h2_22.setObjectName(u"h2_22")
        self.h2_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_22.setReadOnly(False)

        self.MEM_LINE1_21.addWidget(self.h2_22)

        self.h3_22 = QLineEdit(self.verticalLayoutWidget)
        self.h3_22.setObjectName(u"h3_22")
        self.h3_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_22.setReadOnly(False)

        self.MEM_LINE1_21.addWidget(self.h3_22)

        self.h4_22 = QLineEdit(self.verticalLayoutWidget)
        self.h4_22.setObjectName(u"h4_22")
        self.h4_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_22.setReadOnly(False)

        self.MEM_LINE1_21.addWidget(self.h4_22)

        self.h5_22 = QLineEdit(self.verticalLayoutWidget)
        self.h5_22.setObjectName(u"h5_22")
        self.h5_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_22.setReadOnly(False)

        self.MEM_LINE1_21.addWidget(self.h5_22)

        self.h6_22 = QLineEdit(self.verticalLayoutWidget)
        self.h6_22.setObjectName(u"h6_22")
        self.h6_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_22.setReadOnly(False)

        self.MEM_LINE1_21.addWidget(self.h6_22)

        self.h7_22 = QLineEdit(self.verticalLayoutWidget)
        self.h7_22.setObjectName(u"h7_22")
        self.h7_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_22.setReadOnly(False)

        self.MEM_LINE1_21.addWidget(self.h7_22)


        self.MEM.addLayout(self.MEM_LINE1_21)

        self.MEM_LINE1_22 = QHBoxLayout()
        self.MEM_LINE1_22.setSpacing(0)
        self.MEM_LINE1_22.setObjectName(u"MEM_LINE1_22")
        self.index0_22 = QLineEdit(self.verticalLayoutWidget)
        self.index0_22.setObjectName(u"index0_22")
        self.index0_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_22.setReadOnly(True)

        self.MEM_LINE1_22.addWidget(self.index0_22)

        self.h0_23 = QLineEdit(self.verticalLayoutWidget)
        self.h0_23.setObjectName(u"h0_23")
        self.h0_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_23.setReadOnly(False)

        self.MEM_LINE1_22.addWidget(self.h0_23)

        self.h1_23 = QLineEdit(self.verticalLayoutWidget)
        self.h1_23.setObjectName(u"h1_23")
        self.h1_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_23.setReadOnly(False)

        self.MEM_LINE1_22.addWidget(self.h1_23)

        self.h2_23 = QLineEdit(self.verticalLayoutWidget)
        self.h2_23.setObjectName(u"h2_23")
        self.h2_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_23.setReadOnly(False)

        self.MEM_LINE1_22.addWidget(self.h2_23)

        self.h3_23 = QLineEdit(self.verticalLayoutWidget)
        self.h3_23.setObjectName(u"h3_23")
        self.h3_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_23.setReadOnly(False)

        self.MEM_LINE1_22.addWidget(self.h3_23)

        self.h4_23 = QLineEdit(self.verticalLayoutWidget)
        self.h4_23.setObjectName(u"h4_23")
        self.h4_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_23.setReadOnly(False)

        self.MEM_LINE1_22.addWidget(self.h4_23)

        self.h5_23 = QLineEdit(self.verticalLayoutWidget)
        self.h5_23.setObjectName(u"h5_23")
        self.h5_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_23.setReadOnly(False)

        self.MEM_LINE1_22.addWidget(self.h5_23)

        self.h6_23 = QLineEdit(self.verticalLayoutWidget)
        self.h6_23.setObjectName(u"h6_23")
        self.h6_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_23.setReadOnly(False)

        self.MEM_LINE1_22.addWidget(self.h6_23)

        self.h7_23 = QLineEdit(self.verticalLayoutWidget)
        self.h7_23.setObjectName(u"h7_23")
        self.h7_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_23.setReadOnly(False)

        self.MEM_LINE1_22.addWidget(self.h7_23)


        self.MEM.addLayout(self.MEM_LINE1_22)

        self.MEM_LINE1_23 = QHBoxLayout()
        self.MEM_LINE1_23.setSpacing(0)
        self.MEM_LINE1_23.setObjectName(u"MEM_LINE1_23")
        self.index0_23 = QLineEdit(self.verticalLayoutWidget)
        self.index0_23.setObjectName(u"index0_23")
        self.index0_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_23.setReadOnly(True)

        self.MEM_LINE1_23.addWidget(self.index0_23)

        self.h0_24 = QLineEdit(self.verticalLayoutWidget)
        self.h0_24.setObjectName(u"h0_24")
        self.h0_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_24.setReadOnly(False)

        self.MEM_LINE1_23.addWidget(self.h0_24)

        self.h1_24 = QLineEdit(self.verticalLayoutWidget)
        self.h1_24.setObjectName(u"h1_24")
        self.h1_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_24.setReadOnly(False)

        self.MEM_LINE1_23.addWidget(self.h1_24)

        self.h2_24 = QLineEdit(self.verticalLayoutWidget)
        self.h2_24.setObjectName(u"h2_24")
        self.h2_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_24.setReadOnly(False)

        self.MEM_LINE1_23.addWidget(self.h2_24)

        self.h3_24 = QLineEdit(self.verticalLayoutWidget)
        self.h3_24.setObjectName(u"h3_24")
        self.h3_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_24.setReadOnly(False)

        self.MEM_LINE1_23.addWidget(self.h3_24)

        self.h4_24 = QLineEdit(self.verticalLayoutWidget)
        self.h4_24.setObjectName(u"h4_24")
        self.h4_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_24.setReadOnly(False)

        self.MEM_LINE1_23.addWidget(self.h4_24)

        self.h5_24 = QLineEdit(self.verticalLayoutWidget)
        self.h5_24.setObjectName(u"h5_24")
        self.h5_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_24.setReadOnly(False)

        self.MEM_LINE1_23.addWidget(self.h5_24)

        self.h6_24 = QLineEdit(self.verticalLayoutWidget)
        self.h6_24.setObjectName(u"h6_24")
        self.h6_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_24.setReadOnly(False)

        self.MEM_LINE1_23.addWidget(self.h6_24)

        self.h7_24 = QLineEdit(self.verticalLayoutWidget)
        self.h7_24.setObjectName(u"h7_24")
        self.h7_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_24.setReadOnly(False)

        self.MEM_LINE1_23.addWidget(self.h7_24)


        self.MEM.addLayout(self.MEM_LINE1_23)

        self.MEM_LINE1_24 = QHBoxLayout()
        self.MEM_LINE1_24.setSpacing(0)
        self.MEM_LINE1_24.setObjectName(u"MEM_LINE1_24")
        self.index0_24 = QLineEdit(self.verticalLayoutWidget)
        self.index0_24.setObjectName(u"index0_24")
        self.index0_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_24.setReadOnly(True)

        self.MEM_LINE1_24.addWidget(self.index0_24)

        self.h0_25 = QLineEdit(self.verticalLayoutWidget)
        self.h0_25.setObjectName(u"h0_25")
        self.h0_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_25.setReadOnly(False)

        self.MEM_LINE1_24.addWidget(self.h0_25)

        self.h1_25 = QLineEdit(self.verticalLayoutWidget)
        self.h1_25.setObjectName(u"h1_25")
        self.h1_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_25.setReadOnly(False)

        self.MEM_LINE1_24.addWidget(self.h1_25)

        self.h2_25 = QLineEdit(self.verticalLayoutWidget)
        self.h2_25.setObjectName(u"h2_25")
        self.h2_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_25.setReadOnly(False)

        self.MEM_LINE1_24.addWidget(self.h2_25)

        self.h3_25 = QLineEdit(self.verticalLayoutWidget)
        self.h3_25.setObjectName(u"h3_25")
        self.h3_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_25.setReadOnly(False)

        self.MEM_LINE1_24.addWidget(self.h3_25)

        self.h4_25 = QLineEdit(self.verticalLayoutWidget)
        self.h4_25.setObjectName(u"h4_25")
        self.h4_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_25.setReadOnly(False)

        self.MEM_LINE1_24.addWidget(self.h4_25)

        self.h5_25 = QLineEdit(self.verticalLayoutWidget)
        self.h5_25.setObjectName(u"h5_25")
        self.h5_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_25.setReadOnly(False)

        self.MEM_LINE1_24.addWidget(self.h5_25)

        self.h6_25 = QLineEdit(self.verticalLayoutWidget)
        self.h6_25.setObjectName(u"h6_25")
        self.h6_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_25.setReadOnly(False)

        self.MEM_LINE1_24.addWidget(self.h6_25)

        self.h7_25 = QLineEdit(self.verticalLayoutWidget)
        self.h7_25.setObjectName(u"h7_25")
        self.h7_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_25.setReadOnly(False)

        self.MEM_LINE1_24.addWidget(self.h7_25)


        self.MEM.addLayout(self.MEM_LINE1_24)

        self.MEM_LINE1_25 = QHBoxLayout()
        self.MEM_LINE1_25.setSpacing(0)
        self.MEM_LINE1_25.setObjectName(u"MEM_LINE1_25")
        self.index0_25 = QLineEdit(self.verticalLayoutWidget)
        self.index0_25.setObjectName(u"index0_25")
        self.index0_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_25.setReadOnly(True)

        self.MEM_LINE1_25.addWidget(self.index0_25)

        self.h0_26 = QLineEdit(self.verticalLayoutWidget)
        self.h0_26.setObjectName(u"h0_26")
        self.h0_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_26.setReadOnly(False)

        self.MEM_LINE1_25.addWidget(self.h0_26)

        self.h1_26 = QLineEdit(self.verticalLayoutWidget)
        self.h1_26.setObjectName(u"h1_26")
        self.h1_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_26.setReadOnly(False)

        self.MEM_LINE1_25.addWidget(self.h1_26)

        self.h2_26 = QLineEdit(self.verticalLayoutWidget)
        self.h2_26.setObjectName(u"h2_26")
        self.h2_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_26.setReadOnly(False)

        self.MEM_LINE1_25.addWidget(self.h2_26)

        self.h3_26 = QLineEdit(self.verticalLayoutWidget)
        self.h3_26.setObjectName(u"h3_26")
        self.h3_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_26.setReadOnly(False)

        self.MEM_LINE1_25.addWidget(self.h3_26)

        self.h4_26 = QLineEdit(self.verticalLayoutWidget)
        self.h4_26.setObjectName(u"h4_26")
        self.h4_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_26.setReadOnly(False)

        self.MEM_LINE1_25.addWidget(self.h4_26)

        self.h5_26 = QLineEdit(self.verticalLayoutWidget)
        self.h5_26.setObjectName(u"h5_26")
        self.h5_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_26.setReadOnly(False)

        self.MEM_LINE1_25.addWidget(self.h5_26)

        self.h6_26 = QLineEdit(self.verticalLayoutWidget)
        self.h6_26.setObjectName(u"h6_26")
        self.h6_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_26.setReadOnly(False)

        self.MEM_LINE1_25.addWidget(self.h6_26)

        self.h7_26 = QLineEdit(self.verticalLayoutWidget)
        self.h7_26.setObjectName(u"h7_26")
        self.h7_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_26.setReadOnly(False)

        self.MEM_LINE1_25.addWidget(self.h7_26)


        self.MEM.addLayout(self.MEM_LINE1_25)

        self.MEM_LINE1_26 = QHBoxLayout()
        self.MEM_LINE1_26.setSpacing(0)
        self.MEM_LINE1_26.setObjectName(u"MEM_LINE1_26")
        self.index0_26 = QLineEdit(self.verticalLayoutWidget)
        self.index0_26.setObjectName(u"index0_26")
        self.index0_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_26.setReadOnly(True)

        self.MEM_LINE1_26.addWidget(self.index0_26)

        self.h0_27 = QLineEdit(self.verticalLayoutWidget)
        self.h0_27.setObjectName(u"h0_27")
        self.h0_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_27.setReadOnly(False)

        self.MEM_LINE1_26.addWidget(self.h0_27)

        self.h1_27 = QLineEdit(self.verticalLayoutWidget)
        self.h1_27.setObjectName(u"h1_27")
        self.h1_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_27.setReadOnly(False)

        self.MEM_LINE1_26.addWidget(self.h1_27)

        self.h2_27 = QLineEdit(self.verticalLayoutWidget)
        self.h2_27.setObjectName(u"h2_27")
        self.h2_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_27.setReadOnly(False)

        self.MEM_LINE1_26.addWidget(self.h2_27)

        self.h3_27 = QLineEdit(self.verticalLayoutWidget)
        self.h3_27.setObjectName(u"h3_27")
        self.h3_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_27.setReadOnly(False)

        self.MEM_LINE1_26.addWidget(self.h3_27)

        self.h4_27 = QLineEdit(self.verticalLayoutWidget)
        self.h4_27.setObjectName(u"h4_27")
        self.h4_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_27.setReadOnly(False)

        self.MEM_LINE1_26.addWidget(self.h4_27)

        self.h5_27 = QLineEdit(self.verticalLayoutWidget)
        self.h5_27.setObjectName(u"h5_27")
        self.h5_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_27.setReadOnly(False)

        self.MEM_LINE1_26.addWidget(self.h5_27)

        self.h6_27 = QLineEdit(self.verticalLayoutWidget)
        self.h6_27.setObjectName(u"h6_27")
        self.h6_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_27.setReadOnly(False)

        self.MEM_LINE1_26.addWidget(self.h6_27)

        self.h7_27 = QLineEdit(self.verticalLayoutWidget)
        self.h7_27.setObjectName(u"h7_27")
        self.h7_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_27.setReadOnly(False)

        self.MEM_LINE1_26.addWidget(self.h7_27)


        self.MEM.addLayout(self.MEM_LINE1_26)

        self.MEM_LINE1_27 = QHBoxLayout()
        self.MEM_LINE1_27.setSpacing(0)
        self.MEM_LINE1_27.setObjectName(u"MEM_LINE1_27")
        self.index0_27 = QLineEdit(self.verticalLayoutWidget)
        self.index0_27.setObjectName(u"index0_27")
        self.index0_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_27.setReadOnly(True)

        self.MEM_LINE1_27.addWidget(self.index0_27)

        self.h0_28 = QLineEdit(self.verticalLayoutWidget)
        self.h0_28.setObjectName(u"h0_28")
        self.h0_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_28.setReadOnly(False)

        self.MEM_LINE1_27.addWidget(self.h0_28)

        self.h1_28 = QLineEdit(self.verticalLayoutWidget)
        self.h1_28.setObjectName(u"h1_28")
        self.h1_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_28.setReadOnly(False)

        self.MEM_LINE1_27.addWidget(self.h1_28)

        self.h2_28 = QLineEdit(self.verticalLayoutWidget)
        self.h2_28.setObjectName(u"h2_28")
        self.h2_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_28.setReadOnly(False)

        self.MEM_LINE1_27.addWidget(self.h2_28)

        self.h3_28 = QLineEdit(self.verticalLayoutWidget)
        self.h3_28.setObjectName(u"h3_28")
        self.h3_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_28.setReadOnly(False)

        self.MEM_LINE1_27.addWidget(self.h3_28)

        self.h4_28 = QLineEdit(self.verticalLayoutWidget)
        self.h4_28.setObjectName(u"h4_28")
        self.h4_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_28.setReadOnly(False)

        self.MEM_LINE1_27.addWidget(self.h4_28)

        self.h5_28 = QLineEdit(self.verticalLayoutWidget)
        self.h5_28.setObjectName(u"h5_28")
        self.h5_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_28.setReadOnly(False)

        self.MEM_LINE1_27.addWidget(self.h5_28)

        self.h6_28 = QLineEdit(self.verticalLayoutWidget)
        self.h6_28.setObjectName(u"h6_28")
        self.h6_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_28.setReadOnly(False)

        self.MEM_LINE1_27.addWidget(self.h6_28)

        self.h7_28 = QLineEdit(self.verticalLayoutWidget)
        self.h7_28.setObjectName(u"h7_28")
        self.h7_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_28.setReadOnly(False)

        self.MEM_LINE1_27.addWidget(self.h7_28)


        self.MEM.addLayout(self.MEM_LINE1_27)

        self.MEM_LINE1_28 = QHBoxLayout()
        self.MEM_LINE1_28.setSpacing(0)
        self.MEM_LINE1_28.setObjectName(u"MEM_LINE1_28")
        self.index0_28 = QLineEdit(self.verticalLayoutWidget)
        self.index0_28.setObjectName(u"index0_28")
        self.index0_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_28.setReadOnly(True)

        self.MEM_LINE1_28.addWidget(self.index0_28)

        self.h0_29 = QLineEdit(self.verticalLayoutWidget)
        self.h0_29.setObjectName(u"h0_29")
        self.h0_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_29.setReadOnly(False)

        self.MEM_LINE1_28.addWidget(self.h0_29)

        self.h1_29 = QLineEdit(self.verticalLayoutWidget)
        self.h1_29.setObjectName(u"h1_29")
        self.h1_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_29.setReadOnly(False)

        self.MEM_LINE1_28.addWidget(self.h1_29)

        self.h2_29 = QLineEdit(self.verticalLayoutWidget)
        self.h2_29.setObjectName(u"h2_29")
        self.h2_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_29.setReadOnly(False)

        self.MEM_LINE1_28.addWidget(self.h2_29)

        self.h3_29 = QLineEdit(self.verticalLayoutWidget)
        self.h3_29.setObjectName(u"h3_29")
        self.h3_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_29.setReadOnly(False)

        self.MEM_LINE1_28.addWidget(self.h3_29)

        self.h4_29 = QLineEdit(self.verticalLayoutWidget)
        self.h4_29.setObjectName(u"h4_29")
        self.h4_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_29.setReadOnly(False)

        self.MEM_LINE1_28.addWidget(self.h4_29)

        self.h5_29 = QLineEdit(self.verticalLayoutWidget)
        self.h5_29.setObjectName(u"h5_29")
        self.h5_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_29.setReadOnly(False)

        self.MEM_LINE1_28.addWidget(self.h5_29)

        self.h6_29 = QLineEdit(self.verticalLayoutWidget)
        self.h6_29.setObjectName(u"h6_29")
        self.h6_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_29.setReadOnly(False)

        self.MEM_LINE1_28.addWidget(self.h6_29)

        self.h7_29 = QLineEdit(self.verticalLayoutWidget)
        self.h7_29.setObjectName(u"h7_29")
        self.h7_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_29.setReadOnly(False)

        self.MEM_LINE1_28.addWidget(self.h7_29)


        self.MEM.addLayout(self.MEM_LINE1_28)

        self.MEM_LINE1_29 = QHBoxLayout()
        self.MEM_LINE1_29.setSpacing(0)
        self.MEM_LINE1_29.setObjectName(u"MEM_LINE1_29")
        self.index0_29 = QLineEdit(self.verticalLayoutWidget)
        self.index0_29.setObjectName(u"index0_29")
        self.index0_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_29.setReadOnly(True)

        self.MEM_LINE1_29.addWidget(self.index0_29)

        self.h0_30 = QLineEdit(self.verticalLayoutWidget)
        self.h0_30.setObjectName(u"h0_30")
        self.h0_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_30.setReadOnly(False)

        self.MEM_LINE1_29.addWidget(self.h0_30)

        self.h1_30 = QLineEdit(self.verticalLayoutWidget)
        self.h1_30.setObjectName(u"h1_30")
        self.h1_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_30.setReadOnly(False)

        self.MEM_LINE1_29.addWidget(self.h1_30)

        self.h2_30 = QLineEdit(self.verticalLayoutWidget)
        self.h2_30.setObjectName(u"h2_30")
        self.h2_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_30.setReadOnly(False)

        self.MEM_LINE1_29.addWidget(self.h2_30)

        self.h3_30 = QLineEdit(self.verticalLayoutWidget)
        self.h3_30.setObjectName(u"h3_30")
        self.h3_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_30.setReadOnly(False)

        self.MEM_LINE1_29.addWidget(self.h3_30)

        self.h4_30 = QLineEdit(self.verticalLayoutWidget)
        self.h4_30.setObjectName(u"h4_30")
        self.h4_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_30.setReadOnly(False)

        self.MEM_LINE1_29.addWidget(self.h4_30)

        self.h5_30 = QLineEdit(self.verticalLayoutWidget)
        self.h5_30.setObjectName(u"h5_30")
        self.h5_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_30.setReadOnly(False)

        self.MEM_LINE1_29.addWidget(self.h5_30)

        self.h6_30 = QLineEdit(self.verticalLayoutWidget)
        self.h6_30.setObjectName(u"h6_30")
        self.h6_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_30.setReadOnly(False)

        self.MEM_LINE1_29.addWidget(self.h6_30)

        self.h7_30 = QLineEdit(self.verticalLayoutWidget)
        self.h7_30.setObjectName(u"h7_30")
        self.h7_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_30.setReadOnly(False)

        self.MEM_LINE1_29.addWidget(self.h7_30)


        self.MEM.addLayout(self.MEM_LINE1_29)

        self.MEM_LINE1_30 = QHBoxLayout()
        self.MEM_LINE1_30.setSpacing(0)
        self.MEM_LINE1_30.setObjectName(u"MEM_LINE1_30")
        self.index0_30 = QLineEdit(self.verticalLayoutWidget)
        self.index0_30.setObjectName(u"index0_30")
        self.index0_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_30.setReadOnly(True)

        self.MEM_LINE1_30.addWidget(self.index0_30)

        self.h0_31 = QLineEdit(self.verticalLayoutWidget)
        self.h0_31.setObjectName(u"h0_31")
        self.h0_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_31.setReadOnly(False)

        self.MEM_LINE1_30.addWidget(self.h0_31)

        self.h1_31 = QLineEdit(self.verticalLayoutWidget)
        self.h1_31.setObjectName(u"h1_31")
        self.h1_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_31.setReadOnly(False)

        self.MEM_LINE1_30.addWidget(self.h1_31)

        self.h2_31 = QLineEdit(self.verticalLayoutWidget)
        self.h2_31.setObjectName(u"h2_31")
        self.h2_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_31.setReadOnly(False)

        self.MEM_LINE1_30.addWidget(self.h2_31)

        self.h3_31 = QLineEdit(self.verticalLayoutWidget)
        self.h3_31.setObjectName(u"h3_31")
        self.h3_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_31.setReadOnly(False)

        self.MEM_LINE1_30.addWidget(self.h3_31)

        self.h4_31 = QLineEdit(self.verticalLayoutWidget)
        self.h4_31.setObjectName(u"h4_31")
        self.h4_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_31.setReadOnly(False)

        self.MEM_LINE1_30.addWidget(self.h4_31)

        self.h5_31 = QLineEdit(self.verticalLayoutWidget)
        self.h5_31.setObjectName(u"h5_31")
        self.h5_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_31.setReadOnly(False)

        self.MEM_LINE1_30.addWidget(self.h5_31)

        self.h6_31 = QLineEdit(self.verticalLayoutWidget)
        self.h6_31.setObjectName(u"h6_31")
        self.h6_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_31.setReadOnly(False)

        self.MEM_LINE1_30.addWidget(self.h6_31)

        self.h7_31 = QLineEdit(self.verticalLayoutWidget)
        self.h7_31.setObjectName(u"h7_31")
        self.h7_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_31.setReadOnly(False)

        self.MEM_LINE1_30.addWidget(self.h7_31)


        self.MEM.addLayout(self.MEM_LINE1_30)

        self.MEM_LINE1_31 = QHBoxLayout()
        self.MEM_LINE1_31.setSpacing(0)
        self.MEM_LINE1_31.setObjectName(u"MEM_LINE1_31")
        self.index0_31 = QLineEdit(self.verticalLayoutWidget)
        self.index0_31.setObjectName(u"index0_31")
        self.index0_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_31.setReadOnly(True)

        self.MEM_LINE1_31.addWidget(self.index0_31)

        self.h0_32 = QLineEdit(self.verticalLayoutWidget)
        self.h0_32.setObjectName(u"h0_32")
        self.h0_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_32.setReadOnly(False)

        self.MEM_LINE1_31.addWidget(self.h0_32)

        self.h1_32 = QLineEdit(self.verticalLayoutWidget)
        self.h1_32.setObjectName(u"h1_32")
        self.h1_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_32.setReadOnly(False)

        self.MEM_LINE1_31.addWidget(self.h1_32)

        self.h2_32 = QLineEdit(self.verticalLayoutWidget)
        self.h2_32.setObjectName(u"h2_32")
        self.h2_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_32.setReadOnly(False)

        self.MEM_LINE1_31.addWidget(self.h2_32)

        self.h3_32 = QLineEdit(self.verticalLayoutWidget)
        self.h3_32.setObjectName(u"h3_32")
        self.h3_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_32.setReadOnly(False)

        self.MEM_LINE1_31.addWidget(self.h3_32)

        self.h4_32 = QLineEdit(self.verticalLayoutWidget)
        self.h4_32.setObjectName(u"h4_32")
        self.h4_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_32.setReadOnly(False)

        self.MEM_LINE1_31.addWidget(self.h4_32)

        self.h5_32 = QLineEdit(self.verticalLayoutWidget)
        self.h5_32.setObjectName(u"h5_32")
        self.h5_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_32.setReadOnly(False)

        self.MEM_LINE1_31.addWidget(self.h5_32)

        self.h6_32 = QLineEdit(self.verticalLayoutWidget)
        self.h6_32.setObjectName(u"h6_32")
        self.h6_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_32.setReadOnly(False)

        self.MEM_LINE1_31.addWidget(self.h6_32)

        self.h7_32 = QLineEdit(self.verticalLayoutWidget)
        self.h7_32.setObjectName(u"h7_32")
        self.h7_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_32.setReadOnly(False)

        self.MEM_LINE1_31.addWidget(self.h7_32)


        self.MEM.addLayout(self.MEM_LINE1_31)

        self.MEM_LINE1_32 = QHBoxLayout()
        self.MEM_LINE1_32.setSpacing(0)
        self.MEM_LINE1_32.setObjectName(u"MEM_LINE1_32")
        self.index0_32 = QLineEdit(self.verticalLayoutWidget)
        self.index0_32.setObjectName(u"index0_32")
        self.index0_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_32.setReadOnly(True)

        self.MEM_LINE1_32.addWidget(self.index0_32)

        self.h0_33 = QLineEdit(self.verticalLayoutWidget)
        self.h0_33.setObjectName(u"h0_33")
        self.h0_33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_33.setReadOnly(False)

        self.MEM_LINE1_32.addWidget(self.h0_33)

        self.h1_33 = QLineEdit(self.verticalLayoutWidget)
        self.h1_33.setObjectName(u"h1_33")
        self.h1_33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_33.setReadOnly(False)

        self.MEM_LINE1_32.addWidget(self.h1_33)

        self.h2_33 = QLineEdit(self.verticalLayoutWidget)
        self.h2_33.setObjectName(u"h2_33")
        self.h2_33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_33.setReadOnly(False)

        self.MEM_LINE1_32.addWidget(self.h2_33)

        self.h3_33 = QLineEdit(self.verticalLayoutWidget)
        self.h3_33.setObjectName(u"h3_33")
        self.h3_33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_33.setReadOnly(False)

        self.MEM_LINE1_32.addWidget(self.h3_33)

        self.h4_33 = QLineEdit(self.verticalLayoutWidget)
        self.h4_33.setObjectName(u"h4_33")
        self.h4_33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_33.setReadOnly(False)

        self.MEM_LINE1_32.addWidget(self.h4_33)

        self.h5_33 = QLineEdit(self.verticalLayoutWidget)
        self.h5_33.setObjectName(u"h5_33")
        self.h5_33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_33.setReadOnly(False)

        self.MEM_LINE1_32.addWidget(self.h5_33)

        self.h6_33 = QLineEdit(self.verticalLayoutWidget)
        self.h6_33.setObjectName(u"h6_33")
        self.h6_33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_33.setReadOnly(False)

        self.MEM_LINE1_32.addWidget(self.h6_33)

        self.h7_33 = QLineEdit(self.verticalLayoutWidget)
        self.h7_33.setObjectName(u"h7_33")
        self.h7_33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_33.setReadOnly(False)

        self.MEM_LINE1_32.addWidget(self.h7_33)


        self.MEM.addLayout(self.MEM_LINE1_32)

        self.MEM_LINE1_33 = QHBoxLayout()
        self.MEM_LINE1_33.setSpacing(0)
        self.MEM_LINE1_33.setObjectName(u"MEM_LINE1_33")
        self.index0_33 = QLineEdit(self.verticalLayoutWidget)
        self.index0_33.setObjectName(u"index0_33")
        self.index0_33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.index0_33.setReadOnly(True)

        self.MEM_LINE1_33.addWidget(self.index0_33)

        self.h0_34 = QLineEdit(self.verticalLayoutWidget)
        self.h0_34.setObjectName(u"h0_34")
        self.h0_34.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h0_34.setReadOnly(False)

        self.MEM_LINE1_33.addWidget(self.h0_34)

        self.h1_34 = QLineEdit(self.verticalLayoutWidget)
        self.h1_34.setObjectName(u"h1_34")
        self.h1_34.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h1_34.setReadOnly(False)

        self.MEM_LINE1_33.addWidget(self.h1_34)

        self.h2_34 = QLineEdit(self.verticalLayoutWidget)
        self.h2_34.setObjectName(u"h2_34")
        self.h2_34.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2_34.setReadOnly(False)

        self.MEM_LINE1_33.addWidget(self.h2_34)

        self.h3_34 = QLineEdit(self.verticalLayoutWidget)
        self.h3_34.setObjectName(u"h3_34")
        self.h3_34.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h3_34.setReadOnly(False)

        self.MEM_LINE1_33.addWidget(self.h3_34)

        self.h4_34 = QLineEdit(self.verticalLayoutWidget)
        self.h4_34.setObjectName(u"h4_34")
        self.h4_34.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h4_34.setReadOnly(False)

        self.MEM_LINE1_33.addWidget(self.h4_34)

        self.h5_34 = QLineEdit(self.verticalLayoutWidget)
        self.h5_34.setObjectName(u"h5_34")
        self.h5_34.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h5_34.setReadOnly(False)

        self.MEM_LINE1_33.addWidget(self.h5_34)

        self.h6_34 = QLineEdit(self.verticalLayoutWidget)
        self.h6_34.setObjectName(u"h6_34")
        self.h6_34.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h6_34.setReadOnly(False)

        self.MEM_LINE1_33.addWidget(self.h6_34)

        self.h7_34 = QLineEdit(self.verticalLayoutWidget)
        self.h7_34.setObjectName(u"h7_34")
        self.h7_34.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h7_34.setReadOnly(False)

        self.MEM_LINE1_33.addWidget(self.h7_34)


        self.MEM.addLayout(self.MEM_LINE1_33)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(350, 0, 351, 241))
        self.PINS = QVBoxLayout(self.verticalLayoutWidget_2)
        self.PINS.setObjectName(u"PINS")
        self.PINS.setContentsMargins(0, 0, 0, 0)
        self.RA = QHBoxLayout()
        self.RA.setSpacing(0)
        self.RA.setObjectName(u"RA")
        self.ra = QLineEdit(self.verticalLayoutWidget_2)
        self.ra.setObjectName(u"ra")
        self.ra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ra.setReadOnly(True)

        self.RA.addWidget(self.ra)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setReadOnly(True)

        self.RA.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3.setReadOnly(True)

        self.RA.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_4.setReadOnly(True)

        self.RA.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_5.setReadOnly(True)

        self.RA.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_6.setReadOnly(True)

        self.RA.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_7.setReadOnly(True)

        self.RA.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_8.setReadOnly(True)

        self.RA.addWidget(self.lineEdit_8)

        self.lineEdit_9 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_9.setReadOnly(True)

        self.RA.addWidget(self.lineEdit_9)


        self.PINS.addLayout(self.RA)

        self.TrisA = QHBoxLayout()
        self.TrisA.setSpacing(0)
        self.TrisA.setObjectName(u"TrisA")
        self.trisa = QLineEdit(self.verticalLayoutWidget_2)
        self.trisa.setObjectName(u"trisa")
        self.trisa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisa.setReadOnly(True)

        self.TrisA.addWidget(self.trisa)

        self.trisa7 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisa7.setObjectName(u"trisa7")
        self.trisa7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisa7.setReadOnly(True)

        self.TrisA.addWidget(self.trisa7)

        self.trisa6 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisa6.setObjectName(u"trisa6")
        self.trisa6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisa6.setReadOnly(True)

        self.TrisA.addWidget(self.trisa6)

        self.trisa5 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisa5.setObjectName(u"trisa5")
        self.trisa5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisa5.setReadOnly(True)

        self.TrisA.addWidget(self.trisa5)

        self.trisa4 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisa4.setObjectName(u"trisa4")
        self.trisa4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisa4.setReadOnly(True)

        self.TrisA.addWidget(self.trisa4)

        self.trisa3 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisa3.setObjectName(u"trisa3")
        self.trisa3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisa3.setReadOnly(True)

        self.TrisA.addWidget(self.trisa3)

        self.trisa2 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisa2.setObjectName(u"trisa2")
        self.trisa2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisa2.setReadOnly(True)

        self.TrisA.addWidget(self.trisa2)

        self.trisa1 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisa1.setObjectName(u"trisa1")
        self.trisa1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisa1.setReadOnly(True)

        self.TrisA.addWidget(self.trisa1)

        self.trisa0 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisa0.setObjectName(u"trisa0")
        self.trisa0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisa0.setReadOnly(True)

        self.TrisA.addWidget(self.trisa0)


        self.PINS.addLayout(self.TrisA)

        self.PinA = QHBoxLayout()
        self.PinA.setSpacing(0)
        self.PinA.setObjectName(u"PinA")
        self.pina = QLineEdit(self.verticalLayoutWidget_2)
        self.pina.setObjectName(u"pina")
        self.pina.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pina.setReadOnly(True)

        self.PinA.addWidget(self.pina)

        self.pina7 = QPushButton(self.verticalLayoutWidget_2)
        self.pina7.setObjectName(u"pina7")
        self.pina7.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pina7.sizePolicy().hasHeightForWidth())
        self.pina7.setSizePolicy(sizePolicy)

        self.PinA.addWidget(self.pina7)

        self.pina6 = QPushButton(self.verticalLayoutWidget_2)
        self.pina6.setObjectName(u"pina6")

        self.PinA.addWidget(self.pina6)

        self.pina5 = QPushButton(self.verticalLayoutWidget_2)
        self.pina5.setObjectName(u"pina5")

        self.PinA.addWidget(self.pina5)

        self.pina4 = QPushButton(self.verticalLayoutWidget_2)
        self.pina4.setObjectName(u"pina4")

        self.PinA.addWidget(self.pina4)

        self.pina3 = QPushButton(self.verticalLayoutWidget_2)
        self.pina3.setObjectName(u"pina3")

        self.PinA.addWidget(self.pina3)

        self.pina2 = QPushButton(self.verticalLayoutWidget_2)
        self.pina2.setObjectName(u"pina2")

        self.PinA.addWidget(self.pina2)

        self.pina1 = QPushButton(self.verticalLayoutWidget_2)
        self.pina1.setObjectName(u"pina1")

        self.PinA.addWidget(self.pina1)

        self.pina0 = QPushButton(self.verticalLayoutWidget_2)
        self.pina0.setObjectName(u"pina0")

        self.PinA.addWidget(self.pina0)


        self.PINS.addLayout(self.PinA)

        self.line = QFrame(self.verticalLayoutWidget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.PINS.addWidget(self.line)

        self.RB = QHBoxLayout()
        self.RB.setSpacing(0)
        self.RB.setObjectName(u"RB")
        self.rb = QLineEdit(self.verticalLayoutWidget_2)
        self.rb.setObjectName(u"rb")
        self.rb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rb.setReadOnly(True)

        self.RB.addWidget(self.rb)

        self.lineEdit_10 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_10.setReadOnly(True)

        self.RB.addWidget(self.lineEdit_10)

        self.lineEdit_11 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_11.setReadOnly(True)

        self.RB.addWidget(self.lineEdit_11)

        self.lineEdit_12 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_12.setReadOnly(True)

        self.RB.addWidget(self.lineEdit_12)

        self.lineEdit_13 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_13.setReadOnly(True)

        self.RB.addWidget(self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_14.setReadOnly(True)

        self.RB.addWidget(self.lineEdit_14)

        self.lineEdit_15 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_15.setReadOnly(True)

        self.RB.addWidget(self.lineEdit_15)

        self.lineEdit_16 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_16.setReadOnly(True)

        self.RB.addWidget(self.lineEdit_16)

        self.lineEdit_17 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_17.setReadOnly(True)

        self.RB.addWidget(self.lineEdit_17)


        self.PINS.addLayout(self.RB)

        self.TrisB = QHBoxLayout()
        self.TrisB.setSpacing(0)
        self.TrisB.setObjectName(u"TrisB")
        self.trisb = QLineEdit(self.verticalLayoutWidget_2)
        self.trisb.setObjectName(u"trisb")
        self.trisb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisb.setReadOnly(True)

        self.TrisB.addWidget(self.trisb)

        self.trisb7 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisb7.setObjectName(u"trisb7")
        self.trisb7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisb7.setReadOnly(True)

        self.TrisB.addWidget(self.trisb7)

        self.trisb6 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisb6.setObjectName(u"trisb6")
        self.trisb6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisb6.setReadOnly(True)

        self.TrisB.addWidget(self.trisb6)

        self.trisb5 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisb5.setObjectName(u"trisb5")
        self.trisb5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisb5.setReadOnly(True)

        self.TrisB.addWidget(self.trisb5)

        self.trisb4 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisb4.setObjectName(u"trisb4")
        self.trisb4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisb4.setReadOnly(True)

        self.TrisB.addWidget(self.trisb4)

        self.trisb3 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisb3.setObjectName(u"trisb3")
        self.trisb3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisb3.setReadOnly(True)

        self.TrisB.addWidget(self.trisb3)

        self.trisb2 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisb2.setObjectName(u"trisb2")
        self.trisb2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisb2.setReadOnly(True)

        self.TrisB.addWidget(self.trisb2)

        self.trisb1 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisb1.setObjectName(u"trisb1")
        self.trisb1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisb1.setReadOnly(True)

        self.TrisB.addWidget(self.trisb1)

        self.trisb0 = QLineEdit(self.verticalLayoutWidget_2)
        self.trisb0.setObjectName(u"trisb0")
        self.trisb0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisb0.setReadOnly(True)

        self.TrisB.addWidget(self.trisb0)


        self.PINS.addLayout(self.TrisB)

        self.PinB = QHBoxLayout()
        self.PinB.setSpacing(0)
        self.PinB.setObjectName(u"PinB")
        self.pinb = QLineEdit(self.verticalLayoutWidget_2)
        self.pinb.setObjectName(u"pinb")
        self.pinb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pinb.setReadOnly(True)

        self.PinB.addWidget(self.pinb)

        self.pinb7 = QPushButton(self.verticalLayoutWidget_2)
        self.pinb7.setObjectName(u"pinb7")
        self.pinb7.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pinb7.sizePolicy().hasHeightForWidth())
        self.pinb7.setSizePolicy(sizePolicy)

        self.PinB.addWidget(self.pinb7)

        self.pinb6 = QPushButton(self.verticalLayoutWidget_2)
        self.pinb6.setObjectName(u"pinb6")

        self.PinB.addWidget(self.pinb6)

        self.pinb5 = QPushButton(self.verticalLayoutWidget_2)
        self.pinb5.setObjectName(u"pinb5")

        self.PinB.addWidget(self.pinb5)

        self.pinb4 = QPushButton(self.verticalLayoutWidget_2)
        self.pinb4.setObjectName(u"pinb4")

        self.PinB.addWidget(self.pinb4)

        self.pinb3 = QPushButton(self.verticalLayoutWidget_2)
        self.pinb3.setObjectName(u"pinb3")

        self.PinB.addWidget(self.pinb3)

        self.pinb2 = QPushButton(self.verticalLayoutWidget_2)
        self.pinb2.setObjectName(u"pinb2")

        self.PinB.addWidget(self.pinb2)

        self.pinb1 = QPushButton(self.verticalLayoutWidget_2)
        self.pinb1.setObjectName(u"pinb1")

        self.PinB.addWidget(self.pinb1)

        self.pinb0 = QPushButton(self.verticalLayoutWidget_2)
        self.pinb0.setObjectName(u"pinb0")

        self.PinB.addWidget(self.pinb0)


        self.PINS.addLayout(self.PinB)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(350, 270, 160, 80))
        self.LEDS = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.LEDS.setObjectName(u"LEDS")
        self.LEDS.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(730, 0, 420, 241))
        self.SFR = QVBoxLayout(self.verticalLayoutWidget_3)
        self.SFR.setObjectName(u"SFR")
        self.SFR.setContentsMargins(0, 0, 0, 0)
        self.SVS = QHBoxLayout()
        self.SVS.setObjectName(u"SVS")
        self.Sichtbar = QVBoxLayout()
        self.Sichtbar.setObjectName(u"Sichtbar")
        self.S_1 = QHBoxLayout()
        self.S_1.setObjectName(u"S_1")
        self.WREG_K = QLabel(self.verticalLayoutWidget_3)
        self.WREG_K.setObjectName(u"WREG_K")

        self.S_1.addWidget(self.WREG_K)

        self.WREG_V = QLabel(self.verticalLayoutWidget_3)
        self.WREG_V.setObjectName(u"WREG_V")
        self.WREG_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.S_1.addWidget(self.WREG_V)


        self.Sichtbar.addLayout(self.S_1)

        self.S_2 = QHBoxLayout()
        self.S_2.setObjectName(u"S_2")
        self.FSR_K = QLabel(self.verticalLayoutWidget_3)
        self.FSR_K.setObjectName(u"FSR_K")

        self.S_2.addWidget(self.FSR_K)

        self.FSR_V = QLabel(self.verticalLayoutWidget_3)
        self.FSR_V.setObjectName(u"FSR_V")
        self.FSR_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.S_2.addWidget(self.FSR_V)


        self.Sichtbar.addLayout(self.S_2)

        self.S_3 = QHBoxLayout()
        self.S_3.setObjectName(u"S_3")
        self.PCL_K = QLabel(self.verticalLayoutWidget_3)
        self.PCL_K.setObjectName(u"PCL_K")

        self.S_3.addWidget(self.PCL_K)

        self.PCL_V = QLabel(self.verticalLayoutWidget_3)
        self.PCL_V.setObjectName(u"PCL_V")
        self.PCL_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.S_3.addWidget(self.PCL_V)


        self.Sichtbar.addLayout(self.S_3)

        self.S_4 = QHBoxLayout()
        self.S_4.setObjectName(u"S_4")
        self.PCLATH_K = QLabel(self.verticalLayoutWidget_3)
        self.PCLATH_K.setObjectName(u"PCLATH_K")

        self.S_4.addWidget(self.PCLATH_K)

        self.PCLATH_V = QLabel(self.verticalLayoutWidget_3)
        self.PCLATH_V.setObjectName(u"PCLATH_V")
        self.PCLATH_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.S_4.addWidget(self.PCLATH_V)


        self.Sichtbar.addLayout(self.S_4)

        self.S_5 = QHBoxLayout()
        self.S_5.setObjectName(u"S_5")
        self.Status_K = QLabel(self.verticalLayoutWidget_3)
        self.Status_K.setObjectName(u"Status_K")

        self.S_5.addWidget(self.Status_K)

        self.Status_V = QLabel(self.verticalLayoutWidget_3)
        self.Status_V.setObjectName(u"Status_V")
        self.Status_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.S_5.addWidget(self.Status_V)


        self.Sichtbar.addLayout(self.S_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Sichtbar.addItem(self.verticalSpacer)


        self.SVS.addLayout(self.Sichtbar)

        self.Versteckt = QVBoxLayout()
        self.Versteckt.setObjectName(u"Versteckt")
        self.V_1 = QHBoxLayout()
        self.V_1.setObjectName(u"V_1")
        self.PC_K = QLabel(self.verticalLayoutWidget_3)
        self.PC_K.setObjectName(u"PC_K")

        self.V_1.addWidget(self.PC_K)

        self.PC_V = QLabel(self.verticalLayoutWidget_3)
        self.PC_V.setObjectName(u"PC_V")
        self.PC_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.V_1.addWidget(self.PC_V)


        self.Versteckt.addLayout(self.V_1)

        self.S_7 = QHBoxLayout()
        self.S_7.setObjectName(u"S_7")
        self.Stackpointer_K = QLabel(self.verticalLayoutWidget_3)
        self.Stackpointer_K.setObjectName(u"Stackpointer_K")

        self.S_7.addWidget(self.Stackpointer_K)

        self.Stackpointer_V = QLabel(self.verticalLayoutWidget_3)
        self.Stackpointer_V.setObjectName(u"Stackpointer_V")
        self.Stackpointer_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.S_7.addWidget(self.Stackpointer_V)


        self.Versteckt.addLayout(self.S_7)

        self.S_8 = QHBoxLayout()
        self.S_8.setObjectName(u"S_8")
        self.WDTACTIVE = QCheckBox(self.verticalLayoutWidget_3)
        self.WDTACTIVE.setObjectName(u"WDTACTIVE")

        self.S_8.addWidget(self.WDTACTIVE)


        self.Versteckt.addLayout(self.S_8)

        self.S_9 = QHBoxLayout()
        self.S_9.setObjectName(u"S_9")
        self.WDT_K = QLabel(self.verticalLayoutWidget_3)
        self.WDT_K.setObjectName(u"WDT_K")

        self.S_9.addWidget(self.WDT_K)

        self.WDT_V = QLabel(self.verticalLayoutWidget_3)
        self.WDT_V.setObjectName(u"WDT_V")
        self.WDT_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.S_9.addWidget(self.WDT_V)


        self.Versteckt.addLayout(self.S_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Versteckt.addItem(self.verticalSpacer_2)


        self.SVS.addLayout(self.Versteckt)

        self.Stack = QVBoxLayout()
        self.Stack.setSpacing(0)
        self.Stack.setObjectName(u"Stack")
        self.stack = QLabel(self.verticalLayoutWidget_3)
        self.stack.setObjectName(u"stack")
        self.stack.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Stack.addWidget(self.stack)

        self.stack_7 = QLabel(self.verticalLayoutWidget_3)
        self.stack_7.setObjectName(u"stack_7")
        self.stack_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Stack.addWidget(self.stack_7)

        self.stack_6 = QLabel(self.verticalLayoutWidget_3)
        self.stack_6.setObjectName(u"stack_6")
        self.stack_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Stack.addWidget(self.stack_6)

        self.stack_5 = QLabel(self.verticalLayoutWidget_3)
        self.stack_5.setObjectName(u"stack_5")
        self.stack_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Stack.addWidget(self.stack_5)

        self.stack_4 = QLabel(self.verticalLayoutWidget_3)
        self.stack_4.setObjectName(u"stack_4")
        self.stack_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Stack.addWidget(self.stack_4)

        self.stack_3 = QLabel(self.verticalLayoutWidget_3)
        self.stack_3.setObjectName(u"stack_3")
        self.stack_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Stack.addWidget(self.stack_3)

        self.stack_2 = QLabel(self.verticalLayoutWidget_3)
        self.stack_2.setObjectName(u"stack_2")
        self.stack_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Stack.addWidget(self.stack_2)

        self.stack_1 = QLabel(self.verticalLayoutWidget_3)
        self.stack_1.setObjectName(u"stack_1")
        self.stack_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Stack.addWidget(self.stack_1)

        self.stack_0 = QLabel(self.verticalLayoutWidget_3)
        self.stack_0.setObjectName(u"stack_0")
        self.stack_0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Stack.addWidget(self.stack_0)


        self.SVS.addLayout(self.Stack)


        self.SFR.addLayout(self.SVS)

        self.Status_REG = QGridLayout()
        self.Status_REG.setObjectName(u"Status_REG")
        self.DC_V = QLabel(self.verticalLayoutWidget_3)
        self.DC_V.setObjectName(u"DC_V")
        self.DC_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.DC_V, 1, 6, 1, 1)

        self.label_16 = QLabel(self.verticalLayoutWidget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.label_16, 0, 7, 1, 1)

        self.label_9 = QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.label_9, 0, 3, 1, 1)

        self.label_14 = QLabel(self.verticalLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.label_14, 0, 5, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.label_2, 0, 0, 1, 1)

        self.RP_V = QLabel(self.verticalLayoutWidget_3)
        self.RP_V.setObjectName(u"RP_V")
        self.RP_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.RP_V, 1, 1, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.label_5, 0, 2, 1, 1)

        self.RP0_V = QLabel(self.verticalLayoutWidget_3)
        self.RP0_V.setObjectName(u"RP0_V")
        self.RP0_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.RP0_V, 1, 2, 1, 1)

        self.Z_V = QLabel(self.verticalLayoutWidget_3)
        self.Z_V.setObjectName(u"Z_V")
        self.Z_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.Z_V, 1, 5, 1, 1)

        self.C_V = QLabel(self.verticalLayoutWidget_3)
        self.C_V.setObjectName(u"C_V")
        self.C_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.C_V, 1, 7, 1, 1)

        self.TO_V = QLabel(self.verticalLayoutWidget_3)
        self.TO_V.setObjectName(u"TO_V")
        self.TO_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.TO_V, 1, 3, 1, 1)

        self.label_15 = QLabel(self.verticalLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.label_15, 0, 6, 1, 1)

        self.IRP_V = QLabel(self.verticalLayoutWidget_3)
        self.IRP_V.setObjectName(u"IRP_V")
        self.IRP_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.IRP_V, 1, 0, 1, 1)

        self.PD_V = QLabel(self.verticalLayoutWidget_3)
        self.PD_V.setObjectName(u"PD_V")
        self.PD_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.PD_V, 1, 4, 1, 1)

        self.label_13 = QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.label_13, 0, 4, 1, 1)

        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Status_REG.addWidget(self.label_3, 0, 1, 1, 1)


        self.SFR.addLayout(self.Status_REG)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pina7.setDefault(False)
        self.pina6.setDefault(False)
        self.pina5.setDefault(False)
        self.pina4.setDefault(False)
        self.pina3.setDefault(False)
        self.pina2.setDefault(False)
        self.pina1.setDefault(False)
        self.pina0.setDefault(False)
        self.pinb7.setDefault(False)
        self.pinb6.setDefault(False)
        self.pinb5.setDefault(False)
        self.pinb4.setDefault(False)
        self.pinb3.setDefault(False)
        self.pinb2.setDefault(False)
        self.pinb1.setDefault(False)
        self.pinb0.setDefault(False)


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
        self.index0_2.setText(QCoreApplication.translate("MainWindow", u"08", None))
        self.h0_3.setText("")
        self.h1_3.setText("")
        self.h2_3.setText("")
        self.h3_3.setText("")
        self.h4_3.setText("")
        self.h5_3.setText("")
        self.h6_3.setText("")
        self.h7_3.setText("")
        self.index0_3.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.h0_4.setText("")
        self.h1_4.setText("")
        self.h2_4.setText("")
        self.h3_4.setText("")
        self.h4_4.setText("")
        self.h5_4.setText("")
        self.h6_4.setText("")
        self.h7_4.setText("")
        self.index0_4.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.h0_5.setText("")
        self.h1_5.setText("")
        self.h2_5.setText("")
        self.h3_5.setText("")
        self.h4_5.setText("")
        self.h5_5.setText("")
        self.h6_5.setText("")
        self.h7_5.setText("")
        self.index0_5.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.h0_6.setText("")
        self.h1_6.setText("")
        self.h2_6.setText("")
        self.h3_6.setText("")
        self.h4_6.setText("")
        self.h5_6.setText("")
        self.h6_6.setText("")
        self.h7_6.setText("")
        self.index0_6.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.h0_7.setText("")
        self.h1_7.setText("")
        self.h2_7.setText("")
        self.h3_7.setText("")
        self.h4_7.setText("")
        self.h5_7.setText("")
        self.h6_7.setText("")
        self.h7_7.setText("")
        self.index0_7.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.h0_8.setText("")
        self.h1_8.setText("")
        self.h2_8.setText("")
        self.h3_8.setText("")
        self.h4_8.setText("")
        self.h5_8.setText("")
        self.h6_8.setText("")
        self.h7_8.setText("")
        self.index0_8.setText(QCoreApplication.translate("MainWindow", u"38", None))
        self.h0_9.setText("")
        self.h1_9.setText("")
        self.h2_9.setText("")
        self.h3_9.setText("")
        self.h4_9.setText("")
        self.h5_9.setText("")
        self.h6_9.setText("")
        self.h7_9.setText("")
        self.index0_9.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.h0_10.setText("")
        self.h1_10.setText("")
        self.h2_10.setText("")
        self.h3_10.setText("")
        self.h4_10.setText("")
        self.h5_10.setText("")
        self.h6_10.setText("")
        self.h7_10.setText("")
        self.index0_10.setText(QCoreApplication.translate("MainWindow", u"48", None))
        self.h0_11.setText("")
        self.h1_11.setText("")
        self.h2_11.setText("")
        self.h3_11.setText("")
        self.h4_11.setText("")
        self.h5_11.setText("")
        self.h6_11.setText("")
        self.h7_11.setText("")
        self.index0_12.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.h0_13.setText("")
        self.h1_13.setText("")
        self.h2_13.setText("")
        self.h3_13.setText("")
        self.h4_13.setText("")
        self.h5_13.setText("")
        self.h6_13.setText("")
        self.h7_13.setText("")
        self.index0_13.setText(QCoreApplication.translate("MainWindow", u"58", None))
        self.h0_14.setText("")
        self.h1_14.setText("")
        self.h2_14.setText("")
        self.h3_14.setText("")
        self.h4_14.setText("")
        self.h5_14.setText("")
        self.h6_14.setText("")
        self.h7_14.setText("")
        self.index0_14.setText(QCoreApplication.translate("MainWindow", u"60", None))
        self.h0_15.setText("")
        self.h1_15.setText("")
        self.h2_15.setText("")
        self.h3_15.setText("")
        self.h4_15.setText("")
        self.h5_15.setText("")
        self.h6_15.setText("")
        self.h7_15.setText("")
        self.index0_15.setText(QCoreApplication.translate("MainWindow", u"68", None))
        self.h0_16.setText("")
        self.h1_16.setText("")
        self.h2_16.setText("")
        self.h3_16.setText("")
        self.h4_16.setText("")
        self.h5_16.setText("")
        self.h6_16.setText("")
        self.h7_16.setText("")
        self.index0_16.setText(QCoreApplication.translate("MainWindow", u"70", None))
        self.h0_17.setText("")
        self.h1_17.setText("")
        self.h2_17.setText("")
        self.h3_17.setText("")
        self.h4_17.setText("")
        self.h5_17.setText("")
        self.h6_17.setText("")
        self.h7_17.setText("")
        self.index0_17.setText(QCoreApplication.translate("MainWindow", u"78", None))
        self.h0_18.setText("")
        self.h1_18.setText("")
        self.h2_18.setText("")
        self.h3_18.setText("")
        self.h4_18.setText("")
        self.h5_18.setText("")
        self.h6_18.setText("")
        self.h7_18.setText("")
        self.index0_18.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.h0_19.setText("")
        self.h1_19.setText("")
        self.h2_19.setText("")
        self.h3_19.setText("")
        self.h4_19.setText("")
        self.h5_19.setText("")
        self.h6_19.setText("")
        self.h7_19.setText("")
        self.index0_19.setText(QCoreApplication.translate("MainWindow", u"88", None))
        self.h0_20.setText("")
        self.h1_20.setText("")
        self.h2_20.setText("")
        self.h3_20.setText("")
        self.h4_20.setText("")
        self.h5_20.setText("")
        self.h6_20.setText("")
        self.h7_20.setText("")
        self.index0_20.setText(QCoreApplication.translate("MainWindow", u"90", None))
        self.h0_21.setText("")
        self.h1_21.setText("")
        self.h2_21.setText("")
        self.h3_21.setText("")
        self.h4_21.setText("")
        self.h5_21.setText("")
        self.h6_21.setText("")
        self.h7_21.setText("")
        self.index0_21.setText(QCoreApplication.translate("MainWindow", u"98", None))
        self.h0_22.setText("")
        self.h1_22.setText("")
        self.h2_22.setText("")
        self.h3_22.setText("")
        self.h4_22.setText("")
        self.h5_22.setText("")
        self.h6_22.setText("")
        self.h7_22.setText("")
        self.index0_22.setText(QCoreApplication.translate("MainWindow", u"A0", None))
        self.h0_23.setText("")
        self.h1_23.setText("")
        self.h2_23.setText("")
        self.h3_23.setText("")
        self.h4_23.setText("")
        self.h5_23.setText("")
        self.h6_23.setText("")
        self.h7_23.setText("")
        self.index0_23.setText(QCoreApplication.translate("MainWindow", u"A8", None))
        self.h0_24.setText("")
        self.h1_24.setText("")
        self.h2_24.setText("")
        self.h3_24.setText("")
        self.h4_24.setText("")
        self.h5_24.setText("")
        self.h6_24.setText("")
        self.h7_24.setText("")
        self.index0_24.setText(QCoreApplication.translate("MainWindow", u"B0", None))
        self.h0_25.setText("")
        self.h1_25.setText("")
        self.h2_25.setText("")
        self.h3_25.setText("")
        self.h4_25.setText("")
        self.h5_25.setText("")
        self.h6_25.setText("")
        self.h7_25.setText("")
        self.index0_25.setText(QCoreApplication.translate("MainWindow", u"B8", None))
        self.h0_26.setText("")
        self.h1_26.setText("")
        self.h2_26.setText("")
        self.h3_26.setText("")
        self.h4_26.setText("")
        self.h5_26.setText("")
        self.h6_26.setText("")
        self.h7_26.setText("")
        self.index0_26.setText(QCoreApplication.translate("MainWindow", u"C0", None))
        self.h0_27.setText("")
        self.h1_27.setText("")
        self.h2_27.setText("")
        self.h3_27.setText("")
        self.h4_27.setText("")
        self.h5_27.setText("")
        self.h6_27.setText("")
        self.h7_27.setText("")
        self.index0_27.setText(QCoreApplication.translate("MainWindow", u"C8", None))
        self.h0_28.setText("")
        self.h1_28.setText("")
        self.h2_28.setText("")
        self.h3_28.setText("")
        self.h4_28.setText("")
        self.h5_28.setText("")
        self.h6_28.setText("")
        self.h7_28.setText("")
        self.index0_28.setText(QCoreApplication.translate("MainWindow", u"D0", None))
        self.h0_29.setText("")
        self.h1_29.setText("")
        self.h2_29.setText("")
        self.h3_29.setText("")
        self.h4_29.setText("")
        self.h5_29.setText("")
        self.h6_29.setText("")
        self.h7_29.setText("")
        self.index0_29.setText(QCoreApplication.translate("MainWindow", u"D8", None))
        self.h0_30.setText("")
        self.h1_30.setText("")
        self.h2_30.setText("")
        self.h3_30.setText("")
        self.h4_30.setText("")
        self.h5_30.setText("")
        self.h6_30.setText("")
        self.h7_30.setText("")
        self.index0_30.setText(QCoreApplication.translate("MainWindow", u"E0", None))
        self.h0_31.setText("")
        self.h1_31.setText("")
        self.h2_31.setText("")
        self.h3_31.setText("")
        self.h4_31.setText("")
        self.h5_31.setText("")
        self.h6_31.setText("")
        self.h7_31.setText("")
        self.index0_31.setText(QCoreApplication.translate("MainWindow", u"E8", None))
        self.h0_32.setText("")
        self.h1_32.setText("")
        self.h2_32.setText("")
        self.h3_32.setText("")
        self.h4_32.setText("")
        self.h5_32.setText("")
        self.h6_32.setText("")
        self.h7_32.setText("")
        self.index0_32.setText(QCoreApplication.translate("MainWindow", u"F0", None))
        self.h0_33.setText("")
        self.h1_33.setText("")
        self.h2_33.setText("")
        self.h3_33.setText("")
        self.h4_33.setText("")
        self.h5_33.setText("")
        self.h6_33.setText("")
        self.h7_33.setText("")
        self.index0_33.setText(QCoreApplication.translate("MainWindow", u"F8", None))
        self.h0_34.setText("")
        self.h1_34.setText("")
        self.h2_34.setText("")
        self.h3_34.setText("")
        self.h4_34.setText("")
        self.h5_34.setText("")
        self.h6_34.setText("")
        self.h7_34.setText("")
        self.ra.setText(QCoreApplication.translate("MainWindow", u"RA", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.trisa.setText(QCoreApplication.translate("MainWindow", u"Tris", None))
        self.trisa7.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisa6.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisa5.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisa4.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisa3.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisa2.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisa1.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisa0.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.pina.setText(QCoreApplication.translate("MainWindow", u"Pin", None))
        self.pina7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pina6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pina5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pina4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pina3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pina2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pina1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pina0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.rb.setText(QCoreApplication.translate("MainWindow", u"RB", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.lineEdit_14.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.lineEdit_15.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.lineEdit_16.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lineEdit_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.trisb.setText(QCoreApplication.translate("MainWindow", u"Tris", None))
        self.trisb7.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisb6.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisb5.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisb4.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisb3.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisb2.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisb1.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.trisb0.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.pinb.setText(QCoreApplication.translate("MainWindow", u"Pin", None))
        self.pinb7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pinb6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pinb5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pinb4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pinb3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pinb2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pinb1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pinb0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.WREG_K.setText(QCoreApplication.translate("MainWindow", u"W-REG", None))
        self.WREG_V.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.FSR_K.setText(QCoreApplication.translate("MainWindow", u"FSR", None))
        self.FSR_V.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.PCL_K.setText(QCoreApplication.translate("MainWindow", u"PCL", None))
        self.PCL_V.setText(QCoreApplication.translate("MainWindow", u"01", None))
        self.PCLATH_K.setText(QCoreApplication.translate("MainWindow", u"PCLATH", None))
        self.PCLATH_V.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.Status_K.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.Status_V.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.PC_K.setText(QCoreApplication.translate("MainWindow", u"PC", None))
        self.PC_V.setText(QCoreApplication.translate("MainWindow", u"0001", None))
        self.Stackpointer_K.setText(QCoreApplication.translate("MainWindow", u"Stackpointer", None))
        self.Stackpointer_V.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.WDTACTIVE.setText(QCoreApplication.translate("MainWindow", u"WDT aktiv", None))
        self.WDT_K.setText(QCoreApplication.translate("MainWindow", u"WDT", None))
        self.WDT_V.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.stack.setText(QCoreApplication.translate("MainWindow", u"Stack", None))
        self.stack_7.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.stack_6.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.stack_5.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.stack_4.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.stack_3.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.stack_2.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.stack_1.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.stack_0.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.DC_V.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TO", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"IRP", None))
        self.RP_V.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"RP0", None))
        self.RP0_V.setText("")
        self.Z_V.setText("")
        self.C_V.setText("")
        self.TO_V.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"DC", None))
        self.IRP_V.setText("")
        self.PD_V.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"PD", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"RP", None))
    # retranslateUi

