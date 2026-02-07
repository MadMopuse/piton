"""indiv_task.2.2"""
from math import factorial


def fact_num(num: int):
    return factorial(num)


def main():
    num_str = input('Введите целое положительное число: ')
    print()

    if not num_str.isdigit() or num_str.startswith("0"):
        print(f'{num_str} - не является целым положительным числом.')
        return

    num = int(num_str)
    fact = fact_num(num)
    print(f'Факториал числа "{num_str}" равен {fact}.')


main()  