import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def show(data):
    """Vẽ biểu đồ nhiệt thể hiện ma trận tương quan."""
    correlation_matrix = data

    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix Heatmap', fontsize=16)
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('../correlation_spearman.csv', index_col=0)
    show(df)
    df = pd.read_csv('../correlation_pearson.csv', index_col=0)
    show(df)