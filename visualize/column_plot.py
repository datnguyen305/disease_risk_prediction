import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def show(data, column_name, bins=5):
    """
    Vẽ biểu đồ cột, gom nhóm (binning) cho dữ liệu số
    """
    # Kiểm tra cột tồn tại
    if column_name not in data.columns:
        print(f"Cột '{column_name}' không tìm thấy.")
        return

    plt.figure(figsize=(12, 6))

    # Gom nhóm
    plot_data = data.copy()
    x_axis = column_name

    if pd.api.types.is_numeric_dtype(data[column_name]):
        x_axis = f"{column_name}_groups"
        # pd.cut sẽ chia dữ liệu thành 'bins' khoảng bằng nhau
        plot_data[x_axis] = pd.cut(data[column_name], bins=bins)
        print(f"-> Đã gom '{column_name}' thành {bins} nhóm.")

    if pd.api.types.is_numeric_dtype(data[column_name]) and bins is None:
        # Số (không gom nhóm): Sắp xếp theo giá trị
        order = sorted(plot_data[x_axis].unique())
    elif bins is not None:
        order = sorted(plot_data[x_axis].unique().astype(str))
        order = None
    else:
        # cột chữ
        order = plot_data[x_axis].value_counts().index

    # Vẽ biểu đồ
    sns.countplot(x=x_axis, data=plot_data, order=order, palette='viridis')

    # Tính skewness
    skew_text = ""
    if pd.api.types.is_numeric_dtype(data[column_name]):
        skew_val = data[column_name].skew()
        meaning = ""
        if skew_val > 1:
            meaning = "(Lệch phải)"
        elif skew_val < -1:
            meaning = "(Lệch trái)"
        elif -0.5 <= skew_val <= 0.5:
            meaning = "(Đối xứng)"
        skew_text = f"\nSkewness (Gốc): {skew_val:.2f} {meaning}"

    # Trang trí
    plt.title(f'Plot of {column_name} {("(Gom " + str(bins) + " nhóm)") if bins else ""}{skew_text}', fontsize=14)
    plt.xlabel(x_axis, fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
