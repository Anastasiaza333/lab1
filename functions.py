#
# def addition(a,b):
#     c = a + b
#
#     return c
#
# def subtraction(a,b):
#     c = a - b
#
#     return c
#
# def division(a,b):
#
#     while b == 0:
#         print('You cannot divide by zero! Enter another number.')
#         b = float(input('Input second operand: '))
#
#     c = a / b
#
#     return c
#
# def multiplication(a,b):
#     c = a * b
#
#     return c
#
# def power(a,b):
#     c = a ** b
#
#     return c
#
# def square_root(a,b):
#     c = a ** (1/b)
#
#     return c
#
# def modulus(a,b):
#     c = a%b
#
#     return c
#
# def log_history(first_operand, operator, second_operand, result):
#     with open('history_log.txt', 'a') as file:
#         file.write(f"{first_operand} {operator} {second_operand} = {result}\n")
#
# def show_history():
#     try:
#         with open('./source/history_log.txt', 'r') as file:
#             return file.read()
#     except FileNotFoundError:
#         return "No history found."
#
# def show_menu():
#     print("Main Menu")
#     print("1. Calculator")
#     print("2. Settings")
#     #print("3. Exit")