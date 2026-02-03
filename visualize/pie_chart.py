import matplotlib.pyplot as plt
import pandas as pd
import warnings


def show_pie_chart(
    data,
    column_name,
    bins=5,
    min_percent=2,
    min_other_percent=3
):
    """
    Vẽ pie chart cho 1 cột trong DataFrame

    - Categorical: vẽ trực tiếp
    - Numeric: tự động gom nhóm (binning)
    - min_percent: gộp các lát nhỏ hơn % vào 'Others'
    - min_other_percent: nếu 'Others' < % này → ẩn luôn
    - Không hiện warning
    """

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        # Kiểm tra cột
        if column_name not in data.columns:
            print(f"Cột '{column_name}' không tồn tại.")
            return

        col_data = data[column_name].dropna()

        # ===== Xử lý dữ liệu =====
        if pd.api.types.is_numeric_dtype(col_data):
            labels = pd.cut(col_data, bins=bins)
            counts = labels.value_counts().sort_index()
            title_suffix = f"(Gom {bins} nhóm)"
        else:
            counts = col_data.value_counts()
            title_suffix = ""

        total = counts.sum()
        percents = counts / total * 100

        # ===== Gộp lát nhỏ =====
        small_mask = percents < min_percent
        if small_mask.any():
            others_sum = counts[small_mask].sum()
            others_percent = others_sum / total * 100

            counts = counts[~small_mask]

            # 👉 Chỉ thêm Others nếu nó đủ lớn
            if others_percent >= min_other_percent:
                counts['Others'] = others_sum

        # ===== Plot =====
        plt.figure(figsize=(8, 8))
        plt.pie(
            counts,
            labels=counts.index.astype(str),
            autopct='%1.1f%%',
            startangle=90,
            counterclock=False
        )
        plt.title(f'Pie Chart of {column_name} {title_suffix}', fontsize=14)
        plt.tight_layout()
        plt.show()
