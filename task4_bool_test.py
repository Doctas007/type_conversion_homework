# Task 4: bool() Test
# Instructions:
# 1. Convert each value to boolean using bool()
# 2. Print the original value, converted result, and its type
# 3. Observe which values become True and which become False

# Values to test
value1 = 0
value2 = 1

# TODO: Convert value1 to boolean
result1 = None  # Replace None with your code

# TODO: Convert value2 to boolean
result2 = None  # Replace None with your code

# Print results (don't modify these lines)
print("Value:", value1)
print("Converted to boolean:", result1)
print("Type:", type(result1))
print("-" * 20)

print("Value:", value2)
print("Converted to boolean:", result2)
print("Type:", type(result2))
print("-" * 20)

# Testing with empty string
value3 = ""
result3 = bool(value3)
print(f"Value: {value3}")
print(f"Converted to boolean: {result3}")
print(f"Type: {type(result3)}")
print("-" * 20)

# Testing with non-empty string
value4 = "hello"
result4 = bool(value4)
print(f"Value: {value4}")
print(f"Converted to boolean: {result4}")
print(f"Type: {type(result4)}")
print("-" * 20)
