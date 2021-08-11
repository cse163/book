# Zip


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/ff2cbac74ed743bbafe62257da8601d1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

In our next example, we will need to use a very useful function in Python called `zip` . It takes two lists and "zips" them up so you can iterate over pairs of elements from both lists. This is much clearer with an example.  
```python
x = [1,2,3]
y = [4,5,6]
z = zip(x, y)

for p in z:
    print(p)
```

The result of a `zip` is pairs of values from each list! The first values from both lists, then the second values, then the third, and so on. This can be clearer by looking at this picture showing the result of `zip`   
```{image} https://static.us.edusercontent.com/files/h3Jlor1N0B1k8kobm1o9vClc
:alt: TODO
:width: 666
:align: center
```

###  Warning  

It turns out the return type of `zip` is not actually a `list` of these pairs! Try printing out the result of `zip` .  
```python
x = [1, 2, 3]
y = [4, 5, 6]
z = zip(x, y)
print(z)
```

It returns a special `zip` object (also called `zip` ) instead of a `list` ! The `zip` object is what we call a **generator.** It's like a `list` in the sense that it is a sequence of values you can iterate over in a loop, but it's different because you can't actually index into it! Try editing the last block to `print(z[1])` to see that this fails.  
The reason `zip` does not return a `list` is that the operation is **lazy** . It doesn't want to compute the entire sequence of values right away and, instead, waits to compute the pairs as needed. This is exactly like the `range` function! It does not produce a `list` of numbers, but instead is a generator of them.  
A common trick if you want to get all the pairs into a list would be to just convert it to a `list` manually like in the block below.  
```python
x = [1, 2, 3]
y = [4, 5, 6]
z = list(zip(x, y))
print(z)
```

