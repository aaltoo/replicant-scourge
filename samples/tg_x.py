import math
import numpy as np
import matplotlib.pyplot as plt

arr = []

def tenth_function(x, x_0, iterations):

    h = 0.0001

    #F(x) = tg(x) равняется sec^2(x)
    #sec^2(x) равняется 1 / cos^2(x)

    tan_derivative = 1 / (math.cos(x_0) * math.cos(x_0))

    x_1 = x_0 - h * tan_derivative

    arr.append(math.tan(x_0))
    iterations += 1

    if x_0 > x:
        tenth_function(x, x_1, iterations)
    else:
        print('Точка минимума: ', math.tan(x_0))
        print('Кол-во итераций: ', iterations)


tenth_function(-4, -3.5, 0)

x = np.arange(-10, 10.01, 0.01)
plt.plot(np.array(arr))
plt.show()
