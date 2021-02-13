def get_number():
    """ Funkcja pobiera liczbę, którą podał użytkownik i sprawdza jej poprawność.
        Pyta dopóki nie otrzyma poprawnej liczby.
        :rtype: int
        :return: pobrana liczba jako int
    """
    while True:
        try:
            result = int(input("Get the number: "))
            break
        except ValueError:
            print("It's not a number")
    return result

def six_numbers():
    """ Funkcja, tworzy listę z sześciu liczb podanych przez użytkownika.
        :rtype: list
        :return: lista 6 liczb podanych przez użytkowinika
    """
    result = []
    while len(result) < 6:
        number = get_number()
        if number < 1 or number > 49:
            print("Enter numbers from 1 to 49.")
        elif number in result:
            print("You already have that number")
        else:
            result.append(number)
    return result

import random

six_numbers_list = six_numbers()
six_numbers_list.sort()
print(f"Your numbers: {six_numbers_list}")
c_list = []
for i in range(1, 50):
    c_list.append(i)
random.shuffle(c_list)
computer_list = c_list[0:6]
print(computer_list)
result = set(six_numbers_list) & set(computer_list)
print(f"You hit {len(result)} {'number' if len(result) == 1 else 'numbers'}!")
