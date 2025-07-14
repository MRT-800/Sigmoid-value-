import numpy as np
import matplotlib.pyplot as plt

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Step function
def step(x):
    return np.where(x > 0, 1, 0)

# Plot sigmoid and step curves
x = np.linspace(-10, 10, 400)
y_sigmoid = sigmoid(x)
y_step = step(x)

plt.plot(x, y_sigmoid, label='Sigmoid curve')
plt.plot(x, y_step, label='Step function', linestyle='--')

# Take user input
user_input = float(input("Enter any number to evaluate sigmoid: "))
user_output = sigmoid(user_input)
user_step = step(user_input)

# Plot user input on curves
plt.scatter(user_input, user_output, color='red', label=f'Sigmoid({user_input}) = {user_output:.4f}', zorder=5)
plt.scatter(user_input, user_step, color='blue', label=f'Step({user_input}) = {user_step}', zorder=5)
plt.axvline(user_input, color='red', linestyle='--', alpha=0.5)
plt.axhline(user_output, color='red', linestyle='--', alpha=0.5)

# Graph details
plt.title('Sigmoid vs Step Function')
plt.xlabel('Input (x)')
plt.ylabel('Output')
plt.legend()
plt.grid(True)
plt.ylim(-0.1, 1.1)

plt.show()