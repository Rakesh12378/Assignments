import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x=np.arange(0,10)
y=3*x+10
plt.plot(x,y,'r*--',linewidth=1,markersize=5)
plt.xlabel('X-axis',color='blue')
plt.ylabel('Y-axis',color='blue')
plt.title('2D-Diagram',color='blue')
plt.show()