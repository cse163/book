# Data Structure Time Complexity
Back in Lesson 16, we introduced the notion of run-time complexity and talked about this in the context of various complexities of the data structures we learned. Below, we introduce all the important operations for each data structure we learned with a short justification for why.

## List

A
`list`
is a series of values, each with an index (starting at 0, then 1, and so on).

<Element 'list' at 0x7fcd2377e630>
## Set

A
`set`
is a collection of unique values, no sense of “order”. All allowed operations are "magically" implemented in $\mathcal{O}(1)$ time.

<Element 'list' at 0x7fcd26044f40>
## Dictionary

Like a
`set`
, but a
`dict`
maps distinct keys to values.

<Element 'list' at 0x7fcd26044b30>
Understanding how
`set`
and
`dict`
magically do the contains operation in $\mathcal{O}(1)$ time, regardless of how much data is in the structure, is very interesting and the idea we want to understand in this lecture.

