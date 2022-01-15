# numpy

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/b61cd3e801cd48f59b58d0c145ab97ab" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

The first three slides will go by a little fast because you should be mostly familiar with these ideas for `numpy` since they closely match the semantics of `pandas`. The last two reading slides will most likely be the more complex topics of this reading.

Like always, you get better at things with practice and we will continue to get practice with `numpy`!

## Overview

`numpy` is one of the most popular Python libraries that is used for numerical processing. We have used `numpy` (imported as `np`) a few times before, but this week we will really dive into how to use it.

`numpy`'s primary data structure is the `numpy.array`. An array will store a sequence of values **of the same type** . You can think of a `numpy.array` as being something a lot like a `pandas.Series`, but the index is always integer values like a `list`. The syntax to create one of these `numpy.array` s looks like the following.

```{snippet}
import numpy as np
x = np.array([1, 2, 3, 4])
print(x)

# If there are mixed types, it coerces values to the same type (int -> float)
x = np.array([3.14, 2, 3])
print(x)
```

Notice we are calling the function `np.array` passing in a list of values, the return type is a `numpy` class called an `ndarray` (stands for $n$-dimensional array).

## Applications

Any time you need to represent a series of numbers in Python, `numpy` is almost always the way to go because it is an incredibly efficient library for numerical computations. Just like we showed you that using built-in functions like `min` or `max` can significantly improve the speed of your programs, using `numpy` can do the same for numerical processing.

Some example applications include:

- Representing images (each pixel stores a value indicating color)

  - More complex representation where we make an `numpy.array` of `numpy.array`s.

```{image} https://static.us.edusercontent.com/files/5yqR3Z3mkqzYtYSuGzv30lej
:alt: Representing a black and white picture of a cute puppy using a 2-D numpy array.
:width: 743
:align: center
```

- Representing sound (each point in time shows an amplitude for a frequency)

```{image} https://static.us.edusercontent.com/files/hbAOHuHkTlpSkjtKfHKAZSjN
:alt: Representing sound waves using an 1-D numpy array.
:width: 743
:align: center
```

## Creating `numpy.array`s

We showed you how to create `numpy.array`s, but there are a few more helpful ones that are used commonly to make an array of any size.

```{snippet}
import numpy as np

# array initializer takes a list of values
x = np.array([1, 2, 3])

# arange works like range to make a array of number from start (inclusive)
# to stop (exclusive)
x = np.arange(1, 5)
print(x)

# Makes an array storing all 1s of the given length
x = np.ones(5)
print(x)
```
