name = input("Please enter your name: ")
print(f"Hello, {name}!")
birth_year = input("Please enter your birth year: ")
birth_year = int(birth_year)
from datetime import datetime
current_year = datetime.now().year
age = current_year - birth_year
print(f"{name}, you are {age} years old.")