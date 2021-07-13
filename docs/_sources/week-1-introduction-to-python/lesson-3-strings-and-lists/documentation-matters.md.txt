# Documentation Matters

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/13c9ac9a1fef415f9cf9b1755b1e9362?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Whenever you write a function, you should provide some documentation for what it does and any information someone needs to know to use it. Reading code can be hard so we want to provide some instructions people can understand. Code without documentation requires anyone trying to use your code to try and recreate what you were thinking, which essentially ends up with them making guesses at what it does

```{warning}
When I'm trying to understand code without documentation, it often feels like I'm like a way-less-capable version of Amy Adam's character in the movie
<Element 'link' at 0x7fcd260413b0>
. Don't write code where I have to feel like that. Write documentation in English (or whichever language you and your team work in) so people know how to use the code you write!

```

You can always use the
`#`
to leave a note in your code, but we are specifically going to talk about a special notion in Python called a
**doc-string**
that lets you add special documentation for a function. To do this, you use this special triple-quote string (i.e.
`""" documentation """`
)  as the first lines of the function.

```py
def mean(a, b):
    """
    Returns the average of a and b
    """
    return (a + b) / 2
```

Everything that goes inside these triple-quotes now becomes the documentation for a function.

Why does it help to specify this special doc-string? Well Python has built-in tools to help you view the doc-strings for any function!

Python provides a
`help`
function that lets you see the documentation for any function! For long documentation, it brings up a special viewer where you can move up/down with the keys
`j`
/
`k`
and you can quit with the key
`q`
.

```py
help(print)
```

To see how this works with code you write, suppose I wrote the function with the following doc-string and asked for help on it.

```py
def function_with_good_comment():
    """
    This function does some really cool stuff
    """
    print('ABC')

help(function_with_good_comment)
```

What if instead of using the triple-quote docstring, I just put everything after a
`#`
comment since I'm more comfortable with that

```py
def function_with_bad_comment():
    # This function does some really cool stuff, but with a bad comment
    print('ABC')

help(function_with_bad_comment)
```

Unfortunately,  it doesn't show anything! This is why using the doc-string format is so important!


**We will ask that every function you write has one of these doc-string comments describing what it does!**


