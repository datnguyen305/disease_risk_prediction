import pandas as pd

def Z_score(series):
    """
    Tính toán Z-score Normalization
    """
    if not pd.api.types.is_numeric_dtype(series):
        raise TypeError("Z-Score chỉ áp dụng được cho dữ liệu số")

    mean = series.mean()
    std_dev = series.std()

    if std_dev == 0:
        return series
    return (series - mean) / std_dev