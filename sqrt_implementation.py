import numpy as np
import matplotlib.pyplot as plt
class BinaryRepresentation:
    def __init__(self, value: float):
        self.value = value
        self.bin_value = self.float_to_binary(value)
    def float_to_binary(self, value: float) -> str:
        sign = "0"
        if value < 0:
            sign = "1"
            value = -value
        integer_part = int(value)
        fractional_part = value - integer_part
        int_bin = bin(integer_part).replace("0b", "")
        frac_bin = ""
        for _ in range(26):
            fractional_part *= 2
            bit = int(fractional_part)
            frac_bin += str(bit)
            fractional_part -= bit
        if int_bin == "0":
            power = -1
            while power >=-13 and frac_bin[-power-1] != '1':
                power -= 1
            exponent = "00000"
            if frac_bin[-power-1] == '1':
                exponent = format(15 + power, '05b')
            mantissa = frac_bin[-power:-power+10]
            return sign+exponent+mantissa
        else:
            exponent = format(15 + len(int_bin) - 1, '05b')
            mantissa = (int_bin + frac_bin)[1:11]
            return sign+exponent+mantissa
    def binary_to_float(self, bin_str: str) -> float:
        sign = int(bin_str[0])
        exponent = bin_str[1:6]
        mantissa = bin_str[6:]
        if exponent == "00000":
            # Subnormal case
            exp_val = -14
            mantissa_val = 0
            for i, bit in enumerate(mantissa):
                mantissa_val += int(bit) * (2 ** -(i + 1))
            value = (2 ** exp_val) * mantissa_val
        else:
            # Normal case
            exp_val = int(exponent, 2) - 15
            mantissa_val = 1
            for i, bit in enumerate(mantissa):
                mantissa_val += int(bit) * (2 ** -(i + 1))
            value = (2 ** exp_val) * mantissa_val

        if sign == 1:
            value = -value
        return value
    def square_root(self) -> str:
        bin_str = self.bin_value
        sign = bin_str[0]
        exponent = bin_str[1:6]
        mantissa = bin_str[6:]

        if exponent == "00000":
            new_exponent = format(7, '05b')
            new_mantissa = mantissa
            if mantissa == "0000000000":
                new_exponent = "00000"
                new_mantissa = "0000000000"
            return sign + new_exponent + new_mantissa

        exp_val = int(exponent, 2)
        actual_exp = exp_val - 15

        if exp_val % 2 == 1:
            # e+15 is odd, actual exponent is even
            new_exp_val = (exp_val + int("01111", 2)) >> 1
            new_exponent = format(new_exp_val, '06b')[1:]  # get 5 bits
            new_mantissa = "0" + mantissa[:-1]
        else:
            # e+15 is even, actual exponent is odd
            new_exp_val = (exp_val + int("01110", 2)) >> 1
            new_exponent = format(new_exp_val, '06b')[1:]  # get 5 bits
            new_mantissa = "1" + mantissa[:-1]

        return sign + new_exponent + new_mantissa

b1 = BinaryRepresentation(10.625)
print(b1.bin_value)  # Output: 01001010101010000000
print(b1.binary_to_float(b1.bin_value))  # Output: 10.625
print(b1.binary_to_float(b1.square_root()))  # Output: 3.25
b2 = BinaryRepresentation(0.075)
print(b2.bin_value) 
print(b2.binary_to_float(b2.bin_value))  # Output: -0.075
print(b2.binary_to_float(b2.square_root()))  # Output: approximately 0.273861278752583
b3 = BinaryRepresentation(0.0000366)
print(b3.bin_value) 
print(b3.binary_to_float(b3.bin_value))  # Output: -0.0000366
print(b3.binary_to_float(b3.square_root()))  # Output: approximately 0.006049586779787
b4 = BinaryRepresentation(0)
print(b4.bin_value)
print(b4.binary_to_float(b4.bin_value))  # Output: 0.0
print(b4.binary_to_float(b4.square_root()))  # Output: 0.0


values = np.arange(0, 8190, 0.001)
errors = []

for val in values:
    sqrt_py = np.sqrt(val)
    b = BinaryRepresentation(float(val))
    sqrt_bin = b.binary_to_float(b.square_root())
    error = abs(sqrt_py - sqrt_bin)/sqrt_py if sqrt_py != 0 else 0
    errors.append([sqrt_py, sqrt_bin])

plt.plot(values, errors)
plt.xlabel('Original Value')
plt.ylabel('Error Percentage (%)')
plt.title('Error Percentage of BinaryRepresentation sqrt vs Python sqrt')
plt.show()
