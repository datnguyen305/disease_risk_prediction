import numpy as np 
import pandas as pd

class OutlierChecker():
    def __init__(self, data: pd.DataFrame) :
        self.columns_needing_check = ['age', 
            'bmi', 
            'daily_steps', 'sleep_hours', 
            'water_intake_l', 'calories_consumed',
            'resting_hr', 'systolic_bp', 'diastolic_bp'
            ]
        self.data = data
    def check_outlier(self, show = True) -> dict:
        outliers = {}
        for column in self.columns_needing_check:
            Q1 = self.data[column].quantile(0.25)
            Q3 = self.data[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers[column] = self.data[(self.data[column] < lower_bound) | (self.data[column] > upper_bound)]
            if show:
                print(f"\nColumn: {column}")
                print(f"Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
                print(f"Lower bound: {lower_bound:.2f}, Upper bound: {upper_bound:.2f}")
                print(f"Number of outliers: {len(outliers[column])}")
        return outliers

if __name__ == "__main__":
    data = pd.read_csv('../dataset/health_lifestyle_dataset.csv')
    check = OutlierChecker(data)
    check.check_outlier(show=True)