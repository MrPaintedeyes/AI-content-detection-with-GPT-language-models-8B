# DOCUMENTATION: pulled data using the tool from 
# #https://github.com/ranaroussi/yfinance/blob/main/README.md#installation git that leverages the Yahoo! API

# importing the needed packages
import yfinance as yf
import os

# setting up the stock to monitor
stock_name = 'GOOGL'

# creating a folder where storing csv file with our data
os.makedirs('data')

# collecting stock price data from yahoo finance within the last full 10 years
stock_data = yf.download(stock_name, start="2014-01-01", end="2023-12-31")

# saving data in a csv file where indicated by stock_data_file_path
stock_data_file_path = os.path.join('data', f'{stock_name}_stock_data.csv')
stock_data.to_csv(stock_data_file_path)

# printing control message
print(f'Stock data for {stock_name} saved to {stock_data_file_path}')
