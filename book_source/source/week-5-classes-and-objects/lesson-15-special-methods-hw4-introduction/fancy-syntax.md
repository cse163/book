# Fancy Syntax

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/5aafdcb9496e4fd28a06f4f069dbd0d2?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

It turns out that most of the common syntax in Python is really just "special methods" that can be defined in your class. Below is a list of common features you might define when writing your own classes.  

| Syntax |    Method Call    |
|--------|-------------------|
|x < y   |x.__lt__(y)        |
|x == y  |x.__eq__(y)        |
|x >= y  |x.__ge__(y)        |
|print(x)|print(x.__repr__())|
|x[i]    |x.__getitem__(i)   |
|x[i] = v|x.__setitem__(i, v)|

For example, here is a toy class that implements all of these methods to prove that they get called when you use the syntax shown above.  
```python
class SomeClass:
    def __lt__(self, other):
        print('Calling __lt__')
        return False
    
    def __eq__(self, other):
        print('Calling __eq__')
        return False
    
    def __repr__(self):
        print('Calling __repr__')
        return 'SomeString'
    
    def __getitem__(self, i):
        print(f'Calling __getitem__ with {i}')
        return -1
        
    def __setitem__(self, i, v):
        print(f'Calling __setitem__ with {i} and {v}')
        return -1
    
    
x = SomeClass()
y = SomeClass()

print('Less Than')
print(x < y)
print()

print('Greater Than')
print(x > y)
print()

print('Equal')
print(x == y)
print()

print('Not equal')
print(x != y)
print()

print('Print')
print(x)
print()

print('Bracket Notation')
print(x[0])
x[14] = 4
```


```{admonition} Note
:class: note

It turns out that because we implement
`__lt__`
and
`__eq__`
there is no need to implement any other comparison operators (
`__le__`
,
`__gt__`
,
`__ge__`
). This is why when we wrote
`x > y`
it can figure it out just from
`__lt__`
! For example,
`x > y`
can be implemented as
`y.__lt__(x)`
and
`x <= y`
could be implemented as
`x.__lt__(y) or x.__eq_(y)`
!
<br />

<br />
You could have chosen another operator besides
`__lt__`
, but basically if you implement any less than / greater than operator and equals, you get all of the others for free!
<br />


```

