# Advanced Lists


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/0f46f457b6ed496aa6abe13391c07d39" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

##  List Methods  

Just like with strings, `list` also has methods you can call on a `list` object to observe or modify its values. You can call any of these methods on a `list` object.  


|   Function   |                                                                                                  Description                                                                                                   |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|l.append(x)   |Adds x to the end of l                                                                                                                                                                                          |
|l.extend(xs)  |Adds all elements in xs at the end of l                                                                                                                                                                         |
|l.insert(i, x)|Inserts x at index i in l                                                                                                                                                                                       |
|l.remove(x)   |Removes the first instance of x from l                                                                                                                                                                          |
|l.pop([i])    |Removes the value at index i from l. Parameter is optional, default is last index of list.  Note: The syntax [i] for a parameter is commonly used in Python documentation to indicate i is an optional paramter.|
|l.clear()     |Removes all values from l                                                                                                                                                                                       |
|l.index(x)    |Returns the first index that contains x in l. If it is not found it raises an error.                                                                                                                            |
|l.reverse()   |Reverses all the order of elements of l                                                                                                                                                                         |
|l.sort()      |Sorts the values of l                                                                                                                                                                                           |

Notice that `list` s are NOT immutable. This means methods like `append` , `remove` actually modify the list you call the method on.  

The following snippet shows some example of how to call some of these methods  

```python
l = []  # Empty list
l.append(1)
l.append(2)
l.append(3)
l.append(2)

print('Before  remove', l)
l.remove(2)  # Removes first instance of the value 2
print('After   remove', l)

# Can call pop one of two ways because the index is optional
l.pop(1)  # Removes the value at index 1
print('After   pop(1)', l)
l.pop()  # Removes the last value in the list
print('After    pop()', l)

l.extend([4, 5, 6])
print('After extend()', l)
```

##  The `in` keyword  

Have you ever asked yourself, "Is the number `2` in this list of numbers?" Probably not, but we'll show you how to do it anyway!  

The idea of checking if a `list` contains a value is incredibly important for applications like trying to find all the distinct values in a collection or only trying to look at values in a subset of all possible values (like looking at all students from WA, OR, or CA).  

There is a special keyword in Python precisely made for doing these contains queries (we also call them **membership queries** ). The following snippet shows the syntax for this keyword. The syntax goes `value in collection` and it is an expression that evaluates to `True/False` which means you could use it in an `if` statement or a `while` loop. You can try editing the code block to see what happens if you searched for the word `'cats'` instead.  

```python
words = ['I', 'love', 'dogs']
if 'dogs' in words:
    print('Found it!')
else:
    print('No luck :(')
```

Notice that we didn't say you could only use this on lists. It turns out that you can use it on almost all structures we learn in this class that store values. For example, you can use it on strings too: `'og' in 'dogs'` .  

To see if something is not in a list, you can use `not in` as shown in the next example (it's exactly the opposite of the `in` keyword)  

```python
words = ['I', 'love', 'dogs']
if 'cats' not in words:
    print('Not there!')
else:
    print("It's there")
```

