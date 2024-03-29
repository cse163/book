# File Paths

{download}`Download starter code </module-2-data-structures-and-files/lesson-4-lists-and-files/file-paths.zip>`


```{admonition} Warning
:class: warning

This slide has some starter code for you to download to follow along, but there is no code you have to write.


```


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/e959f9e2b2284d598c4136f972427f0b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

Files in your computer are stored in folders. Folders can contain other folders or other files and this makes a hierarchy in your computer. If you have a Mac, you can use the Finder application to navigate these folders. If you have a Windows PC, you can use the File Explorer. For example, below, I have a screenshot of the Finder looking at the files in the folder I downloaded from this lesson.  

```{image} https://static.us.edusercontent.com/files/Hst9iQLxU1Yj7N3tvKPt85Tg
:alt: TODO
:width: 758
:align: center
```

When you open a Python project locally using something like VSCode, it opens the project to some folder that it will use as your workspace. 

Why is it important to know where your workspace is or what files are in it? You usually need to know that in order to specify where files are **relative** to that location. For example, in the terminal, if I type `python main.py` , how does Python know to use the `main.py` for this lesson and not one of the files from the other lessons? It's because files are specified by their **path** rather than their name. When we say `main.py` , we are referring to a file in the current directory named `main.py` . This path is relative to wherever our workspace is. This is probably a little confusing, so another example should hopefully clear it up.  

What if you wanted to print out the lyrics to Carly Rae Jepsen's hit-class "Store" that is *store-d (* ha!) in a folder in this workspace? Try changing the code to `open('store.txt')` instead and run that. You should see that it crashes because it can't find a file named `store.txt` in this workspace. To make this work, you have to specify a **path** to get to that file from this workspace. In this case, the format puts the list of folder names from here to there separated by `/` characters. So to properly open this file, you would use `open('crj/store.txt)'` to tell Python to look in the `crj` folder for the file.  

##  Absolute Paths

You might also see a path that starts with a `/`. We call this an **absolute path**. It's absolute because we think of the path `'/'` as the top-level folder of the computer so we are specifying the path from the top (hence absolute because it's not relative).  

##  Take-away  

You need to think about where your Python program is running from (the workspace) and what path you need to specify to get to the desired file from that workspace.  

