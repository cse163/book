# 🚧 Practice: Largest Earthquake
##  Data  

For this problem, we will be using a dataset containing information about earthquakes around the world. The dataset looks like the following (but it has more rows).  
```{image} https://static.us.edusercontent.com/files/oaCPDgcs0UnvR6oJUZNfHVZP
:alt: TODO
:width: 758
:align: center
```

The dataset is stored in a shared location on Ed with the path  
```text
/course/lecture-readings/earthquakes.csv 

````

##  Problem  

Write a function named `largest_magnitude` that takes a parameter `data` that stores this earthquakes dataset represented as a list of dictionaries as a parameter. It should return the name of the location that experienced the largest earthquake in the dataset. If there are no rows in the dataset, it should return `None` .  
If you only look at the rows of the dataset shown above, the result would be `'Burma'` because it had the earthquake with the largest magnitude (4.9).  
You should not assume the dataset passed has the exact same values or the number of rows like the one shown above. For example, you should not assume the dataset has more than one row. However, you should assume the dataset provided will have all of the columns provided for any row in the dataset (we sometimes call the set of columns of a CSV its **schema** ).  
Note that you do not need to worry about how to parse the data from the CSV format to the list of dictionaries. We implemented this functionality in `cse163_utils.py` and already wrote the code in the main method to call that function for the earthquakes file.  
