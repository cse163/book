# Hashing

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/23e3681131f24f77ad70f256ecf7fbb0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

The secret is that `set` and `dict` use a trick called **hashing** to make everything constant time ($\mathcal{O}(1)$ time). Our class will focus on `set` , but almost everything is analogous for `dict` .

We will explain what hashing is shortly, but the reason it is fast relies on the fact that a `list` allows instant access for some, known, integer index (e.g. `l[14]` ).

```{admonition} Big Idea
:class: note

Create a large `list` to store the values. We call this list a **hash table**. Each value should get a special spot in the `list` so we know exactly where the index is for a given value, allowing instant access to it. The method of determining an index from a value is called a **hash function.**
```

Hash functions are a generic idea of being able to transform a value of any type into an index of the hash table. In the example we show below, we use the values being integers as well but later we will show how to define other hash functions for different types.

## An Example: `set` of `int`

Suppose I wanted to make a `set` of `int` s like in the code cell below. Our goal is to figure out how this structure is interpreted internally such that it can add and check membership of values in $\mathcal{O}(1)$ time. After the code cell, we illustrate how we use this big idea from above to implement this `set` . Below, we show a line of code in the gray code-block and then explain how it affects the hash table idea discussed above.

```{snippet}
nums = set()
nums.add(11)
nums.add(49)
nums.add(24)
print(49 in nums)  # True
print(5 in nums)   # False
```

### Walkthrough

```text
nums = set()
```

From the big idea above, we start by making a large `list` called a **hash table** that has many places to store values. We make the table start with size 10 and since there are no values in it yet, it corresponds to the empty set.

```{image} https://static.us.edusercontent.com/files/fCU2l2bZQGZpjECIWDPT7hUK
:alt: A pictorial representation of the array [None, None, None, None, None, None, None, None, None, None]
:width: 743
:align: center
```

```text
nums.add(11)
```

For this problem, we will tell you the function we will use to get the index a particular value will be stored at, called the **hash function,** is `h(v) = v % 10` . What this means is that for any given value `v` , its index in the hash table will be `v % 10` . (You might already see a potential problem with this approach. Don't worry, we promise that this will work with some later modifications).

Since we are adding the number `11` , its hash value will be `1` (because `11 % 10 == 1` ). We will store the value `11` in index `1` .

```{image} https://static.us.edusercontent.com/files/NKAXurhkfvkPfdmNRKYS3d1G
:alt: A pictorial representation of the array [None, 11, None, None, None, None, None, None, None, None]
:width: 743
:align: center
```

```text
nums.add(49)
```

Like before, we compute the hash value for `49` and get `9` . Therefore, we store the value `49` in index `9` .

```{image} https://static.us.edusercontent.com/files/C12rOvbyYRFCkN4n3V5OQbdu
:alt: A pictorial representation of the array [None, 11, None, None, None, None, None, None, None, 49]
:width: 743
:align: center
```

```text
nums.add(24)
```

Like before, we compute the hash value for `24` and get `4` . Therefore, we store the value `24` in index `4` .

```{image} https://static.us.edusercontent.com/files/a5SMfDjIJy4dlSsP89l9xeU8
:alt: A pictorial representation of the array [None, 11, None, None, 24, None, None, None, None, 49]
:width: 743
:align: center
```

So far, we haven't given much intuition as to why this actually helps us answer membership-queries efficiently. Let's look at the next line of code that needs to look up a value to make the value of this structure clearer.

```text
print(49 in nums)
```

With how we have set up this hash table, how might we answer the question "Is the value `49` inside this `set` ?" If we were just treating this like any other `list` , we would have to search all the indices to find the value. However, we have defined some special structure in the hash table by putting the values in special places. There is only one valid place the value `49` could go in this hash table. Where is it?

If you're thinking index `9` , that's exactly right! We will use the same hash function to help us find values. Since we look at index `9` and we see a `49` there, we can report the value `49` is in the `set` , therefore returning `True` .

The hash function itself will be a cheap operation ($\mathcal{O}(1)$ time). Accessing the value in a `list` for a given index is also $\mathcal{O}(1)$ time, so we can find the value `49` in $\mathcal{O}(1)$ time!

Maybe that's just a fluke, let's try to find a value not in the `set` .

```text
print(14 in nums)
```

What index should `14` go to according to the hash function? `4` !

When we look at index `4` , we see the value `24` . This does not match `14` (so we know `14` is not in the set!) Therefore we should return `False` .

This is exactly how a `set` answers the contains query in $\mathcal{O}(1)$ time! All it does is use a large hash-table and use a hash function to define which index a particular value belongs to.

There are still some questions we have to answer though to make this really work. We will get to how to solve these questions in the following slides.

- What happens if I tried to add the number `19` to the `set` above? This would cause confusion since the value `49` is already in index `9` . This is called a **collision.** We will have to come up with some way of doing **collision resolution.**

- How do we write hash functions for other data other than `int` s? What if the values were `str` instead?
