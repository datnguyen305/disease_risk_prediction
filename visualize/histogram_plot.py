import matplotlib.pyplot as plt

def show(data):
    """Vẽ biểu đồ histogram"""
    data.hist(bins=20, figsize=(15, 10), layout=(-1, 4), edgecolor='black')
    plt.suptitle('Histograms for All Numeric Columns', fontsize=18)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()