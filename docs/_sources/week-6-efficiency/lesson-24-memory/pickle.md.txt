# Pickle

```{admonition} Tip
:class: tip

Loom video can be found here:
[None](https://www.loom.com/share/e16bc40b4ab84837a9de6f21866b25ec)


```

Even though we talked about disk being slow, it's convenient because it is persistent. This means after your computer shuts down, everything on disk will still be there after your restart. This can sometimes be very helpful for data analysis. For example, what if you trained a really great machine learning model and want to save that exact model for the future? This would not be possible if you just stored it in a Python variable, since if your computer restarted or the Python session ended, then *poof* , that model is gone!  
There is a convenient module called `pickle` that lets you save a Python object to a file so that you can read it in later! The following program makes a list of numbers, saves it to a file (and prints out that it was saved) before reading it in again! This is not the most convincing example in an Ed snippet since we run it all at once, but believe us that you can write the "reading" code from a pickle you made yesterday and it will work just fine!  
The one note we will make about `pickle` , is it requires us to use one other feature of reading/writing to files. The `open` call takes a second parameter called `mode` that tells Python how you want to use the file. By default, `mode` has value `'r'` , which means you want to read the file. If you want to write to the file, you need to use the mode `'w'` by making the call `open('file.txt', 'w')` . Even more confusing, since `pickle` needs to write the data in a special binary format (i.e., not plain-text like a `.txt` ), you need to pass in the modes `'rb'` for read binary and `'wb'` for write binary respectively.  
```python
import os
import pickle

# Create a list (can be any data structure, value, or ML model)
special_values = [1, 2, 3]

# Save a pickle of the value. Need to open file in write-binary mode (wb)
with open('good_values.pickle', 'wb') as f:
    pickle.dump(special_values, f)
    
    
# Verifying it saved a file called good_model.pickle
print('Files in Directory:', os.listdir('.'))

# Read the values back in later (e.g., the next day) from the pickle file
# Need to open file in read-binary mode (rb)

with open('good_values.pickle', 'rb') as f:
    new_special_values = pickle.load(f)

# Verify it stores the same values
print(new_special_values)
```

