from constants import global_value

round_number = global_value.round_number
memory_value = global_value.memory_value
def update_round_number(new_value):
    """Оновити кількість знаків після коми."""
    global_value.round_number = new_value


