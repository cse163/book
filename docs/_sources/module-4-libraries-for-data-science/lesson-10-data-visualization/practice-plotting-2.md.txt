# 🚧 Practice: Plotting 2

{download}`Download starter code </module-4-libraries-for-data-science/lesson-10-data-visualization/practice-plotting-2.zip>`

In this problem, we will work with the same iris dataset, but this time the dataset contains some missing values. As a reminder, the dataset has the columns  

-  `sepal_width`     for the width of the flower's sepal  

-  `sepal_length`     for the length of the flower's sepal  

-  `petal_width`     for the width of the flower's petal  

-  `petal_length`     for the length of the flower's petal  

-  `species`     for which species of iris it is (one of     `'setosa'`     ,     `'versicolor'`     , or     `'virginica'`     ).  


For this problem, we have provided no starter code so you will need to recreate it from the last problem! The dataset is stored in `iris_missing.csv` (remember, you will need to specify it as `/home/iris_missing.csv` on Ed).  

First, make a **regression plot** of the dataset stored in `df` with the petal length on the x-axis and the sepal length on the y-axis. The color of the points and the line should be green (use code `'g'` )! Any rows with missing values should be given a value of 0. Look back at the lesson to identify which functions you can use to help you make this plot.  

Second, customize the plot using `matplotlib` to set the following properties  

-  The x-axis should be labeled     `Petal Length (cm)`   

-  The y-axis should be labeled     `Sepal Length (cm)`   

-  The title of the graph should be     `Petal Length vs Sepal Length`   


Save your image to `/home/plot.png` . Remember you will need to pass that extra parameter to make the layout tight.  


```{admonition} Warning
:class: warning

Do not customize the chart in any other way! Part of this test is actually comparing the images so if you add any difference, you might fail the tests!

```

Your final plot should look like this:  

```{image} https://static.us.edusercontent.com/files/yjzwwLKZdyUhdIPr2TknNVES
:alt: TODO
:width: 640
:align: center
```

##  `seaborn` functions  

For convenience, we will put the functions you'll want to select from `seaborn` here.  

-  [None](https://seaborn.pydata.org/generated/seaborn.catplot.html)   

-  [None](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)   

-  [None](https://seaborn.pydata.org/generated/seaborn.relplot.html)   

-  [None](https://seaborn.pydata.org/generated/seaborn.regplot.html)   

-  [None](https://seaborn.pydata.org/generated/seaborn.jointplot.html)   

-  [None](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap)   


