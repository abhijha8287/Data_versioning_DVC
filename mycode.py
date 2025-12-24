import pandas as pd
import os

data = {"Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],    
        "City": ["New York", "Los Angeles", "Chicago"]
        }
df=pd.DataFrame(data)

new_row = {"Name": "David", "Age": 28, "City": "San Francisco"}
df.loc[len(df)] = new_row

new_row2 = {"Name": "Eva", "Age": 22, "City": "Boston"}
df.loc[len(df)] = new_row2

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "people_data.csv")
df.to_csv(file_path, index=False)

print(f"DataFrame saved to {file_path}")