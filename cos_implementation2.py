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
            val+=(b3-(x-b3))*(1/4+1/16)
        else:
            val+=(x-b3)*(1/4+1/16)
        return val
    elif b2 <= x <= b1:
        t1 = 0.5-x
        if t1<=b6:
            return t1*3.140625
        elif t1<=b5:
            return 0.048828125 + (t1-b6)*(1+2+(1/2**3))
        elif t1<=b4:
            return 0.09765625 + (t1-b5)*(2+1+(1/2**4)+(1/2**5))
        elif t1<=b3:
            return 0.1950903 + (t1-b4)*(3)
        else:
            val = 0.382683 + (t1-b3)*(2+1/2+(1/2**4)+(1/2**5))
            if t1>=(3/16):  
                val+=(b3-(t1-b3))*(1/4-1/16)
            else:   
                val+=(t1-b3)*(1/4-1/16)
            return val
    else:
        return 0
def actual_cos(x):
    """
    Computes the accurate value of cos(pi * x) using math.cos.
    """
    return math.cos(math.pi * x)

def actual_sin(x):
    """
    Computes the accurate value of cos(pi * x) using math.cos.
    """
    return math.sin(math.pi * x)

def cos_pix(x):
    """Computes cos_pi_x for x in [-1,1] using above function"""
    x = float(x)
    x = ((x + 1) % 2) - 1 
    # wraps the argument into the range [-1,1]
    x = abs(x)
    # since cosine is even function
    if (0 <= x <= 0.5):
        return cos_pi_x(x)
    elif (0.5 <= x <= 1):
        x = 1-x
        return (-1)*cos_pi_x(x)    

def sin_pix(x):
    x = x - 0.5
    return cos_pix(x)

# Example usage and comparison
import matplotlib.pyplot as plt

x_vals = np.arange(-10, 10, 0.001)
actual_vals = [actual_sin(x) for x in x_vals]
approx_vals = [sin_pix(x) for x in x_vals]
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
percentage_error = [abs((a - b)/ a) * 100 if a != 0 else 0 for a, b in zip(actual_vals, approx_vals)]
print(max(percentage_error))
plt.figure()
plt.plot(x_vals, percentage_error, label='Percentage Absolute Error')
plt.xlabel('x')
plt.ylabel('Percentage Absolute Error (%)')
plt.title('Percentage Absolute Error between actual_cos(x) and cos_pi_x(x)')
plt.legend()
plt.show()
     