"""
Возвращает список первых n чисел Фибоначчи.
"""
def fibonacci_numbers(n_):
    n = int(n_)
    if n <= 0: #
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            next_fib = fib_list[-1] + fib_list[-2]
            fib_list.append(next_fib)
        return fib_list

"""
Возвращает отсортированную копию списка arr с использованием сортировки пузырьком.
"""
def bubble_sort(arr_):
    arr = []
    for item in arr_:
        number = int(item)
        arr.append(number)
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr

"""
Выполняет указанное арифметическое действие (+, -, *, /) между num1 и num2 и возвращает результат.
"""
def calculator(num1_, num2_, operator):
    num1 = int(num1_)
    num2 = int(num2_)
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Деление на ноль недопустимо")
    else:
        raise ValueError("Неподдерживаемая операция")