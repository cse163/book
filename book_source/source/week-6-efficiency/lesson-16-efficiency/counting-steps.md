# Counting Steps

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/ae9ee85dfe704826b74eaf3d413b5ee3?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Instead of trying to measure time, we will instead count "steps" the program takes. This is a very inexact approximation and will feel weird at first but is a very helpful exercise.  
To get an intuition for this, try clicking the "next" button through [None](http://www.pythontutor.com/visualize.html#code=def%20sum1%28n%29%3A%0A%20%20%20%20total%20%3D%200%0A%20%20%20%20for%20i%20in%20range%28n%20%2B%201%29%3A%0A%20%20%20%20%20%20%20%20total%20%2B%3D%20i%0A%20%20%20%20return%20total%0A%20%20%20%20%0A%0Adef%20sum2%28n%29%3A%0A%20%20%20%20return%20n%20*%20%28n%20%2B%201%29%20//%202%0A%20%20%20%20%0A%0Aprint%28sum1%2810%29%29%0Aprint%28sum2%2810%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) with `sum1` and `sum2` . Which of the methods do you have to press "next" on more often? It seems like you have to press "next" twice for every iteration of the loop in `sum1` while for `sum2` , you can just press "next" twice overall (no matter how big `n` is).  
This idea of how many times you have to press "next" in a tool like PythonTutor is exactly the idea for how many "steps" it takes to run a function. We will use these simplified rules to determine the number of steps for a program:  
-  A "simple" line of code takes one step to run. Some common simple lines of code are:  
    -  `print`         statements  
    -  Simple arithmetic (e.g.         `1 + 2 * 3`         )  
    -  Variable assignment or access (e.g.         `x = 4`         ,         `1 + x`         )  
    -  List or dictionary accesses (e.g.         `l[0]`         ,         `l[1] = 4`         ,         `'key' in d`         ).  

-  The number of steps for a sequence of lines is the sum of the steps for each line. By a sequence of lines, we mean something like the code block below (which would have a total of 2 steps)  
    -  ```text
        x = 1
print(x)
        ````



-  The number of steps to execute a loop will be the number of times that loop runs multiplied by the number of steps inside its body.  
-  The number of steps in a function is just the sum of all the steps of the code in its body. The number of steps for a function is the number of steps made whenever that function is called (e.g if a function has 100 steps in it and is called twice, that is 200 steps total).  

This notion of a "step" is very loosey-goosey on purpose and we will see later that it's not important that you get the exact number of steps correct as long as you get an approximation of their relative scale (more on this later). Below we show some example code blocks and annotate their number of steps in the first comment of the code block.  
```py
# Total: 1 step

print(1 + 2 * 3 / 2 % 4)  # 1 step
```

```py
# Total: 4 steps 

print(1 + 2)    # 1 step
print('hello')  # 1 step
x = 14 - 2      # 1 step
y = x ** 2      # 1 step 
```

```py
# Total: 21 steps

print('Starting loop')          # 1 step

# Loop body has a total of 2 steps. It runs 10 times for a total of 20
for i in range(10):             # Runs 10 times 
    print(f'On iteration {i}')  #   - 1 step
    print(i ** 2)               #   - 1 step
```

```py
# Total: 51 steps

print('Starting loop')  # 1 step

# Loop body has a total of 1 step. It runs 30 times for a total of 30
for i in range(30):     # Runs 30 times
    print(i)            #   - 1 step
    
# Loop body has a total of 2 steps. It runs 10 times for a total of 20
for i in range(10):     # Runs 10 times
    print(i)            #   - 1 step
    print(i ** 2)       #   - 1 step
```

What about if we introduce nested loops (we put extra lines to make room for our comments).  
```py
# Total: 521 steps

print('Starting loop')   # 1 step

# Loop body has a total of 26 steps. It runs 20 times for a total of 520
for i in range(20):      # Runs 20 times
    print(i)             #   - 1 step

                         #   Loop body has a total of 1 step. 
                         #   It runs 25 times for total of 25.
    for j in range(25):  #   - Runs 25 times
        print(i * j)     #       - 1 step
```

The nice thing is that for the nested loop case, there is nothing really new!  
