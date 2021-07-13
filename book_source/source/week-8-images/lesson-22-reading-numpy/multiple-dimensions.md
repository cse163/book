# Multiple Dimensions

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/c88750e3a444434296bdcd0690052a77" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

As we alluded to in the applications above, it's possible to make a nested `numpy.array` (can think of it as an array of arrays). A core concept for a `numpy.array` is its **shape** . The shape determines the number of dimensions and how many elements are in one. The `numpy.ones` function actually takes a tuple specifying the shape instead of just a number.  
```py
import numpy as np

x = np.ones((3, 4))
print(x)
```

Notice how it prints out as an array of arrays. Since we passed in `(3, 4)` as the desired shape, it creates a `numpy.array` with 3 rows and 4 columns.  
You can also use the `reshape` function to transform an `numpy.array` from one shape to another. For example, we can use `reshape` to change a single-dimension array to one with two-dimensions. This will only work if the `numpy.array` you are reshaping has the same number of elements as the target shape; it would break if you had 3 values that you tried to reshape into a 10x10.  
```py
import numpy as np

# Create an array of the values 0 to 20 (exclusive)
x = np.arange(20)
print('Before reshape')
print(x)
print()

# Reshape it so it has dimensions 5x4 (5 rows, 4 columns) 
x = x.reshape((5, 4))
print('After reshape')
print(x)
```

##  Accessing Data  

When you have one of these 2D arrays, you can use syntax very similar to `pandas` ' `.loc` to access a particular row or column. You can even use the "slice" syntax from before to access multiple rows and columns.  
```py
import numpy as np

x = np.arange(20).reshape((5, 4))
print('x')
print(x)
print()

# Access one value
print('First - x[1, 2]')
print(x[1, 2])
print()

# Access a subset of the values
# Just like with lists/strs, a:b starts at a (inclusive) and goes to b (exclusive)
print('Second - x[2:4, 1:] ')
print(x[2:4, 1:])
print()

# Access an entire row
print('Third - x[3, :]')
print(x[3, :])  # Can also leave off the : at the end (default is :)
print()

# Access an entire column
print('Fourth - x[:, 2]')
print(x[:, 2])
```

##  Shape  

Since the shape of a `numpy.array` is so important, it is common that you will want to access them. The `numpy.array` has a property called `shape` that returns a `tuple` describing the shape of the array. If it returns `(a, b)` , that means its a 2D array with `a` rows and `b` columns.  
```py
import numpy as np

x = np.arange(4)

y = x.reshape((4, 1))

print('y.shape')
print(y.shape)
print()

print('y')
print(y)
print()

z = x.reshape((1, 4))
print('z.shape')
print(z.shape)
print()

print('z')
print(z)
```

Notice that `y` and `z` have different shapes since we specified the `reshape` differently. `y` has 4 rows and 1 column (which is why it prints "upright") while `z` has 1 row and 4 columns (which is why it prints on one line). If I wanted to get the value 2 from `y` or `z` , we would need to change how we index since you always specify row first then column. So for this example, it would be `y[2, 0]` and `z[0, 2]` .  
You might be wondering, what's the shape of `x` from the last example?  
```py
import numpy as np

x = np.arange(4)
print('x.shape')
print(x.shape)
print()

print('x')
print(x)
```

The way to read this shape is a `tuple` with one element inside of it (and that element is the value `4` ). This is because when we passed in number to `arange` , it returns an `numpy.array` with just one dimension! That means to access the value `2` , you would write `x[2]` (since you only need to specify one value). There are two analogies here:  
-  A 2D     `numpy.array`     is kind of like a     `pandas.DataFrame`     . You have to specify a row + column to get a single value. A 1D     `numpy.array`     is like a     `pandas.Series`     . You only need to specify the index to get a value.  
-  Think of an analogy to geometry. A 1D     `numpy.array`     with shape     `(4,)`     is like a line of length 4. A 2D     `numpy.array`     with shape     `(1, 4)`     is like a rectangle with height     `1`     and width     `4`     . Since the line only has one dimension, you just have to specify one value to indicate a position.  

 
