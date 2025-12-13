import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# index_col replace index column with the defined column
df = pd.read_csv("data/fifa.csv", index_col='Date', parse_dates=True)
# df = pd.read_csv("data/fifa.csv", index_col='Date')
# df = pd.read_csv("data/fifa.csv")

df.head()

plt.figure()
sns.lineplot(data=df)

# in '%matplotlib inline' mode you don't need this
plt.show()


