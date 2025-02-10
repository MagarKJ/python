birth_year = input("Enter your birth year: ")
new_birth_year = int(birth_year) # This will convert the string to an integer
#age = 2021 - birth_year This will throw an error because input() returns a string and you can't subtract a string from an integer
age = 2025 - new_birth_year
print("Your age is: ", age)