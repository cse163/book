# What Does Efficiency Mean?

Programmers spend a lot of time talking about "efficiency", but what does that actually mean?  

Talking about the efficiency of a program requires coming up with some way to measure how much of a particular resource it uses in order to run. This is a very vague statement because a program could be "efficient" in one of many ways depending on which computing resource you care about. Some common examples:  

-  **Computer Time:** How much time it takes the program to run (e.g. microseconds).  

-  **Space/Memory:** How much memory your program requires to run (e.g. kilobytes).  

-  **Programmer Time:** How long did it take you to implement the program correctly (e.g. hours/days).  

-  **Energy:** How much electricity/natural resources does your program require to run (e.g. kiloWatts)  

    -  Example: [Green AI - Schwartz, Dodge, Smith, Etzioni](https://arxiv.org/pdf/1907.10597.pdf)   

Most commonly, when programmers talk about "efficiency", they are referring to the notion of time, or how long a program takes to run. However, it's always a good idea to consider how in different situations, we might value different things.  

##  How does it scale?  

Sometimes it's sufficient to only worry about how much of a resource is used for a given program input, but generally, we tend to worry about how your program will scale. What happens if we double the size of the input? Would your program require twice as much time? Four times the time?  

As data scientists and computer scientists, this is an extremely important question to us since the amount of data available is exploding rapidly. It's not good enough that our algorithm is fast "now", but we should worry about what will happen as new data comes in and we need to process more and more.  