# import functions
# import app_settings
# from constants import global_value


from decimal import Decimal, getcontext

class Calculator:
    def __init__(self, memory_value=Decimal(0), round_number=2):
        """Ініціалізація калькулятора з пам'яттю та кількістю знаків після коми."""
        self.memory_value = memory_value  # Значення в пам'яті
        self.history = []  # Історія обчислень
        self.round_number = round_number  # Кількість знаків після коми
        getcontext().prec = 28  # Встановлення точності для обчислень

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, a, b):
        return a ** b

    def square_root(self, a, _=None):  # Другий параметр не використовується
        if a < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return a.sqrt()  # Використовуємо метод sqrt() для Decimal

    def modulus(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulus by zero.")
        return a % b

    def log_history(self, first_operand, operator, second_operand, result):
        self.history.append(f"{first_operand} {operator} {second_operand} = {result}")

    def show_history(self):
        return '\n'.join(self.history) if self.history else "No history available."

    def recall_memory(self):
        return self.memory_value

    def store_memory(self, value):
        self.memory_value = value

    def add_to_memory(self, value):
        self.memory_value += value

    def clear_memory(self):
        self.memory_value = Decimal(0)

    def get_rounded_result(self, result):
        return round(result, self.round_number)

    def get_user_input(self):
        """Отримати ввід користувача для двох чисел та оператора."""
        operator = input("Enter the operator (+, -, *, /, ^, sq, %): ")
        while not self.is_valid_operator(operator):
            print("Invalid operator. Available operators: +, -, *, /.")
            operator = input("Enter operator (+, -, *, /, ^, sq, %): ")

        user_input1 = input('Input first operand (or MR for memory recall):  ').upper()
        if user_input1 == 'MR':
            first_operand = self.recall_memory()
            print(f"Recalled from memory: {first_operand}")
        else:
            first_operand = Decimal(user_input1)  # Конвертація в Decimal

        if operator != 'sq':
            user_input2 = input('Input second operand (or MR for memory recall):  ').upper()
            if user_input2 == 'MR':
                second_operand = self.recall_memory()
                print(f"Recalled from memory: {second_operand}")
            else:
                second_operand = Decimal(user_input2)  # Конвертація в Decimal
        else:
            second_operand = None  # Для операції квадратного кореня другий операнд не потрібен

        return first_operand, second_operand, operator

    def is_valid_operator(self, operator):
        """Перевірити, чи є оператор дійсним."""
        return operator in ['+', '-', '*', '/', '^', 'sq', '%']

    def calculate(self, first_operand, second_operand, operator):
        """Виконати обчислення на основі введення користувача."""
        try:
            match operator:
                case '+':
                    return self.addition(first_operand, second_operand)
                case '-':
                    return self.subtraction(first_operand, second_operand)
                case '*':
                    return self.multiplication(first_operand, second_operand)
                case '/':
                    return self.division(first_operand, second_operand)
                case '^':
                    return self.power(first_operand, second_operand)
                case 'sq':
                    return self.square_root(first_operand)
                case '%':
                    return self.modulus(first_operand, second_operand)
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def ask_for_continue(self):
        """Запитати користувача, чи хоче він продовжити."""
        return input('Do you want to make another calculation? (yes/no): ').strip().lower() == 'yes'


# Використання класу Calculator у вашій програмі
def calculator():
    calc = Calculator()

    while True:
        try:
            first_operand, second_operand, operator = calc.get_user_input()

            # Викликаємо метод calculate для виконання обчислення
            result = calc.calculate(first_operand, second_operand, operator)

            if result is not None:  # Перевірка, чи результат дійсний
                print('Result: ', calc.get_rounded_result(result))  # Використовуємо метод для округлення

                calc.log_history(first_operand, operator, second_operand, calc.get_rounded_result(result))

                choice_memory = input('Would you like to store result in memory (MS), add to memory (M+), clear memory (MC), or skip? ').upper()
                match choice_memory:
                    case 'MS':
                        calc.store_memory(result)
                        print(f"Stored {result} in memory.")
                    case 'M+':
                        calc.add_to_memory(result)
                        print(f"Added {result} to memory. New memory value: {calc.recall_memory()}.")
                    case 'MC':
                        calc.clear_memory()
                        print("Memory cleared.")

                if input("Do you want to view history? (yes/no): ").strip().lower() == 'yes':
                    print(calc.show_history())

                if not calc.ask_for_continue():  # Виклик методу для запиту про продовження
                    break

        except ValueError as e:
            print(f"Error: {e}")


def main():
    while True:
        print("Menu:")
        print("1. Start calculator")
        print("2. Settings")
        choice = input('Enter your choice: ').strip()

        match choice:
            case '1':
                calculator()
            case '2':
                print("Settings are not implemented yet.")


main()

