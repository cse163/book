# While Loops

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/8cf97c1c51074ede9bb28a47d4761206?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

If you want to repeat some computation, a programming language usually provides a construct called a **loop** that lets you repeat code some number of times. For those that know Java, Python has very similar constructs to the for loop and the while loop.

## While Loop

A **while loop** has a **condition** and a **body.** The while loop proceeds in iterations, each iteration executes the **body** only if the **condition** is `True` , otherwise the loop ends. In general, a loop while loop looks like

```text
while condition:
    # Loop body
    statement
    statement
    statement
```

For example, the code below shows an example of a very simple loop.

```python
x = 1
while x < 100:
    print(x)
    x = x * 2

print('After loop', x)
```

Notice that the condition here is `x < 100` so the loop keeps executing the body ( `print(x)` and `x = x * 2` ) until the next iteration it is false (when `x = 128` ). After the loop ends, it continues on to the code after the loop ( `print('After loop', x)` )

```{admonition} Warning
:class: warning

It was probably easy to miss, but you need a
`:`
at the end of the first line of a
`while`
loop! This is how Python knows you are saying that this is where the condition ends and the body of the loop begins!

```

### A Very Important Point About Python

Notice in the example above, Python is somehow able to differentiate that the `print` statement at the end of the program is outside the loop! How does it decide what is inside or outside a loop? **Indentation.** Unlike other languages that use explicit delimiters (like `{}` in Java) to determine what goes inside a loop, Python only uses indentation.

In Python, getting your indentation right is very important. A very common error for beginning Python programmers comes from incorrectly indenting your code. If you see the error

```text
IndentationError: unexpected indent

```

It means there is an error with your indentation!
