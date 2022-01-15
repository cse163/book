# The Class: Define Your Own Objects

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/e10d04adc79e4015a810538ee96e2c01?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

So we saw that objects exist in Python, but now we want to answer how you can define your own objects!

To do this, you need to write a **class** . A class is a "blueprint" for an object, so you can make many objects from that blueprint. The `pandas` developers defined a `DataFrame` class so that you can construct `DataFrame` objects to use (another common word for "object" is "instance").

We start by showing the syntax for defining our own class and then explaining what the components are.

```{snippet}
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + ': Woof')
```

This defines a new type called `Dog` . The state of the `Dog` will be the **field** `name` . A field is basically a variable that lives inside the object for the duration of its lifetime. The behaviors of the `Dog` include a `bark` method. This code has multiple parts so we try to explain each part

- `class Dog` defines a new class named `Dog`

- `def __init__(self, name)` is a special method called an **initializer** . This is a special method that gets called when you construct the object. **
  Every method defined in the class has to take a special parameter
  ** to indicate which `Dog` object it is working with (remember, there can be many instances built from the same `Dog` blueprint). In this example, we also pass another parameter to the constructor for the dogs name.

  - `self.name = name` creates a field called `name` on the `Dog` instance and initializes it to the parameter's value.

- `def bark(self):` defines a method on the `Dog` class. Like `__init__` it has to take `self` at least, but we decided to include no other parameters.

  - `print(self.name + ': Woof')` prints some output using the value stored in this objects `name` field.

To use a `Dog` object, you would write the following code (we have to redefine the class in the cell below since all the snippets in these readings are independent).

```{snippet}
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + ': Woof')


d1 = Dog('Chester')
d2 = Dog('Scout')
d1.bark()  # Prints: "Chester: Woof"
d2.bark()  # Prints: "Scout: Woof"
```

Notice we call methods on objects as we did before where we say `object.method()` . In the line `d1.bark()` , we call the `bark` method passing `d1` as the value for `self` (that's why `self.name` evaluates to `'Chester'` in that call).

On line 9 and 10 of this program, we construct new instances from this `Dog` class. You can think of this as calling up the `Dog` factory and they make a new object from the blueprint that is the `Dog` class. When passing in the `str` s `'Chester'` or `'Scout'` , we are specifying what value we want for the `name` parameter in the initializer. In fact, when you say `Dog(some_value)` you are really calling that special method `__init__` passing in a new `Dog` instance (which starts out with no state) and the other parameter values specified (in this case `name=some_value` ); the initializer is meant to set up the state of the `Dog` so the client that requested the `Dog` can use it afterwards.

## Recap

Here are some example questions (there are definitely more out there!) that are good to check your understanding of the content! Make sure to include them in your notes and that your notes include enough detail to answer them!

- What is the difference between a class and an object?

- Why does every method defined in a class need to take a self parameter? How do you access the fields/methods of an instance from inside the class definition.

- When calling a method on an object (in the client), why don't you need to pass `self` in as one of the parameters?
