# <i class="far fa-edit fa-fw"></i> Practice: Hashing

**If we do the insertions in the order of the code snippet below, what is the resulting hash table?** Assume the following:

- The hash table has 4 slots

- If there is a collision, add the new value at _front_ of the chain

- We are using the hash function: `h(v) = v % 4`

```text
nums = set()
nums.add(11)
nums.add(43)
nums.add(21)
```

## Question 0

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

```{image} https://static.us.edusercontent.com/files/3a5kYw9Yk85cRF0WuWG2KgCB
:alt: A separate-hash table with a list of 11 followed by 21 at index 1 and a list of 43 at index 3.
:width: 510
:align: center
```

_<i class="far fa-circle fa-fw"></i> Option 1_

```{image} https://static.us.edusercontent.com/files/pyVYySMVbfDvflbWmQd3L6O6
:alt: A separate-hash table with a list of 21 followed by 11 at index 1 and a list of 43 at index 3.
:width: 510
:align: center
```

_<i class="far fa-circle fa-fw"></i> Option 2_

```{image} https://static.us.edusercontent.com/files/0Ba7drq1zhDn8HBLsyuxyLjA
:alt: A separate-hash table with a list of 21 at index 1 and a list of 43 followed by 11 at index 3.
:width: 510
:align: center
```

_<i class="far fa-circle fa-fw"></i> Option 3_

```{image} https://static.us.edusercontent.com/files/Bg32Vizr20bwGCvTAd3D5rqc
:alt: A separate-hash table with a list of 21 at index 1 and a list of 11 followed by 43 at index 3.
:width: 510
:width: 510
:align: center
```

_<i class="far fa-circle fa-fw"></i> Option 4_

None of the above

## Question 1

Now for the hash table you have selected above, what should the return value be for the following call:

```text
11 in nums

```

**<i class="far fa-edit fa-fw"></i> Your Task**

Write your answer down in your own space.

## Question 2

Now for the hash table you have selected above, what should the return value be for the following call:

```text
5 in nums

```

**<i class="far fa-edit fa-fw"></i> Your Task**

Write your answer down in your own space.

## Question 3

Consider the class definition for a `Dog` class below. Which of the following implementations of `__hash__` is the best, in the sense that it is functional and does the best job at meeting the properties of a good hash function

```{snippet}
class Dog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __eq__(self, other):
        return self._name == other._name
```

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

```{snippet}
def __hash__(self):
    return hash(self._name)
```

_<i class="far fa-circle fa-fw"></i> Option 1_

```{snippet}
def __hash__(self):
    return 0
```

_<i class="far fa-circle fa-fw"></i> Option 2_

Assume `random` is a function that generates a random number.

```{snippet}
def __hash__(self):
    return hash(self._name) + random()
```

_<i class="far fa-circle fa-fw"></i> Option 3_

```{snippet}
def __hash__(self):
    return hash(self._name) + hash(self._age)
```
