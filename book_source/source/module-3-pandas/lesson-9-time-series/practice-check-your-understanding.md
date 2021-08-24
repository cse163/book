# 🚧 Practice: Check your understanding

*Make sure you read all instructions on this page* .  

The following questions are here to help you test your understanding of the past reading so far!  


```{admonition} Warning
:class: warning

Completing this quiz requires getting the answers right, but you have multiple attempts!

```

 

## Question 0

Suppose I had this small dataset (shown below) in a variable called `df` . We want to only filter `df` so that we have all the data but the rows where `'C'` is `NaN` .  

Which of the following methods successfully filters this dataset as described?  


| A | B | C |
|--:|--:|--:|
|  1|  2|NaN|
|  3|NaN|  4|
|  5|  6|NaN|
|NaN|  7|  8|
|  9| 10| 11|



**📝 Your Task**

Select one option. Write your answer down in your own space.

*❓ Option 0*

```python
df[df['C'] == np.nan]
```



*❓ Option 1*

```python
df.dropna()
```



*❓ Option 2*

```python
df[df['C'].notnull()]
```



*❓ Option 3*

```python
df[df['C'].notna()]
```



*❓ Option 4*

```python
df['C'].dropna()
```



## Question 1

Suppose we had the same dataset as the previous problem but all the `NaN` values have been replaced with the number 0.  

 

**True or false:** The following code cell prints out the data in sorted order according to column `'A'` .  

```python
df.sort_values('A')
print(df)
```



**📝 Your Task**

Write your answer down in your own space.

