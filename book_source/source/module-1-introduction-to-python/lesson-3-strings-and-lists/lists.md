# Lists


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/a9b0a03d46324244bc0feae35720118a?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

As a reminder, we defined a string as a sequence of characters, where each character has an index; we often refer to strings as being an indexed-sequence of characters for short.  

A few slides back, we learned of some string functions (e.g. `upper` , `lower` , `split` ). Recall that we defined the `split` function to break up some string based on a delimiter (a special character separating values), but we did not really explain what the type of the value returned was.  

Consider the following snippet.  

```python
s = "I'm just going to the store, to the store"
print(s)
print(s.split())
```

The first thing to point out in this example is that we didn't pass any parameter to `split` even though the table in our String Functions slide showed it taking a `delim` parameter! This is because by default (if you don't pass in a delimiter), `split` will break up the string by whitespace.  

The second thing to point out is that that return value broke up all the words in the string and is showing them all! What is the type of that result? It's a `list` . A `list` is an indexed-sequence of values of any type. In some sense, a string is like a special case of a `list` since it is an index-sequence of characters specifically.  


```{admonition} Note
:class: note

For those of you that know Java, a
`list`
is a lot like an array. So in this case, the return type is something like a
`String[]`
. We'll see that this analogy doesn't quite hold up because a
`list`
in Python can do so much more (as we'll see in Lesson 4)!

```

The great thing about `list` s in Python, is that they share a lot of the same syntax for operations as `str` s. The following snippet shows you all of the string syntaxes we learned this lecture also applies to lists.  

```python
l = ['dog', 'says', 'woof']

# Length
print(len(l))         # 3

# Indexing
print(l[1])           # 'says'
print(l[len(l) - 1])  # 'woof'

# Slicing
print(l[1:3])  # ['says', 'woof']
print(l[:1])   # ['dog']

# Looping
for i in range(len(l)):
    print(l[i])

for word in l:
    print(word)
```

Some key differences/things to point out:  

First, to specify the values of a `list`, the syntax uses square brackets around a comma-separated list of values (of any type).  

```python
l1 = ['I', 'love', 'dogs']
l2 = [7, 8, 9]
l3 = ['I', 3, 'dogs']  # can mix types too!
```

Second, because this is now a `list`, not a `str` , the values returned by indexing are different. By indexing into index 0 of `l1` , it returns the value that's in that index (in this case, the `str`  `'I'` ). Similarly, when you slice into a `list` you get a `list` back (although it's shorter).  

##  Assignment  

One way `list` s are able to do a bit more than `str` s comes from the fact that you are allowed to change the contents of a list by assigning into it. Just like you can use an index to get a value out of a list, you can use an index to set a value at a particular spot.  

```python
l1 = ['I', 'love', 'dogs']

print(l1)

l1[0] = 'You'

print(l1)
```

