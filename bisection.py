

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the function for the equation
def f(x):
    """
    This function represents the equation x**3 - 4x - 4.
    
    Parameters:
    x (float): The input value for the equation.
    
    Returns:
    float: The result of the equation.
    """
    return x**3 -  x - 4

# Define the function to find the root of the equation using the bisection method
def bisection_method(a, b, max_iter):
    """
    This function finds the root of the equation using the bisection method.
    
    Parameters:
    a (float): The lower bound of the range.
    b (float): The upper bound of the range.
    max_iter (int): The maximum number of iterations.
    
    Returns:
    float: The root of the equation.
    """
    # Initialize the iteration counter
    iter_count = 0
    
    # Initialize lists to store the results of each iteration
    x_values = []
    f_values = []
    
    # Perform the bisection method
    while iter_count < max_iter:
        # Calculate the midpoint
        c = (a + b) / 2
        
        # Print the result of each iteration
        print(f"Iteration {iter_count+1}: a = {a:.16f}, b = {b:.16f}, c = {c:.16f}, f(c) = {f(c):.16f}")
        
        # Store the results of each iteration
        x_values.append(c)
        f_values.append(f(c))
        
        # Check if the function has opposite signs at the midpoint and one of the bounds
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        # Increment the iteration counter
        iter_count += 1
    
    # Return the root of the equation
    return c

# Define the main function
def main():
    # Define the range of the equation
    a = -10.0
    b = 10.0
    
    # Check if the function has opposite signs at the bounds
    if f(a) * f(b) > 0:
        print("The function does not have opposite signs at the bounds.")
        return
    
    # Define the maximum number of iterations
    max_iter = 15
    
    # Find the root of the equation using the bisection method
    root = bisection_method(a, b, max_iter)
    
    # Print the final result
    print(f"The root of the equation is approximately {root:.4f}.")
    

# Call the main function
if __name__ == "__main__":
    main()

