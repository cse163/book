# Recap: Lists

Recall in the last two lessons, we have used `lists` to represent an indexed-sequence of values. A list can store values of any type. The snippet below shows a quick recap of all the syntax we have introduced for lists (not included: the list of `list` methods).  
```python
# Create a list
l = [1, 2, 'hello']


# Print a list and get a value
print(l)
print(l[1])  # Lists, like str, are 0-indexed


# You can also use slicing on lists, just like str
print(l[1:2])  # [2]
print(l[:2])   # [1, 2]


# You can use assignment to update values in a list (can't with a str)
l[1] = 'dogs'
print(l)


# Two ways to loop over a list
for i in range(len(l)):
    print(l[i])
    
for val in l:
    print(val)


# Build up a list programmatically, fun_numbers from last time
start = 2
stop = 16
result = []  # Empty list
for i in range(start, stop):
    if i % 2 == 0 or i % 5 == 0:
        result.append(i)
print(result)
```

A `list` is an example of a **data structure.** A data structure is some programming construct that stores data. We will learn about 3 other data structures in this lesson. Each one makes different "choices" about how it stores the data and how you access it. It will always help to think of a `list` as a starting point, and identify how these other structures are similar/different to the `list` .  
