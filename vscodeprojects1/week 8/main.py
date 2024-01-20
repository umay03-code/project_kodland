import random


def pas(number):
    elements = "+-/*!&$#?=@<>1234567890.,;\:"
    password = ""

    for i in range(number):
        password += random.choice(elements)

    return password

