# <i class="far fa-edit fa-fw"></i> Practice: Indexes / Trees


The following questions will ask you about indexes and tree indexes.

## Question 0

Consider making an application that uses a large amount of data that has a **write-heavy workload** (this means it is more common for users to upload information to add data to the system rather than querying for information). True or false, you would expect that building a search tree index for your data will improve the performance of your system.





**📝 Your Task**

Write your answer down in your own space.

## Question 1

In your own words, describe one benefit and one downside of using a tree index on top of a dataset. Be specific and give an example.

*This question will be graded by hand for effort and accuracy.*



**📝 Your Task**

Write your answer down in your own space.

## Question 2

Order the following operation run-times from the fastest (top) to slowest (bottom).



**📝 Your Task**

Reorder the following options. Write your answer down in your own space.

*❓ Option 0*

Dict Lookup: O(1)

*❓ Option 1*

KD-Tree Building: O(knlog(n))

*❓ Option 2*

Linear Search: O(n)

*❓ Option 3*

Tree Lookup: O(log(n))

## Question 3

Consider the following sorted list of values shown in the image below. Suppose we have built a binary search tree index on this data and want to figure out how many steps to see if the value **21** is present in the dataset. We will count a single step as counting a node in the tree index for `<=` or comparing the final value in the list for if it equals the query value; this means you will count the number of nodes in the tree you visit plus one extra step for checking the value you find in the list.

```{image} https://static.us.edusercontent.com/files/bpcQtiocxqyAPO7jxlCAyiBd
:alt: TODO
:width: 691
:align: center
```

Report your answer as a number of steps (e.g., `7` )



**📝 Your Task**

Write your answer down in your own space.

## Question 4

Consider the KD-tree for a spatial index we saw in the lesson reading shown again in the picture below. Consider if we were to search for the query point that is the star shown in the image (you can click on it to see a larger version).

What is the sequence of checks we will make in order to determine that the query point is not in the dataset? Like the last problem, this is the nodes you will take down the tree including comparing the final datapoints you land at. For this problem, we want you to write down the **path** , not the just the number of checks. For example, if we were searching for the point with the same coordinates as `g` , the path would be `1,3,6,g` . You should write your answer in this format with commas in between the node labels (no spaces).

```{image} https://static.us.edusercontent.com/files/NguPgC5OZdpeR8u3fElqRMyT
:alt: TODO
:width: 691
:align: center
```







**📝 Your Task**

Write your answer down in your own space.

