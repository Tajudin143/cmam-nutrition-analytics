# Data cleaning script

import pandas as pd

def clean_data(filepath):
    df = pd.read_excel(filepath)

    df['date'] = pd.to_datetime(df['date'])

    df = df.drop_duplicates()

    df = df.fillna(0)

    return df
