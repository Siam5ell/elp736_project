import matplotlib.pyplot as plt
import numpy as np
def decimal_to_binary_and_back(value, precision=10):
    if not (0 <= value < 1):
        raise ValueError("Input must be a decimal number between 0 (inclusive) and 1 (exclusive).")
    
    binary = "0."
    frac = value
    for _ in range(precision):
        frac *= 2
        if frac >= 1:
            binary += "1"
            frac -= 1
        else:
            binary += "0"
    
    reconstructed = 0.0
    for i, bit in enumerate(binary[2:], start=1):  # skip "0."
        if bit == "1":
            reconstructed += 1 / (2 ** i)
    
    return reconstructed

def square_root_piecwise_fixed(x):
    #A function that calculates square root using piecewise linear approximate for input between the range 1 and 2
    if x < 1.125: 
        return 1 + ((x-1)*decimal_to_binary_and_back(0.4853))                  
    elif x < 1.25: 
        return 1 + ((x-1)*decimal_to_binary_and_back(0.459))  + decimal_to_binary_and_back(0.003286354810)     
    elif x < 1.375: 
        return 1 + ((x-1)*decimal_to_binary_and_back(0.4365)) + decimal_to_binary_and_back(0.008894086338)     
    elif x < 1.5: 
        return 1 + ((x-1)*decimal_to_binary_and_back(0.4171)) + decimal_to_binary_and_back(0.016181145649)     
    elif x < 1.625: 
        return 1 + ((x-1)*decimal_to_binary_and_back(0.4001)) + decimal_to_binary_and_back(0.024704843365)     
    elif x < 1.75: 
        return 1 + ((x-1)*decimal_to_binary_and_back(0.3850)) + decimal_to_binary_and_back(0.034150992728)     
    elif x < 1.875: 
        return 1 + ((x-1)*decimal_to_binary_and_back(0.3715)) + decimal_to_binary_and_back(0.044291226149)     
    elif x < 2.0: 
        return 1 + ((x-1)*decimal_to_binary_and_back(0.3593)) + decimal_to_binary_and_back(0.054956213492)     

    return "Invalid Input"
ele = np.arange(1,1.99,0.0001)
y_piece = [((x**0.5)-square_root_piecwise_fixed(x))*100/(x**0.5) for x in ele]
print(max(y_piece))
plt.plot(ele,y_piece)
plt.show()

