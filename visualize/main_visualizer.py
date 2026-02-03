import pandas as pd

from IE313.visualize import distribution_plot
from IE313.visualize import box_plot
from IE313.visualize import scatter_plot
from IE313.visualize import heatmap_plot
from IE313.visualize import histogram_plot
from IE313.visualize import column_plot

class Visualizer:
    """
    Class chính để điều phối việc vẽ các loại biểu đồ khác nhau.
    Mỗi loại biểu đồ được định nghĩa trong một file riêng.
    """
    def __init__(self, dataframe):
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Đối tượng truyền vào phải là một pandas DataFrame.")
        self.df = dataframe

        self.numeric_df = dataframe.select_dtypes(include='number')

    def show_distribution(self, column_name):
        """Gọi hàm vẽ biểu đồ phân phối từ file distribution_plot.py."""
        if column_name not in self.numeric_df.columns:
            print(f"Lỗi: Cột '{column_name}' không phải là dữ liệu number hoặc không tồn tại.")
            return
        print(f"biểu đồ phân phối cho cột '{column_name}'...")
        distribution_plot.show(self.numeric_df, column_name)

    def show_boxplot(self, column_name):
        """Gọi hàm vẽ biểu đồ boxplot từ file box_plot.py."""
        if column_name not in self.numeric_df.columns:
            print(f"Lỗi: Cột '{column_name}' không phải là dữ liệu number hoặc không tồn tại.")
            return
        print(f"biểu đồ boxplot cho cột '{column_name}'...")
        box_plot.show(self.numeric_df, column_name)

    def show_scatter(self, x_column, y_column):
        """Gọi hàm vẽ biểu đồ phân tán từ file scatter_plot.py."""
        if x_column not in self.numeric_df.columns or y_column not in self.numeric_df.columns:
            print(f"Lỗi: Cột '{x_column}' hoặc '{y_column}' không phải là dữ liệu số hoặc không tồn tại.")
            return
        print(f"Đang vẽ biểu đồ phân tán giữa '{x_column}' và '{y_column}'...")
        scatter_plot.show(self.numeric_df, x_column, y_column)

    def show_heatmap(self):
        """Gọi hàm vẽ biểu đồ nhiệt từ file heatmap_plot.py"""
        print("Biểu đồ nhiệt ma trận tương quan")
        heatmap_plot.show(self.numeric_df)

    def show_all_histograms(self):
        """Gọi hàm vẽ histogram cho tất cả các cột số."""
        print("histograms cho tất cả các cột số")
        histogram_plot.show(self.numeric_df)

    def show_column_plot(self, column_name):
        """
        Gọi hàm vẽ biểu đồ cột từ file column_plot.py
        """
        if column_name not in self.df.columns:
            print(f"Lỗi: Cột '{column_name}' không tồn tại trong dữ liệu.")
            return

        print(f"Biểu đồ cột cho '{column_name}'...")
        column_plot.show(self.df, column_name)

