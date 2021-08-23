# 🚧 Practice: Pair

{download}`Download starter code </module-5-classes-and-objects/lesson-15-special-methods-hw4-introduction/practice-pair.zip>`


```{admonition} Note
:class: note

Like we said earlier, we are putting all the questions before the pause and think today, since we won't be having a structured class on Friday. You are welcome to do this now, or come to class and work with groups!

```

Write a class called `Pair` that stores two values and can be used just like a tuple containing two elements. The class you implement should produce the behavior shown in the code cell below. Define the class in `pair.py` .  
You can assume the client will only access index 0 or 1 for a `Pair` .  
The `Pair` class should be immutable so that the client can't change its state. This means all fields should be private and if they try to modify a value in the pair,  like in the last line of the code cell below, it should print an error message and do nothing else. Notice that you will still need to define the method to allow the syntax for assignment, but the behavior just prints the error without changing the state of the object.  
```python
p1 = Pair(1, 2)
p2 = Pair(3, 4)
p3 = Pair(1, 2)

print(p1 == p2)
print(p1 == p3)

print(p1)

print(p1[0])

p1[0] = 14
```

```text
False
True
(1, 2)
1
Error: Pair is immutable!
````

Here is the table of methods shown on the last slide:  

| Syntax |    Method Call    |
|--------|-------------------|
|x < y   |x.__lt__(y)        |
|x == y  |x.__eq__(y)        |
|x >= y  |x.__ge__(y)        |
|print(x)|print(x.__repr__())|
|x[i]    |x.__getitem__(i)   |
|x[i] = v|x.__setitem__(i, v)|

 
