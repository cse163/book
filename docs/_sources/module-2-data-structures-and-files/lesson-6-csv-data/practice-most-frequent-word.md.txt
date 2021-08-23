# 🚧 Practice: Most Frequent Word

{download}`Download starter code </module-2-data-structures-and-files/lesson-6-csv-data/practice-most-frequent-word.zip>`


```{admonition} Note
:class: note

Notice we put this practice problem above the "Pause and Think" because we think it would be more useful for you to try this problem before coming to class! We will have some time to go over it earlier in the class, but it would help if you are most of the way done solving a problem so you and your group can hit the ground running!
<br />

<br />
This practice problem will also be a little bit different since we provide almost all of the code. Most of the content is the reading material here, but we do ask you to make a change to the program to fix some bugs!

```

Let's consider an example using these more advanced dictionary methods to continue one of the problems you worked on last time. For this problem, we are going to try to find the most frequent word in a file. We will suppose we have already implemented and run your code from Lesson 5 to get the counts of each word in a file. Recall, the format of the result is a `dict` where the keys are words, and the values are counts.  
```text
{'green': 2, 'eggs': 6, 'and': 3, 'yam': 2}
# Not a typo, this is the vegetarian-friendly version

````

##  Problem  

We want to write a function called `most_frequent` that takes this `dict` described above as input and returns the word that appears most frequently. If the given `dict` is empty, it should return `None` . You do not need to handle the tie-cases where two words have the same frequency.  
We have provided some starter code for this problem, but it has some bugs. Below, we outline the pseudo-code (i.e., step-by-step strategy) for what our solution is trying to do. Do note that since our solution has some bugs, it might slightly miss the mark on doing one of the things we intended it to do!  
-  Initialize     `max_word`     to keep track of which key (i.e., a word in this example) has the highest count. We start it as     `None`     so we can handle the case when the     `dict`     is empty.  
-  Loop through the     `dict`     to look at each word  
-  For each word, get its count and compare it to the count for the word we currently think is the most frequent word. If we see the count of this word is larger, we set     `max_word`     to this word.  
-  Return the most frequent word.  

Your task is to fix the bugs we introduced in this program so that it successfully passes all the tests! You might want to refer to the "Common Python Errors" link on the [None](https://courses.cs.washington.edu/courses/cse163/20sp/resources.html) .  
