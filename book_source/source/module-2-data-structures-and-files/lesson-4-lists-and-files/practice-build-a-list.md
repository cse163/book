# 🚧 Practice: Build a List

{download}`Download starter code </module-2-data-structures-and-files/lesson-4-lists-and-files/practice-build-a-list.zip>`


```{admonition} Note
:class: note

Notice we have this practice problem before the Pause and Think! We think it would be a good idea to try to do this one
**before**
coming to the class-session!

```

Write a function called `fun_numbers` that takes a start number and stop number and returns a list of all "fun" numbers between start (inclusive) and stop (exclusive). A number is "fun" if it is divisible by 2 or divisible by 5. The result should have the numbers arranged from smallest to largest.  
If there or no fun numbers within the range `start` (inclusive) and `stop` (exclusive) (e.g. if `stop` is less than `start` meaning the range doesn't have any numbers in it), the function should return an empty list.  
For example, `fun_numbers(2, 16)` should produce the list  
```text
[2, 4, 5, 6, 8, 10, 12, 14, 15]
````

While the call `fun_numbers(5, 5)` should produce the empty list: `[]`   
