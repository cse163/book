# Functions

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/03352627cdf844918fd5459a16bd5acc?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

##  Functions  

A **function** is a named procedure with a series of instructions that can be **called** in your program to execute those instructions.  
To call a function, you use its name and use `()` after it to make it a call For example, `print` is actually a function defined by Python, so a "print statement" is really just calling this `print` function.  
```py
print()  # Prints a blank line
```

As we saw earlier, we can pass **parameters** to this function call to give it inputs. For example, the `print` function takes parameters for the things to print.  
```py
print('Hello world!')
```

Functions defined by Python are commonly called **built-in** functions. Some examples of built-in functions we will use commonly in CSE 163 are:  
-  `print`   
-  `range`   
-  Casting:     `int`     ,     `float`     ,     `bool`     ,     `str`   
-  Math:  
    -  `abs`         to find absolute value  
    -  `max`         to find the max of a sequence of numbers  
    -  `min`         to find the min of a sequence of numbers  
    -  `sum`         to find the sum of a sequence of numbers  


Many functions can also **return** a value from their computation. For example `min` returns the minimum value of its inputs. You can do some more complex operations by combining the inputs and outputs of various functions like in the snippet below:  
```py
x = min(4, 7)  # x will store 4 (the return value of this function)
y = max(5, x)  # y will store 5 (the return value of this function)
```

##  Define your own Functions  

In the following snippet, we show how to define a function called `greetings` .  
```py
def greetings():
    print('hola!')
```

Note that by putting nothing in the parentheses, we are saying it takes no parameters.  
To call the function, you need to actually use a function call like we showed before!  
```py
def greetings():
    print('hola!')
    
greetings()
```

###  Defining Parameters or Returns  

If you want to define a function that takes parameters, you put variable names in between the `()` for each parameter you want the function to take. If you want the function to return a value, you use a `return` statement like the example below.  
```py
def mean(a, b):
    print('Calling mean with', a, b)
    return (a + b) / 2


mean(1, 2)  # Have to call it passing in two parameters!
```

##  Functions in Context  

Recall that we said our reading snippets normally don't show the main-method pattern. We make an exception in the next snippet to show a full Python program.  
Notice, we are having you define a function called `main` by saying `def main():` ! The `mean` function only gets called when we are actually running the program and the `main` method calls it.  
```py
def mean(a, b):
    print('Calling mean with', a, b)
    return (a + b) / 2


def main():
    print('The mean of 1 and 2 is:')
    print(mean(1, 2))


# The weird main-method pattern syntax!
if __name__ == '__main__':
    main()
```

 
 
