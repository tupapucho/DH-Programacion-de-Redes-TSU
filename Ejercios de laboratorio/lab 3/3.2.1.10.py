

user_word = input("Ingresa una palabra: ")

for letter in user_word:
    letter = letter.upper()
    if letter in "AEIOU":
        continue
    print(letter)
