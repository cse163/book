# <i class="fas fa-laptop fa-fw"></i> Practice: Filter Long Lines

{download}`Download starter code </module-2-data-structures-and-files/lesson-4-lists-and-files/practice-filter-long-lines.zip>`

Write a method called `filter_long_lines` that takes a file name and a minimum number of words and prints out all of the lines in the file with at least that many words (tokens separated by spaces).

For example, suppose we had a file called `song.txt` had the following contents.

```text
I'm just goin' to the store, to the store
I'm just goin' to the store
You might not see me anymore, anymore
I'm just goin' to the store
```

If we called `filter_long_lines('song.txt', 7)` , it would print the output below because these are all the lines with 7 or more words.

```text
I'm just goin' to the store, to the store
You might not see me anymore, anymore
```

We have provided more scaffolding for you for this checkpoint so you don't have to write as much. All the file-processing stuff is your job though!

_Hint 1:_ You will want to use some of the string functions from [String Functions](/module-1-introduction-to-python/lesson-3-strings-and-lists/string-functions.md) to process each line of the file to find the ones with the right number of words.

_Hint 2:_ You can use the `len` function on lists too!
