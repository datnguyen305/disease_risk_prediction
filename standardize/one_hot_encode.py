import pandas as pd


def apply(dataframe, column_name):
    """
    Thực hiện One-Hot Encoding.
    """
    if column_name not in dataframe.columns:
        return dataframe

    dummies = pd.get_dummies(dataframe[column_name], prefix=column_name, dtype=int)

    # Nối các cột mới vào DataFrame gốc
    df_new = pd.concat([dataframe, dummies], axis=1)

    # Xóa cột gốc (cột chữ) đi vì đã có các cột số thay thế
    df_new = df_new.drop(columns=[column_name])

    return df_new