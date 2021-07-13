# Keyword Arguments

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/00a911a2a8ec482ca6af4fc94be9def7?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

This slide doesn't describe anything particular about `pandas` , but a general feature of Python.  
In the following code cell, we define a function called `div` and show two different ways to call it! The first is the way we have seen it this whole time and the second is a brand-new way!  
```py
def div(a, b):
    print('Dividing', a, 'by', b)
    return a / b

# Method 1: Pass "by position"
div(1, 2)

# Method 2: Pass "by name"
div(a=1, b=2)
# When specifying by name, you can provide them in any order!
div(b=2, a=1)
# Notice, this is different!
div(b=1, a=2)
```

Why did we call these two methods "by position" and "by name"? When you were originally calling `div(1, 2)` you might have taken it a bit for granted how it determined that `a` should be `1` and `b` should be `2` . When calling a function in the way we showed originally, it determined that the first value passed ( `1` ) should be assigned to the first parameter ( `a` ), the second value ( `2` ) for the second parameter ( `b` ), and so on if there were more parameters. This is why we call this "by position" since the position of the value in the function call determines which parameter will have that value.  
Instead, Python also provides a way to specify which parameter should have which value by using the names of the parameters in the function call! When you say `div(b=2, a=1)` you are telling Python you want the parameter `b` to have value `2` and the parameter `a` to have value `1` . Now the position of the arguments doesn't matter, but the name you specify does. Notice that `div(b=1, a=2)` is very different than `div(b=2, a=1` )!  
We will see these named-parameters pop-up quite often in the libraries we learn! They usually provide functions with tons of parameters (with some default values)! It would be horrible if you had to specify them all by position (requiring you to know which parameter came 3rd in the list). Instead, you can pass them by name and it simplifies your code!  
To see how many parameters a `pandas` function actually takes, look at its documentation!  
```py
import pandas as pd
help(pd.read_csv) # Press q to quit
```

###  A note about mixing conventions  

Python lets you use both passing by-name and by-position in a single function call. For example, if you want to use the `print` function, but don't want the new-line on the end, you would write:  
```py
# Try changing end to something else to see it print at the end!
print('Hello world', end='')
```

How does Python determine which is which? It first uses the arguments passed by-position to fill up the first parameters and then fills in the remaining with the ones passed by-name. You aren't allowed to specify something by-name if it was already specified by-position.  
This might make more sense with an example we define.  
```py
def method(a, b, c):
    print(str(a) + ',' + str(b) + ',' + str(c))

# 1 will be interpretted as a's value, rest are by-name
method(1, b=2, c=3)

# Causes an error because we tried to specify a twice!
method(2, a=1, c=3)
```

