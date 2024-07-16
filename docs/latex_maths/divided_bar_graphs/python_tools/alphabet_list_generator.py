import random
import string


def generate_letters(start, n):
    alphabet = string.ascii_lowercase
    start_index = alphabet.index(start)
    end_index = start_index + n
    return list(alphabet[start_index:end_index])


letters = generate_letters("a", 10)
formatted_letters = ", ".join(f'"{letter}"' for letter in letters)
print(f"[{formatted_letters}]")
