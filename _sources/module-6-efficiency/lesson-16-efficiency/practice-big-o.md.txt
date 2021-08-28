# 🚧 Practice: Big-O

For the following problems, select which Big-O complexity best describes the run-time of the program. The complexities should be in terms of their input size $n$ (described for each problem).  

## Question 0

For this problem, let $n$ be the input value `n` .  

```python
def method1(n):
    value = 0
    for i in range(n):
        for j in range(9):
            value += 7 * i + j
    return value ** 2 
```



**📝 Your Task**

Select one option. Write your answer down in your own space.

*❓ Option 0*

$\mathcal{O}(1)$  



*❓ Option 1*

$\mathcal{O}(n)$  



*❓ Option 2*

$\mathcal{O}(n + 9)$  



*❓ Option 3*

$\mathcal{O}(9n)$  



*❓ Option 4*

$\mathcal{O}(9n + 2)$  



*❓ Option 5*

$\mathcal{O}(n^2)$  



## Question 1

For this problem, let $n$ be the input value `n` .  

```python
def method(n):
    t = 0
    for i in range(3):
        for j in range(14):
            t += n
        
        for j in range(200):
            t += j
    return j
```



**📝 Your Task**

Select one option. Write your answer down in your own space.

*❓ Option 0*

$\mathcal{O}(1)$  



*❓ Option 1*

$\mathcal{O}(644)$  



*❓ Option 2*

$\mathcal{O}(8402)$  



*❓ Option 3*

$\mathcal{O}(n)$  



*❓ Option 4*

$\mathcal{O}(n^2)$  



*❓ Option 5*

$\mathcal{O}(n^3)$  



## Question 2

For this problem, let $n$ be the length of the given list of numbers `nums` .  

```python
def method(nums):
    max_diff = None
    for n1 in nums:
        for n2 in nums:
            diff = n1 - n2
            if max_diff is None or diff > max_diff:
                diff = max_diff
    return max_diff
```

 



**📝 Your Task**

Select one option. Write your answer down in your own space.

*❓ Option 0*

$\mathcal{O}(1)$  



*❓ Option 1*

$\mathcal{O}(n)$  

 



*❓ Option 2*

$\mathcal{O}(2n)$  



*❓ Option 3*

$\mathcal{O}(n^2)$  



*❓ Option 4*

$\mathcal{O}(n^3)$  



## Question 3

For this problem, let $n$ be the length of the given list of numbers `nums` . For this problem, you will need to assume that the `max` and `min` functions will be implemented by having to search the whole list.  

```python
def method(nums):
    return max(nums) * min(nums)
```



**📝 Your Task**

Select one option. Write your answer down in your own space.

*❓ Option 0*

$\mathcal{O}(1)$  



*❓ Option 1*

$\mathcal{O}(n)$  



*❓ Option 2*

$\mathcal{O}(2n)$  



*❓ Option 3*

$\mathcal{O}(2n + 2)$  



*❓ Option 4*

$\mathcal{O}(n^2)$  



## Question 4

For this problem, let $n$ be the length of the given list of numbers `nums` .  

```python
def method(nums):
    x = len(nums)
    t = 0
    for i in range(x * x / 2):
        t += i
    return t
```



**📝 Your Task**

Select one option. Write your answer down in your own space.

*❓ Option 0*

$\mathcal{O}(1)$  



*❓ Option 1*

$\mathcal{O}(n/2)$  



*❓ Option 2*

$\mathcal{O}(n)$  



*❓ Option 3*

$\mathcal{O}(n^2)$  



*❓ Option 4*

$\mathcal{O}(n^2 / 2)$  



