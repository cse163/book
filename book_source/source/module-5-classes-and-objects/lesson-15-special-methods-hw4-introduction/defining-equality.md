# Defining Equality

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/11cc2dc8c14943f28ef63a454aa39f93?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

Recall the `Dog` class we wrote in Lesson 13.

```python
class Dog:
    def __init__(self, name):
        self._name = name

    def bark(self):
        print(f'{self._name}: Woof!')


d1 = Dog('Chester')
d2 = Dog('Chester')
d3 = d1

print(d1 is d2)
print(d1 is d3)
print(d1 == d2)
```

With our understanding of `is` , the first two examples should hopefully make sense. However, the third example ( `d1 == d2` ) seems a bit surprising! It seems like these two `Dog` s should be considered value equal since they have the exact same state!

Unfortunately, Python does not automatically know how you want to define value-equality between `Dog` s. By default, Python will treat `==` on your object to mean the same thing as `is` , unless you tell it that value equality should be defined otherwise. In this reading, we will talk about how to tell Python what you want `==` to mean for your object.

To define what `==` should mean, you have to implement a special method called `__eq__` . `__eq__` will be called whenever you use `==` and its return value ( `True` or `False` ) determines the value of `==` . To be more concrete, `x == y` gets translated to `x.__eq__(y)` behind the scenes!

So let's define the `__eq__` method so that `Dog` s can be compared. Notice we are defining what equality means here for the `Dog` class. Let's define it that two `Dog` s are equal if they have the same name (notice we could define it however we want, but with only one field, there aren't a lot of options).

```{admonition} Note
:class: note

Even though
`_name`
is a private field on the
`Dog`
class, it is okay for one
`Dog`
to access the private fields of another
`Dog`
. The rationale here is you are the one that wrote the
`Dog`
class, so you should know how to use their private fields without causing any errors.

```

```python
class Dog:
    def __init__(self, name):
        """
        Creates a new Dog object with the given name
        """
        self._name = name

    def bark(self):
        """
        Prints a message for this dog barking.
        """
        # Uses a slightly fancier syntax called string interpolation
        # You don't need to be able to write these, but we wanted
        # to show off this feature. Everything inside {} gets
        # evaluated in Python!
        print(f'{self._name}: Woof!')

    def __eq__(self, other):
        """
        Returns true if other has the same name as this Dog
        """
        return self._name == other._name


d1 = Dog('Chester')
d2 = Dog('Chester')
d3 = d1

print(d1 is d2)
print(d1 is d3)
print(d1 == d2)
```

And now this code block prints what we would expect.
