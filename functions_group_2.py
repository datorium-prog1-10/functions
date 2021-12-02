def greetings(vards, sveiciens = "Labdien"):
    """
    Šī funkcija sasveicinājas ar lietotāju
    Vajag tikai uzrādīt vārdu
    """    
    print(f"{sveiciens}, {vards}")

greetings("Anna", "Hello")

###################################

def largest(a, b):
    largest_number = None
    if a < b:
        largest_number = b
    elif a > b:
        largest_number = a

    return largest_number

print(largest(12, 7))

####################################
def absolute_value(a):
    if a < 0:
        a = a * (-1)
    return a

print(absolute_value(45))

###############
def some_function(*names):
    for name in names:
        print(f"Hello, {name}")

some_function("Anna", "Miks", "Jenifer")

###############
def other_function(names):
    for name in names:
        print(f"Hello, {name}")

vardu_saraksts = ["Anna", "Miks", "Jenifer"]
other_function(vardu_saraksts)

############################
def sum_numbers(numbers):
    numbers_total = 0
    for number in numbers:
        numbers_total += number
    return numbers_total

print(sum_numbers([2, 5, 7, 4, 3, 2, 5, 4, 3]))

############################
def factorial(number):
    """
    Return the factorial of a given number
    """
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(20))
