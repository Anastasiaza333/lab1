import functions
import app_settings
from constants import global_value

def calculator():
    memory_value= global_value.memory_value
    while True:
        try:
            operator = input("Enter the operator (+, -, *, /, ^, sq, %): ")
            while operator not in ['+', '-', '*', '/','^','%','sq']:
                print("Invalid operator. Available operators: +, -, *, /.")
                operator = input("Enter operator (+, -, *, /, ^, sq, %): ")


            user_input =input('Input first operand (or MR for memory recall):  ').upper()
            if user_input == 'MR':
                first_operand = memory_value
                print(f"Recalled from memory: {first_operand}")
            else:
                first_operand = float(user_input)

            user_input= input('Input second operand (or MR for memory recall):  ').upper()
            if user_input == 'MR':
                second_operand = memory_value
                print(f"Recalled from memory: {second_operand}")
            else:
                second_operand = float(user_input)

            result = 0
            match operator:
                case '+':
                    result = functions.addition(first_operand, second_operand)
                case '-':
                    result = functions.subtraction(first_operand, second_operand)
                case '/':
                    result = functions.division(first_operand, second_operand)
                case '*':
                    result = functions.multiplication(first_operand, second_operand)
                case '^':
                    result = functions.power(first_operand, second_operand)
                case 'sq':
                    result = functions.square_root(first_operand, second_operand)

                case '%':
                    result = functions.modulus(first_operand, second_operand)

            print('Result: ', round(result,global_value.round_number))

            functions.log_history(first_operand,operator,second_operand,round(result,global_value.round_number))

            choice_memory = input('Would you like to store result in memory (MS), add to memory (M+), clear memory (MC), or skip? ').upper()
            match choice_memory:
                case 'MS':
                    memory_value = result
                    print(f"Stored {result} in memory.")
                case 'M+':
                    memory_value += result
                    print(f"Added {result} to memory. New memory value: {memory_value}.")
                case 'MC':
                    memory_value = 0
                    print("Memory cleared.")

            if input("Do you want to view history? (yes/no): ").strip().lower() == 'yes':
                print(functions.show_history())

            if input('Do you want to make another calculation? (yes/no): ').lower() !='yes':
                break

        except ValueError as e:
            print(f"Error: {e}")


def main():
    while True:
        functions.show_menu()

        choice = input('Enter your choice: ').strip()

        match choice:
            case '1':
                calculator()
            case '2':
                app_settings.setting()




main()