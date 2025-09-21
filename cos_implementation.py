import math
import numpy as np

def cos_pi_x(x):
    """
    Computes cos(pi * x) for x in [0, 0.5] using piecewise linear approximations.
    """
    x=float(x)
    if not (0 <= x <= 0.5):
        return 0

    # Define interval boundaries
    b14 = 2 ** -14
    b10 = 2 ** -10
    b9  = 2 ** -9
    b8  = 2 ** -8
    b7  = 2 ** -7
    b6  = 2 ** -6
    b5  = 2 ** -5
    b4  = 2 ** -4
    b3  = 2 ** -3
    b2  = 2 ** -2
    b1  = 2 ** -1

    if 0 <= x < b14:
        return 1
    elif b14 <= x < b10:
        return 1 - (x - b14) * (1 / 2 ** 8)
    elif b10 <= x < b9:
        return 1 - (x - b10) * (1 / 2 ** 7 + 1 / 2 ** 8 + 1 / 2 ** 9)
    elif b9 <= x < b8:
        return 1 - (x - b9) * (1 / 2 ** 6 + 1 / 2 ** 7 + 1 / 2 ** 8)
    elif b8 <= x < b7:
        return 1 - (x - b8) * (1 / 2 ** 5 + 1 / 2 ** 6 + 1 / 2 ** 7 + 1 / 2 ** 9)
    elif b7 <= x < b6:
        return 1 - (x - b7) * (1 / 2 ** 4 + 1 / 2 ** 5 + 1 / 2 ** 6 + 1 / 2 ** 8 + 1 / 2 ** 9)
    elif b6 <= x < b5:
        return 1 - (x - b6) * (1 / 2 ** 3 + 1 / 2 ** 4 + 1 / 2 ** 5 + 1 / 2 ** 7 + 1 / 2 ** 8)
    elif b5 <= x < b4:
        return 1 - (x - b5) * (1 / 2 ** 2 + 1 / 2 ** 3 + 1 / 2 ** 4 + 1 / 2 ** 6 + 1 / 2 ** 8 + 1 / 2 ** 9)
    elif b4 <= x < b3:
        return 0.98046875 - (x - b4) * (1 / 2 + 1 / 2 ** 2 + 1 / 2 ** 3 + 1 / 2 ** 5 + 1 / 2 ** 8)
    elif b3 <= x < b2:
        val = 0.921875 - (x - b3) * (1 + 1 / 2 + 1 / 2 ** 3 + 1 / 2 ** 4 + 1 / 2 ** 5 + 1 / 2 ** 7 + 1 / 2 ** 8 + 1 / 2 ** 9)
        if x>=(3/16):
            val+=(b3-(x-b3))*(1/4)
        else:
            val+=(x-b3)*(1/4)
        return val
    elif b2 <= x <= b1:
        return 0.70703125 - (x - b2) * (2 + 1 / 2 + 1 / 2 ** 2 + 1 / 2 ** 4 + 1 / 2 ** 6)
    else:
        return 0
def actual_cos(x):
    """
    Computes the accurate value of cos(pi * x) using math.cos.
    """
    return math.cos(math.pi * x)
# Example usage and comparison
import matplotlib.pyplot as plt

x_vals = np.arange(0, 0.5, 0.001)
actual_vals = [actual_cos(x) for x in x_vals]
approx_vals = [cos_pi_x(x) for x in x_vals]
# print(approx_vals)
# print(actual_vals)
plt.plot(x_vals, actual_vals, label='actual_cos(x)')
plt.plot(x_vals, approx_vals, label='cos_pi_x(x)', linestyle='--')
plt.xlabel('x')
plt.ylabel('cos(pi * x)')
plt.legend()
plt.title('Comparison of actual_cos(x) and cos_pi_x(x)')
plt.show()
# Plot percentage absolute error
percentage_error = [((a - b)/ a) * 100 if a != 0 else 0 for a, b in zip(actual_vals, approx_vals)]
print(max(percentage_error))
plt.figure()
plt.plot(x_vals, percentage_error, label='Percentage Absolute Error')
plt.xlabel('x')
plt.ylabel('Percentage Absolute Error (%)')
plt.title('Percentage Absolute Error between actual_cos(x) and cos_pi_x(x)')
plt.legend()
plt.show()
        