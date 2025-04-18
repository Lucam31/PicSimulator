import sys
import os
import threading

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cpu import CPU

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Slot, SLOT, QTimer, Q_ARG, QGenericArgument)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QAction, QDesktopServices)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame,
                               QHBoxLayout, QLabel, QLayout, QLineEdit,
                               QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
                               QWidget, QMenu, QFileDialog, QScrollArea)

class LEDWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.led_state = False
        self.setFixedSize(30, 30)

    def toggle_led(self):
        self.led_state = not self.led_state
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        led_color = QColor(255, 172, 28) if self.led_state else QColor(194, 24, 8)  # Grün für an, Rot für aus

        painter.setBrush(led_color)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, self.width(), self.height())




from PySide6.QtCore import QThread, Slot


class Ui_MainWindow(QObject):
    @Slot()
    def on_finished(self) -> None:
        for path in self.dialog.selectedFiles():
            self.onReset()
            fileLines, self.codeNumbers = self.cpu.load_program(path) #fileLines, codenumbers
            self.readFileToScrollArea(fileLines)
        self.cpuThread.quit()
        self.cpuThread.start()
        self.updateIntern()
    @Slot()
    def onReset(self) -> None:
        try:
            self.fileLineslst[self.codeNumbers[self.pc]].setStyleSheet("border: 1px solid None;")
            self.fileLineslst[self.codeNumbers[self.lastpcl]].setStyleSheet("border: 1px solid None;")
        except: pass
        self.cpu.reset()
        self.go.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.cpu.pauseThread = True
        self.stepin.setDisabled(False)
        self.stepover.setDisabled(False)
    @Slot()
    def onCPUFinished(self):
        print("CPU execution finished.")
        self.cpuThread.quit()
        self.cpuThread.wait()
    @Slot()
    def toggleThread(self) -> None:
        if not self.cpu.ready: return
        if self.go.text() == "Go":
            self.go.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
            self.cpu.pauseThread = False
            self.stepin.setDisabled(True)
            self.stepover.setDisabled(True)
        else:
            self.go.setText(QCoreApplication.translate("MainWindow", u"Go", None))
            self.cpu.pauseThread = True
            self.stepin.setDisabled(False)
            self.stepover.setDisabled(False)

    @Slot()
    def on_text_change(self, idx, text):
        try:
            if idx < 128:
                self.cpu.dMemory.writeRegister(idx, int(text, 16), 0)
            else:
                self.cpu.dMemory.writeRegister(idx, int(text, 16), 1)
        except: pass
    @Slot()
    def pinClicked(self, port, pin):
        if port == 'a' and 0 <= pin < len(self.pinalst) and self.pinalst[pin] is not None:
            val = int(self.pinalst[pin].text()) ^ 0x01
            if pin == 3:
                self.cpu.extClk(val)
            self.pinalst[pin].setText(QCoreApplication.translate("MainWindow", str(val), None))
            self.cpu.dMemory.setBit(0x05,7 - pin,val)
        elif port == 'b' and 0 <= pin < len(self.pinblst) and self.pinblst[pin] is not None:
            val = int(self.pinblst[pin].text()) ^ 0x01
            self.pinblst[pin].setText(QCoreApplication.translate("MainWindow", str(val), None))
            self.cpu.dMemory.setBit(0x06, 7 - pin, val)
        elif port == 'status' and 0 <= pin < len(self.pinblst) and self.pinblst[pin] is not None:
            val = int(self.statuslst[pin].text()) ^ 0x01
            self.statuslst[pin].setText(QCoreApplication.translate("MainWindow", str(val), None))
            self.cpu.dMemory.setBit(0x03, 7 - pin, val)
        elif port == 'option' and 0 <= pin < len(self.pinblst) and self.pinblst[pin] is not None:
            val = int(self.optionlst[pin].text()) ^ 0x01
            self.optionlst[pin].setText(QCoreApplication.translate("MainWindow", str(val), None))
            self.cpu.dMemory.setBit(0x01, 7 - pin, val,1)
            self.option_v.setText(QCoreApplication.translate("MainWindow", format(self.cpu.dMemory.readRegister(0x01,1),'02X'), None))
        elif port == 'intcon' and 0 <= pin < len(self.pinblst) and self.pinblst[pin] is not None:
            val = int(self.intconlst[pin].text()) ^ 0x01
            self.intconlst[pin].setText(QCoreApplication.translate("MainWindow", str(val), None))
            self.cpu.dMemory.setBit(0x0b, 7 - pin, val)
            self.intcon_v.setText(QCoreApplication.translate("MainWindow", format(self.cpu.dMemory.readRegister(0x0b),'02X'), None))
        self.cpu.updateUI()
    @Slot()
    def stepOver(self):
        self.cpu.stepOver()
    @Slot()
    def stepIn(self):
        self.cpu.stepIn()
    @Slot()
    def onIgnore(self):
        self.fileLineslst[self.codeNumbers[self.cpu.dMemory.getPCounter()]].setStyleSheet("border: 1px solid None;")
        self.cpu.dMemory.incPCL()
        self.cpu.dMemory.setPCounter()
        self.cpu.updateUI()

    @Slot(int)
    def updateUI(self, data):
        QMetaObject.invokeMethod(self, "_updateUI", Qt.QueuedConnection, Q_ARG(int, data))

    @Slot(int)
    def _updateUI(self, data):
        # memory = data["memory"]
        memory = self.cpu.getMemInHex()
        for i in range(len(memory)):
            self.memorycells[i].setText(QCoreApplication.translate("MainWindow", format(memory[i], '02X'), None))
        self.WREG_V.setText(QCoreApplication.translate("MainWindow", format(data, '02X'), None))
        self.Time_V.setText(QCoreApplication.translate("MainWindow", str(self.cpu.clock) + " us", None))
        stackContent = self.cpu.getStack()
        for i in range(8 - len(stackContent)): stackContent.append(0)
        for i in range(len(stackContent)):
            self.stacklst[7-i].setText(QCoreApplication.translate("MainWindow", f'{stackContent[i]:04}', None))
        self.VT_V.setText(QCoreApplication.translate("MainWindow", str(self.cpu.dMemory.getPrescaler()[2]), None))
        fsr, pcl, self.lastpcl, pclath, self.pc, status, stackP = self.cpu.getUiInfo()
        self.FSR_V.setText(QCoreApplication.translate("MainWindow", f'{fsr:02}', None))
        self.PCL_V.setText(QCoreApplication.translate("MainWindow", f'{pcl:02}', None))
        self.PCLATH_V.setText(QCoreApplication.translate("MainWindow", f'{pclath:02}', None))
        self.Status_V.setText(QCoreApplication.translate("MainWindow", f'{status:02}', None))
        self.PC_V.setText(QCoreApplication.translate("MainWindow", f'{self.pc:04}', None))
        self.Stackpointer_V.setText(QCoreApplication.translate("MainWindow", f'{stackP:02}', None))
        for i in range(8): #update tris
            valA = self.cpu.dMemory.getBit(0x05, i,1)
            self.trisalst[7-i].setText(QCoreApplication.translate("MainWindow", 'i' if (valA == 1) else 'o', None))
            valB = self.cpu.dMemory.getBit(0x06, i, 1)
            self.trisblst[7 - i].setText(QCoreApplication.translate("MainWindow", 'i' if (valB == 1) else 'o', None))
        try:
            self.fileLineslst[self.codeNumbers[self.pc]].setStyleSheet("border: 1px solid red;")
            if self.pc != self.lastpcl:
                self.fileLineslst[self.codeNumbers[self.lastpcl]].setStyleSheet("border: 1px solid None;")
            widget = self.fileLineslst[self.codeNumbers[self.pc]-5]
            scroll_bar = self.scrollArea.verticalScrollBar()
            scroll_bar.setValue(widget.y())
            if self.breakChecklst[self.codeNumbers[self.pc]].isChecked():
                self.go.setText(QCoreApplication.translate("MainWindow", u"Go", None))
                self.cpu.pauseThread = True
                self.stepin.setDisabled(False)
                self.stepover.setDisabled(False)
        except: pass

    def setupUi(self, MainWindow):
        self.cpu = CPU(True)
        self.cpuThread = QThread()  # Create a QThread instance
        self.cpu.moveToThread(self.cpuThread)  # Move CPU to the thread

        # Connect signals
        self.cpu.update_signal.connect(self.updateUI)
        self.cpu.finished_signal.connect(self.onCPUFinished)
        self.cpuThread.started.connect(self.cpu.execute)


        self.codeNumbers = []


        # cpu.load_program()
        # cpu.execute()
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 800)



        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 280, 760))
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
                self.memorycells[j + 8 * i].textChanged.connect(lambda text, idx=j + 8 * i: self.on_text_change(idx, text))

                MEM_LINE.addWidget(self.memorycells[j + 8 * i])

            self.MEM.addLayout(MEM_LINE)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(350, 20, 350, 240))
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

        self.lineEditsA = []
        for i in range(8):
            self.lineEditsA.append(QLineEdit(self.verticalLayoutWidget_2))
            self.lineEditsA[i].setObjectName(u"lineEdit_"+str(2+i))
            self.lineEditsA[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.lineEditsA[i].setReadOnly(True)

            self.RA.addWidget(self.lineEditsA[i])

        self.PINS.addLayout(self.RA)

        self.TrisA = QHBoxLayout()
        self.TrisA.setSpacing(0)
        self.TrisA.setObjectName(u"TrisA")
        self.trisa = QLineEdit(self.verticalLayoutWidget_2)
        self.trisa.setObjectName(u"trisa")
        self.trisa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisa.setReadOnly(True)

        self.TrisA.addWidget(self.trisa)

        self.trisalst = []

        for i in range(8):
            self.trisalst.append(QLineEdit(self.verticalLayoutWidget_2))
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

        self.pinalst = []
        for i in range(8):
            self.pinalst.append(QPushButton(self.verticalLayoutWidget_2))
            self.pinalst[i].clicked.connect(lambda _, pin=i: self.pinClicked('a', pin))
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

        self.lineEditsB = []
        for i in range(8):
            self.lineEditsB.append(QLineEdit(self.verticalLayoutWidget_2))
            self.lineEditsB[i].setObjectName(u"lineEdit_1"+str(i))
            self.lineEditsB[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.lineEditsB[i].setReadOnly(True)

            self.RB.addWidget(self.lineEditsB[i])


        self.PINS.addLayout(self.RB)

        self.TrisB = QHBoxLayout()
        self.TrisB.setSpacing(0)
        self.TrisB.setObjectName(u"TrisB")
        self.trisb = QLineEdit(self.verticalLayoutWidget_2)
        self.trisb.setObjectName(u"trisb")
        self.trisb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trisb.setReadOnly(True)

        self.TrisB.addWidget(self.trisb)

        self.trisblst = []

        for i in range(8):
            self.trisblst.append(QLineEdit(self.verticalLayoutWidget_2))
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
        self.pinblst = []
        for i in range(8):
            self.pinblst.append(QPushButton(self.verticalLayoutWidget_2))
            self.pinblst[i].setObjectName(u"pinb" + str(i))
            self.pinblst[i].clicked.connect(lambda _, pin=i: self.pinClicked('b', pin))
            self.PinB.addWidget(self.pinblst[i])

        self.PINS.addLayout(self.PinB)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(350, 280, 350, 60))
        self.LEDS = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.LEDS.setObjectName(u"LEDS")

        self.ledslst = []

        for i in range(8):
            self.ledslst.append(LEDWidget())
            self.LEDS.addWidget(self.ledslst[i])

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(740, 20, 350, 340))
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

        self.S_10 = QHBoxLayout()
        self.S_10.setObjectName(u"S_10")
        self.VT_K = QLabel(self.verticalLayoutWidget_3)
        self.VT_K.setObjectName(u"VT_K")

        self.S_10.addWidget(self.VT_K)

        self.VT_V = QLabel(self.verticalLayoutWidget_3)
        self.VT_V.setObjectName(u"VT_V")
        self.VT_V.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.S_10.addWidget(self.VT_V)

        self.Versteckt.addLayout(self.S_10)

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

        self.SVS.addLayout(self.Versteckt)

        self.verticalLayoutWidget_stack = QWidget(self.centralwidget)
        self.verticalLayoutWidget_stack.setObjectName(u"verticalLayoutWidget_stack")
        self.verticalLayoutWidget_stack.setGeometry(QRect(1170, 20, 100, 340))

        self.Stack = QVBoxLayout(self.verticalLayoutWidget_stack)
        self.Stack.setObjectName(u"Stack")
        self.stack = QLabel(self.verticalLayoutWidget_3)
        self.stack.setObjectName(u"stack")
        self.stack.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Stack.addWidget(self.stack)

        self.stacklst = []

        for i in range(8):
            self.stacklst.append(QLabel(self.verticalLayoutWidget_3))
            self.stacklst[i].setObjectName(u"stack" + str(i))
            self.stacklst[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.Stack.addWidget(self.stacklst[i])

        self.Stack.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        self.SFR.addLayout(self.SVS)

        self.statusstack = QVBoxLayout()
        self.statusstack.setSpacing(0)

        self.statusheader = QHBoxLayout()

        self.label_16 = QLabel(self.verticalLayoutWidget_3)
        self.label_16.setObjectName(u"label_16")

        self.statusheader.addWidget(self.label_16)

        self.label_9 = QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.statusheader.addWidget(self.label_9)

        self.label_14 = QLabel(self.verticalLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")

        self.statusheader.addWidget(self.label_14)

        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.statusheader.addWidget(self.label_2)

        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.statusheader.addWidget(self.label_5)

        self.label_15 = QLabel(self.verticalLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")

        self.statusheader.addWidget(self.label_15)

        self.label_13 = QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        self.statusheader.addWidget(self.label_13)

        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.statusheader.addWidget(self.label_3)

        self.statusstack.addLayout(self.statusheader)

        self.statusvalues = QHBoxLayout()


        self.statuslst = []

        for i in range(8):
            self.statuslst.append(QPushButton())
            self.statuslst[i].clicked.connect(lambda _, pin=i: self.pinClicked('status', pin))
            self.statusvalues.addWidget(self.statuslst[i])

            self.statusvalues.addItem(QSpacerItem(15, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.statusstack.addLayout(self.statusvalues)

        self.SFR.addLayout(self.statusstack)

        self.optionstack = QVBoxLayout()
        self.optionstack.setSpacing(0)

        self.header = QHBoxLayout()
        self.header.setObjectName(u"header")

        self.option_k = QLabel()
        self.header.addWidget(self.option_k)

        self.option_v = QLabel()
        self.header.addWidget(self.option_v)


        self.headerspacer = QSpacerItem(220, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.header.addItem(self.headerspacer)

        self.optionstack.addLayout(self.header)

        self.optionrowheaders = QHBoxLayout()

        self.rbp = QLabel()
        self.optionrowheaders.addWidget(self.rbp)

        self.IntEdg = QLabel()
        self.optionrowheaders.addWidget(self.IntEdg)

        self.TOCS = QLabel()
        self.optionrowheaders.addWidget(self.TOCS)

        self.TOSE = QLabel()
        self.optionrowheaders.addWidget(self.TOSE)

        self.PSA = QLabel()
        self.optionrowheaders.addWidget(self.PSA)

        self.PS2 = QLabel()
        self.optionrowheaders.addWidget(self.PS2)

        self.PS1 = QLabel()
        self.optionrowheaders.addWidget(self.PS1)

        self.PS0 = QLabel()
        self.optionrowheaders.addWidget(self.PS0)

        self.optionstack.addLayout(self.optionrowheaders)

        self.optionvalues = QHBoxLayout()

        self.optionlst = [QLabel] * 8

        for i in range(8):
            self.optionlst[i] = QPushButton()
            self.optionlst[i].clicked.connect(lambda _, pin=i: self.pinClicked('option', pin))
            self.optionvalues.addWidget(self.optionlst[i])
            self.optionvalues.addItem(QSpacerItem(15, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.optionstack.addLayout(self.optionvalues)


        self.SFR.addLayout(self.optionstack)

        self.intconstack = QVBoxLayout()
        self.intconstack.setSpacing(0)

        self.header2 = QHBoxLayout()
        self.header2.setObjectName(u"header")

        self.intcon_k = QLabel()
        self.header2.addWidget(self.intcon_k)

        self.intcon_v = QLabel()
        self.header2.addWidget(self.intcon_v)

        self.headerspacer2 = QSpacerItem(220, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.header2.addItem(self.headerspacer2)

        self.intconstack.addLayout(self.header2)

        self.intconrowheaders = QHBoxLayout()

        self.gie = QLabel()
        self.intconrowheaders.addWidget(self.gie)

        self.pie = QLabel()
        self.intconrowheaders.addWidget(self.pie)

        self.toie = QLabel()
        self.intconrowheaders.addWidget(self.toie)

        self.inte = QLabel()
        self.intconrowheaders.addWidget(self.inte)

        self.rbie = QLabel()
        self.intconrowheaders.addWidget(self.rbie)

        self.toif = QLabel()
        self.intconrowheaders.addWidget(self.toif)

        self.intf = QLabel()
        self.intconrowheaders.addWidget(self.intf)

        self.rbif = QLabel()
        self.intconrowheaders.addWidget(self.rbif)

        self.intconstack.addLayout(self.intconrowheaders)

        self.intconvalues = QHBoxLayout()

        self.intconlst = [QLabel] * 8

        for i in range(8):
            self.intconlst[i] = QPushButton()
            self.intconlst[i].clicked.connect(lambda _, pin=i: self.pinClicked('intcon', pin))
            self.intconvalues.addWidget(self.intconlst[i])
            self.intconvalues.addItem(QSpacerItem(15, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.intconstack.addLayout(self.intconvalues)

        self.SFR.addLayout(self.intconstack)


        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(1170, 380, 100, 380))
        self.EXECINFOS = QVBoxLayout(self.horizontalLayoutWidget)
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

        self.CTRLBTNS = QVBoxLayout()
        self.CTRLBTNS.setObjectName(u"CTRLBTNS")
        self.stepin = QPushButton(self.horizontalLayoutWidget)
        self.stepin.setObjectName(u"stepin")
        self.stepin.clicked.connect(self.stepIn)

        self.CTRLBTNS.addWidget(self.stepin)

        self.ignore = QPushButton(self.horizontalLayoutWidget)
        self.ignore.setObjectName(u"ignore")
        self.ignore.clicked.connect(self.onIgnore)

        self.CTRLBTNS.addWidget(self.ignore)

        self.reset = QPushButton(self.horizontalLayoutWidget)
        self.reset.setObjectName(u"reset")
        self.reset.clicked.connect(self.onReset)

        self.CTRLBTNS.addWidget(self.reset)

        self.go = QPushButton(self.horizontalLayoutWidget)
        self.go.setObjectName(u"go")
        self.go.clicked.connect(self.toggleThread)

        self.CTRLBTNS.addWidget(self.go)

        self.stepover = QPushButton(self.horizontalLayoutWidget)
        self.stepover.setObjectName(u"stepover")
        self.stepover.clicked.connect(self.stepOver)

        self.CTRLBTNS.addWidget(self.stepover)

        self.stepout = QPushButton(self.horizontalLayoutWidget)
        self.stepout.setObjectName(u"stepout")

        self.CTRLBTNS.addWidget(self.stepout)

        self.EXECINFOS.addLayout(self.CTRLBTNS)


        self.Widget = QWidget(self.centralwidget)
        self.Widget.setGeometry(350, 380, 800, 380)

        self.scrollArea = QScrollArea(self.Widget)
        self.scrollArea.setGeometry(0, 0, 800, 380)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setContentsMargins(0, 0, 0, 0)

        self.contentWidget = QWidget()


        self.FILEFIELD = QVBoxLayout(self.contentWidget)
        self.FILEFIELD.setSpacing(0) 
        self.FILEFIELD.setContentsMargins(0, 0, 0, 0) 


        self.scrollArea.setWidget(self.contentWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 37))


        self.dialog = QFileDialog(MainWindow)

        self.dialog.setFileMode(QFileDialog.ExistingFiles)
        self.dialog.setNameFilter("*.LST *.lst")
        self.dialog.setWindowTitle('Open File...')
        self.dialog.accepted.connect(self.on_finished)


        fileMenu = QMenu("&File", MainWindow)
        self.actionOpen = QAction(QIcon.fromTheme("document-open"), "Open File", MainWindow)
        self.actionOpen.setStatusTip("Open LST File")
        self.actionOpen.setShortcut(QKeySequence.Open)
        self.actionOpen.triggered.connect(self.dialog.open)
        fileMenu.addAction(self.actionOpen)
        self.menubar.addMenu(fileMenu)

        helpMenu = QMenu("&Help", MainWindow)

        self.actionOpenDocumentation = QAction(QIcon.fromTheme("help-contents"), "Open documentation", MainWindow)
        self.actionOpenDocumentation.setStatusTip("Öffne die Dokumentation")
        self.actionOpenDocumentation.triggered.connect(self.open_documentation)

        helpMenu.addAction(self.actionOpenDocumentation)
        self.menubar.addMenu(helpMenu)

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
        for i in range(8):
            self.lineEditsA[i].setText(QCoreApplication.translate("MainWindow", str(7-i), None))
        self.trisa.setText(QCoreApplication.translate("MainWindow", u"Tris", None))
        for v in self.trisalst:
            v.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.pina.setText(QCoreApplication.translate("MainWindow", u"Pin", None))
        for v in self.pinalst:
            v.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.rb.setText(QCoreApplication.translate("MainWindow", u"RB", None))
        for i in range(8):
            self.lineEditsB[i].setText(QCoreApplication.translate("MainWindow", str(7-i), None))
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
        self.VT_K.setText(QCoreApplication.translate("MainWindow", u"VT", None))
        self.VT_V.setText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.WDTACTIVE.setText(QCoreApplication.translate("MainWindow", u"WDT aktiv", None))
        self.WDT_K.setText(QCoreApplication.translate("MainWindow", u"WDT", None))
        self.WDT_V.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.stack.setText(QCoreApplication.translate("MainWindow", u"Stack", None))
        for v in self.stacklst:
            v.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        for i in range(8):
            self.statuslst[i].setText(QCoreApplication.translate("MainWindow", str(self.cpu.dMemory.getBit(0x03,i)), None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TO", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"IRP", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"RP0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"DC", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"PD", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"RP", None))
        self.Freq_K.setText(QCoreApplication.translate("MainWindow", u"Quarzfrequenz", None))
        self.Freq_V.setText(QCoreApplication.translate("MainWindow", u"4,000000 MHz", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1,000us", None))
        self.Time_K.setText(QCoreApplication.translate("MainWindow", u"Laufzeit", None))
        self.Time_V.setText(QCoreApplication.translate("MainWindow", u"0,00 us", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Zur\u00fccksetzen", None))
        self.stepin.setText(QCoreApplication.translate("MainWindow", u"Step in", None))
        self.ignore.setText(QCoreApplication.translate("MainWindow", u"Ignore", None))
        self.reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.go.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.stepover.setText(QCoreApplication.translate("MainWindow", u"Step over", None))
        self.stepout.setText(QCoreApplication.translate("MainWindow", u"Step out", None))
        self.option_k.setText(QCoreApplication.translate("MainWindow", u"Option", None))
        self.option_v.setText(QCoreApplication.translate("MainWindow", format(self.cpu.dMemory.readRegister(0x01,1),'02X'), None))
        self.rbp.setText(QCoreApplication.translate("MainWindow", u"RBP", None))
        self.IntEdg.setText(QCoreApplication.translate("MainWindow", u"IntEdg", None))
        self.TOCS.setText(QCoreApplication.translate("MainWindow", u"TOCS", None))
        self.TOSE.setText(QCoreApplication.translate("MainWindow", u"TOSE", None))
        self.PSA.setText(QCoreApplication.translate("MainWindow", u"PSA", None))
        self.PS2.setText(QCoreApplication.translate("MainWindow", u"PS2", None))
        self.PS1.setText(QCoreApplication.translate("MainWindow", u"PS1", None))
        self.PS0.setText(QCoreApplication.translate("MainWindow", u"PS0", None))
        for i in range(8):
            self.optionlst[i].setText(QCoreApplication.translate("MainWindow", str(self.cpu.dMemory.getBit(0x01,i,1)), None))
        self.intcon_k.setText(QCoreApplication.translate("MainWindow", u"INTCON", None))
        self.intcon_v.setText(QCoreApplication.translate("MainWindow", format(self.cpu.dMemory.readRegister(0x0b),'02X'), None))
        self.gie.setText(QCoreApplication.translate("MainWindow", u"GIE", None))
        self.pie.setText(QCoreApplication.translate("MainWindow", u"PIE", None))
        self.toie.setText(QCoreApplication.translate("MainWindow", u"T0IE", None))
        self.inte.setText(QCoreApplication.translate("MainWindow", u"INTE", None))
        self.rbie.setText(QCoreApplication.translate("MainWindow", u"RBIE", None))
        self.toif.setText(QCoreApplication.translate("MainWindow", u"T0IF", None))
        self.intf.setText(QCoreApplication.translate("MainWindow", u"INTF", None))
        self.rbif.setText(QCoreApplication.translate("MainWindow", u"RBIF", None))
        for i in range(8):
            self.intconlst[i].setText(QCoreApplication.translate("MainWindow", str(self.cpu.dMemory.getBit(0x0b,i)), None))


        self.updateIntern()
    # retranslateUi

    def open_documentation(self):
        doc_url = QUrl.fromLocalFile("/Users/leandergantert/Documents/Projekte/Python/PicSimulator/Dateien/Bewertungsschema_Simulator_DHBW_HSO_2024.pdf")
        QDesktopServices.openUrl(doc_url)

    def updateIntern(self):
        # memory = self.cpu.getMemInHex()
        # for i in range(len(memory)):
        #     self.memorycells[i].setText(QCoreApplication.translate("MainWindow", format(memory[i], '02X'), None))
        # self.WREG_V.setText(QCoreApplication.translate("MainWindow", format(self.cpu.dMemory.getW(), '02X'), None))
        # self.Time_V.setText(QCoreApplication.translate("MainWindow", str(self.cpu.clock) + " us", None))
        QMetaObject.invokeMethod(self, "_updateUI", Qt.QueuedConnection, Q_ARG(int, 0))

    def readFileToScrollArea(self, lines: list):
        # try:
        for i in reversed(range(self.FILEFIELD.count())):
            self.FILEFIELD.removeItem(self.FILEFIELD.itemAt(i))
        # except:
        #     pass

        self.breakChecklst = []
        self.fileLineslst = []

        for line in lines:
            self.linelayout = QHBoxLayout()
            self.linelayout.setSpacing(10)
            self.linelayout.setContentsMargins(0, 0, 0, 0)

            checkbox = QCheckBox()
            checkbox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

            lineedit = QLineEdit()
            lineedit.setReadOnly(True)
            lineedit.setText(line)
            lineedit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            lineedit.setStyleSheet("border: 1px solid None;")

            self.breakChecklst.append(checkbox)
            self.fileLineslst.append(lineedit)

            self.linelayout.addWidget(checkbox)
            self.linelayout.addWidget(lineedit)

            self.FILEFIELD.addLayout(self.linelayout)