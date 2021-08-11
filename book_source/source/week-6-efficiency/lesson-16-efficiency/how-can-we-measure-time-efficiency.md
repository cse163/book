# How Can We Measure Time Efficiency? 


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/5c08694990584f8c9797976a60a760fd?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Consider the following two methods to compute the sum of the numbers from 1 to some input `n` .  
```python
def sum1(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

def sum2(n):
    return n * (n + 1) // 2

print(sum1(10))
print(sum2(10))
```

The second one uses a clever formula discovered by Gauss that computes the sum of the numbers from 1 to n using the formula $$Sum(n) = \frac{n(n + 1)}{2}$$.  
**Which one is more efficient?**   
Most people probably have an intuition that the second seems better, but it's hard to state exactly "why" that's the case. Is it because it has fewer lines to code? While it's definitely shorter, it's also less easy to understand since it requires knowing this obscure formula from math.  
Remember, it's important to state what resources we care about before deciding which is more efficient. As we said before, the most common resource to worry about is **time** (if we ever omit this, you should assume we are discussing time). To answer which one is more efficient, we might actually try to write code to time how long it takes them to finish.  
The details of the snippet below are not important, but we could try timing each implementation by using the `time` package that is built into Python. `time` has a method called `time` that reports the number of seconds since the "epoch" (midnight on Jan 1, 1970 in UTC time). We can then figure out how much time each method call takes.  
```python
import time


def sum1(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


def sum2(n):
    return n * (n + 1) // 2


t0 = time.time()
sum1(10)
t1 = time.time()
sum2(10)
t2 = time.time()


# Using this fancy print syntax we introduced last time!
print(f'sum1 took {t1 - t0} seconds')
print(f'sum2 took {t2 - t1} seconds')
```

The first thing to notice is if you run this code block multiple times, we get different time results! The reason for this is that timing has a lot of uncertainty built into it. One of the biggest sources of uncertainty comes from a trick your computer is playing on you: it makes you think it's able to run many programs (Chrome, Spotify, your OS itself) at once when in reality it is quickly switching between them and running them in sequence. This comes from the fact that your computer can really only "run" one thing at a time for each processor it has (this is an oversimplification, but it works well enough). The result of this fact means that measuring time will be inexact because it depends on how frequently your computer switches away from the Python program to work on something more important!  
In this lesson, we will introduce a different notion of measuring the run-time of a program that doesn't involve relying on the inaccuracies of timing itself.  
However, timing can still give us a general idea of how fast one program is versus another (we can be more confident if we run multiple times and see the same trend). It looks like `sum1` is just a little slower than `sum2` in most runs of the code cell above.  Let's see how the times compare as we increase `n` so that we can identify how these algorithms scale. In the snippet below, we run this comparison multiple times and used some slightly more advanced plotting code to help us visualize the difference (you can click on the pop-up of the image after it runs).  

```{admonition} Warning
:class: warning

Note that understanding the code in this cell is not really relevant to this reading!

```

```python
import time

import matplotlib.pyplot as plt


def sum1(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


def sum2(n):
    return n * (n + 1) // 2


STOP_POINT = 200000000

ns = []
sum1_times = []
sum2_times = []
n = 1
while n < STOP_POINT:
    # Time both methods
    t0 = time.time()
    sum1(n)
    t1 = time.time()
    sum2(n)
    t2 = time.time()
    
    # Compute time to run and print information
    sum1_time = t1 - t0
    sum2_time = t2 - t1
    print(f'sum1({n}) took {sum1_time} seconds')
    print(f'sum2({n}) took {sum2_time} seconds')
    print()
    
    # Add to lists to keep track of times
    ns.append(n)
    sum1_times.append(sum1_time)
    sum2_times.append(sum2_time)
    
    # Update n
    n *= 4


# Plot the times (uses some advanced plotting features)
fig, ax = plt.subplots(1)
ax.plot(ns, sum1_times, label='sum1')
ax.plot(ns, sum2_times, label='sum2')
ax.set_ylabel('Time (seconds)')
ax.set_xlabel('n')
ax.set_title('Comparing run-time of sum1 and sum2')
ax.legend()
fig.savefig('sum1-vs-sum2.png')
```

Notice that `sum2` almost always takes the same amount of time to run in comparison to `sum1` , which takes time proportional to `n` ! Another way to say this is that if we double the input size `n` , it seems like `sum1` takes twice as long to run while `sum2` takes about the same time.  
This gives us more certainty that `sum2` seems more efficient, in terms of time, than `sum1` since we have empirically have seen that it scales very well. However, it would be nice if we could have some way of describing how one algorithm scales when compared to another without having to rely on something as unreliable like time (or requiring us to write so much code to measure the time).  
