import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/noahgift/regression-concepts/master/height-weight-25k.csv")



sns.lmplot(x="Height", y="Weight", data=df)
sns.lmplot(x="Height", y="Weight", data=df, hue="Gender")

