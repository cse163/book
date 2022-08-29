# <i class="fas fa-laptop fa-fw"></i> Practice: Count Words

{download}`Download starter code </module-2-data-structures-and-files/lesson-5-data-structures-tuple-set-dict/practice-count-words.zip>`

Write a method called `count_words` that takes a file name and returns a `dict` that stores the words as keys and values that counts the number of times that word appeared in the file. Remember a token is a sequence of characters separated by spaces.

For example, suppose we had a file called `popular_techno_song.txt` with the following contents ([source](https://answers.yahoo.com/question/index?qid=20100314111115AAz2IGy)).

```text
dun dun dun dun
dun dun dun dun
err
dun dun dun dun dun dun dun dun
dundundundundundundundundundun
er er er er er er ER ER ER ER ER ER der der der der derrr
```

If we called `count_unique_words('popular_techno_song.txt')` , it would return the `dict`

```text
{'dun': 16, 'err': 1, 'dundundundundundundundundundun': 1, 'er': 6, 'ER': 6, 'der': 4, 'derrr': 1}
```

As shown in this example, you don't need to do anything fancy with capitalization or ignoring any punctuation; you should just use the token from the file itself.

_Hint: Try to tackle this problem in parts. Start by writing the starter code like the function header and the code to go through the file word-by-word. Then think about how to store data so that you can answer how many times this particular word has appeared before and how to update it. Is there some structure we learned that lets you store values in this?_
