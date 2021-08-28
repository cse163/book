#!/usr/bin/env python
# coding: utf-8

# # 🚧 Practice/Reading: Pandas Tutorial

# <div style="position: relative; padding-bottom: 62.5%; height: 0;">
#     <iframe src="https://www.loom.com/embed/1caa054531c24d39bb31bd44b646ba92" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
# </div>
# 
# ```{admonition} Jupyter Notebooks
# Reminder, that on this site the Jupyter Notebooks are read-only and you can't interact with them. Click the <i class="fas fa-rocket"></i> button above to launch
# an interactive version of this notebook.
# 
# * With Binder, you get a temporary Jupyter Notebook website that opens with this notebook. Any code you write will be lost when you close the tab. Make sure to download the notebook so you can save it for later!
# * With Colab, it will open Google Colaboratory. You can save the notebook there to your Google Drive. If you don't save to your Drive, any code you write will be lost when you close the tab. You can find the data files for this notebook below:
#   * {download}`tas.csv <./tas.csv>`
#   * {download}`emissions.csv <./emissions.csv>`
# 
# 
# You will need to run all the cells of the notebook to see the output. You can do this with hitting `Shift-Enter` on each cell or clickin the "Run All" button above.
# ```
# 
# The first thing we will do is use the `import` command to load the `pandas` library. We will use this syntax shown below to "rename" `pandas` to `pd` so in your cells below, we only have to write out `pd` whenever we want to use a `pandas` feature.

# In[1]:


import pandas as pd


# Next, we will load the data from the CSV file `tas.csv` that has the example data we were working with before. We will save it in a variable called `df` (stands for data frame which is a common `pandas` term). We do this with a provided function from `pandas` called `read_csv`.

# In[2]:


df = pd.read_csv('tas.csv')
df


# Notice that this shows the CSV in a tabular format! What is `df`? It's a `pandas` object called a **`DataFrame`** which stores a table of values, much like an Excel table. 
# 
# Notice on the top row, it shows the name of the columns (`Name` and `Salary`) and on the left-most side, it shows an index for each row (`0`, `1`, and `2`). 
# 
# `DataFrame`s are powerful because they provide lots of ways to access and perform computations on your data without you having to write much code! 
# 
# ## Accessing a Column
# For example, you can get all of the TAs' names with the following call.

# In[3]:


df['Name']


# `df['Name']` returns another `pandas` object called a **`Series`** that represents a single column or row of a `DataFrame`. A `Series` is very similar to a `list` from Python, but has many extra features that we will explore later.
# 
# Students sometimes get a little confused because this looks like `df` is a `dict` and it is trying to access a key named `Name`. This is not the case! One of the reasons Python is so powerful is it lets people who program libraries "hook into" the syntax of the language to make their own custom meaning of the `[]` syntax! `df` in this cell is really this special object defined by `pandas` called a `DataFrame`.
# 
# 
# ### Problem 0
# In the cell below, write the code to access the `Salary` column of the data and store it in a variable named `ans0`! **For testing purposes, your variable name has to exactly be `ans0`.**

# In[4]:


# Write your answer here!


# Now, `pandas` isn't useful just because it not only lets you access this data conveniently, but also perform computations on them. 
# 
# A `Series` object has many methods you can call on them to perform computation. Here is a list of some of the most useful ones:
# * `mean`: Calculates the average value of the `Series`
# * `min`: Calculates the minimum value of the `Series`
# * `max`: Calculates the maximum value of the `Series`
# * `idxmin`: Calculates the index of the minimum value of the `Series`
# * `idxmax`: Calculates the index of the maximum value of the `Series`
# * `count`: Calculates the number values in the `Series`
# * `unique`: Returns a new `Series` with all the unique values from the `Series`.
# * And many more!
# 
# For example, if I wanted to compute the average `Salary` of the TAs, I would write:

# In[5]:


average_salary = df['Salary'].mean()
average_salary


# 
# ### Reminder: Types matter
# When first learning `pandas`, it's easy to mix up `DataFrame` and `Series`. 
# * A `DataFrame` is a 2-dimensional structure (it has rows and columns like a grid)
# * `Series` is 1-dimensional (it only has "one direction" like a single row or a single column).
# 
# When you access a single column (or as we will see later, a single row) of a `DataFrame`, it returns a `Series`. 
# 
# ### Problem 1
# For this problem, you should compute the "range" of TA salaries (`the maximum value - the minimum value`). **For testing purposes, save the result in a variable called `ans1`.**
# 
# *Hint: You might need to make two separate calls to `pandas` to compute this since you need both the min and the max.*

# In[6]:


# Write your answer here!


# ## Element-wise Operations
# For the rest of this slide, let's consider a slightly more complex dataset that has a few more columns. This dataset tracks the emissions for cities around the world (but only has a few rows).

