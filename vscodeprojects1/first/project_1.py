import random

items= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
empty=[]
number = int(input("write your password's lenght"))

for i in range(number):
    #empty = random.choice(items)
    x = int(len(items))
    password = random.randint(0,x)
    print(items[password])
    empty.append(items[password])


print(empty)

    