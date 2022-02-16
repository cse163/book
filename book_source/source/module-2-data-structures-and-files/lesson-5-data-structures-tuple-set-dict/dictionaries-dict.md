# Dictionaries (dict)

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/117da2a64cdd4b2caaeb503b4c7dd7c7" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

For one of your practice problems for today, you will be implementing a function to find the count of each word in a file. It's not clear how you could use a `list` or `set` to solve this problem since you need to be able to answer the question: "for a given word, how many of them have we seen?"

A `list` seems like it's more on the right track, but unfortunately, the indices have to be numbers! There is no way of using a `list` to say that a word should be an index.

## Introduction to `dict`

The last data structure we are going to learn today is called a dictionary (in Python, written as `dict` ). A `dict` is a very powerful data structure since it acts, in some sense, as a more generalized `list` . Essentially a `dict` is much like a `list` , but allows you to store any type as the index while a `list` only allows numbers from `0` to `len - 1` as valid indices.

To create a `dict` in Python, you use the syntax in the following snippet. Note that `dict` supports the square-bracket notation for accessing a value, but now you can use any value for the index. In fact, `dict` uses a different term for the index to reduce confusion with `list` s: we call the "index" of an entry in a `dict` its **key**. We describe a `dict` as a bunch of key/value pairs that are accessible via the key.

```python
d = {'a': 1, 'b': 17, 47: 'scurvy'}
print(d)
# This makes a dictionary with the following keys/values:
#   The key 'a' is associated to the value 1
#   The key 'b' is associated to the value 17
#   The key  47 is associated to the value 'scurvy'

# You can get/set the value for a key using the square-bracket notation
print(d['b'])

d['dogs'] = 'cute'
print(d)

# If a key already exists in the dict, it will be overwritten if you set it
d['dogs'] = 'very adorable'
print(d)
```

The nice thing is you have a pretty solid understanding of how to use a `dict` already because you know how to use `list` s! The semantics of accessing/setting a value associated to a key are very similar to accessing/setting a value associated to an index in a `list` .

If you try to look up a key that is not in the `dict` , you will run into a `KeyError` , as shown in the following snippet. As a note, we also show how to make an empty `dict` with the syntax `{}` (just like an empty `list` is `[]` ).

```python
d = {}
d['dogs'] = 'very cute'
print(d['cats'])
```

To prevent this error, you can use the `in` keyword to see if a key is in a `dict` before trying to access it.

```python
d = {}
d['dogs'] = 'very cute'
if 'cats' in d:
    print(d['cats'])
else:
    print('No cats!')
```

## Example

Imagine we had a list of strings, and we wanted to find sum of the word lengths that start with each letter. For example, with the list `['cats', 'dogs', 'deers']` we would report the sum of the lengths of strings that start with `'c'` is 4 while the sum of the lengths of strings that start with `d` is 9. We will write a function called `count_lengths` to solve this problem. The function should take a `list` of words (all `str` ) and we can assume none of the `str` are the empty string.

This seems like the task of a `dict` where the keys are the first letters of the words, and the values are the sum of the lengths. Let's try to write a function to use the things we have seen so far to do this!

```python
def count_lengths(words):
    counts = {}
    for word in words:
        first_letter = word[0]
        counts[first_letter] = counts[first_letter] + len(word)
    return counts

print(count_lengths(['cats', 'dogs', 'deers']))
```

We ran into an error! What happened?

It turns out we crashed on the first word in the list `'cats'` . We get the first letter `'c'` and we try to get the value in the dictionary associated to the key `'c'` when we evaluate `counts[first_letter] + len(word)` . Remember though, if a key is not present, we get a `KeyError` which is exactly what happened in this snippet.

To fix this, we need to introduce a common pattern when working with `dict` s. If you are ever adding values to a `dict` , you commonly need to think about the cases:

- This is the first time we have seen the key

- We have seen the key before

Depending on which case you are in, you need to write different code to handle the fact that the key is not present in the `dict` in the first case. We can easily fix this by introducing a check that uses `in` , but the pattern does look a bit odd at first. All of the added code is inside the loop, and is there to avoid getting this `KeyError` .

```python
def count_lengths(words):
    counts = {}
    for word in words:
        first_letter = word[0]
        if first_letter in counts:
            counts[first_letter] = counts[first_letter] + len(word)
        else:
            counts[first_letter] = len(word)
    return counts

print(count_lengths(['cats', 'dogs', 'deers']))
```

To explain what this `if` -check is doing in English: If we haven't seen the key before, we can just go ahead and set it to the length of the current word. If we have seen it before, we take the current sum for this key and add on the length of the current word.

```{admonition} Note
:class: note

A very common bug when you're first working with `dict`s is forgetting this type of pattern to handle the first time you see a key.


```
