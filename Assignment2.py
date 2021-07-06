import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7] #days
y=[160,150,140,145,175,165,180] #sales
plt.xlabel('Days  -->',color='blue')
plt.ylabel('Sales  -->',color='blue')
plt.title('Days vs Sales',color='blue')
plt.plot(x,y,'r*-',linewidth=1,markersize=5)
plt.show()