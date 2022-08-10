import numpy as np
import pandas as pd

df = pd.read_csv("Best Countries for Startups.csv")
df

turkey = df.loc[(df["country"]=="Turkey")]
turkey 

df.describe()

turkeytotal = df.sort_values("total score") 
turkeytotal.head(44)

turkeyquantity = df.sort_values("quantity score") 
asd.head(42)

turkeytotal = df.sort_values("quality score") 
turkeytotal.head(53)

turkeytotal = df.sort_values("quality score") 
turkeytotal.head(57)
 
