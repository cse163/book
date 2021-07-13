# For Loop

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/7b213be0506d4fcc8876aa6863e7991f?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

```{warning}
For those that know Java, the for loop in Python looks quite different than the for loop in Java!
<Element 'break' at 0x7fcd2377e3b0>

<Element 'break' at 0x7fcd2377e680>
If you have taken CSE 143, the for loop in Python behaves a lot more like the for-each loop (also called the "enhanced for loop").

```

In Python, the
**for loop**
lets you iterate over a sequence of values. The for loop has a
**body**
that runs for each item in a
**sequence**
and uses a
**loop variable**
to keep track of the current item.

We'll start by showing an example and then explain the parts.

```py
for i in range(5):
    print('Loop', i)
```

The
`for`
loop has the following components

<Element 'list' at 0x7fcd23760130>
The
`for`
loop operates very similarly to the
`while`
loop, but the key difference is it will loop over the sequence of values specified after the
`in`
keyword. Just like the
`while`
loop, you put a
`:`
at the end of the line containing the keyword
`for`
and the body is indented inside the loop.

## 
		


`range`
is a function in Python provided to make it easy to make sequences of numbers in a range. It turns out, there are three different ways to call
`range`
that let you do slightly different types of loops!

<Element 'list' at 0x7fcd26033810>
There is no reason that these numbers have to be positive! For example, you can use negative numbers for the start/stop or use a negative step size to make the numbers decrease instead! The semantics are exactly the same!

