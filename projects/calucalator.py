from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys
import math

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("991MS Scientific Calculator")
        self.setFixedSize(450, 700)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet("""
            font-size:28px;
            padding:15px;
            background:#f4f4f4;
            border:2px solid black;
        """)

        layout = QGridLayout()

        buttons = [
            ['sin', 'cos', 'tan', 'log'],
            ['√', 'x²', '(', ')'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                btn = QPushButton(text)
                btn.setMinimumHeight(60)
                btn.clicked.connect(self.button_clicked)
                layout.addWidget(btn, r, c)

        widget = QWidget()
        main = QVBoxLayout()
        main.addWidget(self.display)
        main.addLayout(layout)
        widget.setLayout(main)

        self.setCentralWidget(widget)

    def button_clicked(self):
        btn = self.sender().text()

        if btn == '=':
            try:
                expr = self.display.text()
                expr = expr.replace('√', 'math.sqrt')
                expr = expr.replace('sin', 'math.sin')
                expr = expr.replace('cos', 'math.cos')
                expr = expr.replace('tan', 'math.tan')
                expr = expr.replace('log', 'math.log10')
                self.display.setText(str(eval(expr)))
            except:
                zself.display.setText("Error")
        elif btn == 'x²':
            self.display.insert('**2')
        else:
            self.display.insert(btn)

app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec())