# 🚧 Practice: Coding Problem

{download}`Download starter code </module-1-introduction-to-python/lesson-1-first-lesson/practice-coding.zip>`

Some slides (like this one) will ask you to write code to answer them! This is an opportunity to apply what you have learned so far to produce a program that has the right output.

## Get Starter Code

To get the starter code and tests for this problem, click the download link above (or get the files from your instructor). Using the link above, it will download a `zip` file that you can unzip and open up in VS Code. Once you have opened the file in VS Code, you can start editing the files as requested below by this problem.

## The Problem

This problem is not intended to be very complex since you will be getting used to setting up the software for this course. All you need to do for this problem is take the "Hello world!" program we introduced earlier and change it to print "Hello Seattle!" instead.

There are multiple files in the starter code you downloaded. The only one you need to look at and edit is the one called `main.py`.

## Running Tests

With every practice problem, we have included testing code to help you verify if your solution is correct according to the specification of the problem. The testing code will print error messages for any behaviors that don't match the specification. You don't need to understand the testing code at all, but each practice problem includes the following:

- A directory named `test` which contains all of our testing files.
- A Python file named `run_tests.py` to help run the tests.

To run the tests, you have two possible options. It doesn't matter which one you use, so use whichever you find most simple. The instructions below assume you have already opened up the folder with the starter code in VS Code or your editor of choice.

```{admonition} Option 1: Run in VS Code Terminal

Click on the `run_tests.py` in the VS Code file navigator to open the file (you don't need to read or understand the code inside). Right-click anywhere in the editor pane of VS Code and select {guilabel}`Run Python File in Terminal`. This will open the terminal window below the editor pane and will display the test output there.

Once you have done this once, you can simply rerun the command shown in the terminal by pressing the up arrow on your keyboard to bring the command back. You can also just do the right-click option as described above.

To read the test output, see below.
```

```{admonition} Option 2: Run in VS Code Tests
Click on the `run_tests.py` in the VS Code file navigator to open the file (you don't need to read or understand the code inside). Right-click anywhere in the editor pane of VS Code and select {guilabel}`Run Current Test File`. This will cause VS Code to give you some prompts to answer in pop-up dialogues.

* It will prompt "No test framework configured (unittest, pytest or nosetest)". Click {guilabel}`Enable and configure a Test Framework`.
* It will show a list of test frameworks near the top of the screen. **Select `unittest`** from the options shown.
* It will show a list of directories near the top of the screen. **Select `test`** from the options shown.
* It will show a list of patterns for the test file names. **Select `test_*.py`** from the options shown.

VS Code might automatically open the testing tab. If it does not, click the icon on the far-left that looks like a beaker. This will show a list of tests run and whether or not they passed. If you have any errors, you will need to view the output log to inspect them. To do so, click the {guilabel}`Show Test Output` icon above the tests or go to the menu at the top and select {guilabel}`View > Output`.

To read the test output, see below.
```

## Test Output

The test output will be can be seen in the output window at the bottom. For example, if you run the tests without changing the starter code as we requested above, you should see the following output.

```text
F.
======================================================================
FAIL: test_hello_world (test_hello_world.TestHelloWorld)
#name(Testing: Hello world)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<path-to-your-starter-code-folder>test/test_hello_world.py", line 39, in test_hello_world
    self.assertEqual(ans, val, error_message(ans, val))
AssertionError: 'Hello Seattle!' != 'Hello world!'
- Hello Seattle!
+ Hello world!
 :

--------------------
Expected:
'Hello Seattle!'

Received:
'Hello world!'
--------------------


----------------------------------------------------------------------
Ran 2 tests in 0.003s

FAILED (failures=1)
```

To read this:

- The first line of output shows a summary of tests. Seeing `F.` means there were two tests (one for each character). Seeing an `F` means one test had an error, while seeing a `.` means one test passed. As another example, if you saw `.F.FF...F` that means your solution failed 4 tests and passed 5 tests.
  - Note, if you see an `E` in this output, that means the tests encountered an error. An error is different than a failure and it indicates there is a problem with the tests even running at all. Common problems for errors include running the tests incorrectly or from the wrong directory or having a syntax error in your Python program.
- For each failed test, there is an error message describing the test name and a message showing a description of what the test expected and what you returned. You can see from the output above that our tests expected the solution to return `'Hello Seattle!'` but it received `'Hello world!'`.

Once you change the starter code as described in this practice problem, you should pass the tests! When you pass, you'll see the following output.

```text
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```
