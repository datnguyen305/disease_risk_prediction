import seaborn as sns
import matplotlib.pyplot as plt

def show(data, column_name):
    """Vẽ biểu đồ boxplot"""
    plt.figure(figsize=(8, 8))
    sns.boxplot(y=data[column_name])
    plt.title(f'Box Plot of {column_name}', fontsize=16)
    plt.ylabel(column_name, fontsize=12)
    plt.grid(axis='y', alpha=0.75)
    plt.show()