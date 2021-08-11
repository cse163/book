# 🚧 Reading: Working with Directories

{download}`Download starter code </week-5-classes-and-objects/lesson-14-more-classes-and-modules/reading-working-with-directories.zip>`


```{admonition} Warning
:class: warning

This slide is mostly a reading, but is coded as a Practice Problem. You need to change one thing in the provided code to get it to pass the tests (but we tell you what this change is). Remember to press Mark to submit your code!

```

Earlier in the quarter we introduced file processsing so that we could read file contents. For your next assignment, we are going to use files again but add one extra layer to understanding how files on your computer work.  
Your computer stores files, but there is generally a hiearchy to them in the form of **directories** (also called folders). You can see an example of my `163` directory on my computer in the image below. A directory can store files or other directories (which, in turn, can store other files or other directories).  
```{image} https://static.us.edusercontent.com/files/JOLQ8IHbCrDyK9hj40s4Pk78
:alt: TODO
:width: 497
:align: center
```

In this slide, we will see how you can interact with a directory to find all the files inside it. The goal of this program is to print out the name and contents of each file in a directory.  
To accomplish this task, we will need to use the `os` module to interact with your computer's operating system (OS). The program we wrote starts by importing `os` and then uses `os.listdir('people')` to get a list of all the file names in the directory named `people` . To see the contents of the `people` folder, click on the "Toggle Tree View" button on the top-left of the editor. The `people` folder stores three files so, in this example, the result of `os.listdir('people')` will return the list `['carly_rae_jepsen.txt', 'guido_van_rossum.txt', 'latanya_sweeney.txt']` .  
The rest of the program is fairly straight-forward: it defines a helper function that takes a file path and prints out each line of the file. Our main method just loops over this list of file names to print the contents of each file after printing its name. However, if you try running this program (terminal command: `python main.py` ), you'll see we will run into an error because it is unable to read the first file!  
This is somewhat similar to the bug you have probably experienced on the homework when a file is not found. This has to do with how your Python program gets run. Notice in our workspace director, there is no file named `carly_rae_jepsen.txt` . There is a `carly_rae_jepsen.txt` inside the `people` directory, but there is no such file in *this* directory. When we try to call `open('carly_rae_jepsen.txt')` , it causes an error because there is no file with that name here. To read the file located in another directory, we have to specify its **path** from the directory we are running this program in. In this case, the file is stored in the `people` directory so we need to use the path `'people/carly_rae_jepsen.txt'` .  

```{admonition} Note
:class: note

Notice there is no
`/`
at the beginning of the path
`'people/carly_rae_jepsen.txt'`
! This is because the
`people`
directory is in this directory so we can use this relative path. On your homework we need to prepend the path with
`/home`
(with a slash) to specify an absolute path from the "top-level" of the computer.

```

##  Your Task  

There is a simple fix for this program! All we need to do is add the directory name to the front of the path! That means you should change this:  
```text
print_file(file_name)

````

to  
```text
print_file('people/' + file_name)

````

Once you make this change, the program should be able to run and print the contents of the files! **Make sure to press Mark to submit your program!**   
