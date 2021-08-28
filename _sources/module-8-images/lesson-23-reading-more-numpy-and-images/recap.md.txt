# Recap

Last time, we introduced the idea of working with images with a new library called `numpy` . We learned lots of things about the `numpy` library like how to create, index into, and do arithmetic/logical operations with arrays. The code snippet below shows a quick recap of all these features that we discussed.  

While there can be a lot of syntax, the nice thing is a lot of it is fairly similar to `pandas` (since `pandas` was built on top of `numpy` ). It helps to relate what you are learning now to what you learned before. Additionally, the *key concepts* are the most important to come back to always. Whenever I write code that uses `numpy` , I always have to ask myself "What is the shape of the data I have right now?" and "How do I access or transform the data I have to the data I want?". I almost always need a pencil and paper by my side for me to draw out a sketch of the data I have and what I want to do with it.  

##  `numpy`   

```python
import numpy as np

# Create numpy arrays
x = np.array([1, 2, 3])
y = np.arange(6).reshape((2, 3))
z = np.ones((4, 5))

# Index into data
# For 1D array
print(x[0])
print(x[1:3])

# For 2D array
print(y[0, 1])
print(z[1:3, 3:5])

# Arithmetic/Logical Operators with single values
print(x + 3)
print(y < 5)

# Arithmetic/Logical Operators with multiple arrays
print(x + x)
print(x + y)  # Uses broadcasting!
```

##  Images  

We learned that images are most easily represented in Python as `numpy` arrays. The shape of the arrays are common:  

-  2-dimensional for grayscale images. The shape of the image will be     `(height, width)`     .  

-  3-dimensional for color images. The shape of the image will be     `(height, width, 3)`     where the inner-most dimension has shape 3 for each color channel RGB.  


In terms of code for working with images we've seen so far, all of it (besides the code to plot/save output) is simply just using the indexing or array modifications we saw above! So again, our advice of thinking carefully about the shape of the data you have and how to index into or transform it is always the most important thing.  

 

