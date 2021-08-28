# Processing a CSV

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/dd229affd69d4e489a9ad1a7a81e2358" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

Now that we understand what a CSV looks like, let's discuss how we might process that data to answer questions about it. For example, what if I want to find the total of all the TAs' salary?  

You might imagine that we will solve this with the skills we have learned so far in file-processing. We could do something by reading the file line by line in a loop, splitting the line based on commas, and then doing our computation on the data we've extracted. Unfortunately, this ends up being much more complicated than we anticipated:  

-  The code is not very flexible if I want to compute some other value. What if I want to compute the TA who makes the most money? I would have to duplicate all this nasty code to parse the file just to access the information again. This also comes at a cost of efficiency (e.g. speed of program) since, for each task, you will need to re-read the file.  

-  Our example CSV is relatively simple, but they can get much more complicated. It would be nice to separate the logic of **parsing** the data from our **computations** so our code for computations is more readable and maintainable.  


##  List of Dictionaries  

To accomplish this, we will start by storing our data in some data structure ( `list` , `set` , `dictionary` , etc.) that will help us process it later. A very common thing to do when processing this type of data is to store it in a **list of dictionaries**. It helps to see what the data looks like first, then we will explain what it is.  

```text
[
    {'Name': 'Madrona', 'Salary': 3},
    {'Name': 'Rit',     'Salary': 1},
    {'Name': 'Ryan',    'Salary': 3}
]
````

This data structure is a `list` that stores `dict` s as its entries; therefore we call it a list of dictionaries. Each dictionary represents a single row of the dataset: this is why there are 3 dictionaries inside this list. Inside each dictionary, there is a key/value pair for every column of the data showing the values for each row and that column.  

This is a bit complex when you see it at first because the data structures are nested! Inside the `list` are dictionaries! This means if you stored that above data in a variable called data, you could access a dictionary by indexing into a list.  For example, to get the name of the TA at index 1, you might write:  

```python
data = [
    {'Name': 'Madrona', 'Salary': 3},
    {'Name': 'Rit',     'Salary': 1},
    {'Name': 'Ryan',    'Salary': 3}
]
print('Data:', data)
print('Number of rows:', len(data))  # Since data is just a list
print('Row 2:', data[1])

ta = data[1]  # This is a dictionary: {'Name': 'Rit', 'Salary': 1}
print('Name of TA in Row 2:', ta['Name'])

# It helps to print out the types of things
print()
print('Types')
print('type(data)', type(data))
print('type(data[1])', type(data[1]))
print("type(ta['Name'])", type(ta['Name']))
```

It turns out, it's not necessary to save the value of `data[1]` in a variable before accessing it! It is much more common to write code like the following:  

```python
data = [
    {'Name': 'Madrona', 'Salary': 3},
    {'Name': 'Rit',   'Salary': 1},
    {'Name': 'Ryan',  'Salary': 3}
]

print('Name of TA in Row 2:', data[1]['Name'])
```

Let's try another example. **Before running the code snippet below, make a prediction of what each line of code will do and see if your prediction matches reality!**   

```python
data = [
    {'Name': 'Madrona', 'Salary': 3},
    {'Name': 'Rit',   'Salary': 1},
    {'Name': 'Ryan',  'Salary': 3}
]

print('First example')
print(data[2]['Name'])
print()

print('Second example')
print(data['Salary'][0])
```

The first one should print the name "Ryan" because we go to the dictionary at index `2` and then grab its value associated with the key `'Name'` .  

The second one does not work at all and causes an `Error` ! Why is that? Well `data` is a `list` , not a `dictionary` , so we can't say `data['Salary']` ! You have to be careful about the order of the data is represented!  

##  Looping over the list of dictionaries  

Let's look back to our example from earlier where we want to compute the sum of the TAs' salaries. We start by writing a loop to go over each TA in the list (each TA is a dictionary). We then access the `'Salary'` entry in each dictionary and add that to a variable for a cumulative sum.  

```python
data = [
    {'Name': 'Madrona', 'Salary': 3},
    {'Name': 'Rit',   'Salary': 1},
    {'Name': 'Ryan',  'Salary': 3}
]

total_cost = 0
for ta in data:  # ta is a dictionary
    total_cost = total_cost + ta['Salary']
print(total_cost)
```

It sometimes helps to pause and think about the types again. Recall that the type of `data` in this example is `list` . The type of each value inside that `list` is a `dict` (e.g. `{'Name': 'Madrona', 'Salary': 3}` ).  Each of these `dict` s will have the same keys (e.g. `'Name'` and `'Salary'` ).  

##  Reading in a CSV File  

You might be asking: How do you write the code to parse this CSV into the list of dictionaries? <br />  <br /> That actually turns out to be a very hard problem that is well outside of what we have learned so far! There are lots of edge cases to handle around getting the types of the values correct (i.e. knowing when to turn the values of a column into `ints` rather than `str` s).  

We write this method for you and call it `parse`. It will be made available to you on your homework and lessons in a file called `cse163_utils` and you do not need to know how it's implemented. This is similar to how we provide `assert_equals` in `cse163_utils`.  


```{admonition} Note
:class: note

Optional: In fact, this task is actually so nasty to write by yourself, we didn't even do it! We outsourced it to a code-library that we will learn about called
`pandas`
to do the work for us. Why re-implement something that will potentially introduce bugs that
`pandas`
already did for us?

```

