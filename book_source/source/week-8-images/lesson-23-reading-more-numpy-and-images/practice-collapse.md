# 🚧 Practice: Collapse

{download}`Download starter code </week-8-images/lesson-23-reading-more-numpy-and-images/practice-collapse.zip>`

Write a function called `collapse` that takes a **grayscale**  **image** as a parameter and returns the result of "collapsing" each row down to a single column that represents the sum of all the values in that row. The input shape of the image will be `(height, width)` and your return shape should be a `nump.array` with shape `(height, 1)` .  
Consider the input image is represented by the `numpy.array` named `a` with shape `(3, 4)`   
```text
[[0, 1, 2, 3],
 [4, 5, 6, 7],
 [8, 9, 10, 11]]
````

Then the call `collapse(a)` would return the `numpy.array` with shape `(3, 1)` .  
```text
[[ 6], 
 [22], 
 [38]]
````

##  Implementation Details  

-  You will need to use loops to solve this problem! Think carefully about how to iterate over the indices you want! You'll also want to think carefully about what the result shape should be and how to index into it. As we said in the reading, it helps to draw out the values and shapes you have as you are working on solving the problem.  
-  You should not modify the input image, instead, you are making a new result.  
-  Just like there is a     `np.ones`     to make an array of 1s, there is a function     `np.zeros`     to make an array of 0s.  
-  Additionally, these functions return array of floats by default. To make the result an array of ints, you should pass the optional parameter     `dtype=int`     to the     `np.zeros`     call after you pass in the desired shape.  


```{admonition} Note
:class: note

It turns out this problem can actually be solved without loops using some more advanced features of
`numpy`
. However, you should definitely use loops to solve this problem since we want you to practice for convolutions.

```

