# numpy functions

Consider the case where you have a `numpy.array` and want to find the sums of the values. One way to do this is to write a loop over the array since arrays support iteration and it also supports the `len` function. For example, you could write this solution in two ways:  
```python
import numpy as np

x = np.arange(10)

# Option 1: Indexing with range
result = 0
for i in range(len(x)):
    result += x[i]
print(result)

# Option 2: Iterating over array
result = 0
for val in x:
    result += val
print(result)
```

While this works, remember that whenever possible you want to avoid using loops since Python is slow. Conveniently, `numpy` provides a `sum` function to take the sum for us. Like with `pandas` , this `numpy` code is written in that fast language C, so calling out to that is incredibly fast. Kind of confusingly, there are two common ways to call `sum` that are essentially equivalent. We show both since you will probably run into both.  
```python
import numpy as np

x = np.arange(10)

# Option 1: Call it on the array
result = x.sum()
print(result)

# Option 2: Call it on numpy
result = np.sum(x)
print(result)
```

Just like `sum` , `numpy` also provides functions for `min` , `max` , and `mean` which are also commonly used.  
