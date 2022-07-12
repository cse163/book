# Arithmetic and Logical Operators

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/fb823082034e49e29c4f42a59130a3f5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

## Arithmetic Operators

Just like `pandas`, `numpy` supports convenient usage of mathematical and logical operators on `numpy.array`s. The following code cell shows and explains some of the most common operations.

```python
import numpy as np

x = np.arange(4)
print('x')
print(x)
print()

# Add a number to each element in the array
y = x + 3
print('y = x + 3')
print(y)
print()

# Multiply two arrays element-by-element
# Works with any mathematical operation (+, -, *, /, //, **)
z = x * y
print('z = x * y')
print(z)
print()

# This also works for arrays with multiple dimensions
m = x.reshape((2, 2))

print('m / 2')
print(m / 2)
print()

# Order of operations still applies. Same as (m * 3) + (m / 2)
print('m * 3 + m / 2')
print(m * 3 + m / 2)
print()
```

## Logical Operators

You can also use logical operators ( `==` , `<` , `>=` ) to compare elements of `numpy.array`s. You can use `&` (and), `|` (or), and `~` (not) just like `pandas`.

```python
import numpy as np

x = np.arange(4)
print('x')
print(x)
print()

# Comparison
print('x < 3')
print(x < 3)
print()

# Using & (still requires parentheses)
print('(x < 3) & (x % 2 == 0)')
print((x < 3) & (x % 2 == 0))
print()
```

Not surprisingly, just like `pandas`, you can use these `numpy.array`s of `bool` values to filter down to certain values in the `numpy.array`!

```python
import numpy as np

x = np.arange(10)
print('x')
print(x)
print()

mask = (x < 3) & (x % 2 == 0)
print('mask')
print(mask)
print()

y = x[mask]
print('y = x[mask]')
print(y)
```

```{admonition} Note
:class: note

We commonly compare `numpy` and `pandas` since they were designed to be similar. Since we learned `pandas` first, we commonly refer to `numpy` as being similar to `pandas`. However, historically `numpy` came first so it's actually `pandas` that borrowed a lot of the terminology/syntax since it came out later!

```
