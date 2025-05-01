

def newton_forward(x, y):
    n = len(x)
    h = x[1] - x[0]
    y_diff = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        y_diff[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            y_diff[i][j] = y_diff[i + 1][j - 1] - y_diff[i][j - 1]

    print("Forward Difference Table:")
    for i in range(n):
        print(f"x{i+1} = {x[i]} | y{i+1} = {y[i]} | ", end="")
        for j in range(n):
            if y_diff[i][j] != 0:
                print(f"Δ^{j}y{i+1} = {y_diff[i][j]} | ", end="")
        print()

    x_input = float(input("Enter the value of x for which you want to find y: "))

    p = (x_input - x[0]) / h
    y_approx = y_diff[0][0]

    for i in range(1, n):
        prod = 1
        for j in range(i):
            prod *= (p - j)
        y_approx += prod / math.factorial(i) * y_diff[0][i]

    print(f"The approximate value of y at x = {x_input} is: {y_approx}")


if __name__ == "__main__":
    import math

    x = [0, 1, 2, 3, 4]
    y = [1, 2.7183, 7.3891, 20.0855, 54.5982]

    newton_forward(x, y)
    # Example usage
    