import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import linear_model as lm
from sklearn.metrics import mean_squared_error

df = sns.load_dataset('iris')
df.head()

s1 = pd.Series(range(3), index=range(3))

df.tail()

df.apply(np.cumsum, axis=0)

df.columns

df.sepal_length.plot()
plt.show()

df.mean().max().round(0)
df.std().idxmax()


df.sepal_length.median()
df.loc[((df['sepal_length'] > 5) & (df['sepal_length'] < 5.999)), 'sepal_width'].median()




model = lm.LinearRegression()
idxx = list(df.index)
xx = np.array(idxx).reshape(-1,1)
xx = df['petal_length'].values.reshape(-1,1)
df.columns
yy = df[['sepal_width', 'sepal_length']].values.reshape(-1,2)
xx.shape
yy.shape

c = 0
model.fit(yy , xx)
model.coef_
model.predict(np.array([2,3]).reshape(-1,2))
pred= model.predict(np.array([1]).reshape(-1,1))
c += np.abs(model.coef_)

np.abs(c)
int(np.round(c))
model.n
mean_squared_error(yy,pred)


str(int(np.array([1])))

x = [1, 2, 6, 3, 8, 0.5]
y = [0.5, 7, 99, 1.4, 4.7, 6.4]

x = [-2, -1, 0 , 1, 2]
y = [0, 10, 15, 0, 5, -0.3]

d = dict()
for i in range(len(x)):
    d[x[i]] = y[i]

inp = -0.3
l = list(sorted(d.keys()))[0]
h = list(sorted(d.keys()))[-1]
for k in sorted(d.keys()):
    if k < inp and k > l:
        l = k
    if k  > inp and k < h:
        h = k
print(l, h)


list(d.keys())[0]


((15 - 10) / (0 - -1) * (-0.3 - 1) + 10)
mse()


