# Lambdas

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/864c9a4d3dcd48b4b86e6dca7d101835?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Recall earlier in the quarter when we were learning
`pandas`
, we learned that the
`apply`
function could take a function as another parameter! Instead of talking about
`pandas`
, we will simplify this to write our own
`apply_fun`
function that does something similar to a list of values. It takes a list of values and another function as a parameter, and returns a new list that is the result of applying the given function to each element in the input list.

```py
def apply_fun(values, function):
    # Use a list comprehension to apply function to each value
    return [function(v) for v in values]

def times_two(x):
    return 2 * x

numbers = [i for i in range(10)]
print('numbers  :', numbers)
print('times two:', apply_fun(numbers, times_two))
```

Notice that in this example, we treat the
`function`
parameter just like any other parameter, but we are now using it as a function to call (because we are saying the client passes in a function).

It's a bit tedious that we have to write out a whole function called
`times_two`
just so we can pass it in as a parameter. Multiplying something by two should be simple enough so it would be nice if there were a way to use a short-hand to do this for simple operations.

Enter the
**lambda**
(commonly called an
<Element 'italic' at 0x7fcd237565e0>
). The idea behind a lambda is to let you specify a function without needing to go through the whole
`def`
syntax. This works best for very simple operations. Below is an example showing how to do this with our
`apply_fun`
.

```py
def apply_fun(values, function):
    # Use a list comprehension to apply function to each value
    return [function(v) for v in values]

numbers = [i for i in range(10)]
print('numbers  :', numbers)
print('times two:', apply_fun(numbers, lambda v: 2 * v))
```

Notice instead of passing a function named
`times_two`
as the second parameter, we pass
`lambda v: 2 * v`
. The
`lambda`
keyword defines a new function without giving it a name (hence,
<Element 'italic' at 0x7fcd26041900>
). The way to read this is it is a function that takes a single parameter
`v`
and it returns the value of
`2 * v`
. This is essentially just short-hand for the previous example, with the benefit that we don't have to define a whole function called
`times_two`
to do this.

By design, it is very difficult to do something more complex than a one-line expression inside a
`lambda`
since it is meant to be a super quick-and-easy way of defining functions for simple operations.

## An Application: Sorting

One of the most common places
`lambdas`
show up is for sorting values. Suppose we wanted to use  our
`Dog`
class to make a
`list`
of
`Dog`
s. Additionally, suppose I wanted to sort them by their name (alphabetically). There is a function in Python call
`sorted`
that sorts a list of values and returns a new list that has all the values of  the input in sorted order.

```py
class Dog:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


dogs = [Dog('Bella'), Dog('Scout'), Dog('Chester')]
dogs = sorted(dogs)

# Should print in sorted order!
for dog in dogs:
    print(dog.get_name())
```

This runs into a bug though, because Python doesn't know how we want to sort the
`Dog`
objects! There are ways to define how to compare
`Dog`
s, which we will see briefly on Friday's lesson.

However, a common work-around is to use an optional parameter for the
`sorted`
function named
`key`
. The value of
`key`
should a function that takes a single element of the list and returns a value that Python knows how to sort (like a number of a
`str`
); this way Python will sort the
`Dog`
s based on the value that results from their
`key`
function.

So to do this in our example, we need to pass a function as the
`key`
to transform each
`Dog`
into its name so that we can sort it by their name. This is very easy to do with a
`lambda`
!

```py
class Dog:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


dogs = [Dog('Bella'), Dog('Scout'), Dog('Chester')]
dogs = sorted(dogs, key=lambda d: d.get_name())

# Should print in sorted order!
for dog in dogs:
    print(dog.get_name())
```

The way this works is in the sorting algorithm, instead of comparing the
`Dog`
s themselves, the algorithm compares the results of applying
`key`
to each
`Dog`
so it is sorted by
`key`
. The power of this comes from if your class had multiple things that you might want to sort by. You could now tell the
`sorted`
function how you want them to be sorted by passing in different
`key`
functions each time!

