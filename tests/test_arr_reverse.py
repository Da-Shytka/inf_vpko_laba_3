import pytest
from lib import fibonacci_numbers
from lib import bubble_sort
from lib import calculator


# Тесты для функции fibonacci_numbers
def test_fibonacci_numbers_zero(): # проверка на входные данные 0
    result = fibonacci_numbers(0)
    assert result == []

def test_fibonacci_numbers_n(): # проверка на входные данные обычного числа
    result = fibonacci_numbers(7)
    assert result == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_numbers_negative_n(): # проверка на входные данные отрицательного числа
    result = fibonacci_numbers(-5)
    assert result == []

def test_fibonacci_numbers_str_n(): # проверка на входные данные строки
    result = fibonacci_numbers('5')
    assert result == [0, 1, 1, 2, 3]


# Тесты для функции bubble_sort
def test_bubble_sort_empty_list():  # проверка на входные данные 0
    result = bubble_sort([])
    assert result == []

def test_bubble_sort_with_int(): # проверка на входные данные массива
    result = bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    assert result == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bubble_sort_with_str():# проверка на входные данные строки
    result = bubble_sort(['-3', '1', '-4', '1', '5', '-9', '2', '6', '5', '3', '5'])
    assert result == [-9, -4, -3, 1, 1, 2, 3, 5, 5, 5, 6]


# Тесты для функции calculator
def test_calculator_addition():
    result = calculator(5, 3, '+')
    assert result == 8

def test_calculator_addition_str():
    result = calculator('5', '3', '+')
    assert result == 8

def test_calculator_subtraction():
    result = calculator(5, 3, '-')
    assert result == 2

def test_calculator_subtraction_str():
    result = calculator('5', '3', '-')
    assert result == 2

def test_calculator_multiplication():
    result = calculator(5, 3, '*')
    assert result == 15

def test_calculator_multiplication_str():
    result = calculator('5', '3', '*')
    assert result == 15

def test_calculator_division():
    result = calculator(6, 2, '/')
    assert result == 3

def test_calculator_division_str():
    result = calculator('6', '2', '/')
    assert result == 3

def test_calculator_division_by_zero():
    with pytest.raises(ValueError):
        calculator(5, 0, '/')

def test_calculator_division_by_zero_str():
    with pytest.raises(ValueError):
        calculator('5', '0', '/')

def test_calculator_invalid_operator():
    with pytest.raises(ValueError):
        calculator(5, 3, '%')

def test_calculator_invalid_operator_str():
    with pytest.raises(ValueError):
        calculator('5', '3', '%')