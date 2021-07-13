# File Processing

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/620e2a3aca0a45b0ba52c7913f725375?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

**Files** on computers store some type of data. This data could be pictures, a word document, a video game, etc. For the first part of this class, we will only work with files that store text data. One such file type that holds text data is the `.txt` file type.  
For example, if you are using a Mac or Linux system (or are on Ed!), you can open up a terminal and use the `cat` program to print out the contents of a file. Suppose I had a file called `poem.txt` on my computer. If I ran the following command in my terminal, it would print:  
```text

		
````

##  Files in Python  

With Python, you can open and read files using the `open` built-in function. The syntax is shown in the following snippet. Note that the value you pass into the `open` is a **path** to the file. We will talk about file paths in a bit, but think of it like a full-name of a file on a computer!  
```py
with open('/course/lecture-readings/poem.txt') as f:
    content = f.read()  # returns the file contents as a str
    print(content)
```

This syntax looks a little confusing, but the reason why it's necessary is a bit outside of the scope of our class. While maybe a little less satisfying, we will just have to memorize that `with` syntax since it is the "right way" of opening a file in Python. The only thing you really need to take note of on this syntax is the variable name for the file object comes after the `as` keyword. So in the example above, the variable name `f` will refer to the file we just opened inside the `with` block.  

```{admonition} Warning
:class: warning

Even though we don't expect you to understand the details of why this pattern is necessary, you should
**always**
use this
`with`
statement syntax when working with files in Python, including any assessments in CSE 163.

```


```{admonition} Note
:class: note

If you're curious, it has to do with how reading/writing to files is managed by your operating system. Whenever you open a file, it uses some resources in the operating system. A very common bug in programming is to forget to "close" the file to relinquish those resources. The
`with`
syntax we have shown above automatically closes the file when you are done with it so you don't have to think about it at all!
<br />

<br />
This is kind of like the person who doesn't put a shopping cart back after taking their groceries to their car. You don't want to be that person. Instead of having to write the code to close it explicitly, just use this fancy
`with`
syntax to do it for you!

```

A very common pattern is to read the file **line by line** so that you can process each line on its own. We could accomplish this with the `split` function on the content of the file, but Python conveniently provides a `readlines` function on the file object that returns the lines in a list of strings.  
For example, the following code snippet will print out the file with a line number in front of each line. In this example `lines` will store a list of each line in the file and our loop over that just keeps track of a counter and prints that before the line itself.  
As a minor detail, each line will still contain a special **new-line** character ( `\n` ) at the end. To make sure our output doesn't have extra new-lines in it, we `strip` each line to remove this trailing whitespace.  
```py
def number_lines(file_name):
    """
    Takes a file name as a parameter and prints out the file 
    line by line (prefixed with that line's line number)
    """
    with open(file_name) as file:
        # Get the lines from the file
        lines = file.readlines()
        
        line_num = 1
        for line in lines:
            line = line.strip()
            # Remember we have to cast line_num to a str!
            print(str(line_num) + ': ' + line)
            line_num += 1

            
def main():
    number_lines('/course/lecture-readings/poem.txt')
        

if __name__ == '__main__':
    main()
```

So while the code is getting more complex, all of the code kind of falls into solving one of 3 sub-tasks of the problem:  
-  The standard main-method pattern code and defining the function for     `number_lines`   
-  The standard code for opening a file (     `with open...`     ) and to read the lines of a file (     `f.readlines()`     )  
-  The rest is just a problem we could have solved from Lesson 3 that involves looping over a list!  

It usually helps to try to "chunk" the code like this in your head so it makes it more manageable to read!  
##  Processing Token by Token  

Another very common task when processing files, is to also break up each line into each **token** in the line. A token is similar to the notion of a "word" but is generalized to any series of characters separated by spaces. In CSE 163, we commonly use the word "word" and "token" interchangeably to mean a sequence of characters separated by spaces. For example, the string `'I really <3 dogs'` has 4 tokens in it (we would also count it as having 4 words since we are not interested in differentiating between valid English words).  
For example, what if we wanted to print out the number of odd length words on each line? For the file above, our program we want to write should output  
```text
1: 2
2: 1
3: 0
4: 3

````

This might sound complicated at first, but we can actually use what we know about strings in Python to solve this in our loop over the lines of the files. Why? **Because each line is just a string!** Recall, there is a really useful string method called `split` that lets us break apart a string into parts based on some delimiter (in this case, spaces).  
It will help to start by solving a sub-part of this problem before trying to solve the entire thing. What if I was given a string, and wanted to count the number of odd-length words in that string? You could write code that splits the string up by spaces and then loops over that list of words to count up all the ones with odd lengths.  
```py
s = 'I am a really cool sentence.'
words = s.split()
count = 0
for word in words:
    # If the length has a remainder when divided by 2, it's odd
    if len(word) % 2 == 1:
        count += 1

print('Number of odd-length words:', count)
```

Now that we have this sub-problem solved, we can tackle the larger problem of doing this task above multiple times, once for each line in the file.  
We start with the code with the general pattern of looping over the lines of a file  
```py
def count_odd(file_name):
    """
    Takes a file name as a parameter and prints out the file 
    line by line (prefixed with that line's line number)
    """
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            # Do something with line
```

Now that we have that starter code, we can go ahead and use the ideas we saw to count the number of odd length words in a single line inside this loop over the lines! The only other thing that needs to be added is some book-keeping to keep track of the line number for printing.  
```py
def count_odd(file_name):
    """
    Takes a file name as a parameter and for each line
    prints out the line number and the number of odd length words on that line.
    """
    with open(file_name) as file:
        lines = file.readlines()
        line_num = 1
        for line in lines:
            # Break the line into words (this also removes trailing whitespace)
            words = line.split()
            
            # Count the number of odd-length words in this line
            odd_count = 0
            for word in words:
                if len(word) % 2 == 1:
                    odd_count += 1
                    
            # Print it out!
            print(str(line_num) + ': ' + str(odd_count))
            line_num += 1

    
def main():
    count_odd('/course/lecture-readings/poem.txt')
        

if __name__ == '__main__':
    main()
```

