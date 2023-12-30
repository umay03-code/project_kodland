def double_letter(str):
    # Sonuç
    result = ''
    for letter in str:
        result += letter * 2
    return result

def secret_function(a, b):
    #format?
    return f'{a}{b}'

print(double_letter("Merhaba"))
print(secret_function(1,2))
print(secret_function("Merhaba, ", "Dünya!"))