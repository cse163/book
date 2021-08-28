# Slicing Strings


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/ab6d2d5e55744fd6b100f1fc9c7d4e74?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

So we already saw how to index into a string to get a value, but what if you wanted to index into a string to get more than one character (e.g. get the first 10 characters of a string)? Python provides a very powerful syntax for accessing multiple characters in a string called **slicing.**   

The syntax slicing looks very similar to simple indexing but lets you specify a start and a stop index separated by a colon `s[<start>:<stop>]` . The start index is inclusive and the stop is exclusive. For example, you could type the following:  

```python
s = 'hello world!'
print(s[2:7])
```

The slice shown above means "all characters starting at index 2 and up to (not including) 7" (because stop is exclusive, just like with `range` ). If you take this with the picture below, it can clarify why the cell above prints `llo w` .  

```{image} https://static.us.edusercontent.com/files/SQ9WeD8h3lvhbiC8txniO4Rd
:alt: hello world string indexing
:width: 743
:align: center
```

Below, we show some more examples. Feel free to try modifying this to test out your own examples! Notice, you can use more complex start/stop indices like an expression based on the length of the string.  

```python
s = 'hello world!'
print(s[2:5])
print(s[0:len(s)])
print(s[1:len(s)-3])
```

It's very common that you either want to start from the beginning of the string or go to the end in a slice. Python provides a short-hand syntax to infer the start/stop point of a slice by omitting the start/stop value by omitting them before/after a `:` .  

For example, if you were to write the following:  

```python
s = 'hello world!'
print(s[:3])
```

Python infers that the start should be 0 since the start was omitted in the `start:stop` slice.  

Additionally, you can omit the stop point and it will go to the end  

```python
s = 'hello world!'
print(s[3:])
```

##  Step Size  

The last thing that comes up with specifying slices is the fact that you can also specify a **step size** for a slice. For example, you might want *every other* character between 2 (inclusive) and 8 (exclusive). To do this, you can write the following  

```python
s = 'hello world!'
print(s[2:8:2])
```

Notice this behaves exactly the same as the `range` function! Your intuition there for how the step size works applies here.  

##  Recap  

-  Python lets you ask for multiple characters in a sequence using this slice syntax  

-  You can specify a start/stop/step size just like you could with range  

-  You can also leave out a start/stop/step and it infers it for you  


