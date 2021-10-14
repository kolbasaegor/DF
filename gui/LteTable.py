from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class LteTable(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)
