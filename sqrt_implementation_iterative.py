import numpy as np
import struct
import matplotlib.pyplot as plt

def iter_sqrt(x: float) -> float:
    xh = 0.5 * x
    i = struct.unpack('I', struct.pack('f', x))[0]
    i = 0x5F375A86 - (i >> 1)
    y = struct.unpack('f', struct.pack('I', i))[0]
    y = y * (1.5 - xh * y * y)
    y = y * (1.5 - xh * y * y)
    y = y*x
    return y


x = np.arange(0.001, 100, 0.001)  # avoid 0 to prevent division by zero

x_fp16 = x.astype(np.float16)
sqrt_fp16 = np.array([iter_sqrt(float(xi)) for xi in x_fp16], dtype=np.float16)

sqrt_fp64 = np.array([iter_sqrt(float(xi)) for xi in x], dtype=np.float64)

rel_error = (sqrt_fp16.astype(np.float64) - sqrt_fp64) / sqrt_fp64

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x, sqrt_fp64, label='64-bit sqrt')
plt.plot(x, sqrt_fp16, label='16-bit sqrt', alpha=0.7)
plt.xlabel('x')
plt.ylabel('sqrt(x)')
plt.title('Fast Square Root: 16-bit vs 64-bit')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x, rel_error)
plt.xlabel('x')
plt.ylabel('Relative Error')
plt.title('Relative Error (16-bit vs 64-bit)')
plt.grid(True)

plt.show()
print(max(rel_error))
