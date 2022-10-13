
import math


def get_median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[int(len(numbers) / 2)] + numbers[int((len(numbers) / 2) - 1)]) / 2
    else:
        return numbers[math.floor((len(numbers) / 2))]


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        get_median(numbers)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
