import pandas as pd
import datetime
from pandas_datareader import data, wb
import matplotlib.pyplot as plt

# Set the plot style
plt.style.use('ggplot')

# Create datetime objects with start and end date
start = datetime.datetime(2012, 1,1)
end = datetime.datetime(2017, 1,1)

# Read XOM data from yahoo with the specified date range into a dataframe
df = data.DataReader("XOM", "yahoo", start, end)
print (df.head())