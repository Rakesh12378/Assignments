import seaborn as sns
import matplotlib.pyplot as plt
fmri=sns.load_dataset('fmri')
print(fmri.head(5))
sns.relplot(x='timepoint',y='signal',kind='line',data=fmri,col='event',hue='region')
# sns.relplot(x='timepoint',y='signal',kind='line',data=fmri,col='event',hue='region',size='subject')
plt.show()