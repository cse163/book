# Missing Data

```{reading-data}
{static-data-download}`fmri.csv`
```

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/7feef4e9a31d4252a39460a11d758f49?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

[Most data in the world is messy](https://github.com/Quartz/bad-data-guide). It might be in a format that you will have trouble reading from or it might have errors in the data! One of the most common types of errors in datasets is **missing data** , where a row might have some of its column entries just missing!

For example, we have a dataset of fMRI (brain scan) data that, like most real-life datasets, is a little messy. The dataset has the following columns:

- `subject`: An identifier for the person being measured

- `timepoint`: The time in the study

- `event`: What type of stimulus the subject was given

- `region`: Where the fMRI measurement was taken

- `signal`: The measurement value

If we tried to load it into a `DataFrame`, we would see the following.

```{snippet}
import pandas as pd

df = pd.read_csv('fmri.csv')
print(df.tail())  # Prints the last rows
```

Notice that row 1059 has this weird value `NaN` for both the timepoint and the signal!

`NaN` , or "Not a Number", is a common value in Python to represent the absence of a data-value. You should think of it a lot like `None` but has some slightly different properties that make it a little more usable in some numerical processing applications (will be explained in the next section).

The fact that we see `NaN` values in our data means the dataset is messy and we will have to deal with it. There is a myriad of ways to try to handle missing data, some more complicated than others. For right now, we will focus on how to detect missing data in the dataset and how to filter it out!

By default most `pandas` operations just ignore missing values so this isn't a problem if you are just in the `pandas` world. However, we will see this next week that other libraries for data visualization and machine learning will crash if we give them datasets that contain missing values, so we should learn how to deal with that now.

## `NaN` vs. `None`

`NaN` is some kind of numerical equivalent to `None` . It represents a number that is, in some sense, invalid or missing.

In Python, `NaN` operates by two rules:

- Any arithmetic operation on `NaN` , evaluates to `NaN`

- Any boolean comparison on `NaN` , evaluates to `False`

We can access the value `NaN` most easily by using the library `numpy` (commonly imported as `np` ). We will learn more about `numpy` in Module 7!

```{snippet}
import numpy as np

print(np.nan)            # nan
print(1 + np.nan)        # nan
print(np.nan * 1)        # nan
print(1 == np.nan)       # False
print(np.nan == np.nan)  # False
```

That last line is pretty surprising since we compared `np.nan` to `np.nan`. Remember though, one of the rules of `NaN` is that every boolean comparison on `NaN` is `False` !

How is `NaN` different than `None` ? `None` doesn't allow any numeric operations on it, it will cause an error!

```{snippet}
print(1 + None)
```

## `NaN` in `pandas`

So now that we know what this magic-value `NaN` is in our dataset. Let's see how to handle it in `pandas`. Let's start by taking the average of the `'signal'` column (that contains `NaN` values).

```{snippet}
import pandas as pd

df = pd.read_csv('fmri.csv')
print(df['signal'].mean())
```

Luckily for us, `pandas` has some logic built into it to skip `NaN` values for many of the simple operations like `mean` ! However, this won't always work so we will need some special `pandas` methods for finding and removing `NaN` (although, they have a weird naming convention).

- To detect if there are missing values:

  - `isnull()` returns a `bool` `Series`, where `True` marks `NaN` values.

  - `notnull()` returns a `bool` `Series`, where `True` marks non-`NaN` values.

- To return a new `DataFrame` with `NaN` removed:

  - `dropna()` removes all rows with missing data.

  - `fillna(val)` replaces missing data with the given value

The following code block shows how these operations work

```{snippet}
import pandas as pd

df = pd.read_csv('fmri.csv')

# Returns all the rows in df where the signal is not NaN
df[df['signal'].notnull()]

# Returns all the rows in df that did not contain a NaN value
df.dropna()

# Replaces all NaN signals with 0
df['signal'] = df['signal'].fillna(0)
print(df)
```

```{admonition} Warning
:class: warning

Notice that the first two examples don't modify `df`. Why is that? Almost every operation on `pandas` returns a new `DataFrame` or `Series`! For example, `df.dropna()` returns a new `DataFrame` with the `NaN` rows missing. It's not until the last example, do we actually save the return value into
`df` so the result stays.
```

```{admonition} Warning
:class: warning

On take-home assessment 3, we will ask for you to deal with missing data. Think very carefully about which data you want to remove and how you will remove it. A common bug students run into involves removing too many rows or too few rows that have missing data for the relevant columns.
```
