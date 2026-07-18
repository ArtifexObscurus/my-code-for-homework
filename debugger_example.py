
"""
В нас є список [1, 2, 3, 4, 5, 6, 7, 8, 9]
потрібно написати функцію, яка буде проходити по цьому списку
та виводити лише непарні числа

"""

#print odd numbers
def print_only_odd_numbers_in_a_list(nunber_list: list):
    # Пройтися по всим числам
    for number in nunber_list:
        # Перевірити чи конкретне число є парним чи ні
        if not number % 2 == 0:
            # Якщо не парне, то вивести у термінал
            print(number, end=' ')
           
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_only_odd_numbers_in_a_list(numbers)
