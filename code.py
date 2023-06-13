string = input()
strings = ""
for char in string:
    if char.isupper():
        c = char.lower()
        strings +=c
    elif char.islower():
        c = char.upper()
        strings +=c
print(strings)        
        

