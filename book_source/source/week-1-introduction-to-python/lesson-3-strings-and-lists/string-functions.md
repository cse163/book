# String Functions

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/a4e92e76179f4f5bb7118a9b25b41463?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Each string is an **object** . We will talk more about objects in detail in Week 5, but the basic idea is that each string is its own, independent unit that has some **state** and some **behaviors.** The **state** of a string is its characters and their ordering. The **behaviors** of the string are the functions we are allowed to call on them to access or transform the data. You don't need to worry too much about this state/behavior terminology right now as we will emphasize it in Week 5.  
We have seen a simple function already that allows us to index into the string so it can return the character at that index. You can imagine this indexing as just one special function provided to us by the string (although the syntax looks different than the general notion we will show below).  
For example, there is also an `find` function that you can call on a string `s1` , that returns the index of a given string `s2` inside `s1` . For example, you could write the following:  
```py
source = 'I really like dogs'
target = 'll'
print(source.find(target))
```

In this case, it prints 5 because the first occurrence of the substring `'ll'` in `source` appears at index 5. Notice that we call a function on the string `source` by saying `source.<function_name>(...)` where `...` is the parameters we need to pass to that function. If we were to call `target.find(source)` it would be looking for `source` inside `target` and would instead return -1 (as defined in the documentation for `find` ). You can try this in the snippet below.  
```py
source = 'I really like dogs'
target = 'll'
print(target.find(source))
```

Here is a shortlist of useful functions for `str` in Python.  

|   Function    |                                                                                       Description                                                                                       |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|s.lower()      |Returns a new string that is the lowercase version of s                                                                                                                                  |
|s.upper()      |Returns a new string that is the uppercase version of s                                                                                                                                  |
|s.find(target) |Returns the index of the first occurrence of target in s. If not found, returns -1.                                                                                                      |
|s.strip()      |Returns a new string that has all the leading and trailing whitespace removed.Also has functions lstrip() and rstrip() that remove only left whitespace or right whitespace respectively.|
|s.split(delim) |Splits s up into parts using the given delimiter to break the string apart. Returns the result as a list.                                                                                |
|s.join(strings)|Combines the strings in the given list, separated by s                                                                                                                                   |


```{admonition} Warning
:class: warning

Because strings are immutable, all of the methods above like
`upper`
and
`strip`
return
*
			*
strings rather than modifying the original string
`s`
.

```

The last two functions are the most complex, so we will do a short example to clarify their use.  
Suppose we had a string that contained a series of values separated by the `,` character, but we want to print the string out in all upper-case letters separated by `|` characters. We put print statements in between to make the sequence of transformations clearer and to provide comments explaining the step.  
```py
data = 'hunter,madrona,alex,sylvia'
print('Original   :', data)

# Returns a new string that is the upper-case version of data
# Store that new value in the data variable
data = data.upper()
print('After upper:', data)

# Split the data up by a ','. Returns a list of parts.
# We will describe lists later in this reading.
parts = data.split(',')
print('After split:', parts)

# Put those parts back together separated by a '|'
data = '|'.join(parts)
print('After  join:', data)
```

To understand fully how this solution works (i.e. "what is the type of the value returned by split"), we have to wait for a few slides and talk about this other type called `list` .  
##  `len`   

Notice that in the table above we did not show you how to find the length of a string. Recall from the last slide, the syntax for this is `len(s)` . We did not add it to the function list because `len` is not a function defined on a `str` object, but rather a built-in function to Python. We'll see later that `len` works on basically any type that represents a sequence of values. This is a bit weird that there are these different syntaxes for calling these functions, but you'll get used to it with practice and making lots of mistakes!  
 
