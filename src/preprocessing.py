import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df
