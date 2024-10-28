import random


def generate_draw_command(vertices, rotation, width, height):
    # Define the rotation matrix for 0, 90, 180, and 270 degrees clockwise
    if rotation == 0:
        rotation_matrix = [[1, 0], [0, 1]]
    elif rotation == 90:
        rotation_matrix = [[0, 1], [-1, 0]]
    elif rotation == 180:
        rotation_matrix = [[-1, 0], [0, -1]]
    elif rotation == 270:
        rotation_matrix = [[0, -1], [1, 0]]
    else:
        raise ValueError("Rotation must be 0, 90, 180, or 270 degrees")

    # Apply the rotation matrix to each vertex
    rotated_vertices = [(dx * rotation_matrix[0][0] + dy * rotation_matrix[0][1], dx * rotation_matrix[1][0] + dy * rotation_matrix[1][1]) for dx, dy in vertices]

    # Determine the bounding box of the rotated shape
    min_x = min(x for x, y in rotated_vertices)
    max_x = max(x for x, y in rotated_vertices)
    min_y = min(y for x, y in rotated_vertices)
    max_y = max(y for x, y in rotated_vertices)

    # Adjust the bounding box to ensure no negative values
    if min_x < 0:
        offset_x = -min_x
    else:
        offset_x = 0

    if min_y < 0:
        offset_y = -min_y
    else:
        offset_y = 0

    # Determine the restricted start positions
    allowed_start_positions = [
        (x + offset_x, y + offset_y)
        for x in range(width - (max_x - min_x) + 1)
        for y in range(height - (max_y - min_y) + 1)
        if x + offset_x >= 0 and y + offset_y >= 0 and x + offset_x + max_x <= width - 1 and y + offset_y + max_y <= height - 1
    ]

    # Choose a random start position from the allowed positions
    start_x, start_y = random.choice(allowed_start_positions)

    # Generate the absolute coordinates based on the starting point
    absolute_vertices = [(start_x + dx, start_y + dy) for dx, dy in rotated_vertices]

    # Create the draw command
    draw_command = "\\draw " + " -- ".join(f"({x},{y})" for x, y in absolute_vertices) + " -- cycle;"

    return draw_command


# Define vertices for the letter shapes
vertices_dict = {
    "I": [(0, 0), (1, 0), (1, 4), (0, 4)],
    "T": [(0, 3), (3, 3), (3, 2), (2, 2), (2, 0), (1, 0), (1, 2), (0, 2)],
    "L": [(3, 4), (2, 4), (2, 1), (0, 1), (0, 0), (3, 0)],
    "H": [(0, 0), (1, 0), (1, 1), (2, 1), (2, 0), (3, 0), (3, 3), (2, 3), (2, 2), (1, 2), (1, 3), (0, 3)],
    "E": [(0, 0), (3, 0), (3, 1), (1, 1), (1, 2), (2, 2), (2, 3), (1, 3), (1, 4), (3, 4), (3, 5), (0, 5)],
    "TT": [(0, 1), (1, 1), (1, 0), (3, 0), (3, 4), (1, 4), (1, 3), (0, 3)],
    "C": [(2, 4), (2, 3), (1, 3), (1, 1), (2, 1), (2, 0), (0, 0), (0, 4)],
    "U": [(0, 4), (1, 4), (1, 1), (2, 1), (2, 4), (3, 4), (3, 0), (0, 0)],
    "G": [(3, 1), (3, 0), (0, 0), (0, 4), (2, 4), (2, 3), (1, 3), (1, 1), (2, 1), (2, 2), (3, 2)],
    "GG": [(3, 1), (2, 1), (2, 0), (0, 0), (0, 4), (2, 4), (2, 3), (1, 3), (1, 2), (3, 2)],
    "F": [(0, 4), (3, 4), (3, 3), (1, 3), (1, 2), (2, 2), (2, 1), (1, 1), (1, 0), (0, 0)],
}

# Define vertices for the Tetris shapes
# Define vertices for the twelve possible shapes in a set of unique pentominoes
pentominoes_vertices_dict = {
    "T": [(0, 3), (3, 3), (3, 2), (2, 2), (2, 0), (1, 0), (1, 2), (0, 2)],
    "U": [(0, 0), (0, 2), (1, 2), (1, 1), (2, 1), (2, 2), (3, 2), (3, 0)],
    "V": [(0, 0), (0, 3), (1, 3), (1, 1), (2, 1), (3, 1), (3, 0)],
    "W": [(0, 1), (0, 3), (1, 3), (1, 2), (2, 2), (2, 1), (3, 1), (3, 0), (1, 0), (1, 1)],
    "X": [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 2), (3, 2), (3, 1), (2, 1), (2, 0), (1, 0), (1, 1)],
    "Y": [(1, 0), (1, 2), (0, 2), (0, 3), (1,3), (1, 4), (2, 4), (2,0)],
    "Z": [(0, 2), (0, 3), (2, 3), (2, 1), (3, 1), (3, 0), (1, 0), (1, 2)],
    "F": [(0, 1), (0, 2), (1, 2), (1, 3), (3, 3), (3, 2), (2, 2), (2, 0), (1, 0), (1, 1)],
    "I": [(0, 0), (0, 5), (1, 5), (1, 0)],
    "L": [(0, 0), (0, 4), (1, 4), (1, 1), (3, 1), (3, 0)],
    "P": [(0, 0), (0, 3), (2,3), (2, 1), (1, 1), (1, 0)],
    "N": [(0, 0), (0, 3), (1,3), (1, 4), (2, 4), (2, 2), (1, 2), (1, 0)],
}


# Randomly choose a key from the dictionary
random_key = random.choice(list(pentominoes_vertices_dict.keys()))

# Assign the vertices of the chosen pentomino
vertices = pentominoes_vertices_dict[random_key]

rotation = random.choice([0, 90, 180, 270])
width = 10
height = 6
print(generate_draw_command(vertices, rotation, width, height))
