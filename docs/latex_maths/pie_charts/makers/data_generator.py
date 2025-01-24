import random

def generate_random_animal_data(filename="pie_chart_data.txt"):
    # Predefined list of animal names
    animal_names = [
        "Lions", "Elephants", "Monkeys", "Penguins", "Giraffes", "Otters",
        "Zebras", "Hippos", "Bears", "Dolphins", "Kangaroos", "Pandas",
        "Tigers", "Wolves", "Crocodiles"
    ]

    # Generate a random title
    title = "Favourite zoo animals"

    # Generate a random number of categories (3 to 8)
    num_categories = random.randint(3, 8)

    # Select a random subset of animal names
    selected_animals = random.sample(animal_names, num_categories)

    # Randomly choose a data value range
    value_range = random.choice([(5, 20), (5, 50), (5, 100)])
    min_value, max_value = value_range

    # Generate random scores within the chosen range
    scores = [random.randint(min_value, max_value) for _ in range(num_categories)]
    scores.sort(reverse=True)  # Sort scores in descending order

    # Write the data to the file
    with open(filename, "w") as file:
        file.write(f"{title}\n")
        file.write(",".join(map(str, scores)) + "\n")
        file.write(",".join(selected_animals) + "\n")

    print(f"Data generated and saved to {filename}")
    print(f"Categories: {num_categories}, Range: {value_range}, Scores: {scores}")

# Generate the file
generate_random_animal_data()
