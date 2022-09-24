# Data Structures

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/005a2fbfe4f84e548189f6dfd9ce639a?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

So we can see that understanding complexity is important so that you can easily analyze (after some practice) how your algorithm will scale. Another important application of this knowledge is to understand how efficient your code is when using data structures like `list` , `set` , and `dict` .

## List

For example, consider a `list` with $n$ elements in it. It is useful to know that if you `append` a value to the `list` , this will take $\mathcal{O}(1)$ time; this means it's always a constant-time operation no matter how many elements are in it. Not all operations take the same amount of time though.

For example, to run `x in l` where `l` is a `list` , how much time would that take? You might notice it depends on if `x` is in `l` and if it is, where in `l` it is found. Internally, `in` is implemented like the following code snippet.

```python
def in_implementation(l, x):
    """
    Example showing how x in l might be implemented
    """
    for val in l:
        if val == x:
            return True
    return False
```

This means the run-time depends on where `x` is in the `list` ! It turns out that computer scientists tend to think about the worst-case, so when they describe the Big-O of an operation, we usually assume we are talking about the worst possible case (where `x` is not in the `list` or is near the end). This means we describe the `in` operator for `list` s as a $\mathcal{O}(n)$ operation, where the worst case it will have to search through approximately $n$ things.

## Set and Dictionary

One of the magic things about `set` and `dict` , is that almost all of the operations (e.g., adding values, removing values, seeing if something is in the `set` / `dict` ) are actually constant time ($\mathcal{O}(1)$)! That means no matter how much data is stored in them, they can always answer questions like "is this value a key in this `dict` " in constant time. To do this, they use this special trick called "hashing" that we will learn about in future modules.

## An Example

To understand why knowing these differences in performance, think back to the example we used when we introduced `set` s. Recall that we had a file and wanted to count the number of unique words in the file. We came up with two implementations that were nearly identical, except one used a `list` and the other used a `set` . These implementations are shown in the cell below.

```python
def count_unique_list(file_name):
    words = list()
    with open(file_name) as file:
        for line in file.readlines():
            for word in line.split():
                if word not in words:  # O(n)
                    words.append(word) # O(1)
    return len(words)

def count_unique_set(file_name):
    words = set()
    with open(file_name) as file:
        for line in file.readlines():
            for word in line.split():
                if word not in words:  # O(1)
                    words.add(word)    # O(1)
    return len(words)
```

We mentioned it was really that `not in` part of the `list` version that was slowing it down. This is precisely because `not in` for `list` is an $\mathcal{O}(n)$ operation while for `set` , it is $\mathcal{O}(1)$! The analysis ends up being a little bit more complex since the size of the list is changing throughout the program (as you add unique words), but with a little work you can show that the `list` version of this program takes $O(n^2)$ time where $n$ is the number of words in the file while the `set` version only takes $\mathcal{O}(n)$ time.
