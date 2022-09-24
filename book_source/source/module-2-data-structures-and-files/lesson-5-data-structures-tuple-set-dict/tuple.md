# Tuple

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/d82da2364b0542b69f8bdb8aca4cfe40?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

In this lesson, we will learn about a few other **data structures** . They are similar to `list` s in that they store some collection of values, but they differ in the properties and semantics of how the data structure behaves.

For example, when I say `list` , I am implying a few properties:

- There is a notion of integer indices which then provides some defined ordering to the list. There is something that comes first (index 0), something that comes second (index 1), etc.

- The `list` is dynamic in that you can add/remove values at any position in the `list` .

Other data structures might have different properties that encourage them to be used in different contexts. An analogy here comes from thinking about tools in a toolshed. A hammer and screwdriver have different properties that allow one to be the better tool for the job, say, when you want to put a nail in a wall; while yes, you could use a screwdriver for that, it seems like there is another tool that better suits the task. This is why we want to have more than one type of data structure: so we can have the best tool for any given job.

One such data structure is the `tuple` (pronounced either like "two pull" or to rhyme with "supple"). A `tuple` is much like a list in that it has integer indices, but it is different in that it is **immutable.** A `tuple` will have a pre-defined number of values inside of it, and you can't modify them!

The syntax for lists and `tuple` s look very similar but have some key differences.

- The list uses square brackets (i.e., `[1, 2, 3]` is a list) while a `tuple` uses parentheses (i.e., `(1, 2, 3)` is a `tuple`). They both have 3 elements that store 1, then 2, then 3, but while the list could be modified, the tuple can't.

- Tuples don't have any meaningful methods like `list` does since you cannot modify it.

To access values in a `tuple` , you can index into them just like lists. To prove to you that you can't modify `tuple` s, look at the following code segment:

```python
l = [1, 2, 3]
print('l[0] =',l[0])
print('l before', l)
l[1] = 14
print('l  after', l)

t = (1, 2, 3)
print('t[0] =', t[0])
print('t before', t)
t[1] = 14
print('t  after', t)
```

Notice that it prints everything before `'t after'` as it crashes on line 10 and never reaches line 11.

## Unpacking Tuples

One nice feature Python allows you to do is to "unpack" a `tuple` so that you can give a variable name to each component rather than having to specify the values by index (i.e. `t[2]` ). For example, you are allowed to write a program like the following:

```python
t = (4, 5, 6)
print(t[1] + t[2])

a, b, c = t  # "Unpacks" t so that each element gets a variable name
print(b + c)
```

It's very important that your unpacking "matches up" with the `tuple` you are unpacking. For example, the following two snippets show what happens when you try to unpack too many or too few items (both are errors).

```python
t = (4, 5, 6)
a, b, c, d = t  # Try to unpack it into 4 variables
print(b + c)
```

```python
t = (4, 5, 6)
a, b, = t  # Try to only unpack the first two values
print(a)
```

```{admonition} Note
:class: note

While you can also use this unpacking with
`list`
s, it's less common since the whole point of a
`list`
is the dynamic size and ability to modify the contents. It doesn't make as much sense to try to unpack in this manner since it's very dependent on the size of the structure.

```

## Why use this?

So far, it seems like `tuple` s are just `list` s but worse since you can't modify them. Again, it's more about what tool is right for the job. Sure, you can use a screwdriver to put a nail in a wall, but sometimes it just makes more sense to use a hammer! If you know exactly how many elements should go in your data structure, a `tuple` is right for the job! While it's not obvious why it's sometimes nice to know that the data in a `tuple` can't change. You don't have to worry about passing a `tuple` to a function and that function somehow destroying your data or messing it up.

`tuple` s normally appear as a way to return more than one value from a function. For example, if I wanted to write a function that returned both the first and second letter from a word, I could write it such that it returns both!

```python
def first_two(word):
    return  word[0], word[1]

print(first_two('goodbye'))  # ('g', 'o')

# Can unpack here as well
a, b = first_two('goodbye')
print(a)
```

In reality, Python is just implementing this with `tuple` s. The return value of `first_two('goodbye')` is the `tuple` `('g', 'o')` .

Cleverly, Python does not require you to use parentheses around the return value; Python infers you are returning a `tuple` since you returned two things separated by a comma. You can also return more than just two values (but it would need to be pre-defined and fixed-length since you have to write out the return statement!).
