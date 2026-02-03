import seaborn as sns
import matplotlib.pyplot as plt

def show(data):
    """Vẽ biểu đồ nhiệt thể hiện ma trận tương quan."""
    correlation_matrix = data.corr()

    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix Heatmap', fontsize=16)
    plt.show()