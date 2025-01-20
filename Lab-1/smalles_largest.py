def find_largest_and_smallest(numbers):
    largest = smallest = numbers[0]
    for num in numbers[1:]:
       if num > largest:
            largest = num
       elif num < smallest:
            smallest = num
    return largest, smallest
numbers = [3, 5, 7, 2, 8, -1, 4, 10, 12]
largest, smallest = find_largest_and_smallest(numbers)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")