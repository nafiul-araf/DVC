import pandas as pd
import os

# Creating a simple dictionary to hold the data.  A dictionary is a good way
# to organize data before creating a DataFrame.  Each key in the dictionary
# will become a column in the DataFrame, and the values associated with
# each key will be the data in that column.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 28, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [50000, 60000, 45000, 55000, 70000]
}

df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"Sample data saved in {file_path}")