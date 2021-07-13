# None

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/2de919f01af04a5192a584c716a1b199?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Python has a special value in the language called
`None`
to represent the absence of a value. It is common to use
`None`
to represent a result of an invalid query without throwing an explicit error.

For example, suppose we had the following
`increment`
function that we decided should only increment positive values. You could write code to throw an error if it was given a negative value, but it's very common in Python to instead return this "missing value"
`None`
.

```py
def increment(x):
    """
    Returns the value of incrementing a non-negative value x by 1. 
    If x is negative, returns None.
    """
    if x < 0:
        return None
    else:
        return x + 1
    

print(increment(3))
print(increment(-3))
```

```{warning}
Remember: for your take-home assessments, you should always write your code with the main-method pattern. We omit that in most of our lecture readings to keep these snippets shorter.

```


`None`
should not be confused with the value
`0`
!
`0`
is a valid number in Python (i.e.
`1 + 0`
is well defined to be
`1`
) while
`None`
is the absence of a number all together! If you were to run
`1 + None`
it would cause an error since it doesn't make sense to add
`1`
to something that is entirely missing!

A very common error in Python comes from trying to manipulate a
`None`
value in such a way that causes an error like described in the last paragraph.

## 
		Checking for 
		

A very common task in Python is to check if a particular value is
`None`
or not. This is quite easy to do with the
`is`
keyword in Python.
`is`
and
`==`
are quite similar and in this context, you could use either. We will see in a later lecture the difference between
`is`
and
`==`
is and we'll understand why
`is`
is more common for comparing to
`None`
. For now just know that you use
`is`
for
`None`
checks and
`==`
for most other things.

```py
def increment(x):
    """
    Returns the value of incrementing a non-negative value x by 1. 
    If x is negative, returns None.
    """
    if x < 0:
        return None
    else:
        return x + 1
    
    
x = increment(-1)
if x is None:
    print('Failed')
else:
    print(x)

""" Alternatively you could write
if x is not None:
    print(x)
else:
    print('Failed')
"""
```

