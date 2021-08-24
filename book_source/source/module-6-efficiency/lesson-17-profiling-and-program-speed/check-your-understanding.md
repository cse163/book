# 🚧 Check your Understanding

## Question 0

Consider the task of trying to compute the sum of numbers between `1` and `n` . Which one of these implementations do you think is more likely to be the fastest one for a very large `n` ?  



**📝 Your Task**

Select 0 or more options. Write your answer down in your own space.

*❓ Option 0*

```python
def cumulative_sum(n):
    total = 0 
    for i in range(n + 1):
        total += i
    return total
```

 



*❓ Option 1*

```python
def cumulative_sum(n):
    return n * (n + 1) / 2
```

 



*❓ Option 2*

```python
def cumulative_sum(n):
    nums = [i for i in range(n + 1)]
    return sum(nums)
```



## Question 1

Which of the following are reasons data scientists tend to prefer Python over other programming languages like C or Java.  

Select all that apply  



**📝 Your Task**

Select 0 or more options. Write your answer down in your own space.

*❓ Option 0*

Python is generally a very fast language.  



*❓ Option 1*

Python tends to be easier to write/read for data scientists.  



*❓ Option 2*

Python can easily integrate with libraries that are written efficiently in C.  



*❓ Option 3*

Python can solve problems that C or Java cannot.  



