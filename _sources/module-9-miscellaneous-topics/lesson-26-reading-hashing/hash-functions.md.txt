# Hash Functions


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/a55d32cc2e0947249fc4455c6ec6b375" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Our last step to making a fully functional hash table is to define how we can hash values other than integers. For example, what if we wanted to make a `set` of `str` ? How could we possibly figure out which index a `str` goes into based on its value?  

A **hash function** is a function we define to do just that. A hash function is a function that takes a value of some type, and converts it into a number for hashing. So from the hash table's perspective, it just calls `hash` on its input and uses the return value to determine which index the input belongs in!  

A hash function needs to satisfy the following properties:  

-  Needs to return an integer. This integer does not need to be constrained in value (e.g., it can be as large/small as you want and can also be negative).  

    -  We don't put these constraints on the hash because our hash table will take these numbers to appropriately convert it to an index. A hash table implementation will take any hash it gets back from a hash function and transforms it to a valid index for its table by taking the absolute value of the hash and modding it by the table length.  


-  Needs to be "consistent". This essentially means that objects that are equal should return the same value for their hash function. More on this constraint in the next slide.  


This is all pretty abstract right now and it will hopefully make more sense when we describe some example hash functions for `str` s. Before that, we should highlight two additional properties that we will want of a hash function to be considered a "good" hash function to be used in practice.  

-  First, you want your hash function to spread out the values as much as possible. In the extreme case, consider the hash function     `h(v) = 0`     . This is a valid hash function according to our properties above but is a terrible hash function to use in practice. Why? It sends all the values to the same index of the hash table which defeats the purpose of using hashing in the first place!  

-  Second, you want to make it difficult for someone to predict what the hash function will output for a given input. This is to prevent malicious users from trying to create collisions by figuring out values that end up with the same hash. If we make the hash function complex enough, it protects us from someone trying to misuse the hash table. You don't want the hash function to actually be random (since that would make "consistency" hard), but you want it to look random so it's harder for someone to predict.  


##  `str` Example  

Let's consider some various implementation of `__hash__` for the `str` class to see how to come up with a hash function that is both works and is good. Remember that a hash function needs to convert an object of some type to an `int` .  

###  Attempt 1: Length of `str`   

The simplest hash function you could probably think of to take a `str` and output its `len` . If you used this hash function with this implementation, you would see the following behavior.  

```python
hash('')     # 0
hash('hi')   # 2
hash('abc')  # 3
```

This function definitely works since it follows our first two properties. Unfortunately, it doesn't quite follow the properties of a good hash function. First, not all string lengths are equally likely, so it won't utilize the whole range of possible integers (most words have fewer than 20 characters). Secondly, it's very easy for someone to come up with strings that collide. Just pick two strings of the same length!  

Valient first effort, but let's try something else.  

###  Attempt 2: ASCII values  

As we've discussed before, a computer is only able to understand binary (1s and 0s). This means, at the end of the day, almost any piece of data on your computer needs to be represented as a number so it can easily be translated to binary; text data is no exception.  

Your computer uses an encoding to represent each character in some text as a number. A common encoding is called ASCII (the American Standard Code for Information Interchange). In ASCII, the letter `'a'` is represented as the number 97, `'b'` is 98, `'c'` is 99, etc. Every character in the English language (including symbols like `.` , `:` , `!` ) get a number associated for them.  

So then a more clever hash function could take each `str` and turn it into the sum of the ASCII values of its characters. In the snippet below, we show some example computations for the same strings as before.  

```python
hash('')     # 0
hash('hi')   # 104 (h) + 105 (i) = 209
hash('dog')  # 97 (d) + 111 (o) + 103 (g) = 314 
```

This is approach is definitely better than the first attempt! It will use a much wider range of outputs since it includes more information about the string. Unfortunately, it turns out to not be very difficult to cause collisions. Can you figure out two strings that will collide with each other?  

You might notice that *anagrams* , or words that are made up of the same letters in different orders, will end up colliding using this approach. For example , `'dog'` and `'god'` have the same sum of ASCII values.  

###  Attempt 3: Better Sum of ASCII Values  

Instead of just doing a straight-sum of the ASCII values, most programming languages use a slightly more advanced approach to using their hash functions. They generally use a formula like the one shown below. The specifics details of the formula aren't important. What is important is to understand that it tries to improve upon Attempt 2 by including the position of the character in the sum. It does this by multiplying each character's value by a number raised to a power based on the character's index.  

$$hash(s) = \sum_{i=0}^{n-1}s[i]\cdot 31^{n-i-1}$$  

The more important idea here is that trying to include every piece of information possible about your object is best since it causes a better spread of values.  

