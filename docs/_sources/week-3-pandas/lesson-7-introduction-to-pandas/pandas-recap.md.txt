# Pandas Recap
See, that was a ton of syntax! Don't worry though, you'll get plenty of practice with `pandas` over time, this is just your first day! For example, once I started getting better with `pandas` , I stopped using spreadsheets to calculate grades for courses because I got so much better at writing short little programs to compute the values I wanted!  
On this page, we have a "cheat-sheet" version of everything on the last slide. You'll likely find it to be a good reference! However, we still recommend trying to turn this into something of your own making to help solidify the concepts and help you build up a stronger mental model!  
```text
import pandas as pd

# Read a file
df = pd.read_csv('some_file.csv')

# Access a column
df['col']

# Summary statistic of column
df['col'].mean()

# Lots of summary functions to use
#   mean: Calculates the average value of the Series
#   min: Calculates the minimum value of the Series
#   max: Calculates the maximum value of the Series
#   idxmin: Calculates the index of the minimum value of the Series
#   idxmax: Calculates the index of the maximum value of the Series
#   count: Calculates the number values in the Series
#   unique: Returns a new Series with all the unique values from the Series

# Element-wise operations
df['col1'] + df['col2']

# Also works with single values
df['col'] // 2
df['col'] > 2

# Filter a DataFrame (& for and, | for or, ~ for not)
mask1 = df['col'] > 2
df[mask1]

mask2 = df['col2'] == 2
df[mask1 & mask2]
df[mask2 | ~mask1]

# Location: df.loc[row_indexer, column_indexer] (column_indexer is optional, default all)
# Indexers can be many types (can mix and match for row/col!): 
#   * List of values or a slice
#   * Mask
#   * : (for everything)
#   * Single value

# Single value
df.loc[0, 'col'] # Returns value

# List or slice of values
df.loc[[0, 2, 1], ['col1', 'col2']]  # Returns DataFrame
df.loc[0:4, 'col1':'col5']  # Returns DataFrame

# Everything
df.loc[:, :]  # DataFrame

# Other examples
df.loc[0]  # Series, default for column indexer is :
df.loc[0:5, 'col']  # Series
df.loc[1, 'col':'col' ] # Series
df.loc[0:5, ['col1', 'col2']] # DataFrame

````

 
 
