# <i class="far fa-edit fa-fw"></i> Practice: Joins

Suppose we were working with the following two datasets shown below. For each question, report the number of rows in the resulting `DataFrame` (remember, that the number of rows does not include the column header).

## `movies`

| movie_name           | year | movie_id | directed_by |
| -------------------- | ---: | -------: | ----------: |
| Lady Bird            | 2017 |       51 |          23 |
| Grand Budapest Hotel | 2014 |       47 |          16 |
| Parasite             | 2019 |      103 |          14 |
| Frozen               | 2013 |       34 |          18 |
| Moonrise Kingdom     | 2012 |       37 |          16 |

## `directors`

| director_name     | director_id |
| ----------------- | ----------: |
| Bong Joon Ho      |          14 |
| Greta Gerwig      |          23 |
| Wes Anderson      |          16 |
| Quentin Tarantino |          21 |
| Kathryn Bigelow   |          27 |

## Question 0

How many data rows are there in `result` ?

```python
result = movies.merge(directors, left_on='directed_by',
                      right_on='director_id')
```

**📝 Your Task**

Write your answer down in your own space.

## Question 1

How many data rows are there in `result` ?

```python
result = directors.merge(movies, left_on='director_id',
                         right_on='directed_by', how='left')
```

**📝 Your Task**

Write your answer down in your own space.

## Question 2

How many data rows are there in `result` ?

```python
result = movies.merge(directors, left_on='directed_by',
                      right_on='director_id', how='outer')
```

**📝 Your Task**

Write your answer down in your own space.

## Question 3

Suppose we wanted to compute the earliest movie directed by each director. Any director who has directed no movies should have `NaN` as a result.

Which of the following code blocks helps us answer that question? **Select all that apply** .

**📝 Your Task**

Select one or more options. Write your answer down in your own space.

_<i class="far fa-square fa-fw"></i> Option 0_

```python
merged = movies.merge(directors,
                      left_on='directed_by',
                      right_on='director_id',
                      how='right')
result = merged.groupby('director_id')['year'].min()
```

_<i class="far fa-square fa-fw"></i> Option 1_

```python
merged = movies.merge(directors,
                      left_on='directed_by',
                      right_on='director_id',
                      how='left')
result = merged.groupby('director_id')['year'].min()
```

_<i class="far fa-square fa-fw"></i> Option 2_

```python
merged = directors.merge(movies,
                         left_on='director_id',
                         right_on='directed_by',
                         how='right')
result = merged.groupby('director_id')['year'].min()
```

_<i class="far fa-square fa-fw"></i> Option 3_

```python
merged = directors.merge(movies,
                         left_on='director_id',
                         right_on='directed_by',
                         how='left')
result = merged.groupby('director_id')['year'].min()
```

_<i class="far fa-square fa-fw"></i> Option 4_

```python
merged = movies.merge(directors,
                      left_on='directed_by',
                      right_on='director_id')
result = merged.groupby('director_id')['year'].min()
```

## Question 4

Consider the following two datasets.

- The first is our countries dataset. Each row has the name, continent, and geometry of a country (there are other columns, but we don't need to think about them for this problem).

      |    NAME     |  CONTINENT  |    geometry     |

  |-------------|-------------|-----------------|
  |United States|North America|MultiPolgyon(...)|
  |Ethiopia |Africa |Polygon(...) |
  |... |... |... |

- The second is a carbon emissions dataset. The dataset has two columns, the name of the country and the amount of carbon emissions produced by that country last year.

      |   Country   |Carbon|

  |-------------|------|
  |United States| 16.50|
  |Ethiopia | 0.12|
  |... |... |

Suppose we wanted to make a plot of the average carbon emissions **by continent** . Before we do any aggregation to make this map to group countries together by continent, we need to join these datasets so that we can later answer for each continent, what is the average carbon emissions there.

For this problem, we will say any country in the country dataset that does not have an associated row in the carbon emissions dataset should have 0 carbon emissions.

Which of the following is the correct way to combine these datasets by their name? Assume the countries dataset is stored in a variable called `countries` and the carbon emissions data is in a variable called `carbon` and that we have run any relevant imports. **There is only one correct answer in the list below.** It is a useful exercise to make sure you can explain why the other answers are incorrect.

**📝 Your Task**

Select one option. Write your answer down in your own space.

_<i class="far fa-circle fa-fw"></i> Option 0_

```python
countries.merge(carbon,
                left_on='NAME', right_on='Country')
                how='inner')
```

_<i class="far fa-circle fa-fw"></i> Option 1_

```python
countries.merge(carbon,
                left_on='NAME', right_on='Country')
                how='left')
```

_<i class="far fa-circle fa-fw"></i> Option 2_

```python
countries.merge(carbon,
                left_on='NAME', right_on='Country')
                how='right')
```

_<i class="far fa-circle fa-fw"></i> Option 3_

```python
gpd.sjoin(countries, carbon,
          op='intersects', how='inner')
```

_<i class="far fa-circle fa-fw"></i> Option 4_

```python
gpd.sjoin(countries, carbon,
          op='intersects', how='left')
```

_<i class="far fa-circle fa-fw"></i> Option 5_

```python
gpd.sjoin(countries, carbon,
          op='intersects', how='right')
```
