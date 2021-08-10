# 🚧 Practice: Count Unique Words
Write a method called `count_unique_words` that takes a file name and returns the number of unique tokens that appear in that file.  Remember a token is a sequence of characters separated by spaces.  
For example, suppose we had a file called `song.txt` had the following contents.  
```text
I'm just goin' to the store, to the store
I'm just goin' to the store
You might not see me anymore, anymore
I'm just goin' to the store
```

If we called `count_unique_words('song.txt')` , it would return 14. This is because it contains the unique words `["I'm", "just", "goin'", "to", "the", "store,", "store", "You", "might", "not", "see", "me", "anymore,", "anymore"]` . Notice that the tokens `'store,'` and `'store'` are **different** since they are not equal. This is intentional since we don't want you to worry about removing punctuation.  
*Hint: Try to tackle this problem in parts. Start by writing the starter code like the function header and the code to go through the file word-by-word. Then think about how to store data so that you can answer how many words are unique. Is there some structure we learned that lets you store values?*   

```{admonition} Error
:class: error

Some of you might be familiar with other data structures in Python called a
`set`
or
`dict`
and could help you solve this problem. We will learn about those in Lesson 5 and 6 so we don't want you using those quite yet! Focus on using the material we have learned so far!

```

