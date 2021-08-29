# <i class="far fa-edit fa-fw"></i> Practice: Hashing

**If we do the insertions in the order of the code snippet below, what is the resulting hash table?** Assume the following:

-  The hash table has 4 slots

-  If there is a collision, add the new value at     *front*     of the chain

-  We are using the hash function:     `h(v) = v % 4`


```text
nums = set()
nums.add(11)
nums.add(43)
nums.add(21)
````

## Question 0





**📝 Your Task**

Select one option. Write your answer down in your own space.

*❓ Option 0*



```{image} https://static.us.edusercontent.com/files/3a5kYw9Yk85cRF0WuWG2KgCB
:alt: TODO
:width: 510
:align: center
```



*❓ Option 1*



```{image} https://static.us.edusercontent.com/files/pyVYySMVbfDvflbWmQd3L6O6
:alt: TODO
:width: 510
:align: center
```



*❓ Option 2*



```{image} https://static.us.edusercontent.com/files/0Ba7drq1zhDn8HBLsyuxyLjA
:alt: TODO
:width: 510
:align: center
```



*❓ Option 3*



```{image} https://static.us.edusercontent.com/files/Bg32Vizr20bwGCvTAd3D5rqc
:alt: TODO
:width: 510
:align: center
```



*❓ Option 4*

None of the above



## Question 1

Now for the hash table you have selected above, what should the return value be for the following call:

```text
11 in nums

````



**📝 Your Task**

Write your answer down in your own space.

## Question 2

Now for the hash table you have selected above, what should the return value be for the following call:

```text
5 in nums

````



**📝 Your Task**

Write your answer down in your own space.

## Question 3

Consider the class definition for a `Dog` class below. Which of the following implementations of `__hash__` is the best, in the sense that it is functional and does the best job at meeting the properties of a good hash function

```python
class Dog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __eq__(self, other):
        return self._name == other._name
```



**📝 Your Task**

Select one option. Write your answer down in your own space.

*❓ Option 0*

```python
def __hash__(self):
    return hash(self._name)
```



*❓ Option 1*

```python
def __hash__(self):
    return 0
```



*❓ Option 2*

Assume `random` is a function that generates a random number.

```python
def __hash__(self):
    return hash(self._name) + random()
```



*❓ Option 3*

```python
def __hash__(self):
    return hash(self._name) + hash(self._age)
```



