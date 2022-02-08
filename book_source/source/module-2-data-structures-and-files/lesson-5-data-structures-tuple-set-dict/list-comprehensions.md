# List Comprehensions

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/3765af6fbd7e4be69fa677ec1fdc8c77?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

In this slide, you will learn some fancy syntax to make it easier to create lists storing specific values.

So far, we have seen how you can specify a list by hand. We have used the following syntax.

```{snippet}
nums = [1, 2, 3]
print(nums)
```

What if I wanted to make a list of the numbers from 1 to 10? We could do that, but it would take a little bit more typing.

```{snippet}
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums)
```

What about numbers 1 to 100? That would be ridiculous to type out! You might be thinking back to the `list` bmethods we learned in Lesson 4, and might realize we could do build up the `list` programmatically. Here is an example using the `list` methods we have learned.

```{snippet}
nums = []
for i in range(1, 101):
    nums.append(i)
print(nums)
```

This is handy because `range` defines a sequence of numbers we are interested in, and then we just `append` them to our list.

This is a very common pattern in Python, so it provides some nice syntax called a **list comprehension** to help you build up these lists. We first show the code and then explain the parts.

```{snippet}
nums = [i for i in range(1, 101)]
print(nums)
```

This is very similar to our first approach, where we spelled out what was inside the list, like in `[1, 2, 3]` . However, now we are using a loop inside the definition of a list to help us specify the values. You should read a list comprehension in the following way (newlines and comments added for clarity)

```{snippet}
nums = [                   # 3) Store the result in a list called nums
    i                      # 2) The value you will put in the list
    for i in range(1, 101) # 1) What you are looping over
]
print(nums)
```

This is just a compact syntax for writing the full loop we showed earlier! It's a bit weird when you first see it that the `for` comes after the value, but you get used to it with practice. This syntax can be very handy for specifying things really quickly.

## Transforming Values

One of the nice things about list comprehensions is they let you pretty easily transform your values before putting them in the list. In the last example, we just put `i` in the list but that isn't the only option! For example, what if we wanted to put in the squares of all the even numbers between 1 and 10? We could write a list comprehension for that too!

```{snippet}
squares = [i ** 2 for i in range(1, 11)]
print(squares)
```

Again, you should read it in the order we showed above:

- What are you looping over? `range(1, 11)` using loop variable `i`

- What value are you storing in the result? `i ** 2` (i.e. $i^2$)

- What are we storing the result as? A `list` named `squares`

## Filtering Values

One last thing list comprehensions allow you to do is filter values from the original sequence to just the ones you want! For example, what if we only wanted the squares of numbers divisible by 3 between 1 and 10? Now you could implement this specific task by changing the `range` call to include a step-size, but you could imagine having a more complex condition that you can't simply solve it using that approach.

**Take a second to think about how we would write this without a list comprehension.**

It would be similar to our approach above that uses a call to `append` , but would be different in that it has an if-statement to only `append` some times. It would look something like the snippet below.

```{snippet}
squares = []
for i in range(1, 11):
    if i % 3 == 0:  # This is the new addition!
        squares.append(i ** 2)
print(squares)
```

Python provides a syntax for conditionally including a value in a list comprehension using an `if` statement inside the comprehension. Again, the syntax looks a bit weird at first.

```{snippet}
squares = [i ** 2 for i in range(1, 11) if i % 3 == 0]
print(squares)
```

Like before, we will write this out in another way to show what is going on:

```{snippet}
squares = [               # 4) Store the result in a list called squares
    i ** 2                # 3) What value should be stored in the result?
    for i in range(1, 11) # 1) What you are looping over
    if i % 3 == 0         # 2) Should we include the value in the result?
]
print(squares)
```

You probably are thinking that it's kind of weird to put the `if` statement after the loop at the end, and you're right, it's not super intuitive why they decided to put it there. You get used to this ordering though for the comprehension since they are so useful!
