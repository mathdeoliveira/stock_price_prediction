download_currency_data:
	cd data/raw && python ../../src/data_collect/collect_currencies_data.py

download_indices_data:
	cd data/raw && python ../../src/data_collect/collect_indices_data.py

download_stocks_data:
	cd data/raw && python ../../src/data_collect/collect_stocks_data.py

merge_data:
	cd data/raw && python ../../src/data_collect/merge_data.py

process_data:
	python src/data_process/process_data.py

run: download_currency_data download_indices_data download_stocks_data merge_data process_data