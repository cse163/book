# 🚧 Practice: EdPost
Write a class called `EdPost` that represents a question on the message board. The `EdPost` class should have an initializer that takes an argument for each of the 3 fields your class should have.  
-  The name of the post (a     `str`     ) stored in a field     `title`     . This parameter should not have a default value.  
-  The topic of the post (a     `str`     ) stored in a field     `tag`     . This field should have the default value     `General`     .  
-  The comments on the post (a     `list`     ) stored in a field     `comments`     . The field should have the default value of an empty     `list`     .  

**Your fields should have the names described above but should be made private.**   
Your class should have the following methods.  
-  An initializer that takes the parameters to initialize the fields as described above (in that order).  
    -  *Hint: Remember the initializer is just like any other method, except that it has a special method name.*   

-  A method named     `get_title`     that returns the title of the post.  
-  A method called     `get_tag`     that returns the tag on the post  
-  A method called     `add_comment`     that adds a comment (a     `str`     ) to this post.  
-  A method called     `display`     that prints out information about the post the following format (using     `{value}`     to be a placeholder for a value). The comments should appear in the order they were added, one on each line. Each comment should be indented by two spaces.  

```text
{title} ({tag})
Comments:
  {comment 1}
  {comment 2}
  ...
````

For example, the following main program would produce the following output  
```python
post1 = EdPost('Typo in spec?', 'Assignment 1')
post1.add_comment('There was a typo!')
post1.add_comment('And maybe another typo?')

post2 = EdPost("What's Hunter's favorite dog?")
post2.add_comment("There can't be just one!")

post1.display()

print()

post2.display()
```

```text
Typo in spec? (Assignment 1)
Comments:
  There was a typo!
  And maybe another typo?

What's Hunter's favorite dog? (General)
Comments:
  There can't be just one!

````


```{admonition} Warning
:class: warning

Many students previously reported difficulty getting the formatting right for this
`display`
output. Here are two hints:
<br />

<br />
1) Recall that reading the output of the Mark interface can be tricky. Try running the main program in the terminal to see the output.
<br />
2) Pay careful attention to the amount of whitespace you are using. It might help to replace spaces with another symbol (e.g.,
`~`
) so you can visually inspect the number of spaces you are using.

```

##  A Note on Testing  

Even though we are asking you to make your fields private, we do a bad thing and access the private fields of your class. This is so we can test your implementation matches our specification. We make this decision for its pedagogical benefit, despite its poor style.  
##  A Note About Naming Convention  

Python uses `snake_case` for almost everything. All your functions, variables, fields, and even file names should use `snake_case` . The one major exception is class names which should be `CapitalCase` (where the first letter of each word is capitalized). This is why we will call the class `EdPost` but the file name will be `ed_post.py` .  
