# Joins

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/45449525974a471ca97929ea5b13d2fc?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

We're going to take a quick step away from geospatial data for the next flew slides, but this concept will be very relevant for the example we will be doing with geospatial data.  
Let's go back to the world of CSV data that we would process with `pandas` . Suppose I had two different `DataFrame` shown below. The left one `tas` stores information about the TAs and `grading` on the right stores information about students and which TA will be grading them ( `ta_id` and `grader_id` will match if that TA is grading that student). Our final goal will be trying to find the number of students each TA will grade.  
```{image} https://static.us.edusercontent.com/files/XefeN513eek9ajoDicHmXplz
:alt: TODO
:width: 758
:align: center
```

You might wonder why I would represent data in this way such that they are in separate tables. This is a very common situation when you have data coming from many sources! You might have gotten two datasets from completely different sources, but you know there is an identifier column that relates information in one table to that of another. From my perspective as a teacher, this is a very common situation for my data where I get all my data identifying you (name, email, UW NetID, section) from MyUW while I get your grade data from Ed (where it stores your email and grades).  
The process of trying to combine two datasets in such a way to "align" them based on some column values is called a **join** . If we were to join these columns on `ta_id` and `grader_id` , you would imagine that the process looks something like this pseudo-code (this is not real Python!).  
```text
for t in tas:
  for g in grading:
    if t['ta_id'] == g['grader_id']:
        output(t, g)

````

To explain in English, the process of joining them on `ta_id` and `grader_id` finds all pairs of rows from each table, and keeps them if they match on `ta_id` and `grader_id` .  
Now this pseudo-code isn't going to actually look like what we will write for `pandas` . Joining is such a common operation with data that `pandas` provides a function to do so that looks like the following (there is a bit of setup to create the datasets):  
```py
import pandas as pd

# Make the tas DataFrame
tas = pd.DataFrame([
    {'ta_name': 'Ryan',   'ta_id': 1},
    {'ta_name': 'James',  'ta_id': 2},
    {'ta_name': 'Nicole', 'ta_id': 3},
])
print('tas')
print(tas)
print()

# Make the grading DataFrame
grading = pd.DataFrame([
    {'grader_id': 2, 'student_name': 'Flora'},
    {'grader_id': 3, 'student_name': 'Paul'},
    {'grader_id': 1, 'student_name': 'Wen'},
    {'grader_id': 3, 'student_name': 'Andrew'},

])
print('grading')
print(grading)
print()

# Join the datasets by ta_id and grader_id
merged = tas.merge(grading, left_on='ta_id', right_on='grader_id')
print('merged')
print(merged)
```

Notice that the output contains all pairs of rows that match up on `ta_id` and `grader_id` ! There are now two rows for `Nicole` because there were two rows in the original `grading` table that had her ID. At this point `merged` is a new `DataFrame` with the four columns shown in the output above. To compute how many students each TA was grading, we could easily solve this with a `groupby` on this new `DataFrame` !  
You might be wondering, what would happen to rows that don't "line up". What if there was a TA who didn't have anyone they were grading or a student had a `grader_id` for a grader that doesn't exist in the other table? Suppose we had the following dataset instead. We removed James from the left table and changed Wen to be graded by Nicole on the right.  
```{image} https://static.us.edusercontent.com/files/Gr191GcMoBCpwe1U78FtMLM2
:alt: TODO
:width: 743
:align: center
```

Let's see what happens when we run `merge` on these datasets.  
```py
import pandas as pd

# Make the tas DataFrame
tas = pd.DataFrame([
    {'ta_name': 'Ryan',   'ta_id': 1},
    {'ta_name': 'Nicole', 'ta_id': 3},
])
print('tas')
print(tas)
print()

# Make the grading DataFrame
grading = pd.DataFrame([
    {'grader_id': 2, 'student_name': 'Flora'},
    {'grader_id': 3, 'student_name': 'Paul'},
    {'grader_id': 3, 'student_name': 'Wen'},
    {'grader_id': 3, 'student_name': 'Andrew'},

])
print('grading')
print(grading)
print()

# Join the datasets by ta_id and grader_id
merged = tas.merge(grading, left_on='ta_id', right_on='grader_id')
print('merged')
print(merged)
```

Nicole is the only TA represented in this result! The rows that have IDs that did not "line up" with any other row got tossed out. This makes sense in the context of the pseudo-code we showed above since they didn't have any matches. The topic of what to do with rows with missing values is very interesting and is the topic of the next slide.  
