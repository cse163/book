# <i class="fas fa-laptop fa-fw"></i> Practice: Shakiness by Location

{download}`Download starter code </module-2-data-structures-and-files/lesson-6-csv-data/practice-shakiness-by-location.zip>`

For this problem, we will use the same earthquakes dataset as the last problem.

We want you to write a function named `shakiness_by_location` that takes a parameter that represents the earthquakes dataset from the last problem in the list of dictionaries format. This function should return a `dict` that stores how "shaky" each location in the dataset is. To define what this means, the return value should be a `dict` whose keys are location names and whose values are the sum of all the earthquakes' magnitudes that occurred at that location. If there are no earthquakes in the dataset, it should return an empty `dict` .

For example, suppose our dataset stored in a variable named `data` contained the following rows (only showing the `name` and `magnitude` columns since those are the only relevant ones).

```text
[
    {'name': 'Seattle', 'magnitude': 4},
    {'name': 'Genovia', 'magnitude': 6},
    {'name': 'Seattle', 'magnitude': 3.5}
]
```

Then the call `shakiness_by_location(data)` would return

```text
{'Seattle': 7.5, 'Genovia': 6}

```

Like the last problem, you should not assume anything about the number of rows in the dataset or their values, but you may assume it has all the columns as the dataset used in the last problem.
