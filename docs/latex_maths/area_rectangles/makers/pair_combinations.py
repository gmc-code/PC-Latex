import itertools
import random

# Define the range of integers
numbers = range(2, 10)  # 10 is exclusive, so this includes 2 to 9

# Generate all unique combinations of 2 elements from the 'numbers' list
unique_combinations = list(itertools.combinations(numbers, 2))

# Shuffle the list of combinations
random.shuffle(unique_combinations)

# Print the shuffled results
print(unique_combinations)
for combo in unique_combinations:
    print(combo)
