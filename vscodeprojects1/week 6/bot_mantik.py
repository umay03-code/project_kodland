import random

def gen_pass(pass_length):
    #,isim
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

#password, isim = gen_pass(18,"umay")

#print(password, isim)

def rand_emoji():
    emojies = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emojies)

def head_tail():
    coin = ["head","tail"]
    return random.choice(coin)

def greeting_a():
    g = ["hiii!", "hello!", "hey buddy!", "oh hi!!", "what's it choom?"]
    return random.choice(g)

def send_off_a():
    s = ["i'm doing well", "glad you asked ^^", "nothing new", "ahh i think i lost my heart. hey! did you stole it?"]
    return random.choice(s)

def feeling_a():
    f = ["byee!", "see you soon ^^", "oh... are you leaving :(", "have a nice day!","take care"]
    return random.choice(f)