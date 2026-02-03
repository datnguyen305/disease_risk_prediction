import numpy as np 
import pandas as pd

class DataTypeChecker:
    def __init__(self, data: pd.DataFrame) -> dict:
        self.data = data
    def check_column_types(self, show = True):
        """
        Check and print the data types of each column in the DataFrame.
        """
        df_dtype_mapping = {}
        for column, dtype in self.data.dtypes.items():
            df_dtype_mapping[column] = dtype

        # Show = True, display the data types
        if show:
            for column, dtype in df_dtype_mapping.items():
                print(f" - {column}: {self.data[column].head().values} ({dtype})")
        return df_dtype_mapping

if __name__ == "__main__":
    data = pd.read_csv('dataset/health_lifestyle_dataset.csv')
    check = DataTypeChecker(data)
    check.check_column_types(show=True)