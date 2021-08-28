# 🚧 Practice: Types

Consider the emissions dataset from the earlier slide. We have put an image of the dataset below as a reminder.  

```{image} https://static.us.edusercontent.com/files/rJ5l2H3MwTkBcJxIDhaYtapL
:alt: TODO
:width: 742
:align: center
```

The following questions are all multiple-choice questions about queries on this dataset. Assume the dataset is stored in a variable named `df` .  

Notice that in all of these questions, we are asking about the type of the value resulting from that expression, and **not** its `dtype` (the type of the values inside it).  

## Question 0

What is the type of the following expression? If we stored the result of this expression in a variable, what is its type?  

```python
df['country']
```



**📝 Your Task**

Select one option. Write your answer down in your own space.

*❓ Option 0*

`str`  



*❓ Option 1*

`int`  



*❓ Option 2*

`Series`  



*❓ Option 3*

`list`  



*❓ Option 4*

`DataFrame`  



*❓ Option 5*

There is no type, this code causes an error.  



## Question 1

What is the type of the following expression? If we stored the result of this expression in a variable, what is its type?  

```python
df.loc[df['emissions'] > 100, ['emissions', 'city']]
```



**📝 Your Task**

Select one option. Write your answer down in your own space.

*❓ Option 0*

`str`  



*❓ Option 1*

`int`  



*❓ Option 2*

`Series`  



*❓ Option 3*

`list`  



*❓ Option 4*

`DataFrame`  



*❓ Option 5*

There is no type, this code causes an error.  



## Question 2

What is the type of the following expression? If we stored the result of this expression in a variable, what is its type?  

```python
df.loc[1, 'city':'country']
```



**📝 Your Task**

Select one option. Write your answer down in your own space.

*❓ Option 0*

`str`  



*❓ Option 1*

`int`  



*❓ Option 2*

`Series`  



*❓ Option 3*

`list`  



*❓ Option 4*

`DataFrame`  



*❓ Option 5*

There is no type, this code causes an error.  



## Question 3

What is the type of the following expression? If we stored the result of this expression in a variable, what is its type?  

```python
df.loc[3, 'emissions']
```



**📝 Your Task**

Select one option. Write your answer down in your own space.

*❓ Option 0*

`str`  



*❓ Option 1*

`int`  



*❓ Option 2*

`Series`  



*❓ Option 3*

`list`  



*❓ Option 4*

`DataFrame`  



*❓ Option 5*

There is no type, this code causes an error.  



