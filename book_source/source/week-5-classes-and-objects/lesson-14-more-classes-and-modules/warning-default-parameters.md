# Warning: Default Parameters

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/495504e315c04f199f3f8756f37eb053?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Last week, we learned about how to define **default parameters** for your function. What this means is we specify what a default value should be for a parameter and the client can optionally provide a value for that parameter (it takes the default value if not specified). For example,  
```python
def some_function(x, y=2):
    print(x * y)

some_function(4, 5)
some_function(3)  # default will be y=2
```

One important thing to mention: you are allowed to give default values for any parameter you want, however, there is a rule about the order of parameters when you define default values. If you define a default value for a parameter, every parameter after that one in the list of parameters must also have a default value. This means you would not be able to write a function like the one below. If you run it, you will see an error.  
```python
def some_function(a, b=2, c): 
   print(a * b * c)
```

##  A Curious Case  

Default parameters are great, but there is one case you have usually think about when you are programming in Python.  
Suppose I wanted to write a function called `append_to` that takes a value and a `list` and appends the value to the end of the list, returning the `list` back to the caller. Suppose we wanted to make the `list` parameter optional, in which case the default value is the empty list. In the following cell, we define such a method and then call it a couple of times. **Before you press Run, think about what this program should print out.**   
```python
def append_to(element, to=[]):
    to.append(element)
    return to

my_list = append_to(12)
print(my_list)
my_other_list = append_to(42)
print(my_other_list)
```

If you're like me, you would have expected it to print:  
```text
[12]
[42]
````

However, in reality, it prints:  
```text
[12]
[12, 42]
````

Don't believe me? Try running it yourself by pressing the Run button!  
##  What is going on?  

It turns out that when we specify the default parameter `to=[]` , **
			it only creates one 
			** If you think about drawing the memory model here, whenever you omit the `to` parameter and it uses the default, it is always referring to the same `list` instance! That means `my_list` , `my_other_list` and `to` (only in the case when the default value is used) all refer to one `list` object.  
You can check out [None](http://www.pythontutor.com/live.html#code=some_list%20%3D%20%5B1,%202,%203%5D%0Aempty_list%20%3D%20%5B%5D%0A%0Adef%20append_to%28val,%20to%3D%5B%5D%29%3A%0A%20%20%20%20to.append%28val%29%0A%20%20%20%20return%20to%0A%20%20%0A%23%20Try%20passing%20in%20an%20existing%20list%20%0Aappend_to%284,%20some_list%29%0A%0A%23%20Now%20use%20defaults%0Amy_first_list%20%3D%20append_to%2812%29%0Aprint%28my_first_list%29%0A%0Amy_second_list%20%3D%20append_to%2842%29%0Aprint%28my_second_list%29&cumulative=false&curInstr=20&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) to see a visualization of the memory model for this program above.  
At this point, some students might confuse this with creating a list regularly using the `[]` syntax. That is not the case. Each time you specify `[]` it makes a new empty list. The problem here is Python only evaluates the default-parameter once when the function is first loaded (before it's called) so all function calls that use the default value share that one value for the default-parameter.  
##  How do we fix this?  

The general pattern is to make the default value `None` and then write code inside the method to create an empty `list` if the value is `None` . For example, the fixed code block using this pattern would look like:  
```python
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to

my_list = append_to(12)
print(my_list)
my_other_list = append_to(42)
print(my_other_list)
```

And now it prints the output we expected originally!  Each time `append_to` was called and the default-value `None` was used, we then created a new `list` to return so there are now 2 `list` objects in this program above.  
##  Fancier Syntax  

It can be kind of tedious to sometimes write out an entire if-else block to set a value. Python has a **conditional expression** that lets you write this in shorter syntax (some call this the "ternary operator"). Below we show the original if-else block (the original way you're familiar with) and then we show the conditional expression that achieve the same value assignment.  
```python
condition = True  # Or any boolean value

# Option 1
if condition:
    x = 14
else:
    x = 42
print(x)

# Option 2
x = 14 if condition else 42
print(x)
```

The syntax looks a little weird at first, but it's meant to read like English "x should have the value 14 if the condition is true, otherwise, it should be 42".  
We could then rewrite our `append_to` example using this slightly cleaner syntax:  
```python
def append_to(element, to=None):
    to = [] if to is None else to
    to.append(element)
    return to

my_list = append_to(12)
print(my_list)
my_other_list = append_to(42)
print(my_other_list)
```

Line 2 of this code block can be read to mean " `to` should reference a new `list` if `to is None` (the default), otherwise `to` should be `to` (whatever was passed to the call).  
