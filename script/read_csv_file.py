import pandas as pd

def reading(file_path):
    data = pd.read_csv(file_path)
    return data