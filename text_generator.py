import random
import string

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'

letter_input_1 = input("Enter 'v' for vowels, 'c' for comments, 'l' for any letter: ")
letter_input_2 = input("Enter 'v' for vowels, 'c' for comments, 'l' for any letter: ")
letter_input_3 = input("Enter 'v' for vowels, 'c' for comments, 'l' for any letter: ")


def generator():
    """Generates three random characters."""
    if letter_input_1 == 'v':
        letter1 = random.choice(vowels)
    elif letter_input_1 == 'c':
        letter1 = random.choice(consonants)
    else:
        letter1 = random.choice(string.ascii_lowercase)

    if letter_input_2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input_2 == 'c':
        letter2 = random.choice(consonants)
    else:
        letter2 = random.choice(string.ascii_lowercase)

    if letter_input_3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input_3 == 'c':
        letter3 = random.choice(consonants)
    else:
        letter3 = random.choice(string.ascii_lowercase)

    name = letter1 + letter2 + letter3

    return name

print(generator())
