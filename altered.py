import pandas as pd
import os

dict1 = {'name': ['manish','dishant', 'raghav', 'bhavishye'], 
         'age': [23, 23, 24, 22],
         'city': ['tonk', 'jaipur', 'gurgaon', 'delhi']}

df = pd.DataFrame(dict1)
print(df)
df.index.name = "id" # convert index name as id

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'data.csv')
df.to_csv(file_path, index=False)