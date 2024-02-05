from PyQt5.QtWidgets import QApplication
import sys

from view.calculator_ui import CalculatorUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorUI()
    window.setGeometry(100, 100, 900, 400)
    window.show()
    sys.exit(app.exec_())
