# 🚧 Practice: Build a List Comprehension

{download}`Download starter code </module-2-data-structures-and-files/lesson-5-data-structures-tuple-set-dict/practice-build-a-list-comprehension.zip>`

Write a function called `fun_numbers` that takes a start number and stop number and returns a list of all "fun" numbers between start (inclusive) and stop (exclusive). A number is "fun" if it is divisible by 2 or divisible by 5. The result should have the numbers arranged from smallest to largest.  

You may assume the parameters are valid which means they will be integers and `start <= stop` . If there are no fun numbers in the range, it should return an empty list.  

For example, `fun_numbers(2, 16)` should produce the list  

```text
[2, 4, 5, 6, 8, 10, 12, 14, 15]
````

While the call `fun_numbers(5, 5)` should produce the empty list: `[]`   

**This is exactly the same as the practice problem from Lesson 4, but you should use a list comprehension to solve the problem instead.**   

