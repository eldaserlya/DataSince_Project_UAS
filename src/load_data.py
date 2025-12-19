import os
import pandas as pd

def load_tae():
    base_dir = os.getcwd()
    data_path = os.path.join(base_dir, "data", "tae.data")
    cols = ["english_speaker","instructor","course","semester","class_size","target"]
    return pd.read_csv(data_path, header=None, names=cols)

