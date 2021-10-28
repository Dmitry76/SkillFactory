import pandas as pd
import matplotlib.pyplot as plt
s = pd.Series([1,2,3,4,3,2,10,6])
df = pd.DataFrame([[1,2,3,4,5],[2,4,6,4,2]])
s.plot()
plt.show()

print(df)
df.plot()
plt.show()