import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Name":["Anna","Ben","Cara"],
    "Marks":[85,92,78]
})

plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.show()