msg="hellooo PYThon 0970"
digits = 0
space = 0
vowels = 0
consonants = 0
special = 0
for i in msg:
    
    if i.isdigit():
        digits += 1
    elif i.isspace():
        space += 1
    elif i.lower() in"aeiou":
        vowels += 1
    elif i.isalpha():
        consonants += 1
    else :
        special += 1



print("Consonants:", consonants)
print("Vowel:",vowels)
print("Space:",space)
print("Digits:",digits)
print("Special:",special)
        