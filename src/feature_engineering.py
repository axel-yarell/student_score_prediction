import pandas as pd

def encode_features(df):
    df_encoded = df.copy()
    categorical_cols = ['gender', 'race/ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
    df_encoded = pd.get_dummies(df_encoded, columns=categorical_cols, drop_first=True)
    return df_encoded
