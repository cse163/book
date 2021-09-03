# Indexing (Databases)


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/f1a3d4af3f6b4f75b369902cce641b8e?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

Suppose you work at Spacebook (a cheap knock-off of Facebook and MySpace) and you are working on the team that manages Spacebook profiles. Suppose your team has a Python class to define a single Spacebook user, shown in the snippet below, and stores instances of this class in a list.  

```python
class SBUser:
    def __init__(self, name, user_id):
        self._name = name
        self._user_id = user_id
        self._posts = []

    def get_name(self):
        return self._name

    def get_user_id(self):
        return self._user_id

    def make_post(self, msg):
        self._posts.append(msg)


users = [
    SBUser('Hunter', 1),
    SBUser('Ece', 14),
    SBUser('Alex', 29),
    SBUser('Trinh', 42),
    SBUser('Madrona', 109)
]
```

Now suppose Jasmine goes to her Spacebook profile (`https://www.spacebook.com/profile.php?id=42` [don't go to this link, it's spam]). The Spacebook service needs to find the appropriate object for the given user ID so it can display their information.  

The key question is: How can we find the `SBUser` object for Jasmine without needing to search through all of the Python objects in this list to find the object with matching user ID? If we had to loop over the whole list, then loading a user profile would be an $\mathcal{O}(n)$ operation where $n$ is the number of Spacebook users. Now, this probably doesn't seem like a big deal with our measly 5 users, but we plan to beat our competitor Facebook one day so it would be nice if we don't have to loop through all 1.7 billion users we plan to have one day.  

You could imagine making a `dict` where the key is the user id and the value is the `SBUser` so that we can look up the value with $\mathcal{O}(1)$ lookup. This is an excellent solution, but one that we will pretend we are not able to use right now. We want to showcase a different type of solution at this point since we will use it to understand a data structure that we can make finding geospatial objects more quickly.  

Putting everything in a `dict` where the keys are user IDs is a specific approach to a more general idea called **indexing** . This terminology is reminiscent of the index of a `list` or a `pandas` object since it's the same in principle. Indexing is a process of storing your information in a particular way (almost always by using a little extra memory), to allow efficient lookup by some value.  In other words, indexing is the process of making a new data structure that allows faster lookup a particular value.  

In the next slide, we will see a special data structure called a **binary search tree** that lets us create an index over our data.  

 

