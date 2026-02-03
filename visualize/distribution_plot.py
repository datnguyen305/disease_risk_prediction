import seaborn as sns
import matplotlib.pyplot as plt

def show(data, column_name):
    """Vẽ biểu đồ phân phối"""
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column_name], kde=True, bins=30)
    plt.title(f'Distribution of {column_name}', fontsize=16)
    plt.xlabel(column_name, fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(axis='y', alpha=0.75)
    plt.show()