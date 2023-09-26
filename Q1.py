import numpy as np

def objective_function(x):
    return x**2 - 3*x + 4

def gradient(x):
    return 2*x - 8

def line_search_method(initial_x, learning_rate, epsilon):
    x = initial_x
    
    while abs(gradient(x)) > epsilon:
        x = x - learning_rate * gradient(x)
    
    return x

initial_x = 0.0
learning_rate = 0.1
epsilon = 1e-6

optimal_x = line_search_method(initial_x, learning_rate, epsilon)

print(f"The optimal solution is x = {optimal_x}, f(x) = {objective_function(optimal_x)}")
