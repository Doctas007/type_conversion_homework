# Task 10: Boolean Logic
# Instructions:
# 1. Convert each value to boolean using bool()
# 2. Print the original value, its type, and boolean result
# 3. Observe which values become True and which become False

# Values to test
value1 = 0  # integer zero
value2 = 1  # integer one
value3 = ""  # empty string
value4 = "hello"  # non-empty string
value5 = 0.0  # zero as float

# TODO: Convert each value to boolean
result1 = None  # Replace None with your code
result2 = None  # Replace None with your code
result3 = None  # Replace None with your code
result4 = None  # Replace None with your code
result5 = None  # Replace None with your code


# Print results (don't modify these lines)
def print_result(value, result):
    print("Value:", value)
    print("Type:", type(value))
    print("Converted to boolean:", result)
    print("-" * 30)


print_result(value1, result1)
print_result(value2, result2)
print_result(value3, result3)
print_result(value4, result4)
print_result(value5, result5)

# Test with empty string
value3 = ""
result3 = bool(value3)
print(f"Value: {value3}")
print(f"Type: {type(value3)}")
print(f"Converted to boolean: {result3}")
print("-" * 30)

# Test with non-empty string
value4 = "hello"
result4 = bool(value4)
print(f"Value: {value4}")
print(f"Type: {type(value4)}")
print(f"Converted to boolean: {result4}")
print("-" * 30)

# Test with float
value5 = 0.0
result5 = bool(value5)
print(f"Value: {value5}")
print(f"Type: {type(value5)}")
print(f"Converted to boolean: {result5}")
print("-" * 30)
