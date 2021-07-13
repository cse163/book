# Data Structure Time Complexity
Back in Lesson 16, we introduced the notion of run-time complexity and talked about this in the context of various complexities of the data structures we learned. Below, we introduce all the important operations for each data structure we learned with a short justification for why.  
##  List  

A `list` is a series of values, each with an index (starting at 0, then 1, and so on).  
-  Add:     `l.append(v)`     takes $\mathcal{O}(1)$ time  
    -  Just adds to the end of the         `list`   

-  Contains:     `v in l`     takes $\mathcal{O}(n)$ time  
    -  Has to search through whole list for         `v`   

-  Get:     `l[i]`     take $\mathcal{O}(1)$ time  
    -  The way         `list`         is implemented, provided instant access to a value if you know its index. This is because         `list`         s are a contiguous block of memory and it is easy for the computer to go to spot         `i`   


##  Set  

A `set` is a collection of unique values, no sense of “order”. All allowed operations are "magically" implemented in $\mathcal{O}(1)$ time.  
-  Add:     `s.add(v)`     takes $\mathcal{O}(1)$ time  
-  Contains:     `v in s`     takes $\mathcal{O}(1)$ time  

-  Get: s     `[i]`      **not allowed**   

##  Dictionary  

Like a `set` , but a `dict` maps distinct keys to values.  
-  Add:     `d[k] = v`     takes $\mathcal{O}(1)$ time  

-  Contains:     `k in d`     takes $\mathcal{O}(1)$ time  

-  Get:     `d[k]`     take $\mathcal{O}(1)$ time  

Understanding how `set` and `dict` magically do the contains operation in $\mathcal{O}(1)$ time, regardless of how much data is in the structure, is very interesting and the idea we want to understand in this lecture.  
