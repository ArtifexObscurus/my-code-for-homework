
"""
В нас є список [1, 2, 3, 4, 5, 6, 7, 8, 9]
потрібно написати функцію, яка буде проходити по цьому списку
та виводити лише непарні числа

"""

#print_odd_numbers
def print_odd_numbers(nunber_list: list[int]):

    """
    A function that receives a list of numbers and prints only odd numbers    
    """
    # Пройтися по всім числам
    for number in nunber_list:
        # Перевірити чи конкретне число є парним чи ні
        if not number % 2 == 0:
            # Якщо не парне, то вивести у термінал
            print(number, end=' ')  
                     
numbers = [1, 2, 3, 4, 5, 6, 7, 67, 9]
print_odd_numbers(numbers)
