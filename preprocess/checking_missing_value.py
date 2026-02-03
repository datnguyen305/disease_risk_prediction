import pandas as pd

class missing_value_checking:
    def __init__(self, dataframe):
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Đối tượng phải là pandas dataFrame")
        self.df = dataframe
        self.results = {}

    def check_missing_values(self):
        """
        Kiểm tra các giá trị bị thiếu (missing values).
        """
        print("Start: Kiểm tra giá trị bị thiếu")
        total_rows = len(self.df)
        missing_count = self.df.isnull().sum()
        missing_percentage = (missing_count / total_rows)*100

        missing_df = pd.DataFrame({
            'count': missing_count,
            'percentage': missing_percentage
        })

        missing_df = missing_df[missing_df['count'] > 0]

        if missing_df.empty:
            print("--- Không có giá trị nào bị thiếu. ---")
            self.results['missing_values'] = "Không có giá trị nào bị thiếu"
        else:
            print(f"--- Tìm thấy {int(missing_df['count'].sum())} giá trị bị thiếu.---")
            self.results['missing_values'] = missing_df

if __name__ == "__main__":
        df = pd.read_csv('../dataset/health_lifestyle_dataset.csv')
        checker = missing_value_checking(df)
        missing_info = checker.check_missing_values()
