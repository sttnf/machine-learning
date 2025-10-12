import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../DATA/day.csv")
df.head()

df_processed = (
    df
    .drop(columns=["dteday"])
).copy()

corr_matrix = df_processed.corr()
corr_matrix.head()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix,
            annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Korelasi Variabel")
plt.show()
