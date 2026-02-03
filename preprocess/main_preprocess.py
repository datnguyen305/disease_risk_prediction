from checking_datatype import DataTypeChecker
from checking_missing_value import missing_value_checking
from Checking_duplicate_data import duplicate_checking
from checking_outlier import OutlierChecker
from metrics_of_spread import StatisticsAnalyzer
import pandas as pd 
if __name__ == "__main__":
    print("This is the IE313.preprocess package.")
    data = pd.read_csv('./dataset/health_lifestyle_dataset.csv')
    dtype_check = DataTypeChecker(data)
    dtype_check.check_column_types(show=True) 

    missing_check = missing_value_checking(data)
    missing_check.check_missing_values()

    duplicate_check = duplicate_checking(data)
    duplicate_check.check_duplicates()

    outlier_check = OutlierChecker(data)
    outlier_check.check_outlier(show=True)

    stats_analyzer = StatisticsAnalyzer(data)
    stats_analyzer.calculate_spread_metrics()

