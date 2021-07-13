# Comma Separated Values (CSV)

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/d590b946c39840f2ac6ad61ebe184a17" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

The first type of data we will explore this quarter will be a well-structured type of text-data called a CSV. If you are familiar with an Excel Spreadsheet, you already understand the basic idea behind what a CSV is!  
Consider a spreadsheet of TA salaries:  

| Name  |Salary|
|-------|-----:|
|Madrona|     3|
|Rit    |     1|
|Ryan   |     3|

A table has two main components to it:  
-  Rows: In this example, each row corresponds to one TA  
-  Columns: Each column defines a different aspect or component of your data. In this case we have one column for the TA's name and the other for the TA's salary.  

A CSV file is just a well-formatted file that preserves this tabular structure of rows/columns in a format that is more easily read by programs written in Python. The CSV file that corresponds to this table looks like the following  
```text
Name,Salary
Madrona,3
Rit,1
Ryan,3
````

Notice that each row appears on its own line and each column value is separated by a comma (hence the name Comma Separated Values). It's usually conventional to have the first line of the CSV store the names of the columns so that you can refer to them by name later.  
