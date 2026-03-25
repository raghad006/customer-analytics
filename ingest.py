import pandas as pd
import sys 

data=sys.argv[1]
df = pd.read_csv(data)

df.to_csv("data_raw.csv", index=False) 

print(f"Saved raw data to data_raw.csv from {data}")