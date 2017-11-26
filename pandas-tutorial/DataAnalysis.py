import pandas as pd
import sys

# Setting Pandas display options
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

'''
url = 'https://simple.wikipedia.org/wiki/List_of_U.S._states'

df = pd.read_html(url)
print df[0][0]


#slicing
for abbv in df[0][0][1:] :
    print str(abbv)


#Merging DataFrames 
pd.merge(df1, df2, on=[])

'''

# Read from wikipedia
canon_cameras_comparison_url = 'https://en.wikipedia.org/wiki/Comparison_of_Canon_EOS_digital_cameras'
dfs = pd.read_html(canon_cameras_comparison_url)

# Read the first dataframe from list of dataframes
df = dfs[0]

# Set columns to take values from first row
df.columns = df.iloc[0]

# Drop first record
df = df[1:]

# Filter rows based on models
filtered_df = df[df['Model'].isin(['5D Mk IV', '800D Rebel T7i', '6D Mk II', '7D Mk II', '70D', '80D'])]

'''
Converting default encoding to utf-8
'''
reload(sys)
sys.setdefaultencoding('gbk')
# Write to html
filtered_df.to_html('comparison.html', header=True, index=False)
