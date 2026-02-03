from min_max import apply as min_max_scale
from z_score import Z_score
from one_hot_encode import apply as one_hot_encode

def standardize_dataframe(df, numeric_columns=None, categorical_columns=None, method='min-max'):
    """
    Chuẩn hóa DataFrame bằng các phương pháp khác nhau cho cột số và mã hóa one-hot cho cột phân loại.
    
    Tham số:
    df: pd.DataFrame - DataFrame cần chuẩn hóa
    numeric_columns: list - Danh sách tên cột số cần chuẩn hóa
    categorical_columns: list - Danh sách tên cột phân loại cần one-hot encode
    method: str - Phương pháp chuẩn hóa ('min-max' hoặc 'z-score')
    
    Trả về:
    pd.DataFrame - DataFrame đã được chuẩn hóa và mã hóa
    """
    import pandas as pd
    df_standardized = df.copy()

    # Tự động phát hiện cột số nếu không truyền vào
    if numeric_columns is None:
        numeric_columns = df_standardized.select_dtypes(include=['number']).columns.tolist()

    # Tự động phát hiện cột phân loại nếu không truyền vào
    if categorical_columns is None:
        categorical_columns = df_standardized.select_dtypes(include=['object', 'category']).columns.tolist()

    # Chuẩn hóa các cột số
    for col in numeric_columns:
        if col in df_standardized.columns:
            if method == 'min-max':
                df_standardized[col] = min_max_scale(df_standardized[col])
            elif method == 'z-score':
                df_standardized[col] = Z_score(df_standardized[col])
            else:
                raise ValueError("Phương pháp chuẩn hóa không hợp lệ. Chọn 'min-max' hoặc 'z-score'.")

    # One-Hot Encode các cột phân loại
    for col in categorical_columns:
        if col in df_standardized.columns:
            df_standardized = one_hot_encode(df_standardized, col)

    return df_standardized

if __name__ == "__main__":
    import pandas as pd

    # Ví dụ sử dụng
    data = pd.read_csv('dataset/health_lifestyle_dataset.csv')
    standardized_data = standardize_dataframe(data, method='z-score')
    standardized_data.to_csv('health_lifestyle_dataset_zscore.csv', index=False)
    print("DataFrame đã được chuẩn hóa Z-Score và lưu thành công.")

    standardize_data = standardize_dataframe(data, method='min-max')
    standardize_data.to_csv('health_lifestyle_dataset_minmax.csv', index=False)
    print("DataFrame đã được chuẩn hóa Min-Max và lưu thành công.")