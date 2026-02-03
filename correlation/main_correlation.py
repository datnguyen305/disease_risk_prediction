import pandas as pd
import numpy as np  

def calc_correlation(df: pd.DataFrame, method: str = 'pearson', save_path: str = None) -> pd.DataFrame:    
    """
    Tính ma trận tương quan cho DataFrame với phương pháp bất kỳ:
    - 'pearson'
    - 'spearman'
    - 'kendall'

    Args:
        df (pd.DataFrame): dữ liệu đầu vào
        method (str): loại correlation ('pearson', 'spearman', 'kendall')
        save_path (str): đường dẫn để lưu file CSV (optional)

    Returns:
        pd.DataFrame: bảng correlation matrix
    """
    df_numeric = df.select_dtypes(include=[np.number])
    if method not in ['pearson', 'spearman', 'kendall']:
        raise ValueError("Method phải là 'pearson', 'spearman' hoặc 'kendall'.")
    corr = df_numeric.corr(method=method)
    if save_path:
        corr.to_csv(save_path)
    return corr
if __name__ == "__main__":
    df = pd.read_csv('./dataset/health_lifestyle_dataset.csv')
    print("Tính ma trận tương quan với phương pháp Pearson:")
    corr_matrix = calc_correlation(df, method='pearson', save_path='correlation_pearson.csv')
    print("Đã Lưu ma trận tương quan Pearson vào './results/correlation_pearson.csv'")
    corr_matrix = calc_correlation(df, method='spearman', save_path='correlation_spearman.csv')
    print("Đã Lưu ma trận tương quan Spearman vào './results/correlation_spearman.csv'")
