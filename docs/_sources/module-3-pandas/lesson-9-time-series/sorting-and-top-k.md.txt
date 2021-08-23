# Sorting and top-k

Another very common operation in `pandas` needs you to sort the data. This could either be for presentation reasons or you might be interested in finding the "top 10" rows based on some criteria. `pandas` makes sorting really easy! Using the same fMRI dataset from before, the following snippet shows how to  
```python
import pandas as pd

df = pd.read_csv('/course/lecture-readings/fmri.csv')

print(df.sort_values('signal'))
```

Notice that this prints out all the data where the rows sorted by `'signal'` . Notice that the index of each row stays the same meaning the index is no longer in sorted-order!  

```{admonition} Warning
:class: warning

Like in the last slide
`df.sort_values('signal')`
does not actually sort
`df`
! It returns a new
`DataFrame`
where all the rows are sorted by
`'signal'`
.
<br />

<br />
If you want to keep the sorting, you need to save the result in a variable (i.e.
`df = df.sort_values('signal')`
)

```

##  Top-k  

Instead of actually sorting the data, you might want to find the 10 highest signals in the data. `pandas` also provides a way to do this with the `nlargest` function.  
```python
import pandas as pd

df = pd.read_csv('/course/lecture-readings/fmri.csv')

# Returns a new DataFrame with the 10 rows with the largest `signal`.
print(df.nlargest(10, 'signal'))  
```

 
