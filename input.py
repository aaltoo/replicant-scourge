import math
import numpy as np
import matplotlib.pyplot as plt

arr = []
h = 0.000001
x = -4
x_0 = -3.5
iterations = 0


def tg():
    # F(x) = tg(x) равняется sec^2(x)
    # sec^2(x) равняется 1 / cos^2(x)
    tan_derivative = 1 / (math.cos(x_0) * math.cos(x_0))
    arr.append(math.tan(x_0))
    x_1 = x_0 - h * tan_derivative
    return x_1


while x_0 > x:
    x_0 = tg()
    iterations += 1

print('Кол-во итераций: ', iterations)
print('Точка минимума: ', math.tan(x_0))


x = np.arange(-10, 10.01, 0.01)
plt.plot(np.array(arr))
plt.show()
