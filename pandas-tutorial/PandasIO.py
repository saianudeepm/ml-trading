# using data from https://www.quandl.com/data/ZILLOW/Z94538_MLPAH-Zillow-Home-Value-Index-Zip-Median-Listing-Price-All-Homes-94538-Fremont-CA
import os
import pandas as pd



current_path = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(current_path, "../data/ZILLOW-Z94538_MLPAH.csv")

df = pd.read_csv(input_file_path)
'''
Reading a file as CSV
df = pd.read_csv(input_file_path, index_col=0) #set index column while reading into df
df = pd.read_csv(input_file_path, names=['Date', 'Fremont_HPI'], index_col=0)  # read with column header names and set index column
df.set_index('Date', inplace=True) # set the index permenantly modifying the dataframe
'''
print df.head

'''
Write to a file
df.to_csv('output.csv')
df.to_html('test.html') # convert to html table data
'''

'''
Rename columns
df2 = pd.read_csv(input_file_path)
df2.rename(columns={'Value': 'Fremont_HPI'}, inplace=True)
'''

