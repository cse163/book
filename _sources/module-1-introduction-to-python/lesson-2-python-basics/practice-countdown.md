# <i class="fas fa-laptop fa-fw"></i> Practice: Countdown

{download}`Download starter code </module-1-introduction-to-python/lesson-2-python-basics/practice-countdown.zip>`

This problem is very similar to the last practice problem, but now we want you to write a function called `countdown` that takes a starting number of seconds and starts the countdown from there instead (still counting by 10s). The format of the output will be slightly different to accommodate this starting point.

If the sequence does not evenly end with a `0` (e.g. if the countdown starts from `15` ), then `0` will not be printed. This shown in the example calls below.

The `countdown` function should take one `int` parameter for the starting point. You may assume the parameter is an `int`. If the parameter value is less than `0` , it should instead print `Start must be non-negative!` .

Here are four example calls to the function and their output is shown after ( `print` statements included to space out output).

```python
countdown(60)
print()
countdown(15)
print()
countdown(-4)
print()
countdown(0)
```

```text
60 second countdown
60
50
40
30
20
10
0
Done!

15 second countdown
15
5
Done!

Start must be non-negative!

0 second countdown
0
Done!
```

_Hint: The lines of numbers should all be produced by your for loop while the first and last lines will appear outside the loop (since they only happen once)._

## Requirements

- Your solution should use a `for` loop and should not use a `while` loop.

- Your program should use the main-method pattern (we provided the starter code) and should define a function named `countdown` (as described above) before the `main` method.
