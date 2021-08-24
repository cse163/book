# Strings


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/c3d8b5eb6e194b05932ba6331c001740?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

You should have seen strings in your previous programming course. As a reminder, a string is a common data type in programming languages to represent text. In Python, the name of the type `str` represents a string (we use String and `str` interchangeably in this text for readability, but Python always refers to them as `str` ).  

In Python, you define a `str` by putting texts in quotes as shown in the following snippet. You can use either a `'` or a `"` , they are the same (but the opening one has to match the closing one).  

```python
s1 = 'hello world'
s2 = "CSE 163 is fun!"

print(s1)
print(s2)
```


```{admonition} Note
:class: note

Which quotation mark you use is a matter of personal preference. Generally it's best to just pick one and be consistent throughout your program as much as possible. Hunter prefers single quotes, but that's just a preference! 😊
<br />

<br />
It's acceptable to deviate from your preferred style when you want to work with a string that contains a character like
`'`
(e.g. the
`str`

`"you won't"`
). In that case, it would not work to define a
`str`
like
`'you won't'`
since Python would read the apostrophe as the closing of the string. So if you want to use one of the quotation marks inside the
`str`
, that means you have to use the other type outside to wrap the
`str`
(e.g.
`"you won't").`


```

##  String Concatenation  

Strings provide lots of ways of accessing and transforming the text data to do almost anything you want! One of the most common things you want to do with strings is to combine them. In the following snippet, we use **string concatenation** to add on one string to the end of another  

```python
s1 = 'hello world'
s2 = "CSE 163 is fun!"

print(s1 + s2)

```

The `+` operator in this context will work with two values of type `str` to create a new `str` that has the characters from the first followed by the second. Importantly, this does not modify either of `s1` or `s2` , but rather creates a new string that has the same characters as both of them. In fact, strings are what we call **immutable** , meaning that you can't change the characters of a particular string at all!  

Take a second and think about what the following code snippet should be based on this description of string concatenation before pressing Run... ... ... Okay! Press Run! Did it do what you expected?  

```python
s = 'hello world'
n = 163
print(s + n)
```

It crashed! What happened?!?!  

If you previously had known Java, you probably expected it to do what Java does in this situation and turn the `163` (which is of type `int` ) into a `str` and then do `str` concatenation. Python instead says that string concatenation is only defined between two values that are both of type `str` . It doesn't want to do any of this magic conversion between types for you.  

To fix this, you have to explicitly turn the value `163` into a `str` ! You could easily just change the code to wrap the value `163` in quotes so it is `'163'` , but that only works under a very narrow set of circumstances. Instead, we will use casting (from [None](https://edstem.org/us/courses/3016/lessons/7871/slides/38559) ) to convert the number into a `str` since this is a strategy that works in many situations!  

The fixed code snippet would look like the following:  

```python
s = 'hello world'
n = 163
print(s + str(n))
```

##  String Indexing  

When we think of strings, we commonly think of them as a sequence of characters, where each character has an **index** in the string. For example, the string `'hello world'` should really be thought of as a sequence of characters in the image shown below. Each character has its own spot in the sequence, and the spots are ordered starting at index 0 going up to the end of the string.  

```{image} https://static.us.edusercontent.com/files/aBbZgPzwwhJOQ5ZP73ZtqsFn
:alt: TODO
:width: 743
:align: center
```

Python lets you access a character at a specific index by using this `[]` notation to index into the `str` itself. Consider the following code snippet ( *think about what it will print before you press run).*   

```python
s = 'hello world'
print(s[0])
print(s[2])
print(s[10])
```

Each of these goes into the string, and grabs and returns the character at the particular index.  

Trying to get the last character is a very common operation, so it would be annoying to have to count by hand how many characters you need to go till the end. Thankfully, Python provides a way to find the number of characters, called the **length** , of the string. If you have a `str` named `s` , then using the built-in function `len` tells you the number of characters in it.  

Let's try to grab that last character using the `len` function in the following snippet  

```python
s = 'hello world'
print('Length of string:', len(s))
print('Last character:', s[len(s)])
```

The crash this time was because we went "out of bounds" of the string. What went wrong? Well if you look at the first line of output, it actually succeeded in printing out the length. For this string, the length is `11` . So we then tried to access `s[len(s)]` which is the same as `s[11]` . See the problem here?  

The last valid index of this string is 10. Even though there are 11 characters, the valid indices go from 0 to 10. This is precisely because the first index of the string starts at 0. To fix this, we need to ask for one-index earlier in our code.  

```python
s = 'hello world'
print('Length of string:', len(s))
print('Last character:', s[len(s) - 1])
```

##  Looping over a String  

Suppose that I needed to print the characters of a string out, one on each line. We can still use all the programming constructs we've seen in the past to help us solve problems!  

One idea to solve this is to use a for loop that loops over all the possible indices. The loop would need to start at 0 (inclusive) to the length of the string (exclusive).  

```python
s = 'hello world'
for i in range(len(s)):
    print(s[i])
```

This works perfectly well, but Python provides a much clearer way to loop over a sequence of values like a `str` . To understand how this works, we first have to think hard about the for loop above works.  

How does the for loop know to start `i` at `0` , then `1` , then `2` , then all the way to `len(s) - 1` ? This is how the `range` function is defined based on the parameter. A for loop simply iterates over the sequence you tell it to. The trick here is that we have to think carefully about how to call the `range` function, so that the sequence of values it returns represent valid indices in our `str` . <br />  <br /> So if a for loop can loop over a sequence of indices returned the case, would it also be possible to just loop over the `str` directly? Earlier, we defined a `str` as a sequence of characters, so it seems like it should be a candidate to be looped over. That intuition is exactly right! The following snippet shows how to do this!  

```python
s = 'hello world'
for c in s:
    print(c)
```

The first value in this sequence is `'h'` , then `'e'` , etc., which is the exact same sequence of values the loop variable `c` will take on over the iterations of the loop!  

