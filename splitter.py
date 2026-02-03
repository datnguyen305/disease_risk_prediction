from sklearn.model_selection import train_test_split
import os
import pandas as pd

class DataSplitter:
    def __init__(self, dataframe, target_column):
        self.df = dataframe
        self.target = target_column

    def split(self, test_size=0.2, random_state=42, exclude_columns=None, save_folder='processed_data'):
        """
        Chia dữ liệu và lưu file
        """
        print(f"-Đang chia dữ liệu (Test size: {test_size}) ")

        # Tách X và y
        X = self.df.drop(columns=[self.target])
        y = self.df[self.target]

        if exclude_columns:
            X = X.drop(columns=exclude_columns, errors='ignore')

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

        print(f"-> Kích thước Train: {X_train.shape}")
        print(f"-> Kích thước Test:  {X_test.shape}")

        # 2. LOGIC LƯU FILE CHẮC CHẮN
        if save_folder:
                full_path = os.path.abspath(save_folder)
                os.makedirs(full_path, exist_ok=True)

                print(f"Đang lưu file vào: {full_path}")

                # Lưu file
                X_train.to_csv(os.path.join(full_path, 'X_train.csv'), index=False)
                X_test.to_csv(os.path.join(full_path, 'X_test.csv'), index=False)

                # Lưu y (label)
                y_train.to_csv(os.path.join(full_path, 'y_train.csv'), index=False, header=[self.target])
                y_test.to_csv(os.path.join(full_path, 'y_test.csv'), index=False, header=[self.target])

                print("Đã lưu các files csv")

        return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    df = pd.read_csv('./health_lifestyle_dataset_zscore.csv')
    splitter = DataSplitter(dataframe=df, target_column='bmi')

    X_train, X_test, y_train, y_test = splitter.split(
        test_size=0.2,
        exclude_columns=['Person ID'],  # Thử loại bỏ cột ID
        save_folder='test_split_output'  # Lưu kết quả test vào đây
    )