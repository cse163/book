# Hashing in Practice

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/3a324a37a735426cb462e3eff854ad86" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

We mentioned before that when defining that a hash function needs to be "consistent". Consistency is all about maintaining the deep relationship between the notions of equality and hashing.  
We briefly showed this in the last slide, but to get the hash for a Python object you can call the built-in `hash` function like in the snippet below.  
```py
print(hash('hello world'))
print(hash(4.275))
```

Just like most Python concepts, this is really calling a special method on a Python object named `__hash__` .  So `hash(x)` gets translated to `x.__hash__()` . You should always prefer to call the built-in function for readability rather than referring to the special method explicitly.  
Hashing and equality have an important relationship. If you define `__eq__` (to define what `==` does), you need to implement `__hash__` so that it is consistent with the definition of `__eq__` .  
We've mentioned "consistent" a few times by this point: what do we mean by that? A hash function is consistent if whenever `a == b` , then `hash(a) == hash(b)` . In English, this says that any objects that are equal must hash to the same value. Notice this is a one-way if statement. It says nothing about `hash(a) == hash(b)` implying `a == b` . In fact, we explicitly ignore this requirement in the notion of allowing collisions in our hash table.  
##  Example Class  

So whenever you implement a class, it's important to make sure `__eq__` and `__hash__` consistent. Almost all implementations of `__hash__` just rely on using Python's `hash` function on your fields so you don't have to come up with something as complex as the last `str` hash function we showed on the last slide.  
An example of a class that does this well is shown in the following snippet.  
```py
class Example:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    
    def __eq__(self, other):
        return self._a == other._a and self._b == other._b

    def __hash__(self):
        return hash((self._a, self._b))
```

Notice that in this example, the `Example` class has 3 fields but we only defined `__eq__` to check two of them. This means in the `__hash__` method, we can only look at the fields we used for the equality check to make sure two objects that are equal will hash to the same value!.  
