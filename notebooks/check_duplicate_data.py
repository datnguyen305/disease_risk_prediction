import pandas as pd

class duplicate_checking:
    """
    thực hiện các bước kiểm tra cơ bản trên một DataFrame
    """
    def __init__(self, dataframe):
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Đối tượng truyền vào phải là một pandas DataFrame.")
        self.df = dataframe
        self.results = {}

    def check_duplicates(self):
        """
        Kiểm tra số lượng các dòng bị trùng lặp nếu có.
        """
        print("\nStart: kiểm tra dữ liệu trùng lặp")
        duplicate_count = self.df.duplicated().sum()

        if duplicate_count == 0:
            print("=>--- Không có dòng nào bị trùng lặp ---")
        else:
            print(f"--- Tìm thấy {duplicate_count} dòng bị trùng lặp ---")

        self.results['duplicate_rows'] = duplicate_count