from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication, QColor, QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QGridLayout, QHBoxLayout, QApplication, \
    QWidget, QLabel, QGraphicsDropShadowEffect
import sys
from controller.calculator_logic import CalculatorLogic
from view.history_dialog import HistoryDialog


class CalculatorUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("QMainWindow { background-color: #f8f8ff; }")
        self.setWindowIcon(QIcon("D:/ITGate(AI Diploma)/Projects/Scientific Calculator/calculator_icon.png"))
        self.setWindowTitle("Scientific Calculator")

        self.current_mode = "Main"
        self.saved_text = ""
        self.cal_logic = CalculatorLogic()

        self.create_widgets()
        self.main_layouts()
        self.buttons_action()

    def showEvent(self, event):
        super().showEvent(event)
        self.center_on_screen()

    def center_on_screen(self):
        screen_geometry = QGuiApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.setGeometry(x, y, self.width(), self.height())

    def create_widgets(self):
        self.entry_line_edit = QLineEdit()
        self.entry_line_edit.setCursorPosition(0)
        self.entry_line_edit.setFocus()
        self.entry_line_edit.setText(self.saved_text)

        self.history_button = QPushButton()
        self.history_button.setIcon(QIcon("D:/ITGate(AI Diploma)/Projects/Scientific Calculator/calculator_clock.png"))

        self.clear_button = QPushButton("C")
        self.backward_button = QPushButton("←")
        self.forward_button = QPushButton("→")
        self.new_line_button = QPushButton("↵")

        self.number_buttons = [QPushButton(str(i)) for i in range(1, 10)]
        self.number_buttons.append(QPushButton("0"))
        self.dot_button = QPushButton(".")

        self.root_button = QPushButton('√')
        self.exp_power_button = QPushButton("e^x")
        self.sin_button = QPushButton("sin")
        self.cos_button = QPushButton("cos")
        self.tan_button = QPushButton("tan")
        self.pi_button = QPushButton("π")

        self.absolute_button = QPushButton("|x|")
        self.power_of_2_button = QPushButton('x²')
        self.e_constant_button = QPushButton("e")

        self.circle_left_bracket_button = QPushButton("(")
        self.circle_right_bracket_button = QPushButton(")")
        self.ln_button = QPushButton("ln")
        self.log_button = QPushButton("log")
        self.round_button = QPushButton("round")

        self.ceil_button = QPushButton("ceil")
        self.floor_button = QPushButton("floor")
        self.median_button = QPushButton("median")
        self.mode_button = QPushButton("mode")
        self.variance_button = QPushButton("variance")

        self.abst_button = QPushButton(",")
        self.reminder_button = QPushButton("%")

        self.sin_inverse_button = QPushButton("sin⁻¹")
        self.cos_inverse_button = QPushButton("cos⁻¹")
        self.tan_inverse_button = QPushButton("tan⁻¹")
        self.mean_button = QPushButton("mean")
        self.standard_deviation_button = QPushButton("stdev")
        self.standard_deviationp_button = QPushButton("stdevp")
        self.factorial_button = QPushButton("x!")
        self.combination_button = QPushButton("nCk")
        self.permutation_button = QPushButton("nPk")
        self.radian_angle_button = QPushButton("rad")
        self.gradian_angle_button = QPushButton("grad")
        self.degree_angle_button = QPushButton("Deg")

        self.matrix_add = QPushButton("([] + [])")
        self.matrix_sub = QPushButton("([] - [])")
        self.matrix_multi = QPushButton("([] * [])")
        self.matrix_division = QPushButton("([] / [])")
        self.matrix_scaler_multi = QPushButton("( a , [])")

        self.linear_equ = QPushButton("linear equ")
        self.quadratic_equ = QPushButton("quadratic equ")

        self.division_button = QPushButton("÷")
        self.multiplication_button = QPushButton("x")
        self.plus_button = QPushButton("+")
        self.subtract_button = QPushButton("-")
        self.equal_button = QPushButton("=")

        self.main_label = QLabel("Basic Mode")

        self.func_button = QPushButton("Func")

    def apply_styles(self):
        self.main_label_style()
        self.all_button_style()
        self.buttons_dimensions()

    def main_label_style(self):
        self.main_label.setStyleSheet("QLabel { font-size: 20px; color: black; }")

    def special_style(self):
        special_style = (
            "QPushButton { background-color: #FFA500 ; color: white; font-size: 24px; border-radius: 10px; }"
            "QPushButton:hover { background-color: #FF8C00; }"
            "QPushButton:pressed { background-color: #dcdcdc; }"
        )

        for button in [self.new_line_button, self.multiplication_button, self.division_button, self.plus_button,
                       self.subtract_button, self.backward_button, self.forward_button]:
            button.setStyleSheet(special_style)
            button.setFixedHeight(40)

            button_shadow = QGraphicsDropShadowEffect()
            button_shadow.setBlurRadius(10)
            button_shadow.setColor(QColor(0, 0, 0, 100))
            button.setGraphicsEffect(button_shadow)

    def button_style(self):
        button_style = (
            "QPushButton { background-color: #f8f8ff; color: black; border-radius: 10px;"
            " padding: 10px; font-size: 18px; }"
            "QPushButton:hover { background-color: #D3D3D3; }"
            "QPushButton:pressed { background-color: white; }"
        )

        for button in self.number_buttons + [self.root_button, self.exp_power_button, self.sin_button, self.cos_button,
                                             self.tan_button, self.circle_left_bracket_button,
                                             self.circle_right_bracket_button,
                                             self.ln_button,
                                             self.pi_button, self.absolute_button, self.power_of_2_button,
                                             self.log_button,
                                             self.round_button, self.abst_button, self.reminder_button,
                                             self.permutation_button,
                                             self.combination_button, self.sin_inverse_button, self.cos_inverse_button,
                                             self.tan_inverse_button, self.factorial_button, self.mean_button,
                                             self.standard_deviationp_button,
                                             self.standard_deviation_button, self.degree_angle_button,
                                             self.radian_angle_button,
                                             self.gradian_angle_button, self.e_constant_button, self.dot_button,
                                             self.clear_button,
                                             self.equal_button, self.func_button, self.ceil_button, self.floor_button,
                                             self.median_button, self.mode_button, self.variance_button,
                                             self.matrix_division, self.matrix_add, self.matrix_multi, self.matrix_sub,
                                             self.matrix_scaler_multi, self.linear_equ, self.quadratic_equ]:
            button.setStyleSheet(button_style)

            button_shadow = QGraphicsDropShadowEffect()
            button_shadow.setBlurRadius(10)
            button_shadow.setColor(QColor(0, 0, 0, 100))
            button.setGraphicsEffect(button_shadow)

            button.setFixedHeight(40)

    def line_edit_style(self):
        line_edit_style = (
            "QLineEdit { background-color: white; color: black; font-size: 24px; border: 2px solid white; "
            "border-radius: 10px; selection-background-color: #008000; selection-color: white; }")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(0, 0, 0, 100))

        self.entry_line_edit.setGraphicsEffect(shadow)
        self.entry_line_edit.setStyleSheet(line_edit_style)

    def history_button_style(self):
        self.history_button.setStyleSheet(
            "QPushButton { border: none; margin: 0; padding: 0; background-color: transparent; }"
            "QPushButton:hover { background-color: #D3D3D3; }"
            "QPushButton:pressed { background-color: #dcdcdc; }"
        )

    def equal_button_style(self):
        self.equal_button.setStyleSheet(
            "QPushButton { background-color: #dcdcdc; color: black; font-size: 20px; border-radius: 10px;}"
            "QPushButton:hover { background-color: #FF8C00; }"
            "QPushButton:pressed { background-color: #dcdcdc; }"
        )

    def clear_button_style(self):
        self.clear_button.setStyleSheet(
            "QPushButton { background-color: #dcdcdc; color: black; font-size: 20px; border-radius: 10px; }"
            "QPushButton:hover { background-color: #FF8C00; }"
            "QPushButton:pressed { background-color: #dcdcdc; }"
        )

    def func_button_style(self):
        self.func_button.setStyleSheet(
            "QPushButton { background-color: #FFA500 ;font-size: 24px; border-radius: 10px; color: white; }"
            "QPushButton:hover { background-color: #FF8C00; }"
            "QPushButton:pressed { background-color: #dcdcdc; }"
        )

    def all_button_style(self):
        self.line_edit_style()
        self.special_style()
        self.button_style()
        self.func_button_style()
        self.clear_button_style()
        self.equal_button_style()
        self.history_button_style()

    def buttons_dimensions(self):
        self.entry_line_edit.setFixedHeight(100)
        self.equal_button.setFixedSize(100, 40)
        self.clear_button.setFixedSize(50, 40)
        self.func_button.setFixedSize(100, 40)
        self.history_button.setFixedSize(40, 40)

    def main_layouts(self):
        v_layout = QVBoxLayout()

        layers_layout = QHBoxLayout()

        left_layer_layout = QGridLayout()
        left_layer_layout.addWidget(self.root_button, 0, 0)
        left_layer_layout.addWidget(self.exp_power_button, 0, 1)
        left_layer_layout.addWidget(self.absolute_button, 0, 2)
        left_layer_layout.addWidget(self.power_of_2_button, 0, 3)
        left_layer_layout.addWidget(self.sin_button, 1, 0)
        left_layer_layout.addWidget(self.cos_button, 1, 1)
        left_layer_layout.addWidget(self.tan_button, 1, 2)
        left_layer_layout.addWidget(self.pi_button, 1, 3)

        left_layer_layout.addWidget(self.ln_button, 2, 0)
        left_layer_layout.addWidget(self.log_button, 2, 1)
        left_layer_layout.addWidget(self.reminder_button, 2, 3)
        left_layer_layout.addWidget(self.round_button, 2, 2)

        left_layer_layout.addWidget(self.circle_left_bracket_button, 3, 0)
        left_layer_layout.addWidget(self.circle_right_bracket_button, 3, 1)
        left_layer_layout.addWidget(self.abst_button, 3, 2)

        layers_layout.addLayout(left_layer_layout)

        layers_layout.addSpacing(20)

        middle_layer_layout = QGridLayout()
        middle_layer_layout.addWidget(self.number_buttons[0], 0, 0)
        middle_layer_layout.addWidget(self.number_buttons[1], 0, 1)
        middle_layer_layout.addWidget(self.number_buttons[2], 0, 2)
        middle_layer_layout.addWidget(self.number_buttons[3], 1, 0)
        middle_layer_layout.addWidget(self.number_buttons[4], 1, 1)
        middle_layer_layout.addWidget(self.number_buttons[5], 1, 2)
        middle_layer_layout.addWidget(self.number_buttons[6], 2, 0)
        middle_layer_layout.addWidget(self.number_buttons[7], 2, 1)
        middle_layer_layout.addWidget(self.number_buttons[8], 2, 2)
        middle_layer_layout.addWidget(self.number_buttons[9], 3, 1)
        middle_layer_layout.addWidget(self.dot_button, 3, 0)
        middle_layer_layout.addWidget(self.new_line_button, 3, 2)
        layers_layout.addLayout(middle_layer_layout)

        layers_layout.addSpacing(20)

        right_layer_layout = QGridLayout()
        right_layer_layout.addWidget(self.division_button, 0, 0)
        right_layer_layout.addWidget(self.multiplication_button, 0, 1)
        right_layer_layout.addWidget(self.plus_button, 1, 0)
        right_layer_layout.addWidget(self.subtract_button, 1, 1)
        right_layer_layout.addWidget(self.forward_button, 2, 0)
        right_layer_layout.addWidget(self.backward_button, 2, 1)
        right_layer_layout.addWidget(self.equal_button, 3, 0)
        right_layer_layout.addWidget(self.clear_button, 3, 1)
        layers_layout.addLayout(right_layer_layout)

        v_layout.addWidget(self.entry_line_edit)

        first_row_layout = QHBoxLayout()
        first_row_layout.addWidget(self.history_button)
        first_row_layout.addWidget(self.main_label, alignment=Qt.AlignHCenter)
        v_layout.addLayout(first_row_layout)
        v_layout.addLayout(layers_layout)

        func_button_layout = QHBoxLayout()
        func_button_layout.addStretch()
        func_button_layout.addWidget(self.func_button)
        func_button_layout.addStretch()

        v_layout.addLayout(func_button_layout)

        central_widget = QWidget()
        central_widget.setLayout(v_layout)
        self.setCentralWidget(central_widget)

        self.apply_styles()

    def func_layouts(self):
        v_layout = QVBoxLayout()

        layers_layout = QHBoxLayout()

        middle_layer_layout = QGridLayout()
        middle_layer_layout.addWidget(self.sin_button, 0, 0)
        middle_layer_layout.addWidget(self.cos_button, 0, 1)
        middle_layer_layout.addWidget(self.tan_button, 0, 2)
        middle_layer_layout.addWidget(self.combination_button, 0, 3)
        middle_layer_layout.addWidget(self.permutation_button, 0, 4)
        middle_layer_layout.addWidget(self.factorial_button, 0, 5)

        middle_layer_layout.addWidget(self.sin_inverse_button, 1, 0)
        middle_layer_layout.addWidget(self.cos_inverse_button, 1, 1)
        middle_layer_layout.addWidget(self.tan_inverse_button, 1, 2)
        middle_layer_layout.addWidget(self.floor_button, 1, 3)
        middle_layer_layout.addWidget(self.variance_button, 1, 4)
        middle_layer_layout.addWidget(self.ceil_button, 1, 5)

        middle_layer_layout.addWidget(self.matrix_add, 2, 0)
        middle_layer_layout.addWidget(self.matrix_sub, 2, 1)
        middle_layer_layout.addWidget(self.matrix_multi, 2, 2)
        middle_layer_layout.addWidget(self.matrix_division, 2, 3)
        middle_layer_layout.addWidget(self.matrix_scaler_multi, 2, 4)
        middle_layer_layout.addWidget(self.linear_equ, 2, 5)

        middle_layer_layout.addWidget(self.mean_button, 3, 0)
        middle_layer_layout.addWidget(self.median_button, 3, 1)
        middle_layer_layout.addWidget(self.mode_button, 3, 2)
        middle_layer_layout.addWidget(self.standard_deviation_button, 3, 3)
        middle_layer_layout.addWidget(self.standard_deviationp_button, 3, 4)
        middle_layer_layout.addWidget(self.quadratic_equ, 3, 5)

        layers_layout.addLayout(middle_layer_layout)

        layers_layout.addSpacing(20)

        right_layer_layout = QGridLayout()
        right_layer_layout.addWidget(self.gradian_angle_button, 0, 0)
        right_layer_layout.addWidget(self.degree_angle_button, 0, 1)
        right_layer_layout.addWidget(self.radian_angle_button, 0, 2)

        right_layer_layout.addWidget(self.division_button, 1, 0)
        right_layer_layout.addWidget(self.multiplication_button, 1, 1)
        right_layer_layout.addWidget(self.plus_button, 1, 2)
        right_layer_layout.addWidget(self.subtract_button, 2, 0)
        right_layer_layout.addWidget(self.forward_button, 2, 1)
        right_layer_layout.addWidget(self.backward_button, 2, 2)
        right_layer_layout.addWidget(self.e_constant_button, 3, 0)
        right_layer_layout.addWidget(self.equal_button, 3, 1)
        right_layer_layout.addWidget(self.clear_button, 3, 2)
        layers_layout.addLayout(right_layer_layout)

        v_layout.addWidget(self.entry_line_edit)
        v_layout.addWidget(self.main_label, alignment=Qt.AlignHCenter)
        v_layout.addLayout(layers_layout)

        func_button_layout = QHBoxLayout()
        func_button_layout.addStretch()
        func_button_layout.addWidget(self.func_button)
        func_button_layout.addStretch()

        v_layout.addLayout(func_button_layout)

        central_widget = QWidget()
        central_widget.setLayout(v_layout)
        self.setCentralWidget(central_widget)

        self.apply_styles()

    def show_func_buttons(self):
        self.saved_text = self.entry_line_edit.text()
        self.create_widgets()
        self.main_label.setText("Custom Functions")
        self.func_layouts()

    def show_main_buttons(self):
        self.saved_text = self.entry_line_edit.text()
        self.create_widgets()
        self.main_label.setText("Basic Mode")
        self.main_layouts()

    def toggle_mode(self):
        if self.current_mode == "Main":
            self.current_mode = "Func"
            self.func_button.setText("Main")
            self.show_func_buttons()
        else:
            self.current_mode = "Main"
            self.main_label.setText("Main")
            self.show_main_buttons()

        self.buttons_action()

    def show_history(self):
        history = self.cal_logic.get_history()
        history_dialog = HistoryDialog(history)
        history_dialog.exec_()

    def buttons_action(self):
        for button in self.number_buttons:
            button.clicked.connect(self.number_button_clicked)

        self.root_button.clicked.connect(self.square_root)
        self.reminder_button.clicked.connect(self.reminder_func)
        self.round_button.clicked.connect(self.round_func)
        self.tan_button.clicked.connect(self.tan_func)
        self.sin_button.clicked.connect(self.sin_func)
        self.cos_button.clicked.connect(self.cos_func)
        self.circle_left_bracket_button.clicked.connect(self.circel_left_bracket)
        self.circle_right_bracket_button.clicked.connect(self.circel_right_bracket)
        self.abst_button.clicked.connect(self.comma)
        self.ln_button.clicked.connect(self.ln_func)
        self.log_button.clicked.connect(self.log_func)
        self.exp_power_button.clicked.connect(self.exp_power_func)
        self.power_of_2_button.clicked.connect(self.power_func)
        self.absolute_button.clicked.connect(self.abs_func)
        self.pi_button.clicked.connect(self.pi_func)
        self.clear_button.clicked.connect(self.clear_line_edit)
        self.backward_button.clicked.connect(self.backward_func)
        self.forward_button.clicked.connect(self.forward_func)
        self.new_line_button.clicked.connect(self.clear_single_char)
        self.plus_button.clicked.connect(self.add_func)
        self.multiplication_button.clicked.connect(self.multi_func)
        self.division_button.clicked.connect(self.division_func)
        self.subtract_button.clicked.connect(self.sub_func)
        self.equal_button.clicked.connect(self.equal_func)
        self.dot_button.clicked.connect(self.dot_func)
        self.sin_inverse_button.clicked.connect(self.sin_inverse_func)
        self.cos_inverse_button.clicked.connect(self.cos_inverse_func)
        self.tan_inverse_button.clicked.connect(self.tan_inverse_func)
        self.mean_button.clicked.connect(self.mean_func)
        self.standard_deviation_button.clicked.connect(self.standard_deviation_func)
        self.standard_deviationp_button.clicked.connect(self.population_standard_deviation_func)
        self.factorial_button.clicked.connect(self.factorial_func)
        self.combination_button.clicked.connect(self.combination_func)
        self.permutation_button.clicked.connect(self.permutation_func)
        self.e_constant_button.clicked.connect(self.e_constant_func)
        self.median_button.clicked.connect(self.median_func)
        self.mode_button.clicked.connect(self.mode_func)
        self.floor_button.clicked.connect(self.floor_func)
        self.ceil_button.clicked.connect(self.ceil_func)
        self.variance_button.clicked.connect(self.variance_func)
        self.matrix_add.clicked.connect(self.matrix_add_func)
        self.matrix_sub.clicked.connect(self.matrix_sub_func)
        self.matrix_multi.clicked.connect(self.matrix_multi_func)
        self.matrix_scaler_multi.clicked.connect(self.matrix_scaler_multi_func)
        self.matrix_division.clicked.connect(self.matrix_division_func)
        self.linear_equ.clicked.connect(self.linear_equation_func)
        self.quadratic_equ.clicked.connect(self.quadratic_equation_func)
        self.gradian_angle_button.clicked.connect(self.grad_angle)
        self.radian_angle_button.clicked.connect(self.radian_angle)
        self.degree_angle_button.clicked.connect(self.degree_angle)
        self.func_button.clicked.connect(self.toggle_mode)

        self.history_button.clicked.connect(self.show_history)

    def number_button_clicked(self):
        sender = self.sender()
        number = sender.text()
        self.entry_line_edit.insert(number)
        self.entry_line_edit.setFocus()

    def insert_text_at_cursor(self, text, cursor_offset=None):
        current_position = self.entry_line_edit.cursorPosition()
        text_before_cursor = self.entry_line_edit.text()[:current_position]
        text_after_cursor = self.entry_line_edit.text()[current_position:]

        new_text = text_before_cursor + text + text_after_cursor

        if cursor_offset is None:
            cursor_offset = len(text)

        self.entry_line_edit.setText(new_text)
        self.entry_line_edit.setCursorPosition(current_position + cursor_offset)
        self.entry_line_edit.setFocus()

    def square_root(self):
        self.insert_text_at_cursor('√', cursor_offset=1)

    def abs_func(self):
        self.insert_text_at_cursor('abs()', cursor_offset=4)

    def exp_power_func(self):
        self.insert_text_at_cursor('e^', cursor_offset=2)

    def power_func(self):
        self.insert_text_at_cursor('²', cursor_offset=0)

    def factorial_func(self):
        self.insert_text_at_cursor('!', cursor_offset=0)

    def sin_func(self):
        self.insert_text_at_cursor('sin()', cursor_offset=4)

    def cos_func(self):
        self.insert_text_at_cursor('cos()', cursor_offset=4)

    def tan_func(self):
        self.insert_text_at_cursor('tan()', cursor_offset=4)

    def sin_inverse_func(self):
        self.insert_text_at_cursor('sin⁻¹()', cursor_offset=6)

    def cos_inverse_func(self):
        self.insert_text_at_cursor('cos⁻¹()', cursor_offset=6)

    def tan_inverse_func(self):
        self.insert_text_at_cursor('tan⁻¹()', cursor_offset=6)

    def log_func(self):
        self.insert_text_at_cursor('log()', cursor_offset=4)

    def round_func(self):
        self.insert_text_at_cursor('round()', cursor_offset=6)

    def standard_deviation_func(self):
        self.insert_text_at_cursor('stdev()', cursor_offset=6)

    def population_standard_deviation_func(self):
        self.insert_text_at_cursor('stdevp()', cursor_offset=7)

    def mean_func(self):
        self.insert_text_at_cursor('mean()', cursor_offset=5)

    def permutation_func(self):
        self.insert_text_at_cursor('P( , )', cursor_offset=2)

    def combination_func(self):
        self.insert_text_at_cursor('C( , )', cursor_offset=2)

    def median_func(self):
        self.insert_text_at_cursor('median()', cursor_offset=7)

    def mode_func(self):
        self.insert_text_at_cursor('mode()', cursor_offset=5)

    def floor_func(self):
        self.insert_text_at_cursor('floor()', cursor_offset=6)

    def ceil_func(self):
        self.insert_text_at_cursor('ceil()', cursor_offset=5)

    def variance_func(self):
        self.insert_text_at_cursor('variance()', cursor_offset=9)

    def matrix_add_func(self):
        self.insert_text_at_cursor('add([] , [])', cursor_offset=5)

    def matrix_sub_func(self):
        self.insert_text_at_cursor('sub([] , [])', cursor_offset=5)

    def matrix_multi_func(self):
        self.insert_text_at_cursor('multi([] , [])', cursor_offset=7)

    def matrix_scaler_multi_func(self):
        self.insert_text_at_cursor('s( , [])', cursor_offset=2)

    def matrix_division_func(self):
        self.insert_text_at_cursor('div([] , [])', cursor_offset=5)

    def linear_equation_func(self):
        self.insert_text_at_cursor('L:(,)', cursor_offset=3)

    def quadratic_equation_func(self):
        self.insert_text_at_cursor('Q:( , , )', cursor_offset=3)

    def ln_func(self):
        self.insert_text_at_cursor("ln()", cursor_offset=3)

    def backward_func(self):
        current_position = self.entry_line_edit.cursorPosition()
        new_position = current_position - 1
        self.entry_line_edit.setCursorPosition(new_position)
        self.entry_line_edit.setFocus()

    def forward_func(self):
        current_position = self.entry_line_edit.cursorPosition()
        new_position = current_position + 1
        self.entry_line_edit.setCursorPosition(new_position)
        self.entry_line_edit.setFocus()

    def e_constant_func(self):
        self.entry_line_edit.insert("e")
        self.entry_line_edit.setFocus()

    def pi_func(self):
        self.entry_line_edit.insert('π')
        self.entry_line_edit.setFocus()

    def reminder_func(self):
        self.entry_line_edit.insert('%')
        self.entry_line_edit.setFocus()

    def comma(self):
        self.entry_line_edit.insert(',')
        self.entry_line_edit.setFocus()

    def circel_left_bracket(self):
        self.entry_line_edit.insert('(')
        self.entry_line_edit.setFocus()

    def circel_right_bracket(self):
        self.entry_line_edit.insert(')')
        self.entry_line_edit.setFocus()

    def clear_line_edit(self):
        self.entry_line_edit.setText('')
        self.entry_line_edit.setCursorPosition(0)
        self.entry_line_edit.setFocus()

    def dot_func(self):
        self.entry_line_edit.insert('.')
        self.entry_line_edit.setFocus()

    def division_func(self):
        self.entry_line_edit.insert('÷')
        self.entry_line_edit.setFocus()

    def multi_func(self):
        self.entry_line_edit.insert('X')
        self.entry_line_edit.setFocus()

    def sub_func(self):
        self.entry_line_edit.insert('-')
        self.entry_line_edit.setFocus()

    def add_func(self):
        self.entry_line_edit.insert('+')
        self.entry_line_edit.setFocus()

    def clear_single_char(self):
        self.entry_line_edit.backspace()
        self.entry_line_edit.setFocus()

    def grad_angle(self):
        result = self.cal_logic.to_gradian(float(self.entry_line_edit.text()))
        self.entry_line_edit.setText(str(result))

    def radian_angle(self):
        result = self.cal_logic.to_radian(float(self.entry_line_edit.text()))
        self.entry_line_edit.setText(str(result))

    def degree_angle(self):
        result = self.cal_logic.to_degree(float(self.entry_line_edit.text()))
        self.entry_line_edit.setText(str(result))

    def equal_func(self):
        current_text = self.entry_line_edit.text()
        result = self.cal_logic.receive_text(current_text)
        self.entry_line_edit.setText(result)
