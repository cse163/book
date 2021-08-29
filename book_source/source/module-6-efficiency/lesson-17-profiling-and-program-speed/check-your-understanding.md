# <i class="far fa-edit fa-fw"></i> Check your Understanding

## Question 0

Consider the task of trying to compute the sum of numbers between `1` and `n` . Which one of these implementations do you think is more likely to be the fastest one for a very large `n` ?

**📝 Your Task**

Select one or more options. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

```python
def cumulative_sum(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
```

_<i class="far fa-circle fa-fw"></i> Option 1_

```python
def cumulative_sum(n):
    return n * (n + 1) / 2
```

_<i class="far fa-circle fa-fw"></i> Option 2_

```python
def cumulative_sum(n):
    nums = [i for i in range(n + 1)]
    return sum(nums)
```

## Question 1

Which of the following are reasons data scientists tend to prefer Python over other programming languages like C or Java.

Select all that apply

**📝 Your Task**

Select one or more options. Write your answer down in your own space.

_<i class="far fa-square fa-fw"></i> Option 0_

Python is generally a very fast language.

_<i class="far fa-square fa-fw"></i> Option 1_

Python tends to be easier to write/read for data scientists.

_<i class="far fa-square fa-fw"></i> Option 2_

Python can easily integrate with libraries that are written efficiently in C.

_<i class="far fa-square fa-fw"></i> Option 3_

Python can solve problems that C or Java cannot.
