# Slow Python


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/5e53d4b490bf4898b12b866867fdb631?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

We have briefly mentioned that Python generally uses an interpreter to run. This is opposed to how you might have used Java CSE 142/143 where you compiled your program before you ran it. When you interpret a program, you are essentially compiling it **as you run it** . This requirement to translate your code from human-readable Python to computer-understandable computer instructions while it is running causes a huge slow-down for Python. On top of being interpreted, the fact that variables store values of dynamic types also tends to add to this inefficiency.  
##  Computer Language  

Programs written in languages like Python are readable by humans but are not readable by computers. A compiler or interpreter's job is to translate this human-readable code to something the computer can understand.  
##  Compiled and Statically Typed  

Consider this example snippet from the programming language C. Notice, it is very similar to Python, but we specify the types in front of the variable name.  
```c
/* C code */

int a = 1;
int b = 2;
int c = a + b;
```

When people usually use C, they use a compiler to translate their C code into something the computer can understand (commonly `gcc` ). This roughly translates to machine instructions in the following way  
```text
Assign <int> 1 to a
Assign <int> 2 to b
call add<int, int>(a, b)
Assign <int> the result to c

````

One of the big benefits of this usage of C is the fact that this translation happens before you run the program in a step called **compiling** . When you compile the program, you pre-translate the programming language to the computer language. That way when you actually go to run the program, you can run this pre-compiled program to avoid the cost of translating while you run.  
##  Interpreted and Dynamically Typed  

Python brings a whole new set of challenges to this translation because the variables can store any type of data. Additionally, it's common for this translation to computer language to happen in an **interpreter** that runs at the same time the program is running. By default when you just use the provided `python` command, it is interpreting your code.  
Consider the equivalent Python program.  
```python
a = 1
b = 2
c = a + b
```

This roughly maps to the machine instructions:  
```text
1. Assign 1 to a
  1a. Set a->PyObject_HEAD->typecode to integer
  1b. Set a->val = 1
2. Assign 2 to b
  2a. Set b->PyObject_HEAD->typecode to integer
  2b. Set b->val = 2
3. call add(a, b)
  3a. find typecode in a->PyObject_HEAD
  3b. a is an integer; value is a->val
  3c. find typecode in b->PyObject_HEAD
  3d. b is an integer; value is b->val
  3e. call add<int, int>(a->val, b->val)
  3f. result of this is result, and is an integer.
4. Create a Python object c
  4a. set c->PyObject_HEAD->typecode to integer
  4b. set c->val to result

````

There are a TON of steps here even though the high-level programs are doing basically the same thing! Most of the extra steps come from the fact that Python needs to take extra steps to identify what the types of the values are (since the variables can store dynamic types),  
Note that the specific output here is actually made up, so don't put too much emphasis on trying to understand each step of these made-up machine codes. The important thing to realize is that there are more lines, and most of the extra lines come from the work Python does behind the scenes to allow dynamic typing.  
##  Comparing Models  

So if even a simple program that just makes variables can have so many machine-instructions, you might be able to imagine how much more complex (and slower) things get once you start adding in concepts like looping (e.g., on each iteration of the loop you have to double-check the type of the loop variable each time you access it).  
So part of the reason Python tends to be slower is that these extra steps to check types just lead to more instructions to run than an equivalent C program. The other big slow down comes from the fact that we commonly use a Python interpreter, which is also doing this translation to machine code on the fly as you run the program. Both of these factors in combination can lead to some **significant** slowdowns in real programs.  
For example, consider the programs below in C and Python to manually compute `m * n` using loops. You wouldn't actually write this code in practice, but it's a nice way to show why looping in Python is slow. Note that EdStem hides the fact that they first compile the C code before you run it, while they just immediately run the Python interpreter on the Python. You'll find the Python code runs MUCH slower than the C version (assuming the Python version doesn't time out).  
```python
m = 10000
n = 25000

product = 0
for i in range(m):
    for j in range(n):
        product += 1

print('Product is:', product)
```

```c
#include <stdio.h>

int main() {
    int m = 10000;
    int n = 25000;

    int product = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            product++;
        }
    }

    printf("Product is: %d", product);

    return 0;
}
```

So while this example is awfully contrived, you can see that one program that takes a long time in Python can be executed very quickly in C.  
##  Why the Difference in `max_diff` times?  

So now that we have this comparison between Python and C, you might be wondering how this relates back to seeing a difference in runtime between `max_diff2` and `max_diff3` from our earlier example.  
Hopefully, it is clear why `max_diff1` is the slowest (because it is an $\mathcal{O}(n^2)$ algorithm.  
The real question comes from why `max_diff3` was faster than `max_diff2` . This has to do with the fact that many of the Python built-in functions are implemented in this language C! This means by calling out to them instead, you are making your program faster because it gets to use the benefits of the speed of C.  
So not only is it more readable to use the `max` function rather than writing it yourself, it tends to be much faster too since you can avoid interpreting as much Python code.  
##  Why Use Python  

Even though Python is slow, it has a lot of benefits going for it that make it a *fantastic* language to use, especially for data scientists.  
-  It is way easier to program than languages like C. Even though its is fast to run, trying to write a correct program in C is a pain in the *#!$@! For example, students in CSE 333 are currently doing an assignment just like your take-home asseement 4 with a search engine but in C. The search engine itself is the easy part of the HW for them, but writing it in C is the hard part 🤯  
    -  This is important because developer time is also a valuable resource! Sometimes it's best to be able to write something quick and easy for other people to read (in Python).  This lets you iterate on ideas and experiment with prototypes rather than pre-maturely trying to optimize by writing a program in a difficult to use language like C.  

-  Python provides incredible support for pre-compiled libraries to leverage the best of both worlds. For example, consider     `pandas`     . Most of the library is actually written in C! By letting them figure out how to write the gross, efficient code, we can leverage it with the nice Python syntax while still gaining speed benefits. This is why we made you avoid loops with     `pandas`     in HW2 and HW3. Writing a loop for something that can be done with     `pandas`     itself is WAY slower.  

If you find your program is running slower than you expected, use a profiler to identify the slower part of the program. More likely than not, you can rewrite that portion to use a pre-compiled library like `pandas` to speed up your program! <br />   

```{admonition} Note
:class: note

Editor's Note: It's technically incorrect to say that one language is faster/slower than another. A programming language is just a language defining what words and grammar is allowed. It puts no constrains on how the program can be run. To those that study the design and implementation of programming languages, saying "Python is slow" makes as little sense  as the claim "The English language is faster than the Japanese language".
<br />

<br />
People often confuse the language itself for the tools we generally use to run programs in the language. The language Python is different than the program
`python`
that runs Python programs you write (kind of meta to think about a program running your program, no?). It might be the case that the design of the language lends itself to be run in an interpreter rather an a compiler, there technically isn't a fundamental limitation between the two. There exists compilers that turn Python code into machine code, but those tools tend to not be very popular since their artificats are usually not very fast and it makes it hard to use other tools in the Python ecosystem.
<br />

<br />
It's also not the case that programming languages that don't force you to write down types are slower. There are many languages (see SML) that don't require you to write types down, but have very strict rules that allow for certain operations on data in how they automatically infer types. Python's lack of type annotations and the fact that they allow very flexible use of variables, make it pretty tough to write sound type-checkers for their programs.
<br />

<br />
However, we state the technically incorrect "Python is slow" idiom here since it's easier to say and has the right sentiment even though it is technically wrong.L

```

