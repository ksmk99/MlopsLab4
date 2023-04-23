import dvc.api
import pandas as pd

data_path = dvc.api.get_url('Data_sets/dataset3.csv', remote="data_remote2")
df = pd.read_csv(data_path.replace("root/", ""))
print(df)
