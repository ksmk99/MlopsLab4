import dvc.api
import pandas as pd

data_path = dvc.api.get_url('Data_sets/dataset1.csv', remote="data_remote")
df = pd.read_csv(data_path)
print(df)