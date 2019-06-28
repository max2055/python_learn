import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,20,100)   # 创建一个列表
plt.plot(x,np.sin(x))       # 对于每个点的sin值绘图
plt.show()                  # 显示