from decimal import Decimal, getcontext
import app_settings
from functions import addition, subtraction, multiplication, division, power, modulus
from constants import global_value

class Calculator:
    def __init__(self, memory_value=Decimal(global_value.memory_value), round_number=global_value.round_number):
        """Ініціалізація калькулятора з пам'яттю та кількістю знаків після коми."""
        self.memory_value = memory_value  # Значення в пам'яті
        self.history = []  # Історія обчислень
        self.round_number = round_number  # Кількість знаків після коми
        getcontext().prec = 28  # Встановлення точності для обчислень

    def addition(self, a, b):
        return addition(a, b)

    def subtraction(self, a, b):
        return subtraction(a, b)

    def multiplication(self, a, b):
        return multiplication(a, b)

    def division(self, a, b):
        return division(a, b)

    def power(self, a, b):
        return power(a, b)

    def square_root(self, a):
        return a ** Decimal(0.5)  # Зміна тут

    def modulus(self, a, b):
        return modulus(a, b)

    def log_history(self, first_operand, operator, second_operand, result):
        """Метод для збереження історії обчислень."""
        if second_operand is not None:
            self.history.append(f"{first_operand} {operator} {second_operand} = {result}")
        else:
            self.history.append(f"{operator} {first_operand} = {result}")

    def show_history(self):
        """Показати історію обчислень."""
        if not self.history:
            return "No history available."
        return "\n".join(self.history)

    def recall_memory(self):
        return self.memory_value

    def store_memory(self, value):
        self.memory_value = value

    def add_to_memory(self, value):
        self.memory_value += value

    def clear_memory(self):
        self.memory_value = Decimal(0)

    def get_rounded_result(self, result):
        """Метод для округлення результату відповідно до налаштувань."""
        return round(result, self.round_number)  # Використання self.round_number

    def get_user_input(self):
        operator = input("Enter the operator (+, -, *, /, ^, sq, %): ")
        while not self.is_valid_operator(operator):
            print("Invalid operator. Available operators: +, -, *, /, ^, sq, %.")
            operator = input("Enter operator (+, -, *, /, ^, sq, %): ")

        user_input1 = input('Input first operand (or MR for memory recall):  ').upper()
        if user_input1 == 'MR':
            first_operand = self.recall_memory()
            print(f"Recalled from memory: {first_operand}")
        else:
            first_operand = Decimal(user_input1)

        if operator != 'sq':
            user_input2 = input('Input second operand (or MR for memory recall):  ').upper()
            if user_input2 == 'MR':
                second_operand = self.recall_memory()
                print(f"Recalled from memory: {second_operand}")
            else:
                second_operand = Decimal(user_input2)
        else:
            second_operand = None

        return first_operand, second_operand, operator

    def is_valid_operator(self, operator):
        return operator in ['+', '-', '*', '/', '^', 'sq', '%']

    def calculate(self, first_operand, second_operand, operator):
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
        return input('Do you want to make another calculation? (yes/no): ').strip().lower() == 'yes'



def setting():
    """Функція для налаштувань калькулятора, яка дозволяє змінювати кількість знаків після коми."""
    while True:
        print("1. Change the number of decimal places")
        print(f"Current value after comma: {global_value.round_number}")
        print("0. Back to main menu")

        menu_setting = input('Enter your choice: ')

        match menu_setting:
            case '1':
                try:
                    new_round_number = int(input('Enter number of decimal places: '))
                    app_settings.update_round_number(new_round_number)  # Виклик функції для оновлення
                    print(f"Number of decimal places set to: {global_value.round_number}")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            case '0':
                break



# Використання класу Calculator у вашій програмі
def calculator():
    calc = Calculator()

    while True:
        try:
            first_operand, second_operand, operator = calc.get_user_input()

            result = calc.calculate(first_operand, second_operand, operator)

            if result is not None:
                rounded_result = calc.get_rounded_result(result)
                print('Result: ', rounded_result)  # Використовуємо метод для округлення

                calc.log_history(first_operand, operator, second_operand, rounded_result)

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

                if not calc.ask_for_continue():
                    break

        except ValueError as e:
            print(f"Error: {e}")


def main():
    while True:
        print("Menu:")
        print("1. Start calculator")
        print("2. Settings")
        print("3. Exit")
        choice = input('Enter your choice: ').strip()

        match choice:
            case '1':
                calculator()
            case '2':
                setting()  # Виклик функції налаштувань
            case '3':
                print("Exiting the program...")
                break

main()
