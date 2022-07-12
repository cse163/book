# Recap

In Lesson 12, we learned about **classes** and **objects** . Here's a quick recap of the terminology that we learned since it will be important to know these terms.

- A **class** is a blueprint that can be used to construct _instances_ of that blueprint. A class defines the _state_ of the _object_ and what _behaviors_ it has. For example, we defined the `Dog` class as follows:

  ```python
  class Dog:
  def __init__(self, name):
      self.name = name

  def bark(self):
      print(self.name + ': Woof')
  ```

- An **object** (or **instance** ) is an instantiation of a _class_ that has its own set of fields. You can create an instance of the `Dog` class by using the following syntax.

  ```python
  d = Dog('Fido')
  ```

- The **state** of the object is represented by its **fields.** A field is essentially a variable owned by that object that is around for that object's lifetime. The `Dog` class has the field `name` .

- The **behavior** of an object is defined by the methods written in its _class._ The `Dog` class has the method `bark` .

- Variables store **references** to objects rather than the objects themselves. This means the following program has 2 `Dog` objects and 3 `Dog` references.

  ```python
  d1 = Dog('Chester')
  d2 = Dog('Scout')
  d3 = d1
  ```

- A **memory model** is a picture that helps us see which objects exist in our program and which variables reference which objects. <br />

  ```{image} https://static.us.edusercontent.com/files/klq5hkNl8mnQsfjtNrk2bwxq
  :alt: TODO
  :width: 360
  :align: center
  ```

- `__init__` is a special method used when creating an instance of the object. It determines which parameters need to be passed when you create a new instance.

- Every method defined in a class needs to take a parameter `self` so the method can access the fields/methods of the instance the method is being called on.

  ```python
  d1 = Dog('Chester')
  d2 = Dog('Scout')
  d3 = d1
  d1.bark()  # When running, self refers to Dog('Chester')
  d2.bark()  # When running, self refers to Dog('Scout')
  d3.bark()  # When running, self refers to Dog('Chester')
  ```
