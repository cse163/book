# <i class="fas fa-laptop"></i> Practice: count_votes

{download}`Download starter code </module-1-introduction-to-python/lesson-3-strings-and-lists/practice-count_votes.zip>`

Write a function called `count_votes` that takes a list of numbers indicating votes for candidates 0, 1, or 2 and returns a new `list` of length 3 showing how many counts each candidate got. For example:

```python
votes = [1, 0, 1, 1, 2, 0]
result = count_votes(votes)
print(result)  # [2, 3, 1]
```

The returned list has a 2 at index 0 because a 0 appeared twice in the votes.

### Requirements

- You may assume the input `list` only contains values that are 0, 1, or 2.

- You should not modify the contents of the list.
