import pandas as pd
import datetime
from pandas_datareader import data, wb
import matplotlib.pyplot as plt
import numpy as np

# Set the plot style
plt.style.use('ggplot')

# Create datetime objects with start and end date
start = datetime.datetime(2012, 1,1)
end = datetime.datetime(2017, 1,1)

# Read XOM data from yahoo with the specified date range into a dataframe
df = data.DataReader("XOM", "yahoo", start, end)
print (df.head())

# Plot the column `Adj Close` (access it like a dictionary) with X-axis being the index column(Date here).
df['Adj Close'].plot()
#plt.show()

# print two columns
print df[['Open','High']]

# print column values into a list
print df['Open'].head().tolist()

# Convert numpy array to list of list
print np.array(df[['Open','High']]).tolist()

# Create a new Data frame
new_df = pd.DataFrame(np.array(df[['Open','High']]))
print new_df