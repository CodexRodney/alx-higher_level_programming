def print_last_digit(number):
    if number < 0:
        number = - number
    c = number % 10
    return c
