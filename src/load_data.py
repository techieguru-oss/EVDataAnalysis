import pandas as pd
import os

def load_dataset(filepath):
    if not filepath.endswith('.csv'):
        raise ValueError(f"Expected a .csv file, got: {filepath}")
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    return pd.read_csv(filepath)