"""
Simple Calculator
"""
# Provide your solution here
def calculate(a: int, b: int, operator: str):
    print(a, b, operator)

if operator == "-" or "+" or "*" or "/":
    print(calculate)
elif operator == "/" & 0:
    print("Division by 0 is not allowed")
else:
    print("Invalid operator")


"""
Reverse Word
"""
# Provide your solution here
def reverse_word(word: str):
    return(reversed(word.upper()))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

reverse_word("Eva")