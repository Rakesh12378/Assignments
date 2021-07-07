import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import randn

df=pd.DataFrame(randn(10,4),columns=['a','b','c','d'])
print(df)

df.plot(kind='bar')
plt.title("Bar Graph",color='b')
plt.xlabel("X-axis",color='b')
plt.ylabel("Y-axis",color='b')
plt.xticks(rotation=0, horizontalalignment="center")
plt.show()