memory_value = 0
round_number=0

class GlobalValue:
    def __init__(self):
        self.round_number = 2  # За замовчуванням 2 знаки після коми
        self.memory_value = 0   # Значення пам'яті

global_value = GlobalValue()  # Створюємо екземпляр
