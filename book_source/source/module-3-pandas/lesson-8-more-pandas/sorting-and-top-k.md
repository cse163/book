# Sorting and top-k

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/1223f3c9c2ff4068bb013ea8b8e3a4a3?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

```{reading-data}
{static-data-download}`fmri.csv`
```

## New Data

For this slide, let's change the data up a bit to give you a sense of how generic this work in `pandas` can be. We have been using examples with earthquake data that came from a CSV format, but many datasets provide CSV formats of their data.

In this slide, we will use an example from fMRI (e.g., brain scans) data to show activation in various regions of the brain. Don't worry, you don't need to actually understand how brains work to follow along with this example, but we did want to show how all of these examples are just stand-ins for basically anything you want to compute (assuming it's in a CSV). Note that this dataset has a special value called `NaN` in it that we will talk more about in the next module!

```{snippet}
import pandas as pd

df = pd.read_csv('fmri.csv')
print(df)
```

## Sorting

Another very common operation in `pandas` needs you to sort the data. This could either be for presentation reasons or you might be interested in finding the "top 10" rows based on some criteria. `pandas` makes sorting really easy!

```{snippet}
import pandas as pd

df = pd.read_csv('fmri.csv')

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

## Top-k

Instead of actually sorting the data, you might want to find the 10 highest signals in the data. `pandas` also provides a way to do this with the `nlargest` function.

```{snippet}
import pandas as pd

df = pd.read_csv('fmri.csv')

# Returns a new DataFrame with the 10 rows with the largest `signal`.
print(df.nlargest(10, 'signal'))
```
