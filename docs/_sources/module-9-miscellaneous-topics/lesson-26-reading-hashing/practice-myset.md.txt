# 🚧 Practice: MySet

{download}`Download starter code </module-9-miscellaneous-topics/lesson-26-reading-hashing/practice-myset.zip>`

##  Part 1: `MySet`   

In the file `my_set.py` , write a class named `MySet` that implements something like the `set` implemented with a hash table that we have been describing in this reading. `MySet` will be simpler than the full hash table we described in the reading and will be more similar to the first version described in the [None](https://edstem.org/us/courses/3016/lessons/7903/slides/38827) .  
Namely, the `MySet` should have the following behaviors:  
-  The     `MySet`     class should only store non-negative     `int`     values in its hash table.  
-  **You may assume the input values don't collide in the hash table.**     This means you do not need to implement separate chaining. Recall that a collision is when two different values end up at the same index.  
-  Your hash table should be fixed-size and you shouldn't ever rehash. Make your hash table be size 10 and store it as a field with type     `list`     .  

Since we are in the simplified setting where the values are just `int` s, you do not need to use the built-in `hash` function to get an index for a particular value. Instead, you should just use the function `h(v) = v % 10` to determine the index.  
Your `MySet` should implement the following methods. Some of them are special methods so we can use nicer syntax in Part 2.  
-  `__init__(self)`     that sets up any initial state you need for the other functions.  
    -  *Hint*         : Recall you can make a list of a certain length by using the syntax         `[1] * n`         which will make a list of         `n`         1s.  

-  `add(self, v)`     that adds a given value to this     `MySet`     .  
    -  *Hint*         : Make sure you think about the case if we         `add`         the same value twice!  
    -  Notice that this does not have underscores before/after the name. We are not trying to define the behavior for one of the pre-defined "special functions" (like         `__init__`         ), instead, we are defining a new function called         `add`         .  

-  `__contains__(self, v)`     returns     `True`     or     `False`     depending on whether or not the given value is in this     `MySet`     .  
    -  This allows the client to use the syntax         `5 in ms`         where         `ms = MySet()`         .  

-  `__len__(self)`     returns the number of elements in this     `MySet`     .  
    -  This allows the client to use the syntax         `len(ms)`         where         `ms = MySet()`         .  


**Requirements**   
-  You should implement these functions so that they all have complexity $\mathcal{O}(1)$. For this checkpoint, this means your program should not have any loops!  
-  All fields should be private.  
-  You should not use the     `set`     class in any way in your implementation. You should implement     `MySet`     using a     `list`     as your hash table.  

##  Part 2: `my_set_client.py`   

In the file `my_set_client.py` , write a client of `MySet` that does the following things:  
-  Imports the     `MySet`     class.  
-  Constructs a     `MySet`     instance and adds the numbers     `14`     ,     `2`     , and     `17`     and     `2`     .  
-  Prints the result of querying the     `MySet`     if it contains the value     `2`     .  
-  Prints the result of querying the     `MySet`     if it contains the value     `4`     .  
-  Prints the     `len`     of the     `MySet`     .  

**Requirements**   
-  Your program should use the main-method pattern.  
-  You should not explicitly call any of the special methods on the     `MySet`     from your program. This means instead of using     `ms.__len__()`     , you should use     `len(ms)`     .  

##  A Note About Naming Convention  

Python uses `snake_case` for almost everything. All your functions, variables, fields, and even file names should use `snake_case` . The one major exception is class names which should be `CapitalCase` (where the first letter of each word is capitalized). This is why we will call the class `MySet` but the file name will be `my_set.py` .  
