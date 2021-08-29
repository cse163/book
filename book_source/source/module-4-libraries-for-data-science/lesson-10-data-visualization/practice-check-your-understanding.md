# <i class="far fa-edit fa-fw"></i> Practice: Check your understanding

*Make sure you read all instructions on this page* .

The following questions are here to help you test your understanding of the past reading so far!


## Question 0

Suppose I had this small dataset (shown below) in a variable called `df`. We want to only filter `df` so that we have all the data but the rows where `'C'` is `NaN`.

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

```text
df[df['C'] == np.nan]
```



*❓ Option 1*

```text
df.dropna()
```



*❓ Option 2*

```text
df[df['C'].notnull()]
```



*❓ Option 3*

```text
df[df['C'].notna()]
```



*❓ Option 4*

```text
df['C'].dropna()
```



