# Python Modes

{download}`Download starter code </module-2-data-structures-and-files/lesson-4-lists-and-files/python-modes.zip>`


```{admonition} Warning
:class: warning

This slide has some starter code for you to download to follow along, but there is no code you have to write.


```


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/b27fda7ec1724f85b14fb2bae3382806" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

It turns out there are actually two "mode"s that people commonly interact with Python.  

##  Script  

This is the way we have been doing it so far: Write a `.py` file and run it with `python file.py` .  

This slide has starter code containing a file called `test_script.py` . You can download the code and run it in the terminal using `python test_script.py`! You should see it print out some output.  

##  Interactive  

The other main way of interacting with Python is an interactive mode. The interactive mode lets you easily demo new ideas or quickly find out what something will do without going through the hassle of writing a full script to test that out. Scripts are still the predominant way of writing Python programs (in this class too) since you can easily send someone your Python file.  

There is a simple way to interact with a Python and a slightly more complex way. We'll start with the simple one and the next slide will show the more complex one.  

###  REPL  

A common feature in most programming languages is to provide an interactive mode that lets you type individual lines of Python code and it tells you the output! Programmers commonly call these interactive modes **REPL**s ( **R** ead **E** valuate **P** rint **L** oop).  

Try it out! Open the terminal and type `python` (notice, no file name afterwards). This will put you in a special Python mode where it asks you to type something in! Try the following things  

-  `1 + 1`   

-  `min(4, 17)`   

-  `min(4, 'hello')`     (should crash)  

-  `print('hello world')`   


You can also do multi-line things like for loops or while loops in this mode, but it gets a bit complex to edit those (it is much easier to do these in the other option for interaction we will show on the next slide).  

To exit this Python interpreter, you will need to call the `exit()` function or press `Ctrl-D` .  


```{admonition} Warning
:class: warning

A kind of weird behavior, but sometimes if your Python script has a syntax error, it throws you into this interactive mode. This is very frustrating for beginners since it's not obvious how to quit the interpreter! You can always exit this with
`exit()`
or
`Ctrl-D`
.

```

On the next slide, we introduce a more complex way of interacting with Python that's more popular nowadays. 
