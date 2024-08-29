import pandas as pd

def read_csv(file_path):
    return pd.read_csv(file_path)

def write_csv(df, file_path):
    df.to_csv(file_path, index=False)
