numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)
print(numbers) # [0, 1, 2, 3, 4, 5, 6]
numbers.remove(3)
print(numbers) # [0, 1, 2, 4, 5, 6]
print(2 in numbers) # True
print(len(numbers)) # 6
numbers.clear()
print(numbers) # [] empty list