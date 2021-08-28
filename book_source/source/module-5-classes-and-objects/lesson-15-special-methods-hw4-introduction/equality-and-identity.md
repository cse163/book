# Equality and Identity


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/607ec0c54b254632b1ac27651717e5f0?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

Consider the code block below and the question: Are `l1` and `l2` equal?  

```python
l1 = [1, 2, 3]
l2 = [1, 2, 3]
```

This sounds like a simple question, but the answer can be complex since it depends on what we mean by "equal". Equality usually means one of two things:  

-  The objects have states that are equivalent. We call this     **value equality.**   

-  The objects are actually the same object. We call this     **identity equality.**   


To understand these two notions of equality, remember to think back to the memory model we could construct for this code. Recall that `l1` and `l2` refer to different `list` instances because `[1, 2, 3]` evaluates to a brand new `list` .  

```{image} https://static.us.edusercontent.com/files/CmtTeBSblCEUgH3AtpoN8bAJ
:alt: TODO
:width: 400
:align: center
```

The first notion of equality, value equality, is asking if both `list` s store the same values. In this case, we would consider them equal because they both store the same values in the same order: 1, 2, and 3.  

The second notion of equality, identity equality, is asking if both variables refer to the same list. In this case, there are two `list` objects (that just happen to have the same values inside), but they can't have the same identity because they are different objects!  

For a more familiar analogy, think about two identical twins. We might consider them to be value-equivalent, assuming (unrealistically) they are the same in all ways that matter to being "human". However, we would not consider them identity-equivalent since they are fundamentally two different people.  

To capture these two notions of equality, Python has two ways to check "equals" depending on what definition you want to use.  

-  `x == y`     compares     `x`     and     `y`     are value-equivalent.  

-  `x is y`     compares     `x`     and     `y`     's identity to see if they are the same object (i.e. identity-equivalent).  


With that knowledge, you should try to predict what the following code block will output before running the code!  

```python
l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l1

print('Compare ==')
print('l1 == l2', l1 == l2)
print('l1 == l3', l1 == l3)
print('l2 == l3', l2 == l3)
print()

print('Compare is')
print('l1 is l2', l1 is l2)
print('l1 is l3', l1 is l3)
print('l2 is l3', l2 is l3)
```

 

