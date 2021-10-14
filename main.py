import sys
from PyQt5.QtWidgets import QApplication
from gui.App import App

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = App()
    sys.exit(app.exec_())
