def sasveicinaties(vards, sveiciens = "Labdien"):
    """
    Si funkcija sasveicinajas ar lietotaju
    Funkcijas ir viens parametrs - vards
    """    
    print(f"{sveiciens}, {vards}")

sasveicinaties("Anna", "Hello")

#######################################
def lielaka_vertiba(a, b):
    lielaka = None
    if a < b:
        lielaka = b
    elif a > b:
        lielaka = a
    else:
        lielaka = None
    
    return lielaka

print(lielaka_vertiba(lielaka_vertiba(2, 4), 7))

###############################################
def absolute_value(a):
    if a < 0:
        a = a * (-1)    
    return a

a = -8
print(absolute_value(a))

###############################################
print(abs.__doc__)

######################################
def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return(a * factorial(a - 1))

print(factorial(20))