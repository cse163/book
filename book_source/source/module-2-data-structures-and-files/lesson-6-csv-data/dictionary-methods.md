# Dictionary Methods


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/cc2e27f4df774142a4aa2d232a40bcb3" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

In Lesson 5, we learned about the dictionary or `dict` type in Python to store a relationship between **keys** and **values** . For example, you could define a dictionary with some keys and values, and then access/modify using the bracket-syntax we used for `list` s.  
```python
d = {'a': 1, 'b': 2}
d['c'] = 3
d['a'] = 4
print(d['b'])
print(d)
```

`dict` s, like `list` s, are objects so they also have methods you can call on them. We show a table with the most common methods below. In the next section, we show an example using some of these methods.  

|  Function  |                    Description                     |
|------------|----------------------------------------------------|
|dict() or {}|Creates a new, empty dictionary                     |
|d.pop(key)  |Removes key from the d                              |
|d.keys()    |Returns a collection of all the keys in d           |
|d.values()  |Returns a collection of all the values in d         |
|d.items()   |Returns a collection of all (key, value) tuples in d|

##  Looping over a Dictionary  

You might have been wondering from the last lesson how you would loop over a `dict` . With the methods we have shown, you might see how you could loop over the keys of a dictionary. For example, if you want to iterate over the keys of a `dict` , you use the `keys` method. The `keys` method returns a collection (similar to a `set` ) of all the keys in the `dict` .  
```python
d = {'a': 1, 'b': 2, 'c': 3}
for k in d.keys():
    print(k, '-', d[k])
```

Similarly, you could use the `values` method to get a collection of all the values in a `dict` . A common approach is to use the `items` method to get a tuple of both keys and values for each entry.  
```python
d = {'a': 1, 'b': 2, 'c': 3}
for pair in d.items():  # pair will be a tuple: (key, value)
    print(pair[0], '-', pair[1])
```

In this example, `d.items()` returns a sequence of tuples and the for loop is looping over that.  
Recall, that last time we learned about the tuple and that you can **unpack** them to store their values inside separate variables.  
```python
p = (1, 2)
print(p)

a, b = p
print(a)  # same as p[0]
print(b)  # same as p[1]
```

You can use this same technique in the loop over the items to make a variable for both the key and the value!  This unpacks the tuple and gives a variable name to each component.  
```python
d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():  # unpacks the tuple into k and v
    print(k, '-', v)
```

This is a very common pattern when looping over dictionaries and you need both the key and the value so it's good to know it! Nothing technically new is happening here since it's just using the unpacking semantics we saw in the previous code block, but it's more complicated now that it can also be used for a loop variable.  
