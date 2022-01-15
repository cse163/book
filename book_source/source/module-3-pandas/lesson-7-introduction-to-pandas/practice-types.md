# <i class="far fa-edit fa-fw"></i> Practice: Types

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

```{snippet}
df['country']
```

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

`str`

_<i class="far fa-circle fa-fw"></i> Option 1_

`int`

_<i class="far fa-circle fa-fw"></i> Option 2_

`Series`

_<i class="far fa-circle fa-fw"></i> Option 3_

`list`

_<i class="far fa-circle fa-fw"></i> Option 4_

`DataFrame`

_<i class="far fa-circle fa-fw"></i> Option 5_

There is no type, this code causes an error.

## Question 1

What is the type of the following expression? If we stored the result of this expression in a variable, what is its type?

```{snippet}
df.loc[df['emissions'] > 100, ['emissions', 'city']]
```

**<i class="far fa-edit fa-fw"></i> class="far fa-edit fa-fw"></i> Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

`str`

_<i class="far fa-circle fa-fw"></i> Option 1_

`int`

_<i class="far fa-circle fa-fw"></i> Option 2_

`Series`

_<i class="far fa-circle fa-fw"></i> Option 3_

`list`

_<i class="far fa-circle fa-fw"></i> Option 4_

`DataFrame`

_<i class="far fa-circle fa-fw"></i> Option 5_

There is no type, this code causes an error.

## Question 2

What is the type of the following expression? If we stored the result of this expression in a variable, what is its type?

```{snippet}
df.loc[1, 'city':'country']
```

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

`str`

_<i class="far fa-circle fa-fw"></i> Option 1_

`int`

_<i class="far fa-circle fa-fw"></i> Option 2_

`Series`

_<i class="far fa-circle fa-fw"></i> Option 3_

`list`

_<i class="far fa-circle fa-fw"></i> Option 4_

`DataFrame`

_<i class="far fa-circle fa-fw"></i> Option 5_

There is no type, this code causes an error.

## Question 3

What is the type of the following expression? If we stored the result of this expression in a variable, what is its type?

```{snippet}
df.loc[3, 'emissions']
```

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

`str`

_<i class="far fa-circle fa-fw"></i> Option 1_

`int`

_<i class="far fa-circle fa-fw"></i> Option 2_

`Series`

_<i class="far fa-circle fa-fw"></i> Option 3_

`list`

_<i class="far fa-circle fa-fw"></i> Option 4_

`DataFrame`

_<i class="far fa-circle fa-fw"></i> Option 5_

There is no type, this code causes an error.
