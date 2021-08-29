# <i class="far fa-edit"></i> Practice: Broadcasting

What is the result of the following operation? For reference, we have shown the rules of broadcasting below.

```text
x = np.arange(3).reshape((3, 1))
y = np.arange(3)
x + y
````

##  Rules of Broadcasting

-  If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded on it’s left side.

-  If the shape of two arrays does not match on any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape. This will happen for all dimensions that don't match and one has a shape equal to 1.

-  If in any dimension the sizes disagree and neither is equal to 1, an error is raised.


## Question 0





**📝 Your Task**

Select one option. Write your answer down in your own space.

*❓ Option 0*

```text
array([[0, 1, 2],
       [1, 0, 0],
       [2, 0, 0]])

````



*❓ Option 1*

```text
array([0, 2, 4])

````



*❓ Option 2*

```text
array([[0, 1, 2],
       [1, 2, 3],
       [2, 3, 4]])

````



*❓ Option 3*

```text
array([[0, 1, 2],
       [1, 1, 1],
       [2, 2, 2]])

````



*❓ Option 4*

Causes some Error



*❓ Option 5*

Other



