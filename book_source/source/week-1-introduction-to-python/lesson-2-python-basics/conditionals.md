# Conditionals


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/c1af397581d1469c90f707a968c58022?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Conditional statements let you execute code conditionally based on some condition; they are similar in nature to the `while` loop but only run at most once.  
In Python, the keywords to control these conditionals are `if` , `elif` (read "else if") and `else` . For those that know Java, these keywords exactly match the semantics of Java's `if` , `else if` and `else` keywords.  
A conditional block is an `if` block optionally followed by any number of `elif` blocks optionally followed by at most one `else` block.  
```python
x = 14
if x < 10:
    print('A')
elif x >= 13:
    print('B')
elif x >= 20:
    print('Not possible')
else:
    print('C')
```

This code prints `B` because the first `if` test fails ( `x < 10` is `False` ) and then the second test succeeds ( `x >= 13` is `True` ) so we enter the second body.  
Two questions you should consider:  
-  What values of     `x`     enter the     `else`     statement?  
-  Why is it not possible to enter the third block (the second     `elif`     block)?  

You should think about these questions before clicking onto the next slide to see the answer!  
