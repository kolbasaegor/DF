from PyQt5.QtGui import QFont, QDoubleValidator, QIntValidator, QPalette
from gui.MplCanvas import MplCanvas
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QCheckBox, QApplication
from math import pi

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 100
        self.top = 100
        self.title = 'DF Computational Practicum'
        self.width = 1400
        self.height = 800
        self.x0 = pi
        self.y0 = 1.0
        self.X = 4*pi
        self.N = 100
        self.e_visible = False
        self.ie_visible = False
        self.rk_visible = False
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.errorPalette = QPalette()
        self.UiComponents()

    def UiComponents(self):
        self.mplCanvas = MplCanvas(self)
        self.mplCanvas.move(0, 0)

        self.button = QPushButton("PLOT GRAPHS", self)
        self.button.setFont(QFont('Times', 20))
        self.button.setGeometry(1010, 690, 380, 100)
        self.button.clicked.connect(self.buttonClicked)

        self.buttonLTE = QPushButton("LTE", self)
        self.buttonLTE.setFont(QFont('Times', 20))
        self.buttonLTE.setGeometry(1010, 590, 185, 90)
        # self.buttonLTE.clicked.connect(self.buttonLTEClicked)

        self.buttonGTE = QPushButton("GTE", self)
        self.buttonGTE.setFont(QFont('Times', 20))
        self.buttonGTE.setGeometry(1205, 590, 185, 90)
        # self.buttonGTE.clicked.connect(self.buttonGTEClicked)

        self.init_label = QLabel(self)
        self.init_label.setGeometry(1080, 40, 250, 50)
        self.init_label.setFont(QFont('Arial', 16))
        self.init_label.setText("Initial Parameters")

        self.x0_label = QLabel(self)
        self.x0_label.move(1060, 100)
        self.x0_label.setFont(QFont('Arial', 16))
        self.x0_label.setText("x0 = ")

        self.y0_label = QLabel(self)
        self.y0_label.move(1060, 160)
        self.y0_label.setFont(QFont('Arial', 16))
        self.y0_label.setText("y0 = ")

        self.X_label = QLabel(self)
        self.X_label.move(1060, 220)
        self.X_label.setFont(QFont('Arial', 16))
        self.X_label.setText("X  = ")

        self.N_label = QLabel(self)
        self.N_label.move(1060, 280)
        self.N_label.setFont(QFont('Arial', 16))
        self.N_label.setText("N  = ")

        self.x0_input = QLineEdit(self)
        self.x0_input.setGeometry(1150, 90, 200, 50)
        self.x0_input.setFont(QFont('Arial', 16))
        self.x0_input.setPlaceholderText('3,14')
        self.x0_input.setValidator(QDoubleValidator(-99.99, 99.99, 2))

        self.y0_input = QLineEdit(self)
        self.y0_input.setGeometry(1150, 150, 200, 50)
        self.y0_input.setFont(QFont('Arial', 16))
        self.y0_input.setPlaceholderText('1')
        self.y0_input.setValidator(QDoubleValidator(-99.99, 99.99, 2))

        self.X_input = QLineEdit(self)
        self.X_input.setGeometry(1150, 210, 200, 50)
        self.X_input.setFont(QFont('Arial', 16))
        self.X_input.setPlaceholderText('12,56')
        self.X_input.setValidator(QDoubleValidator(-99.99, 99.99, 2))

        self.N_input = QLineEdit(self)
        self.N_input.setGeometry(1150, 270, 200, 50)
        self.N_input.setFont(QFont('Arial', 16))
        self.N_input.setPlaceholderText('100')
        self.N_input.setValidator(QIntValidator(1,1000))

        self.met_label = QLabel(self)
        self.met_label.setGeometry(1080, 380, 250, 50)
        self.met_label.setFont(QFont('Arial', 16))
        self.met_label.setText("Show methods")

        self.e_cb = QCheckBox("Euler Method", self)
        self.e_cb.setGeometry(1010, 440, 250, 50)
        self.e_cb.setFont(QFont('Arial', 16))

        self.ie_cb = QCheckBox("Improved Euler Method", self)
        self.ie_cb.setGeometry(1010, 480, 420, 50)
        self.ie_cb.setFont(QFont('Arial', 16))

        self.rk_cb = QCheckBox("Runge-Kutta Method", self)
        self.rk_cb.setGeometry(1010, 520, 420, 50)
        self.rk_cb.setFont(QFont('Arial', 16))





    def buttonClicked(self):
        try:
            self.x0 = float(self.x0_input.text().replace(',', '.'))
            if self.x0 == 0:
                raise ZeroDivisionError
        except:
            self.x0_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")

        try:
            self.y0 = float(self.y0_input.text().replace(',', '.'))
        except:
            self.y0_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")

        try:
            self.X = float(self.X_input.text().replace(',', '.'))
        except:
            self.X_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")

        try:
            self.N = int(self.N_input.text())
        except:
            self.N_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")

        if self.x0 == 0:
            self.x0_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
        elif self.X <= self.x0:
            self.X_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
        elif self.N < 1:
            self.N_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
        else:
            self.setDefaultColor()
            self.mplCanvas.plot(self.e_cb.checkState(), self.ie_cb.checkState(), self.rk_cb.checkState(),
                                self.x0, self.y0, self.X, self.N)
            self.show()

    def setDefaultColor(self):
        self.x0_input.setStyleSheet("QLineEdit { }")
        self.x0_input.setPlaceholderText(str(self.x0))
        self.y0_input.setStyleSheet("QLineEdit { }")
        self.y0_input.setPlaceholderText(str(self.y0))
        self.X_input.setStyleSheet("QLineEdit { }")
        self.X_input.setPlaceholderText(str(self.X))
        self.N_input.setStyleSheet("QLineEdit { }")
        self.N_input.setPlaceholderText(str(self.N))






