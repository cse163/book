# Types and Booleans

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/dc02aef95fae4c9d9fc56b8ba8c3080f?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

## `bool` Type in Python

As mentioned before, each Python value has a value and a type. We have only seen numeric types so far `int` for integer values (e.g., `3` ) and `float` for real-number values (e.g., `3.4` ). There are many other types of data in Python. One of these types is `bool` for values that only take on the values `True` or `False` .

```{admonition} Note
:class: note

For those that know Java, this is the equivalent to Java's
`boolean`
.

```

Just like any other value, you can store `bool` s in variables.

```python
b1 = True
b2 = False
print(b1, b2)
```

With `bool` it's common to do logical operations to combine different `bool` values. Below is a sample program that shows the different operations you can use on `bool` types.

```python
b1 = False
b2 = True

# and: True if and only if both values are True
print(b1 and b2)

# or: True if either value (or both!) is True
print(b1 or b2)

# not: Negates the value of the boolean expression
#      (True becomes False, False becomes True)
print(not b2 and b1)
print(not (b2 and b1))
```

The following table shows how `and` , `or` , and `not` evaluate.

```{image} https://static.us.edusercontent.com/files/NOJE62A1lo1V9wG3GSxFedc5
:alt: TODO
:width: 480
:align: center
```

Notice that the last two lines printed different values! In this case, the parentheses matter in this example because of the **precedence of operators.** Much like with arithmetic operators like `+` and `*` , logical operators have different "order of operations" (which programmers call "precedence").

For example, the expression `1 * 2 + 3` is **not** the same as `1 * (2 + 3)` because `*` has higher precedence (you might have learned PEMDAS to remember precedence for numeric operators).

In the snippet above, `not` has higher precedence so the third `print` statement's expression is interpreted as `((not b2) and b1)` .

We won't show the full precedence table for Python, since it has many operators we haven't learned yet. But just know that order of operations matters and you can always put parentheses around expressions to force the evaluation order you want.

### Comparisons

You can also create `bool` values by doing comparisons between other values. There are additional operators in Python that let you logically compare values.

```python
x = 3
print(x < 4)   # "Is x is less than 4?"
print(x >= 5)  # "Is x greater than or equal to 5?"
print(x == 2)  # "Is x equal to 2?"
print(x != 2)  # "Is x not equal to 2?"
```

## Casting Types

You can convert a value between types with **casting**. Casting takes a value of one type and converts it to its corresponding value in another type.

For example, the following program shows how a number like `1.4` (a `float` ) can be converted to an `int` using casting.

```python
x = 1.4
print('x =', x)
print('To int:', int(x))
```

Casting has a lot of complex rules of which values can or can't be cast to another type. For example, Python provides a convenient way of converting data in text (type `str` ) to the cast-type. For example, below you can see casting can extract the value from the `str` but it might fail if it doesn't make sense to do a particular conversion.

```python
x = "1.7"
print('To float:', float(x))
print('To int:', int(x))   # This causes an error!
```
