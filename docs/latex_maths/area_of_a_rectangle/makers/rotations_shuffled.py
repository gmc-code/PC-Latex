import random


def get_rotations_shuffled():
    # Define the range of angles with weighting for 0
    angles = [0, 0, 0, 0, 0, 10, 30, -10, -30, -45] * 2
    # Shuffle list
    random.shuffle(angles)
    return angles

# Print the shuffled results
print(get_rotations_shuffled())
