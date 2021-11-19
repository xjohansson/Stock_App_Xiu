import pandas as pd 
df=pd.read_csv("..\data\AAPL_TIME_SERIES_DAILY.csv")
print(df.head())

class StockDataLocal:
    """Class method to get and process local stock data"""

    def __init__(self, data_folder_path: str = "../data/") -> None:
        self._data_folder_path = data_folder_path

    def stock_dataframe(self, stockname: str) -> list:
        """Returns:list of two dataframes, one for daily time series, one for interdaily """
        stock_df_list = []

        for path_ending in ["_TIME_SERIES_DAILY.csv", "_TIME_SERIES_INTRADAY_EXTENDED.csv"]:
            path = self._data_folder_path + stockname + path_ending
            print(path)
            