# In[7]:


df2 = pd.read_csv('emissions.csv')
df2


# If we wanted to access the emissions column, we could write:

# In[8]:


df2['emissions']


# Or if we wanted to access the population columm, we could write:

# In[9]:


df2['population']


# One useful feature of `pandas` is it lets you combine values from different `Series`. For example, if we wanted to, we could add the values of the emissions column and the population column.

# In[10]:


df2['emissions'] + df2['population']


# Notice, this returns a new `Series` that represents the sum of those two columns. The first value in the `Series` is the sum of the first values in the two that were added, the second is the sum of the second two, etc. It does not modify any of the columns of the dataset (you will need to do an assignment to change a value).
# 
# ### Problem 2
# In the cell below, find the maximum "emissions per capita" (emissions divided by population). Start by computing this value for each city and then find the maximum value of that `Series` (using one of the `Series` methods shown above). **For testing purposes, save the result in a variable called `ans2`.**
# 
# *Hint: You can save a `Series` in a variable! It's just like any other Python value!*

# In[11]:


# Write your answer here!


# These element-wise computations also work if a one of the values is a single value rather than a `Series`. For example, the following cell adds 4 to each of the populations. Notice this doesn't modify the original `DataFrame`, it just returns a new `Series` with the old values plus 4.

# In[12]:


df2['population'] + 4


# You can see here that the output of the `Series` actually tells you a bit about the values to help you out! The `dtype` property tells you the type of the data. In this case it uses a specialized integer type called `int64`, but for all intents and purposes that's really just like an `int`. As a minor detail, it also stores the Name of the column the `Series` came from for refernce.
# 
# Another useful case for something like this is to compare the values of a column to a value. For example, the following cell computes which cities have an emissions value of 200 or more. Notice that the `dtype` here is `bool` since each value is a `True/False`.

# In[13]:


df2['emissions'] >= 200


# ## Filtering Data 
# You might have wondered why being able to compare a `Series` to some value is something we deemed "useful" since it doesn't seem like it does anything helpful. The power comes from using this `bool` `Series` to **filter** the `DataFrame` to the rows you want.
# 
# For example, what if I wanted to print the names of the cities that have an emissions of 200 or more? I can use this `bool` `Series` to filter which rows I want! The syntax looks like the following cell.

# In[14]:


df3 = df2[df2['emissions'] >= 200]
df3['city']


# That's pretty cool how we can get this result without having to write any loops!
# 
# Notice the return value has type `DataFrame`, so we can than use the syntax we learned at the beginning to grab a single column from that `DataFrame` (thus returning a `Series`). 
# 
# 
# The way this works is the indexing-notation for `DataFrames` has special cases for which type of value you pass it.
# * If you pass it a `str` (e.g., `df2['emissions']`), it returns that column as a `Series`.
# * If you pass it a `Series` with `dtype=bool` (e.g., `df2[df2['emissions'] >= 200]`), it will return a `DataFrame` of all the rows that `Series` had a `True` value for!
# 
# There is no magic with this, they just wrote an if-statement in their code to do different things based on the type provided!
# 
# We commonly call a `Series` with `dtype=bool` used for this context a **mask**. It usually makes your program more readable to save those masks in a variable. The following cell shows the exact same example, but adding a variable for readability for the mask.

# In[15]:


high_emissions = df2['emissions'] >= 200
df3 = df2[high_emissions]
df3['city']


# ### Filtering on Multiple Conditions
# You can combine masks using logical operators to make complex queries. There are three logical operators for masks (like `and`, `or`, and `not` but with different symbols).
# * `&` does an element-wise `and` to combine two masks
# * `|` does an element-wise `or` to combine two masks
# * `~` does an element-wise `not` of a single mask
# 
# For example, if you want to find all cities that have high emissions or are in the US, you would probably try writing the following (but you'll run into a bug).
# 
# ```python
# df2[df2['emissions'] >= 200 | df2['country'] == 'USA']
# ```
# 
# The problem comes from **precedence** (order of operations). Just like how `*` gets evaluated before `+`, `|` gets evaluated first because it has the highest precedence (so does `&`). This makes Python interpret the first sub-expression as (`200 | df['country']`), which causes an error since this operator is not defined for these types.
# 
# Whenever you run into ambiguities from precedence, on way you can always fix it is to the sub-expressions in parentheses like in the following cell.

# In[16]:


df2[(df2['emissions'] >= 200) | (df2['country'] == 'USA')]


# A much more readable solution involves saving each mask in a variable so you don't have to worry about this precedence. This has an added benefit of giving each condition a human-readable name if you use good variable names!

# In[17]:


high_emissions = df2['emissions'] >= 200
is_usa = df2['country'] == 'USA'
df2[high_emissions | is_usa]


