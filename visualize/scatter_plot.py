import seaborn as sns
import matplotlib.pyplot as plt

def show(data, x_column, y_column):
    """Vẽ biểu đồ phân tán"""
    plt.figure(figsize=(10, 7))
    sns.scatterplot(x=x_column, y=y_column, data=data, alpha=0.6)
    plt.title(f'Scatter Plot: {y_column} vs. {x_column}', fontsize=16)
    plt.xlabel(x_column, fontsize=12)
    plt.ylabel(y_column, fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.show()