# Time Series

```{reading-data}
{static-data-download}`bicycles.csv`
```

**Time series** data is data that represents a sequence of events separated by time. This is generally more than just having a column for "date". We think about time series data being a dataset that's **indexed** by the time each event happened.

For example, here is a time series dataset showing the number of bikers over Seattle's Fremont Bridge.

```{snippet}
import pandas as pd

df = pd.read_csv('bicycles.csv')
print(df)
```

Notice that each row represents a slice of time, where each slice shows the number of bikers going over the east side or the west side of the bridge.

`pandas` does an excellent job working with time series data! Let's read the dataset in again, but this time give some extra parameters to `pandas` so that it knows to treat the date itself as the index. Remember, the index of a `DataFrame` is just a value that uniquely identifies each row. By default, the index is a row number, but you could use any column of unique values as an index!

Recall that in the last lesson, we learned about keyword arguments (i.e., passing parameters by name). This feature is incredibly useful to library writers since they can have their functions take many parameters (many of which have default values, which we will learn how to do next week) that you can specify by name rather than having to know the exact order they come in. For reference, `pd.read_csv` has about 49 parameters! With keyword arguments, you can just specify them by name rather than having to specify all 49 by position!

To get `pandas` to recognize the fact that this is a time-series dataset, we need to tell it which column contains the unique identifiers ( `index_col='Date'` ) and pass in a special parameter to tell it to interpret these as dates ( `parse_dates=True` ). The following snippet shows how to do this, and **notice in its output it shows the date column shows the index** !

```{snippet}
import pandas as pd

df= pd.read_csv('bicycles.csv',
                index_col='Date', parse_dates=True)
print(df)
```

In the next slide, we will show many of the ways we can use this new-found ability to have the date as the index.
