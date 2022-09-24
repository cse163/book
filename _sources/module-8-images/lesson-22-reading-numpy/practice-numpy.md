# <i class="far fa-edit fa-fw"></i> Practice: numpy

The following questions will give you a chance to practice the new information and syntax you just saw about `numpy`. You should try to do these all by hand using your understanding of the material, and you should try to avoid plugging these into your computer.

Recall that learning a new library can be a daunting task since there is just so much information! You have a lot of experience learning libraries, so hopefully, this time is easier since you can rely on your past experience with `pandas`.

## Question 0

What is the shape of the following `numpy.array`?

```python
np.arange(14)
```

Including the formatting of the `tuple` , but do not include spaces. For example, if it is a tuple of length 1 write something like `(4,)` and if it is a tuple of length 2, write something like `(1,2)`. There should be no spaces in your answer.

**<i class="far fa-edit fa-fw"></i> Your Task**

Write your answer down in your own space.

## Question 1

What is the shape of `m` in the following code block?

```python
x = np.arange(20).reshape((4, 5))
m = x / 2 + 1
```

Including the formatting of the `tuple` , but do not include spaces. For example, if it is a tuple of length 1 write something like `(4,)` and if it is a tuple of length 2, write something like `(1,2)`.

**<i class="far fa-edit fa-fw"></i> Your Task**

Write your answer down in your own space.

## Question 2

What is the shape of `m` in the following code block?

```python
x = np.arange(20).reshape((4, 5))
m = x[1:, 2:4]
```

Including the formatting of the `tuple` , but do not include spaces. For example, if it is a tuple of length 1 write something like `(4,)` and if it is a tuple of length 2, write something like `(1,2)`. There should be no spaces in your answer.

**<i class="far fa-edit fa-fw"></i> Your Task**

Write your answer down in your own space.

## Question 3

Suppose we had a `numpy.array` named `x` with some sequence of values. For this problem, assume we are not allowed to use the `!=` comparison (even though that's a totally valid approach).

Which of the following options will help us select all the values in `x` that are greater than 10 and are not divisible by 3?

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

`x[x > 10 and not x % 3 == 0]`

_<i class="far fa-circle fa-fw"></i> Option 1_

`x[(x > 10) and not x % 3 == 0]`

_<i class="far fa-circle fa-fw"></i> Option 2_

`x[x > 10 & ~x % 3 == 0]`

_<i class="far fa-circle fa-fw"></i> Option 3_

`x[(x > 10) & ~(x % 3 == 0)]`

## Question 4

Now that we have learned about `numpy`, we can now explore the return value from `plt.subplots`. The return for the `Axes` is really a `numpy.array` of the given shape where each value is an `Axes` object!

For example, if we made a `subplots` using the following line, it would produce the figure below.

```text
fig, axs = plt.subplots(3, 4)
```

```{image} https://static.us.edusercontent.com/files/4sJPr39zfQ9hSrsobUDRuc19
:alt: A grid of axes objects with 3 rows and 4 columns, with the first row of axes being named ax1, ax2, ax3, ax4, and the remaining rows named accordingly in sequence.
:width: 691
:align: center
```

Where we have labeled each `Axes` in the variable `axs` as if we had unpacked it into the individual variables

```text
fig, [[ax1, ax2, ax3, ax4], [ax5, ax6, ax7, ax8], [ax9, ax10, ax11, ax12]] = plt.subplots(3, 4)
```

You can tell that as there are more plots, trying to unpack each `Axes` to a variable from the returned `numpy.array` is unwieldy. Instead, for large plots, it's common to just store the result in a variable `axs` and index into it.

Suppose we wanted to draw on `ax7` in the picture above. Which access to `axs` would give us a reference to that `Axes` object?

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

`axs[0, 0]`

_<i class="far fa-circle fa-fw"></i> Option 1_

`axs[0, 1]`

_<i class="far fa-circle fa-fw"></i> Option 2_

`axs[0, 2]`

_<i class="far fa-circle fa-fw"></i> Option 3_

`axs[0, 3]`

_<i class="far fa-circle fa-fw"></i> Option 4_

`axs[0, 4]`

_<i class="far fa-circle fa-fw"></i> Option 5_

`axs[1, 0]`

_<i class="far fa-circle fa-fw"></i> Option 6_

`axs[1, 1]`

_<i class="far fa-circle fa-fw"></i> Option 7_

`axs[1, 2]`

_<i class="far fa-circle fa-fw"></i> Option 8_

`axs[1, 3]`

_<i class="far fa-circle fa-fw"></i> Option 9_

`axs[1, 4]`