# ### Problem 3
# In the cell below, write code to select all rows from the dataset that are in France and have a population greater than 50. **For testing purposes, save the result in a variable called `ans3`**

# In[18]:


# Write your answer here!


# ## Location
# We've shown you how to select specific columns or select specific rows based on a mask. In some sense, it's a little confusiong that `df[val]` can be used to grab columns or rows depending on what is passed. This is because this syntax we have shown below, is really just special cases of a more generic syntax that lets you specific some location in the `DataFrame`. `pandas` provides this shorthand for convencience in some cases, but this more general syntax below works in many more!
# 
# In its most general form, the `loc` property lets you specify a **row indexer** and a **column indexer** to specify which rows/columns you want. The syntax looks like the following (where things in `<...>` are placeholders)
# 
# ```
# df.loc[<row indexer>, <column index>]
# ```
# 
# The row indexer refers to the index of the `DataFrame`. Recall, when we display a `DataFrame`, it shows values to the left of each row to identify each row in the `DataFrame`.
# 
# It turns out the the column indexer is optional, so you can leave that out. For example, if I want to get the first row (row with index 0), I could write:

# In[19]:


df2.loc[0]


# Interestingly, this actually returns a `Series`! It looks different than the `Series` returned from something like `df['name']` since now it has an index that are the column names themselves! This means I could index into a specifc column by doing something like:

# In[20]:


s = df2.loc[0]
s['city']


# Now this was a bit tedious to have to use double `[]` to acess the column as well, which is exactly why `loc` lets you specify a column as a "column indexer". Instead, it's more common to write:

# In[21]:


df2.loc[0, 'city']


# You might be wondering: I've used the word "indexer" a few times but haven't defined what that means! By indexer, I mean some value to indicate which rows/columns you want. So far, I have shown how to specify a single value as an indexer, but there are actually many options to chose from! You can always mix-and-match these and use different ones for the rows/cols.
# 
# ### List of indices and slices
# For example, you can use a list of values as an indexer to select many rows or many columns:

# In[22]:


df2.loc[[1,2,3], ['city', 'country', 'emissions']]


# Notice now it returns a `DataFrame` instead of a single value.
# 
# You can also use slice syntax like you could for `list`/`str` to access a range of values. There are a couple oddities about this:
# * The start/stop points are **both inclusive** which is different than for `list`/`str` where the stop point is exclusive.
# * They do some fancy "magic" that let you use ranges with strings to get a range of column names.
# 
# For example

# In[23]:


df2.loc[1:3, 'city':'emissions']


# The way to read this `loc` access is "all the rows starting at index 1 and to index 3 (both inclusive) and all the columns starting at city and going to emissions (both inclusive)".
# 
# How does it define the "range of strings"? It uses the order of the columns in the `DataFrame`.
# 
# ### Mask
# 
# You can also use a `bool` Series as an indexer to grab all the rows or columns that are marked `True`. This is similar to masking we saw before, but can now put the mask as a possible indexer.

# In[24]:


high_emissions = df2['emissions'] >= 200
is_usa = df2['country'] == 'USA'
df2.loc[high_emissions | is_usa]


# Notice in the last cell, I left out the column indexer and it gave me all the column (that is the default for the column indexer).
# 
# ### `:` for everything
# 
# Instead of relying on defaults, you can explicitly ask for "all of the columns" using the special range `:`. This is a common syntax for many numerical processing libraries so `pandas` adopts it too. It looks like the following

# In[25]:


df2.loc[[0, 4, 2], :]


# You can also do this for the rows as well! 

# In[26]:


df2.loc[:, 'city']


# A tip to help you read these in your head is to read `:` by itself as "all".
# 
# ### Recap Indexers
# So we saw the `.loc` property here is kind of like a universal way of asking your data. You can specify a row indexer and a column indexer to select your data. We saw the following things used as indexers:
# * A single value (row index for rows, column name for columns)
# * A list of values or a slice (row index for for rows, column names for columns)
# * A mask
# * `:` to select all values
# 
# 
# ### Return Values
# One thing that is also complex about `.loc` is the type of the value returns depends on the types of the indexers. Recall that a `pandas` `DataFrame` is a 2-dimensional strucutre (rows and columns) while a `Series` is a single `row` or single `column`.
# 
# To tell what the return type of a `.loc` call is, you need to look for the "single value" type of indexer.
# * If both the row and column indexers are a single value, returns a single value. This will be whatever the value is at the location so its type will be the same as the `dtype` of the column it comes from.
# * If only one of the row and colum indexers is a single value (meaning the other is multiple values), returns a `Series`.
# * If neither of the row and column indexers are single values (meaning both are multiple values), returns a `DataFrame`.
