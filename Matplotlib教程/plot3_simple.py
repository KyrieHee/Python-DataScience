import matplotlib.pyplot as plt
import numpy as np

#:从-1-----1之间等间隔采50个数
x = np.linspace(-1, 1, 50)
y = 2*x + 1

plt.plot(x, y)
plt.show()