# Conditionals Answered

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/e375761784214d178f674ee415b0761f?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

In the previous slide, we showed the following code block and asked a couple of questions.

```py
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


## 
		What values of 
		

The only values of
`x`
that can cause the code to enter the
`else`
block are
`10`
,
`11`
, and
`12`
. Any number less than
`10`
will enter the first
`if`
while any number greater than
`12`
will enter the first
`elif`
.

## 
		Why is it not possible to enter the second 
		

Using the logic from the previous question, no value of
`x`
can satisfy this condition if it doesn't satisfy the previous two. To enter the second
`elif`
block,
`x`
would need to be some value
`>= 10`
,
`< 13`
, and
`>= 20`
. No such number exists!

