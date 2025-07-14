import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

num = float(input("Enter a number: "))
result = sigmoid(num)
print(f"Sigmoid value of {num} is {result}")