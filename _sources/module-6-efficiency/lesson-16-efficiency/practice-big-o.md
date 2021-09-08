# <i class="far fa-edit fa-fw"></i> Practice: Big-O

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

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

$\mathcal{O}(1)$

_<i class="far fa-circle fa-fw"></i> Option 1_

$\mathcal{O}(n)$

_<i class="far fa-circle fa-fw"></i> Option 2_

$\mathcal{O}(n + 9)$

_<i class="far fa-circle fa-fw"></i> Option 3_

$\mathcal{O}(9n)$

_<i class="far fa-circle fa-fw"></i> Option 4_

$\mathcal{O}(9n + 2)$

_<i class="far fa-circle fa-fw"></i> Option 5_

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

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

$\mathcal{O}(1)$

_<i class="far fa-circle fa-fw"></i> Option 1_

$\mathcal{O}(644)$

_<i class="far fa-circle fa-fw"></i> Option 2_

$\mathcal{O}(8402)$

_<i class="far fa-circle fa-fw"></i> Option 3_

$\mathcal{O}(n)$

_<i class="far fa-circle fa-fw"></i> Option 4_

$\mathcal{O}(n^2)$

_<i class="far fa-circle fa-fw"></i> Option 5_

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

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

$\mathcal{O}(1)$

_<i class="far fa-circle fa-fw"></i> Option 1_

$\mathcal{O}(n)$

_<i class="far fa-circle fa-fw"></i> Option 2_

$\mathcal{O}(2n)$

_<i class="far fa-circle fa-fw"></i> Option 3_

$\mathcal{O}(n^2)$

_<i class="far fa-circle fa-fw"></i> Option 4_

$\mathcal{O}(n^3)$

## Question 3

For this problem, let $n$ be the length of the given list of numbers `nums` . For this problem, you will need to assume that the `max` and `min` functions will be implemented by having to search the whole list.

```python
def method(nums):
    return max(nums) * min(nums)
```

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

$\mathcal{O}(1)$

_<i class="far fa-circle fa-fw"></i> Option 1_

$\mathcal{O}(n)$

_<i class="far fa-circle fa-fw"></i> Option 2_

$\mathcal{O}(2n)$

_<i class="far fa-circle fa-fw"></i> Option 3_

$\mathcal{O}(2n + 2)$

_<i class="far fa-circle fa-fw"></i> Option 4_

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

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

$\mathcal{O}(1)$

_<i class="far fa-circle fa-fw"></i> Option 1_

$\mathcal{O}(n/2)$

_<i class="far fa-circle fa-fw"></i> Option 2_

$\mathcal{O}(n)$

_<i class="far fa-circle fa-fw"></i> Option 3_

$\mathcal{O}(n^2)$

_<i class="far fa-circle fa-fw"></i> Option 4_

$\mathcal{O}(n^2 / 2)$
