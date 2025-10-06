import random

def get_ints_shuffled_one_dig_first():
    # Define the range of integers
    numbers1 = list(range(1, 10))
    numbers2 = list(range(10, 21))

    # Shuffle each list
    random.shuffle(numbers1)
    random.shuffle(numbers2)

    # Join the two lists
    numbers = numbers1 + numbers2
    return numbers

# Print the shuffled results
print(get_ints_shuffled_one_dig_first())
