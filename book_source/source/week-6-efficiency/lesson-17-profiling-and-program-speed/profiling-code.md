# Profiling Code


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/90ee7401ddbb412a87347a5a333c7476?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Think back to our example of finding the maximum difference between elements in a list.  
```python
def max_diff1(nums):
    # Find the max difference between any pair of nunber
    max_diff = 0
    for n1 in nums:
        for n2 in nums:
            diff = abs(n1 - n2)
            if diff > max_diff:
                max_diff = diff
    return max_diff

def max_diff2(nums):
    # Realize the max difference is the same as the max 
    # number minus the min number
    min_num = nums[0]
    max_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return max_num - min_num

def max_diff3(nums):
    # Same as max_diff2 but uses Python built-ins
    return max(nums) - min(nums)
```

Even though we saw that `max_diff2` and `max_diff3` have the same Big-O runtime, which one do we think is faster? It turns out `max_diff3` is **MUCH** faster in practice.  
##  Profiler  

*
			Note: Ed does not have the following tool installed, so we describe its output rather than actually running it for you! If you are interested in trying this out, you can install it from your terminal using 
			*  *on your computer if you are using Mac/Linux. For Windows, you will likely need to use the Anaconda Navigator to install it.*   
An easier way to identify the relative runtime of programs is to use something called a **profiler** . A profiler is a program that helps you analyze the runtime of the programs you write. Profilers are beneficial because they can give you more detailed information with relatively little code. Particularly with profiling, we rarely care about the raw times themselves, but rather, the times relative to other functions.  
A common profiler is the `line_profiler` package (also called `kernprof` ). `kernprof` is nice because it lets you annotate your functions with an `@profile` tag to have it profile your method. For example, the following snippet shows a file called `test.py` that defines these three functions with an `@profile` annotation above each function.  
```python
# File: test.py

@profile
def max_diff1(nums):
    """
    Returns the largest difference between any two numbers in the given list.

    Assumes there is at least one number in the list.
    """
    max_diff = 0
    for n1 in nums:
        for n2 in nums:
            diff = abs(n1 - n2)
            if diff > max_diff:
                max_diff = diff
    return max_diff


@profile
def max_diff2(nums):
    """
    Returns the largest difference between any two numbers in the given list.

    Assumes there is at least one number in the list.
    """
    min_num = nums[0]
    max_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    return abs(max_num - min_num)


@profile
def max_diff3(nums):
    """
    Returns the largest difference between any two numbers in the given list.

    Assumes there is at least one number in the list.
    """
    return max(nums) - min(nums)


@profile
def main():
    nums = list(range(5000))
    print(max_diff1(nums))
    print(max_diff2(nums))
    print(max_diff3(nums))


if __name__ == '__main__':
    main()
```

Now, we can run this program in the profiler, we use the command `kernprof -v -l test.py` (assuming you have it installed) and get the following output.  
```text
Total time: 24.1163 s
File: test.py
Function: max_diff1 at line 5

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     5                                           @profile
     6                                           def max_diff1(nums):
     7                                               """
     8                                               Returns the largest difference between any two numbers in the given list.
     9
    10                                               Assumes there is at least one number in the list.
    11                                               """
    12         1          1.0      1.0      0.0      max_diff = 0
    13      5001       1585.0      0.3      0.0      for n1 in nums:
    14  25005000    6858540.0      0.3     28.4          for n2 in nums:
    15  25000000    9716627.0      0.4     40.3              diff = abs(n1 - n2)
    16  25000000    7537822.0      0.3     31.3              if diff > max_diff:
    17      4999       1736.0      0.3      0.0                  max_diff = diff
    18         1          1.0      1.0      0.0      return max_diff

Total time: 0.006862 s
File: test.py
Function: max_diff2 at line 21

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    21                                           @profile
    22                                           def max_diff2(nums):
    23                                               """
    24                                               Returns the largest difference between any two numbers in the given list.
    25
    26                                               Assumes there is at least one number in the list.
    27                                               """
    28         1          1.0      1.0      0.0      min_num = nums[0]
    29         1          0.0      0.0      0.0      max_num = nums[0]
    30      5001       1664.0      0.3     24.2      for num in nums:
    31      5000       1804.0      0.4     26.3          if num < min_num:
    32                                                       min_num = num
    33      5000       1746.0      0.3     25.4          elif num > max_num:
    34      4999       1643.0      0.3     23.9              max_num = num
    35
    36         1          4.0      4.0      0.1      return abs(max_num - min_num)

Total time: 0.000135 s
File: test.py
Function: max_diff3 at line 39

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    39                                           @profile
    40                                           def max_diff3(nums):
    41                                               """
    42                                               Returns the largest difference between any two numbers in the given list.
    43
    44                                               Assumes there is at least one number in the list.
    45                                               """
    46         1        135.0    135.0    100.0      return max(nums) - min(nums)

Total time: 39.8858 s
File: test.py
Function: main at line 49

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    49                                           @profile
    50                                           def main():
    51         1        124.0    124.0      0.0      nums = list(range(5000))
    52         1   39873513.0 39873513.0    100.0    print(max_diff1(nums))
    53         1      12023.0  12023.0      0.0      print(max_diff2(nums))
    54         1        146.0    146.0      0.0      print(max_diff3(nums))
````

This output shows both how long each function took to run (in the output above the function code) as well as how much time was spent on each line inside each function. You can see that even for `n=5000` , `max_diff1` took 20 seconds to run! While `max_diff2` and `max_diff3` look close in runtime in comparison, `max_diff3` still runs about 50x faster than `max_diff2` !  
To understand why `max_diff3` is the fastest, we need to discuss why Python is a very slow language by design.  
