# <i class="fas fa-laptop fa-fw"></i> Practice: Fibonacci

{download}`Download starter code </module-1-introduction-to-python/lesson-2-python-basics/practice-fibonacci.zip>`

Write a function named `fibonacci` to compute the first Fibonacci number larger than a given value `n` .

The Fibonacci Sequence is the following sequence of numbers: 1, 1, 2, 3, 5, 8, 13, ... The sequence starts with 1 and 1. The next number in the sequence is the sum of the previous two.

Your function should **return** the first Fibonacci number in the sequence that exceeds the given value `n` . For example, the following snippet that uses your function shows the output in the comments next to each line.

```python
print(fibonacci(3))  # 5
print(fibonacci(6))  # 8
print(fibonacci(-2)) # 1
```

_Hint: You will want to store the previous two numbers in the sequence in variables, one to keep track of the current number and one to keep track of the previous. The next number is the sum of `curr` and `prev`._

## Requirements

- Your solution should have the main-method pattern. You do not need to define any other functions for this problem!
