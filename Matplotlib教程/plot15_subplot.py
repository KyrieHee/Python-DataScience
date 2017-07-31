import matplotlib.pyplot as plt

plt.figure()
#2,2,1第二行第二列 第一个
plt.subplot(2,2,1)
plt.plot([0,1], [0,1])

plt.subplot(222)
plt.plot([0,1], [0,2])

plt.subplot(223)
plt.plot([0,1], [0,4])

plt.subplot(224)
plt.plot([0,1], [0,5])

plt.show()