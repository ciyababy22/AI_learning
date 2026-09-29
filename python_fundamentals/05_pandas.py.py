import pandas as pd

data = {
    "Name":["Anna","Ben","Cara"],
    "Marks":[85,92,78]
}

df = pd.DataFrame(data)

print(df)
print(df.describe())