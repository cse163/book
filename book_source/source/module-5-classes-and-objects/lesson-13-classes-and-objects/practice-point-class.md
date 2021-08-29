# <i class="fas fa-laptop fa-fw"></i> Practice: Point class

{download}`Download starter code </module-5-classes-and-objects/lesson-13-classes-and-objects/practice-point-class.zip>`

Define a class `Point` that represents a 2D point `(x, y)` in the file `point.py` .

The `Point` class should have fields for the `x` and `y` coordinates and should have the following methods.

- An initializer that takes the `x` and `y` values.

- A method named `get_x` that returns the `x` value of this `Point` .

- A method named `get_y` that returns the `y` value of this `Point` .

- A method named `set_x` that takes a new `x` value and updates this `Point` 's `x` to the parameter.

- A method named `set_y` that takes a new `y` value and updates this `Point` 's `y` to the parameter.

- A method name `display` that returns a `str` representation of the point. It should return `'(x, y)'` where `x` is its `x` value and `y` is its y value.

For example, your class should have the following behavior (return value shown in comments). This is essentially the same as `main.py` (which you don't need to edit).

```python
p = Point(1, 2)
p.get_x()    # 1
p.set_y(4)
p.display()  # '(1, 4)'
```
