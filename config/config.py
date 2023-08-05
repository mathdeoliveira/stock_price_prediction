import datetime

# # Data collect
# JPMorgan Chase & Co. (Segmento: Bancos) Ticker: JPM
# Bank of America Corporation (Segmento: Bancos) Ticker: BAC
# Wells Fargo & Company (Segmento: Bancos) Ticker: WFC
tickers = ["JPM", "BAC", "WFC"]
currencies = ["DEXUSUK", "DEXUSEU"]
fred_source = "fred"
indices = ["SP500", "DJIA", "VIXCLS"]
start_date = datetime.datetime(2010, 1, 1)
end_date = datetime.datetime(2023, 10, 23)
collected_data_db = "collect_data.sqlite"
columns_drop = ["Date", "Date_x", "Date_y"]
date_to_index = "Date"

# Treinamento
validation_size = 0.3
num_folds = 10
scoring = "neg_mean_squared_error"
