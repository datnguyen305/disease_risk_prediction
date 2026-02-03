import pandas as pd

def apply(series):
    """
    Tính MIN-MAX
    """
    if not pd.api.types.is_numeric_dtype(series):
        raise TypeError("Min-Max Scaling chỉ áp dụng cho dữ liệu số")

    min_val = series.min()
    max_val = series.max()

    if max_val == min_val:
        return series
    return (series - min_val) / (max_val - min_val)