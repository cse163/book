# Python Basics


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/fdf9802363e74c8db885031d985be706?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

In an Ed reading, there will be multiple Python **snippets** . You should think of each snippet as its own Python file (like Hunter showed at the end of Lecture 1). Recall from the Ed Tutorial, you can (and should!) run each block as you're reading to see its output.  

```{admonition} Tip
:class: tip

You can also (and are encouraged) to edit the block to see what would happen if you tried to change the code in some way! Go out and explore a bit! 😊
<br />

<br />

*Tip:*
You can always get the original code back for a reading slide by refreshing the page.

```

###  Print Statements  

We saw that the `print` statement in Python is very simple  
```py
print('Hello world!')
```

One thing that Python is really good at is providing slightly different ways of using the same syntax to do helpful things. For example, you can also pass multiple values to the `print` function and it adds spaces between them!  
```py
print('Hello', 'world', '!')
```

###  Python Program + Main Method Pattern  

A Python program is a series of statements that get executed from top to bottom. Right now the only statement we know is the print statement. But we will learn others!  
In CSE 163, we will ask you to put a little bit of starter code in every program you write. We call this the **main-method pattern** . We can't really motivate why you need to use this quite yet; you'll have to trust us that it is the right thing to do. We introduce this pattern now to get you in the practice of writing from the onset of your Python journey. We will come back in future weeks and actually dive into what this pattern does and why it's necessary.  
Recall that we could write a Python program in a file (in Ed, it shows we write a Python snippet) to print hello world like the following:  
```py
print('Hello world')
```

However, instead, we will commonly ask you to write a few extra lines of code "around" the program you wanted to write as the following.  

```{admonition} Note
:class: note

The line that starts with a
`#`
is a comment (i.e. not real code, just a description).

```

```py
def main():
    # Put your code, indented inside here
    print('Hello world!')
    
    
if __name__ == '__main__':
    main()
```

We'll start you off by providing the main-method pattern as a starter code for your practice problems on Ed, but you will get used to writing these weird symbols by yourself! Again, we promise to explain this later, we just can't right now!  

```{admonition} Warning
:class: warning

We said that these Python snippets are basically like a Python file, which is mostly true. However, a big difference is we will commonly
**omit**
the main-method pattern in these readings' snippets. The intent here is to keep the readings shorter and better at communicating the big idea of the reading.
<br />

<br />

**For your take-home assessments, you will always need to use the main-method pattern for the files you write.**


```

###  Variables  

Variables store values. Each Python value is composed of a value and its type. Unlike Java, Python doesn't require you to define the type of a variable. Additionally, throughout the lifetime of the program running, the variable can be made to hold a new value of a different type using an **assignment statement** .  
The following snippet creates a variable named `x` that stores the value `3` of type `int` (for integer) and a variable named `y` that stores the value `4.2` of type `float` (for floating-point number). One line 3, it then re-assigned `x` to store the value `3.7` of type `float` . This is why the program prints `x = 3.7` and `y = 4.2` .  
```py
x = 3
y = 4.2
x = 3.7

print('x =', x)
print('y =', y)
```

The mental model you have in your head should think of each variable as a box that stores a value. After Line 2 has run, the state of the program is  
```text
  +-------+      +-------+
x |   3   |    y |  4.2  |
  +-------+      +-------+  
````

After Line 3 has run, the state of the program is  
```text
  +-------+      +-------+
x |  3.7  |    y |  4.2  |
  +-------+      +-------+  

````

When we get to lines 5 and 6, they just "look inside" the box and use whatever value that's in the current state of the program!  

```{admonition} Warning
:class: warning

For those that now Java, this is a big difference than what you have seen before. In Java, a
**variable's type**
is determined by the variable itself (e.g.,
`int x`
). But in Python, a variable's type is determined
**by the value in the variable.**

<br />

<br />
Another way of phrasing this, is that it doesn't make sense to think of Python variables as having types. A variable in Python is just a box to store values of any types, the value itself knows what type it is (
`4`
knows it is an
`int`
,
`4.2`
knows it is a
`float`
).

```

###  Expressions  

Python supports many operations for built-in types. Specifically, here are the operations defined for numeric types like `int` and `float` .  
-  Addition:     `a + b`   
-  Subtraction:     `a - b`   
-  Multiplication:     `a * b`   
-  Division:     `a / b`     (e.g.,     `7 / 3 == 2.333333333`     )  
-  Integer division:     `a // b`     (e.g.,     `7 // 3 == 2`     )  
-  Mod:     `a % b`     (i.e., leftover from integer division as in     `7 % 3 == 1`     )  
-  Exponentiation:     `a ** b`     (i.e., raise to a power $a^b$)  

You can also nest expressions (and use parentheses to define order) since all expressions evaluate to some value. You can do something complex like the following:  
```py
a = 3
print(a - (2 * a) + (a ** (1 + 2)))
```

##  Recap  

We saw a lot of things, but hopefully, most of them are pretty familiar to what you've seen before (except the main-method pattern which is weird and takes a little while to get used to).  
