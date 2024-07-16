import random


def generate_numbers(n, total, min_value):
    # adjustments to ranint are based on testing and intuition
    numbers = [
        random.randint(min_value, int((total - min_value * (n - 1)) / (n**0.5)))
        for _ in range(n)
    ]
    s = sum(numbers)
    numbers = [int(x / s * total) for x in numbers]
    diff = total - sum(numbers)
    numbers = sorted(numbers, reverse=False)
    # print(numbers, diff)  # testing only
    for i in range(diff):
        numbers[i] += 1
    return sorted(numbers, reverse=True)


numbers = generate_numbers(10, 100, 5)
print(numbers)

numbers = generate_numbers(5, 100, 10)
print(numbers)

numbers = generate_numbers(5, 100, 5)
print(numbers)