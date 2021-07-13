# Dissolve

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/f59c69e387da4953832d2efe0001eef0?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Consider our world dataset from last time. Recall we use `geopandas` to process and plot datasets that contain information about the location of an event. As a reminder, the following snippet shows a preview of the data and a plot of the world's GDP.  
```py
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
df = gpd.read_file('/course/lecture-readings/geo_data/ne_110m_admin_0_countries.shp')

# Preview data
print(df.columns)
print(df.head())

# Plot data
df.plot(column='GDP_MD_EST', legend=True)
plt.savefig('world_gdp.png')
```

##  GDP by Continent  

Suppose we wanted to compute the total population for each continent. Since our dataset is tabular, you might suspect that since we are trying to compute a value "for each" group, that we would want to use a group-by! This is exactly the right idea! Remember, a group-by operation is one where we want to put each row into a group (e.g., the continent the country belongs to) and compute an aggregate for each group (e.g., the sum of the population). It turns out while `GeoDataFrame` s do have a `groupby` function, it is not going to behave as we want it to!  
The big problem for `groupby` here is that it comes from `pandas` and is not geospatial aware. What this means is that if we were to use a `groupby` here, it would not know how to handle the geometry column of the `GeoDataFrame` ! This means there is not a well-defined answer for what the resulting geometry for the continent should be.  
However, don't worry! `geopandas` provides another function called `dissolve` that behaves **exactly** like `groupby` , but has added logic to combine all the geometries for the group into one. This means you can still compute aggregates like `sum` , `min` , `max` , `mean` for the columns of interest. Additionally, it will combine the `geometry` column in a special way to make one `geometry` for the group. The default (and most common) thing to do is to just take the overlap of all the geometries for that group.  
Below, we run a full example that dissolves by the continent to show the total population in each continent, and then below explain the syntax. When you run the snippet, you should see an output that looks like we would expect: where each continent is its own color that looks like to have a value that is the sum of all the countries in that continent.  
```py
import geopandas as gpd
import matplotlib.pyplot as plt

df = gpd.read_file('/course/lecture-readings/geo_data/ne_110m_admin_0_countries.shp')

# Filter down to just the columns of interest
populations = df[['POP_EST', 'CONTINENT', 'geometry']]
# Run the dissolve (groupby) operation
populations = populations.dissolve(by='CONTINENT', aggfunc='sum')

# Then plot the result
populations.plot(column='POP_EST', legend=True)
plt.savefig('plot.png')
```

Notice this `dissolve` call has a lot of the same components as a `groupby` , but the syntax looks quite different. Instead of saying `df.groupby('col1')['col2'].sum()` , you say `df.dissolve(by='col1', aggfunc='sum')` . The `dissolve` operation is applied to ALL columns of the `GeoDataFrame` . As a result, it is common that you will need to filter down to just the columns of interest before doing a dissolve. In our example with `col1` and `col2` , you would need to filter `df` down to `['col1', 'col2', 'geometry']` since the the `dissolve` only happens on those columns.  
Don't believe us when we say that you can't use `groupby` here? Try it out in the following snippet and see what the resulting plot looks like! The problem comes from the fact that our `groupby` call throws away the geometry column, making this a non-geospatial dataset; it would not be easy to modify this to account for the geometry in the way that `dissolve` is designed to do!  
```py
import geopandas as gpd
import matplotlib.pyplot as plt

df = gpd.read_file('/course/lecture-readings/geo_data/ne_110m_admin_0_countries.shp')
populations = df.groupby('CONTINENT')['POP_EST'].sum()

populations.plot()
plt.savefig('wrong_figure.png')
```

