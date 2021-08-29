# <i class="fas fa-laptop fa-fw"></i> Practice: Population Maps

{download}`Download starter code </module-7-geospatial-data/lesson-20-dissolve-join/practice-population-maps.zip>`

Write a program in `main.py` that reads in the world dataset and makes a plot containing three axes in one figure. The top-most plot should plot the population (column `POP_EST` ) by country (the original data format). The middle plot should plot the population aggregated by the sub-region (column `SUBREGION` ). The last plot should plot the population aggregated by the continent (column `CONTINENT` ).

The final result should look like the one below.

```{image} https://static.us.edusercontent.com/files/vl5wN71vcxzGJULdLyYAZ9tu
:alt: TODO
:width: 640
:align: center
```

### Implementation Details

- Read the data in from the file `/course/lecture-readings/geo_data/ne_110m_admin_0_countries.shp`

- Each plot on each axis should have a legend.

- Recall to save a figure, you can call `savefig` on a `Figure` object. You should save the visualization to a file named `populations.png` .

- Your program should use the main-method pattern and should not define any global variables.

- Instead of the "Run" button, we now have a "Check" button to help you verify the output of your program. You still need to press Mark to submit.
