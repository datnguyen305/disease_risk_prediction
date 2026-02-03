import pandas as pd

class StatisticsAnalyzer:
    """
    tính độ đo phân tán (metrics of spread)
    """

    def __init__(self, dataframe):
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Đối tượng phải là pandas dataFrame")
        self.numeric_df = dataframe.select_dtypes(include='number')
        print(f"Chọn {len(self.numeric_df.columns)} là cột dữ liệu số để phân tích.")

    def calculate_spread_metrics(self, show=True) -> pd.DataFrame:
        """
        Các độ đo bao gồm: Range, Variance, Standard Deviation
        """
        print("--- Tính toán các độ đo phân tán ---")

        # 1. Miền giá trị (Range) = Max - Min
        data_range = self.numeric_df.max() - self.numeric_df.min()

        # 2. Phương sai (Variance)
        variance = self.numeric_df.var()

        # 3. Độ lệch chuẩn (Standard Deviation)
        std_dev = self.numeric_df.std()

        # Tổng hợp kết quả
        spread_df = pd.DataFrame({
            'Range': data_range,
            'Variance': variance,
            'Std_Deviation': std_dev,
        })

        if show:
            print(spread_df)
        return spread_df