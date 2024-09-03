import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# 읽어야 할 csv file이 있는지 없는 지 검사
def load_csv(path : str):
    fish_data = pd.read_csv(path)
    partition_cols = ["Label"]
    fish_data.to_parquet(
        "~/.fish_data/", 
        partition_cols=partition_cols,
        index=False
        )
    
    return fish_data.head(5)


def predict():
    df = pd.read_parquet("~/.fish_data/")
    
    x = df[["weight", "length"]]
    y = df["target"]


def agg():
    ...