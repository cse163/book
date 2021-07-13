# Join Types

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/dbfef11ad462496984ff19cfa2ccb233?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

To handle rows that don't line up, we actually think of there being multiple types of joins. The join I described earlier is called an
**inner-join.**
An inner-join only shows rows that have values that appear in both tables.

Before listing the other joins, we note that we commonly refer to a "left" table and a "right" table in the join process. For the
`pandas`
call, this is determined by
`
			`
. The
`how`
parameter determines which type of join to use in the list below. There is no inherent difference between what goes on the left vs the right, it's just determined by which dataset you indicate as the left.

There are four common types of joins:

<Element 'list' at 0x7fcd236d6360>
With the same, modified, dataset from the last slide, try out the various join strategies by changing the value of the
`how`
parameter!

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
merged = tas.merge(grading, left_on='ta_id', right_on='grader_id',
                   how='left')
print('merged')
print(merged)
```

You should try experimenting with this since one of the practice problems for today will get you practicing doing the outputs of these joins!

