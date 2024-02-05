import math
import re
import numpy as np

from model.history_manager import HistoryManager


class CalculatorLogic:
    def __init__(self):
        self.counter = 0
        self.pi = 3.141592653589793
        self.gradian_ratio = 200 / self.pi
        self.degree_ratio = 180 / self.pi

        self.history_manager = HistoryManager()

    def receive_text(self, text):
        try:
            result = self.evaluate_expression(text)
            operation = {"expression: ": text, "result = ": result}
            self.history_manager.add_operation(operation)
            return str(result)
        except Exception as e:
            print(e)
            return "Error"

    def get_history(self):
        return self.history_manager.get_formatted_history()

    def evaluate_expression(self, expression):
        expression = expression.replace('X', '*').replace('÷', '/')
        operators = {
            '+': CalculatorLogic.add, '-': CalculatorLogic.subtract, '*': CalculatorLogic.multiply,
            '/': CalculatorLogic.divide,
            'sin': self.sin_func, 'cos': self.cos_func, 'tan': self.tan_func,
            'log': CalculatorLogic.log, 'ln': CalculatorLogic.ln, 'abs': CalculatorLogic.abs_func,
            'round': CalculatorLogic.round_func, '%': CalculatorLogic.remainder_func,
            '√': CalculatorLogic.square_root, 'π': self.pi_func, '^': CalculatorLogic.power_2_func,
            'e^': self.exponential_function, 'sin⁻¹': self.sin_inverse, 'cos⁻¹': self.cos_inverse,
            'tan⁻¹': self.tan_inverse, 'floor': CalculatorLogic.floor_func,
            'ceil': CalculatorLogic.ceil_func, 'stdev': CalculatorLogic.standard_deviation_function,
            'stdevp': CalculatorLogic.population_standard_deviation_function, 'mean': CalculatorLogic.mean_func,
            'median': CalculatorLogic.median_func, 'mode': CalculatorLogic.mode_func, '!': self.factorial_func,
            'variance': CalculatorLogic.population_variance_func, 'P': self.permutations_formula,
            'C': self.combination_formula, 'L': CalculatorLogic.solve_linear_equation,
            'Q': CalculatorLogic.solve_quadratic_equation, 'e': CalculatorLogic.e_func, 'add': self.matrix_addition,
            'sub': self.matrix_subtraction, 'multi': self.matrix_multiplication, 's': self.matrix_scalar_multiplication,
            'div': self.matrix_division
        }

        tokens = CalculatorLogic.tokenize(expression)
        postfix_expression = CalculatorLogic.infix_to_postfix(tokens)
        result_stack = []

        for token in postfix_expression:
            if token not in operators:
                if token.startswith('[') and token.endswith(']'):
                    result_stack.append(self.parse_matrix(token))
                else:
                    result_stack.append(float(token))
            elif token in operators:
                if token == "e^":
                    result_stack.append(postfix_expression.pop())
                result = operators[token](result_stack)
                result_stack.append(result)

        return result_stack[-1]

    @staticmethod
    def parse_matrix(matrix_str):
        matrix_str = matrix_str.strip('[]')
        rows = matrix_str.split('],[')
        matrix = []
        for row in rows:
            elements = row.split(',')
            row_values = [float(element) for element in elements]
            matrix.append(row_values)
        return matrix

    @staticmethod
    def tokenize(expression):
        tokens = re.findall(
            r"\[.*?\]|\d+\.\d+|\d+|[()+\-*\/^√π%]|sin⁻¹|sin|cos⁻¹|cos|tan⁻¹|tan|log|ln|e|abs|round|√|²|floor|ceil|mean|median|mode|stdev|stdevp|!|variance|P|C|L|Q|add|sub|div|s|multi|c",

            expression)
        fixed_tokens = []
        i = 0
        while i < len(tokens):
            if tokens[i][0] == '[' and tokens[i][-1] == ']':
                fixed_tokens.append(tokens[i])
                i += 1
            elif tokens[i] == '-' and (
                    i == 0 or tokens[i - 1] in ['(', '+', '-', '*', '/', '^', '√', 'sin', 'cos', 'tan', 'log', 'ln',
                                                'e', 'abs', 'round', 'π']):
                fixed_tokens.append(tokens[i] + tokens[i + 1])
                i += 2
            elif tokens[i] == 'e' and i + 1 < len(tokens) and tokens[i + 1] == '^':
                fixed_tokens.append('e^')
                i += 2
            elif tokens[i] == '²':
                fixed_tokens.append('^')
                i += 1
            elif tokens[i] == '!':
                fixed_tokens.append(tokens[i])
                i += 1
            else:
                fixed_tokens.append(tokens[i])
                i += 1

        return fixed_tokens

    @staticmethod
    def infix_to_postfix(infix_tokens):
        output = []
        operator_stack = []

        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, 'sin': 3, 'cos': 3, 'tan': 3, 'sin⁻¹': 3, 'π': 3,
                      'log': 3, 'ln': 3, 'e': 3, 'pi': 3, 'abs': 3, 'round': 3, '%': 3, '√': 4, 'cos⁻¹': 4,
                      'tan⁻¹': 3, 'floor': 4, 'ceil': 4, 'mean': 4, 'median': 4, 'mode': 4, 'stdev': 4, 'stdevp': 4,
                      '!': 4, 'variance': 4, 'P': 3, 'C': 3, 'L': 3, 'Q': 3, 'add': 2, 'sub': 2, 'div': 2, 'multi': 2,
                      's': 2, 'c': 2}

        for token in infix_tokens:
            if token.isnumeric() or (token[0] == '-' and token[1:].isnumeric()):
                output.append(token)
            elif token in precedence:
                while (operator_stack and
                       operator_stack[-1] in precedence and
                       precedence[operator_stack[-1]] >= precedence[token]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()
            elif token.isalpha():
                operator_stack.append(token)
            elif token[0] == '-' and token[1:].isalpha():
                output.append(token)
            else:
                output.append(token)

        while operator_stack:
            output.append(operator_stack.pop())

        return output

    @staticmethod
    def add(stack):
        b = stack.pop()
        a = stack.pop()
        return a + b

    @staticmethod
    def subtract(stack):
        b = stack.pop()
        a = stack.pop()
        return a - b

    @staticmethod
    def multiply(stack):
        b = stack.pop()
        a = stack.pop()
        return a * b

    @staticmethod
    def divide(stack):
        b = stack.pop()
        a = stack.pop()
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    @staticmethod
    def remainder_func(stack):
        y = stack.pop()
        x = stack.pop()
        if y != 0:
            remainder = x % y
            return remainder
        else:
            raise ValueError("Division by zero")

    @staticmethod
    def square_root(stack):
        n = stack.pop()
        if n < 0:
            raise ValueError("Square root of a negative number is undefined")
        x = n / 2.0
        epsilon = 1e-10
        while True:
            new_x = 0.5 * (x + n / x)

            if abs(new_x - x) < epsilon:
                return new_x
            x = new_x

    def pi_func(self, stack):
        return self.pi

    @staticmethod
    def e_func(stack):
        return 2.718281828

    @staticmethod
    def log(stack):
        num = stack.pop()
        if num <= 0:
            raise ValueError("Logarithm of a non-positive number")
        return math.log10(num)

    @staticmethod
    def ln(stack):
        num = stack.pop()
        if num <= 0:
            raise ValueError("Natural logarithm of a non-positive number")
        return math.log(num)

    @staticmethod
    def abs_func(stack):
        n = stack.pop()
        result = 0
        if n < 0:
            result = n * -1
        elif n > 0 or n == 0:
            result = n
        return result

    @staticmethod
    def round_func(stack):
        n = stack.pop()
        index = CalculatorLogic.get_first_digit_after_decimal(n)
        if n < 0:
            if index < 5:
                result = int(n)
            else:
                result = int(n - 1)
        else:
            if index < 5:
                result = int(n)
            else:
                result = int(n + 1)

        return result

    @staticmethod
    def floor_func(stack):
        x = stack.pop()
        return int(x) if x >= 0 or x.is_integer() else int(x) - 1

    @staticmethod
    def ceil_func(stack):
        x = stack.pop()
        return int(x) if x.is_integer() or x < 0 else int(x) + 1

    @staticmethod
    def get_first_digit_after_decimal(num):
        num_str = str(num)
        decimal_index = num_str.find('.')

        if decimal_index != -1 and decimal_index < len(num_str) - 1:
            first_digit_after_decimal = int(num_str[decimal_index + 1])
            return first_digit_after_decimal
        else:
            return None

    @staticmethod
    def mean_func(stack):
        number_of_values = len(stack)
        summation = sum(stack)
        result = summation / number_of_values

        stack.clear()
        return result

    @staticmethod
    def mode_func(stack):
        number_of_values = len(stack)
        values = np.zeros(number_of_values)
        for i in range(number_of_values):
            values[i] = stack.pop()
        frequency_dict = {}
        mode = 0
        for value in values:
            if value in frequency_dict:
                frequency_dict[value] += 1
            else:
                frequency_dict[value] = 1

        max_frequency = max(frequency_dict.values())
        for key, value in frequency_dict.items():
            if value == max_frequency:
                mode = key
        return mode

    @staticmethod
    def median_func(stack):
        stack.sort()
        number_of_data = len(stack)
        values = np.zeros(number_of_data)
        for i in range(number_of_data):
            values[i] = stack.pop()
        if number_of_data % 2 != 0:
            index = int((number_of_data / 2))
            median = values[index]
            return median
        else:
            index1 = int((number_of_data / 2) - 1)
            index2 = int(number_of_data / 2)
            median = (values[index1] + values[index2]) / 2
            return median

    @staticmethod
    def population_variance_func(stack):
        number_of_data = len(stack)
        mean = CalculatorLogic.mean_func(stack.copy())
        squared_diff = [(x - mean) ** 2 for x in stack]
        stack.clear()
        return sum(squared_diff) / number_of_data

    @staticmethod
    def standard_deviation_function(stack):
        number_of_data = len(stack)
        values = stack.copy()
        if number_of_data < 2:
            raise ValueError("Sample standard deviation requires at least two data points.")

        mean = CalculatorLogic.mean_func(values)
        sum_squared_diff = sum((x - mean) ** 2 for x in stack)
        variance = sum_squared_diff / (number_of_data - 1)
        for _ in range(number_of_data):
            stack.pop()

        return variance ** 0.5

    @staticmethod
    def population_standard_deviation_function(stack):
        number_of_data = len(stack)
        values = stack.copy()
        if number_of_data < 1:
            raise ValueError("Population standard deviation requires at least one data point.")

        mean = CalculatorLogic.mean_func(values)
        sum_squared_diff = sum((x - mean) ** 2 for x in stack)
        variance = sum_squared_diff / number_of_data
        return variance ** 0.5

    def factorial_func(self, stack):
        n = stack.pop()
        if n == 0 or n == 1:
            return 1
        elif n < 0:
            n = n * -1
            return -(n * self.factorial_func([n - 1]))
        else:
            return n * self.factorial_func([n - 1])

    def combination_formula(self, stack):
        k = stack.pop()
        n = stack.pop()
        sub_value = n - k
        fact_n = self.factorial_func([n])
        fact_k = self.factorial_func([k])
        fact_sub = self.factorial_func([sub_value])
        return fact_n / (fact_sub * fact_k)

    def permutations_formula(self, stack):
        k = stack.pop()
        n = stack.pop()
        sub_value = n - k
        fact_n = self.factorial_func([n])
        fact_sub = self.factorial_func([sub_value])
        return fact_n / fact_sub

    def exponential_function(self, stack, terms=20):
        x = float(stack.pop())
        result = 0
        for n in range(terms):
            result += (x ** n) / self.factorial_func([n])
        return result

    @staticmethod
    def power_2_func(stack):
        x = stack.pop()
        result = 1
        for _ in range(2):
            result *= x
        return result

    @staticmethod
    def power_func(x, n):
        result = 1
        for _ in range(n):
            result *= x
        return result

    def sin_func(self, stack, terms=10):
        x = stack.pop()
        x = CalculatorLogic.to_radian(self, x)
        result = 0
        for n in range(terms):
            term = ((-1) ** n) * (x ** (2 * n + 1) / math.factorial(2 * n + 1))
            result += term
        return result

    def cos_func(self, stack, terms=10):
        x = stack.pop()
        x = CalculatorLogic.to_radian(self, x)
        result = 0

        for n in range(terms):
            term = ((-1) ** n) * (CalculatorLogic.power_func(x, 2 * n) / self.factorial_func([2 * n]))
            result += term

        tolerance = 1e-15
        if self.abs_func([result]) < tolerance:
            result = 0

        return result

    def tan_func(self, stack):
        x = stack.pop()
        return self.sin_func([x]) / self.cos_func([x])

    def sin_inverse(self, stack, terms=10):
        x = stack.pop()
        x = CalculatorLogic.to_radian(self, x)
        result = 0
        for n in range(terms):
            term = (self.factorial_func([2 * n]) * CalculatorLogic.power_func(x, 2 * n + 1)) / (
                        (4 ** n) * (self.factorial_func([n]) ** 2) * (2 * n + 1))
            result += term
        return result

    def cos_inverse(self, stack, terms=10):
        x = stack.pop()
        return self.pi / 2 - self.sin_inverse([x], terms)

    def tan_inverse(self, stack):
        x = stack.pop()
        x = CalculatorLogic.to_radian(self, x)
        if x < -1 or x > 1:
            raise ValueError("Input out of range for arctan function.")

        result = 0.0
        current_term = x
        divisor = 1.0

        for i in range(1, 1000):
            result += current_term / divisor
            current_term *= -x * x
            divisor += 2

        return result

    def to_radian(self, angle):
        if isinstance(angle, (int, float)):
            angle = math.radians(angle)
            return angle
        elif isinstance(angle, str):
            try:
                angle_value = float(angle[:-1])
                unit = angle[-1].lower()
            except ValueError:
                raise ValueError("Invalid angle format")

            if unit == 'r':
                return angle_value
            elif unit == 'd':
                return math.radians(angle_value)
            elif unit == 'g':
                return math.radians(self.from_gradian(angle_value))
            else:
                raise ValueError("Invalid unit. Use 'r', 'd', or 'g'.")
        else:
            raise ValueError("Invalid angle format")

    def to_degree(self, angle):
        return self.to_radian(angle) * 180 / self.pi

    def to_gradian(self, angle):
        rad = self.to_radian(angle)
        res = rad * self.gradian_ratio
        return self.to_radian(angle) * self.gradian_ratio

    def from_gradian(self, gradian):
        return gradian / self.gradian_ratio

    @staticmethod
    def matrix_addition(matrices):
        if len(matrices) == 2:
            matrix2 = list(matrices.pop())
            matrix2 = matrix2[0]
            matrix1 = list(matrices.pop())
            matrix1 = matrix1[0]
            result_matrix = []
            for i in range(len(matrix1)):
                row = matrix1[i] + matrix2[i]
                result_matrix.append(row)
            return result_matrix
        matrices_length = len(matrices)
        if matrices_length % 2 == 0:
            matrix2 = matrices[:(matrices_length//2)]
            matrix2 = [row[0] for row in matrix2]
            matrix1 = matrices[(matrices_length//2):]
            matrix1 = [row[0] for row in matrix1]
            matrix3 = []
            for i in range(len(matrix2)):
                row = []
                for j in range(len(matrix2[0])):
                    row.append(matrix2[i][j] + matrix1[i][j])
                matrix3.append(row)

            matrices.clear()
            return matrix3

    @staticmethod
    def matrix_subtraction(matrices):
        if len(matrices) == 2:
            matrix2 = list(matrices.pop())
            matrix2 = matrix2[0]
            matrix1 = list(matrices.pop())
            matrix1 = matrix1[0]
            result_matrix = []
            for i in range(len(matrix1)):
                row = matrix1[i] - matrix2[i]
                result_matrix.append(row)
            return result_matrix
        matrices_length = len(matrices)
        if matrices_length % 2 == 0:
            matrix2 = matrices[:(matrices_length // 2)]
            matrix2 = [row[0] for row in matrix2]
            matrix1 = matrices[(matrices_length // 2):]
            matrix1 = [row[0] for row in matrix1]
            matrix3 = []
            for i in range(len(matrix2)):
                row = []
                for j in range(len(matrix2[0])):
                    row.append(matrix2[i][j] - matrix1[i][j])
                matrix3.append(row)

            matrices.clear()
            return matrix3

    @staticmethod
    def matrix_multiplication(matrices):
        matrices = [row[0] for row in matrices]
        num_values = len(matrices[0])
        counter = 1
        for item in matrices[1:]:
            if len(item) == num_values:
                counter += 1
            else:
                break
        if counter == len(matrices):
            matrix1 = matrices[:((counter+1)//2)]
            matrix2 = matrices[((counter+1)//2):]
        else:

            matrix1 = matrices[:counter]
            matrix2 = matrices[counter:]

        if len(matrix1[0]) != len(matrix2):
            raise ValueError(
                "Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        matrix3 = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                total = 0
                for k in range(len(matrix1[0])):
                    total += matrix1[i][k] * matrix2[k][j]
                row.append(total)
            matrix3.append(row)

        return matrix3

    @staticmethod
    def matrix_scalar_multiplication(stack):
        scalar, *matrix = stack
        matrix = [row[0] for row in matrix]
        result_matrix = [[matrix[i][j] * scalar for j in range(len(matrix[0]))] for i in range(len(matrix))]
        stack.clear()
        return result_matrix

    @staticmethod
    def matrix_inverse(matrix):
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        if det == 0:
            raise ValueError("Matrix is singular, does not have an inverse")

        inverse_matrix = [
            [matrix[1][1] / det, -matrix[0][1] / det],
            [-matrix[1][0] / det, matrix[0][0] / det]
        ]

        return inverse_matrix

    @staticmethod
    def matrix_division(matrices):
        matrices = [row[0] for row in matrices]
        num_values = len(matrices[0])
        counter = 1
        for item in matrices[1:]:
            if len(item) == num_values:
                counter += 1
            else:
                break
        if counter == len(matrices):
            matrix1 = matrices[:((counter+1)//2)]
            matrix2 = matrices[((counter+1)//2):]

        else:

            matrix1 = matrices[:counter]
            matrix2 = matrices[counter:]

        if len(matrix1[0]) != len(matrix2):
            raise ValueError(
                "Number of columns in the first matrix must be equal to the number of rows in the second matrix")

        matrix3 = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                total = 0
                for k in range(len(matrix1[0])):
                    total += matrix1[i][k] * matrix2[k][j]
                row.append(total)
            matrix3.append(row)

        return matrix3

    @staticmethod
    def solve_linear_equation(stack):
        b = stack.pop()
        a = stack.pop()
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero in a linear equation")
        if b < 0:
            x = b / a
        else:
            x = -b / a
        return x

    @staticmethod
    def solve_quadratic_equation(stack):
        c = stack.pop()
        b = stack.pop()
        a = stack.pop()
        discriminant = CalculatorLogic.square_root([b ** 2 - 4 * a * c])
        root1 = (-b + discriminant) / (2 * a)
        root2 = (-b - discriminant) / (2 * a)
        return root1, root2
