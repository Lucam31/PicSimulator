import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cpu import CPU

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot, SLOT)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QAction)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget, QMenu, QFileDialog)

class Ui_MainWindow(object):
    @Slot()
    def on_finished(self) -> None:
        for path in self.dialog.selectedFiles():
            self.cpu.load_program(path)
            self.plainTextEdit.setPlainText(self.cpu.getFile())
    def setupUi(self, MainWindow):
        self.cpu = CPU(self)
        # self.cpu.load_program()
        # self.cpu.execute()
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)



        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 280, 760))
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

        self.index = [QLineEdit] * 32
        self.memorycells = [QLineEdit] * 256
        for i in range(32):
            MEM_LINE = QHBoxLayout()
            MEM_LINE.setSpacing(0)
            self.index[i] = QLineEdit(self.verticalLayoutWidget)
            self.index[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.index[i].setReadOnly(True)

            MEM_LINE.addWidget(self.index[i])

            for j in range(8):
                self.memorycells[j + 8 * i] = QLineEdit(self.verticalLayoutWidget)
                self.memorycells[j + 8 * i].setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.memorycells[j + 8 * i].setReadOnly(False)

                MEM_LINE.addWidget(self.memorycells[j + 8 * i])

            self.MEM.addLayout(MEM_LINE)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(350, 10, 351, 241))
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

        self.trisalst = [QLineEdit] * 8

        for i in range(8):
            self.trisalst[i] = QLineEdit(self.verticalLayoutWidget_2)
            self.trisalst[i].setObjectName(u"trisa" + str(i))
            self.trisalst[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.trisalst[i].setReadOnly(True)
            self.TrisA.addWidget(self.trisalst[i])

        self.PINS.addLayout(self.TrisA)

        self.PinA = QHBoxLayout()
        self.PinA.setSpacing(0)
        self.PinA.setObjectName(u"PinA")
        self.pina = QLineEdit(self.verticalLayoutWidget_2)
        self.pina.setObjectName(u"pina")
        self.pina.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pina.setReadOnly(True)

        self.PinA.addWidget(self.pina)

        self.pinalst = [QPushButton] * 8

        for i in range(8):
            self.pinalst[i] = QPushButton(self.verticalLayoutWidget_2)
            self.pinalst[i].setObjectName(u"pina" + str(i))
            self.PinA.addWidget(self.pinalst[i])

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

        self.trisblst = [QLineEdit] * 8

        for i in range(8):
            self.trisblst[i] = QLineEdit(self.verticalLayoutWidget_2)
            self.trisblst[i].setObjectName(u"trisb" + str(i))
            self.trisblst[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.trisblst[i].setReadOnly(True)
            self.TrisB.addWidget(self.trisblst[i])

        self.PINS.addLayout(self.TrisB)

        self.PinB = QHBoxLayout()
        self.PinB.setSpacing(0)
        self.PinB.setObjectName(u"PinB")
        self.pinb = QLineEdit(self.verticalLayoutWidget_2)
        self.pinb.setObjectName(u"pinb")
        self.pinb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pinb.setReadOnly(True)

        self.PinB.addWidget(self.pinb)

        self.pinblst = [QPushButton] * 8

        for i in range(8):
            self.pinblst[i] = QPushButton(self.verticalLayoutWidget_2)
            self.pinblst[i].setObjectName(u"pinb" + str(i))
            self.PinB.addWidget(self.pinblst[i])

        self.PINS.addLayout(self.PinB)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(350, 270, 311, 60))
        self.LEDS = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.LEDS.setObjectName(u"LEDS")
        self.LEDS.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(740, 10, 450, 250))
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

        self.stacklst = [QLabel] * 8

        for i in range(8):
            self.stacklst[i] = QLabel(self.verticalLayoutWidget_3)
            self.stacklst[i].setObjectName(u"stack" + str(i))
            self.stacklst[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.Stack.addWidget(self.stacklst[i])

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

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(680, 270, 490, 90))
        self.EXECINFOS = QHBoxLayout(self.horizontalLayoutWidget)
        self.EXECINFOS.setObjectName(u"EXECINFOS")
        self.EXECINFOS.setContentsMargins(0, 0, 0, 0)
        self.QUARTTIME = QVBoxLayout()
        self.QUARTTIME.setObjectName(u"QUARTTIME")
        self.Freq_K = QLabel(self.horizontalLayoutWidget)
        self.Freq_K.setObjectName(u"Freq_K")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        self.Freq_K.setFont(font)

        self.QUARTTIME.addWidget(self.Freq_K)

        self.Freq_V = QLabel(self.horizontalLayoutWidget)
        self.Freq_V.setObjectName(u"Freq_V")
        self.Freq_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.QUARTTIME.addWidget(self.Freq_V)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.QUARTTIME.addWidget(self.label)


        self.EXECINFOS.addLayout(self.QUARTTIME)

        self.EXECTIME = QVBoxLayout()
        self.EXECTIME.setObjectName(u"EXECTIME")
        self.EXECTIME.setContentsMargins(0, -1, -1, -1)
        self.Time_K = QLabel(self.horizontalLayoutWidget)
        self.Time_K.setObjectName(u"Time_K")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.Time_K.setFont(font1)

        self.EXECTIME.addWidget(self.Time_K)

        self.Time_V = QLabel(self.horizontalLayoutWidget)
        self.Time_V.setObjectName(u"Time_V")
        self.Time_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.EXECTIME.addWidget(self.Time_V)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.EXECTIME.addWidget(self.pushButton)


        self.EXECINFOS.addLayout(self.EXECTIME)

        self.CTRLBTNS = QGridLayout()
        self.CTRLBTNS.setObjectName(u"CTRLBTNS")
        self.CTRLBTNS.setHorizontalSpacing(-1)
        self.stepin = QPushButton(self.horizontalLayoutWidget)
        self.stepin.setObjectName(u"stepin")

        self.CTRLBTNS.addWidget(self.stepin, 1, 1, 1, 1)

        self.ignore = QPushButton(self.horizontalLayoutWidget)
        self.ignore.setObjectName(u"ignore")

        self.CTRLBTNS.addWidget(self.ignore, 0, 1, 1, 1)

        self.reset = QPushButton(self.horizontalLayoutWidget)
        self.reset.setObjectName(u"reset")

        self.CTRLBTNS.addWidget(self.reset, 0, 0, 1, 1)

        self.go = QPushButton(self.horizontalLayoutWidget)
        self.go.setObjectName(u"go")
        self.go.clicked.connect(self.cpu.execute)

        self.CTRLBTNS.addWidget(self.go, 1, 0, 1, 1)

        self.stepover = QPushButton(self.horizontalLayoutWidget)
        self.stepover.setObjectName(u"stepover")

        self.CTRLBTNS.addWidget(self.stepover, 1, 2, 1, 1)

        self.stepout = QPushButton(self.horizontalLayoutWidget)
        self.stepout.setObjectName(u"stepout")

        self.CTRLBTNS.addWidget(self.stepout, 0, 2, 1, 1)


        self.EXECINFOS.addLayout(self.CTRLBTNS)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(350, 380, 821, 361))
        self.FILEFIELD = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.FILEFIELD.setObjectName(u"FILEFIELD")
        self.FILEFIELD.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox = QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)


        self.FILEFIELD.addLayout(self.verticalLayout_2)

        self.plainTextEdit = QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.FILEFIELD.addWidget(self.plainTextEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 37))


        self.dialog = QFileDialog(MainWindow)

        self.dialog.setFileMode(QFileDialog.ExistingFiles)
        self.dialog.setNameFilter("*.LST *.lst")
        self.dialog.setWindowTitle('Open File...')
        self.dialog.finished.connect(self.on_finished)


        fileMenu = QMenu("&File", MainWindow)
        self.actionOpen = QAction(QIcon.fromTheme("document-open"), "Open File", MainWindow)
        self.actionOpen.setStatusTip("Open LST File")
        self.actionOpen.setShortcut(QKeySequence.Open)
        self.actionOpen.triggered.connect(self.dialog.open)
        fileMenu.addAction(self.actionOpen)
        self.menubar.addMenu(fileMenu)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        for v in self.pinalst:
            v.setDefault(False)

        for v in self.pinblst:
            v.setDefault(False)


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

        val = 0
        for v in self.index:
            hex_value = format(val, '02X')
            v.setText(QCoreApplication.translate("MainWindow", hex_value, None))
            val += 8
        for v in self.memorycells:
            v.setText("")

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
        for v in self.trisalst:
            v.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.pina.setText(QCoreApplication.translate("MainWindow", u"Pin", None))
        for v in self.pinalst:
            v.setText(QCoreApplication.translate("MainWindow", u"0", None))
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
        for v in self.trisblst:
            v.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.pinb.setText(QCoreApplication.translate("MainWindow", u"Pin", None))
        for v in self.pinblst:
            v.setText(QCoreApplication.translate("MainWindow", u"0", None))
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
        for v in self.stacklst:
            v.setText(QCoreApplication.translate("MainWindow", u"0000", None))
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
        self.Freq_K.setText(QCoreApplication.translate("MainWindow", u"Quarzfrequenz", None))
        self.Freq_V.setText(QCoreApplication.translate("MainWindow", u"4,000000 MHz", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1,000us", None))
        self.Time_K.setText(QCoreApplication.translate("MainWindow", u"Laufzeit", None))
        self.Time_V.setText(QCoreApplication.translate("MainWindow", u"0,00 us", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"zur\u00fccksetzen", None))
        self.stepin.setText(QCoreApplication.translate("MainWindow", u"Step in", None))
        self.ignore.setText(QCoreApplication.translate("MainWindow", u"Ignore", None))
        self.reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.go.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.stepover.setText(QCoreApplication.translate("MainWindow", u"Step over", None))
        self.stepout.setText(QCoreApplication.translate("MainWindow", u"Step out", None))
        self.checkBox.setText("")


        self.updateUI()
    # retranslateUi

    def updateUI(self):
        memory = self.cpu.getMemInHex()
        for i in range(len(memory)):
            self.memorycells[i].setText(QCoreApplication.translate("MainWindow", format(memory[i], '02X'), None))
        self.WREG_V.setText(QCoreApplication.translate("MainWindow", format(self.cpu.dMemory.getW(), '02X'), None))

