from PyQt5.QtGui import QFont, QDoubleValidator, QIntValidator, QPalette
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from gui.MplCanvas import MplCanvas
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QCheckBox, QDialog
from math import pi


class App(QDialog):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.left = 100
        self.top = 100
        self.title = 'DF Computational Practicum'
        self.width = 1600
        self.height = 800
        self.x0 = pi
        self.y0 = 1.0
        self.X = 4 * pi
        self.N = 20
        self.FROM = None
        self.TO = None
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.errorPalette = QPalette()
        self.buttonTextSize = 16
        self.labelTextSize = 14
        self.UiComponents()

    def UiComponents(self):
        shift = 200
        shift_y = 45
        shift_y2 = 110
        self.validator = QDoubleValidator(-1000, 1000, 4)
        self.validator.setNotation(QDoubleValidator.StandardNotation)

        self.mplCanvas = MplCanvas(self)

        self.toolbar = NavigationToolbar(self.mplCanvas, self)
        self.toolbar.coordinates = False

        self.button = QPushButton("Plot", self)
        self.button.setFont(QFont('Times', self.buttonTextSize))
        self.button.setGeometry(1010 + shift, 690, 185, 100)
        self.button.clicked.connect(self.buttonClicked)

        self.buttonLTE = QPushButton("LTE", self)
        self.buttonLTE.setDisabled(True)
        self.buttonLTE.setFont(QFont('Times', self.buttonTextSize))
        self.buttonLTE.setGeometry(1010 + shift, 590, 185, 90)
        self.buttonLTE.clicked.connect(self.buttonLTEClicked)

        self.buttonED = QPushButton("Error\ndepending", self)
        self.buttonED.setDisabled(True)
        self.buttonED.setFont(QFont('Times', self.buttonTextSize))
        self.buttonED.setGeometry(1205 + shift, 690, 185, 90)
        self.buttonED.clicked.connect(self.buttonEDClicked)

        self.buttonGTE = QPushButton("GTE", self)
        self.buttonGTE.setDisabled(True)
        self.buttonGTE.setFont(QFont('Times', self.buttonTextSize))
        self.buttonGTE.setGeometry(1205 + shift, 590, 185, 90)
        self.buttonGTE.clicked.connect(self.buttonGTEClicked)

        self.init_label = QLabel(self)
        self.init_label.setGeometry(1080 + shift, 40 - shift_y, 250, 50)
        self.init_label.setFont(QFont('Arial', self.labelTextSize, italic=True))
        self.init_label.setText("Initial Parameters")

        self.x0_label = QLabel(self)
        self.x0_label.move(1060 + shift, 100 - shift_y)
        self.x0_label.setFont(QFont('Arial', self.labelTextSize))
        self.x0_label.setText("x0 = ")

        self.y0_label = QLabel(self)
        self.y0_label.move(1060 + shift, 160 - shift_y)
        self.y0_label.setFont(QFont('Arial', self.labelTextSize))
        self.y0_label.setText("y0 = ")

        self.X_label = QLabel(self)
        self.X_label.move(1060 + shift, 220 - shift_y)
        self.X_label.setFont(QFont('Arial', self.labelTextSize))
        self.X_label.setText("X  = ")

        self.N_label = QLabel(self)
        self.N_label.move(1060 + shift, 280 - shift_y)
        self.N_label.setFont(QFont('Arial', self.labelTextSize))
        self.N_label.setText("N  = ")

        self.x0_input = QLineEdit(self)
        self.x0_input.setGeometry(1150 + shift, 90 - shift_y, 200, 50)
        self.x0_input.setFont(QFont('Arial', self.labelTextSize))
        self.x0_input.setPlaceholderText(str(self.x0))
        self.x0_input.setValidator(self.validator)

        self.y0_input = QLineEdit(self)
        self.y0_input.setGeometry(1150 + shift, 150 - shift_y, 200, 50)
        self.y0_input.setFont(QFont('Arial', self.labelTextSize))
        self.y0_input.setPlaceholderText(str(self.y0))
        self.y0_input.setValidator(self.validator)

        self.X_input = QLineEdit(self)
        self.X_input.setGeometry(1150 + shift, 210 - shift_y, 200, 50)
        self.X_input.setFont(QFont('Arial', self.labelTextSize))
        self.X_input.setPlaceholderText(str(self.X))
        self.X_input.setValidator(self.validator)

        self.N_input = QLineEdit(self)
        self.N_input.setGeometry(1150 + shift, 270 - shift_y, 200, 50)
        self.N_input.setFont(QFont('Arial', self.labelTextSize))
        self.N_input.setPlaceholderText(str(self.N))
        self.N_input.setValidator(QIntValidator(1, 1000))

        self.met_label = QLabel(self)
        self.met_label.setGeometry(1080 + shift, 380 - shift_y2 + 20, 250, 50)
        self.met_label.setFont(QFont('Arial', self.labelTextSize, italic=True))
        self.met_label.setText("Show methods")

        self.e_cb = QCheckBox("Euler Method", self)
        self.e_cb.setGeometry(1010 + shift, 440 - shift_y2, 250, 50)
        self.e_cb.setFont(QFont('Arial', self.labelTextSize))

        self.ie_cb = QCheckBox("Improved Euler Method", self)
        self.ie_cb.setGeometry(1010 + shift, 480 - shift_y2, 420, 50)
        self.ie_cb.setFont(QFont('Arial', self.labelTextSize))

        self.rk_cb = QCheckBox("Runge-Kutta Method", self)
        self.rk_cb.setGeometry(1010 + shift, 520 - shift_y2, 420, 50)
        self.rk_cb.setFont(QFont('Arial', self.labelTextSize))

        self.grid_label = QLabel(self)
        self.grid_label.setGeometry(1080 + shift, 460, 250, 50)
        self.grid_label.setFont(QFont('Arial', self.labelTextSize, italic=True))
        self.grid_label.setText("Grid size")

        self.grid_label = QLabel(self)
        self.grid_label.setGeometry(1010 + shift, 520, 100, 50)
        self.grid_label.setFont(QFont('Arial', self.labelTextSize))
        self.grid_label.setText("from")

        self.from_input = QLineEdit(self)
        self.from_input.setGeometry(1280, 520, 100, 50)
        self.from_input.setFont(QFont('Arial', self.labelTextSize))
        self.from_input.setValidator(QIntValidator(1, 100))

        self.grid_label2 = QLabel(self)
        self.grid_label2.setGeometry(1390, 520, 100, 50)
        self.grid_label2.setFont(QFont('Arial', self.labelTextSize))
        self.grid_label2.setText("to")

        self.to_input = QLineEdit(self)
        self.to_input.setGeometry(1430, 520, 120, 50)
        self.to_input.setFont(QFont('Arial', self.labelTextSize))
        self.to_input.setValidator(QIntValidator(1, 100))

    def correct_grid(self):
        from_copy = self.from_input.text()
        to_copy = self.to_input.text()

        if len(from_copy) == 0 or int(from_copy) == 0:
            if len(to_copy) == 0 or int(to_copy) == 0:
                self.to_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
            self.from_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
            return False
        if len(to_copy) == 0 or int(to_copy) == 0:
            if len(from_copy) == 0 or int(from_copy) == 0:
                self.from_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
            self.to_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
            return False
        self.FROM = int(from_copy)
        if int(to_copy) <= int(from_copy):
            self.to_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
            return False
        self.TO = int(to_copy)

        self.to_input.setStyleSheet("QLineEdit { background-color: white;}")
        self.from_input.setStyleSheet("QLineEdit { background-color: white;}")

        return True


    def correct_input(self):
        x0_copy = self.x0_input.text()
        y0_copy = self.y0_input.text()
        X_copy = self.X_input.text()
        N_copy = self.N_input.text()

        if len(x0_copy) != 0:
            x0_copy = x0_copy.replace('-', '')
            if x0_copy.replace(',', '').isdigit():
                self.x0 = float(self.x0_input.text().replace(',', '.'))
                if self.x0 == 0:
                    self.x0_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
                    return False
            else:
                print(x0_copy.replace(',', ''))
                self.x0_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
                return False
            self.x0_input.setStyleSheet("QLineEdit { background-color: white;}")

        if len(y0_copy) != 0:
            y0_copy = y0_copy.replace('-', '')
            if y0_copy.replace(',', '').isdigit():
                self.y0 = float(self.y0_input.text().replace(',', '.'))
            else:
                self.y0_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
                return False
            self.y0_input.setStyleSheet("QLineEdit { background-color: white;}")

        if len(X_copy) != 0:
            X_copy = X_copy.replace('-', '')
            if X_copy.replace(',', '').isdigit():
                self.X = float(self.X_input.text().replace(',', '.'))
                if self.X <= self.x0 or self.X * self.x0 <= 0:
                    self.X_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
                    self.x0_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
                    return False
            else:
                self.X_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
                return False
            self.X_input.setStyleSheet("QLineEdit { background-color: white;}")

        if len(N_copy) != 0:
            if N_copy.isdigit() or len(N_copy) == 0:
                self.N = int(self.N_input.text())
                if self.N < 1:
                    self.N_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
                    return False
            else:
                self.N_input.setStyleSheet("QLineEdit { background-color: #ed808b;}")
                return False
            self.N_input.setStyleSheet("QLineEdit { background-color: white;}")

        return True

    def buttonClicked(self):
        if self.correct_input():
            self.mplCanvas.plot(self.e_cb.checkState(), self.ie_cb.checkState(), self.rk_cb.checkState(),
                                self.x0, self.y0, self.X, self.N)
            if self.e_cb.checkState() + self.ie_cb.checkState() + self.rk_cb.checkState() > 0:
                self.buttonLTE.setEnabled(True)
                self.buttonGTE.setEnabled(True)
                self.buttonED.setEnabled(True)
            else:
                self.buttonLTE.setDisabled(True)
                self.buttonGTE.setDisabled(True)
                self.buttonED.setDisabled(True)

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

    def buttonLTEClicked(self):
        if self.correct_input():
            self.mplCanvas.plotLTE(self.e_cb.checkState(), self.ie_cb.checkState(), self.rk_cb.checkState(),
                                   self.x0, self.y0, self.X, self.N)
            self.show()

    def buttonGTEClicked(self):
        if self.correct_input():
            self.mplCanvas.plotGTE(self.e_cb.checkState(), self.ie_cb.checkState(), self.rk_cb.checkState(),
                                   self.x0, self.y0, self.X, self.N)
            self.show()

    def buttonEDClicked(self):
        if self.correct_grid():
            self.mplCanvas.plotED(self.e_cb.checkState(), self.ie_cb.checkState(), self.rk_cb.checkState(),
                                  self.FROM, self.TO, self.x0, self.y0, self.X)
            self.show()
