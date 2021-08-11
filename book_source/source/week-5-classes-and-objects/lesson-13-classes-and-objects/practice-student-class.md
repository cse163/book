# 🚧 Practice: Student class

{download}`Download starter code </week-5-classes-and-objects/lesson-13-classes-and-objects/practice-student-class.zip>`

This problem has 2 parts. The first involves writing a class named `Student` and the second involves writing a client program that uses that class.  
##  Part 0: Student Class  

Define a class `Student` that represents a student at UW in the file `student.py` .  
In general you will have to determine which fields your class should have, but for the purpose of testing this practice problem, we will tell you the names and the values they should store.  
-  `name`     stores the name of the student.  
-  `student_number`     stores the student number of the student.  
-  `classes`     is a     `dict`     that stores course names as keys and number of credits as values. The keys will be     `str`     and the values should be     `int`     .  

The `Student` should have the following methods.  
-  An initializer that takes in the student number, and the name of a file containing information about their schedule (more on this below).  
-  A method named     `get_name`     that returns the student's name.  
-  A method named     `get_student_number`     that returns the student's student number.  
-  A method called     `get_credits_for`     that takes a class name and returns the number of credits this student is taking for that class. If the student is not taking the given class, this method should return     `None`     .  
-  A method named     `get_classes`     that returns a list of the classes the student is taking.  

###  Student Initializer  

The initializer for the student should take the parameters described above which includes a file name. Suppose for example that the file `nicole.txt` stored the contents shown below. You can extract the student's name as the name of the file without the file type at the end. Her file says that Nicole is taking CSE 163 for 4 credits, PHIL 100 for 4 credits, and CSE 390HA for 1 credit.  
```text
CSE163 4
PHIL100 4
CSE390HA 1
```

You could then construct a `Student` object for Nicole by calling  
```text
nicole = Student(1234567, 'nicole.txt')
````

To implement this, you will need to recall back to how to read a file in Python so that you can build up this `dict` . Your algorithm for this should split each line and use casting to turn the second value into an `int` . You may assume the file will be in this expected format and does not have multiple lines for the same class, but you should not assume anything about the number of lines in the file (it may be empty). If the file is empty, then the `classes` will be an empty `dict` .  
##  Part 1: Client  

In the file `main.py` , write a runnable program to create some `Student` objects and print some of their state. Your program should use the main method pattern and all of the steps below can be in the main method.  
-  You should create an object for Pablo (his student number 1551515). Pablo's schedule file is     `pablo.txt`     .  
-  You should create an object for Arlo (her student number 1231231). Arlo's schedule file is stored in     `arlo.txt`     .  
-  On one line for each student, you should use the     `Student`     object you made to print the name, student number, and the number of credits they are enrolled in for     `'CSE163'`     . The format is shown below. You should use the functions that you defined on the     `Student`     class rather than accessing the fields from your client program directly.  

```text
pablo 1551515 None
arlo 1231231 4
```

Remember, you will need to import the `Student` class from `student.py` .  
