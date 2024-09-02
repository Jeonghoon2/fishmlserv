import pandas as pd

# 읽어야 할 csv file이 있는지 없는 지 검사
def load_csv(path : str):

    fish_data = pd.read_csv(path)
    return fish_data.head(5)

# 물고기 별로 Partition 후 Parquet 형태로 저장
def predict():
    ...

def agg():
    ...