# Main Method Pattern

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/020818cc801841cb97393a741104047b?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

```{admonition} Note
:class: note

A note about the format of this reading: This reading involves using multiple Python files. If a code block has a comment at the top saying
<br />

`# File: hello_world.py`
<br />

We are indicating that you should read the contents of that code block being in the file with the indicated name.
```

Recall from the first lesson, we saw that there were two ways of writing a "Hello world" program

```{snippet}
# File: hello_world.py

print('Hello world')
```

```{snippet}
# File: hello_world.py

def main():
    print('Hello world')


if __name__ == '__main__':
    main()
```

We showed that regardless of which one you used if you ran `python hello_world.py` it would print out `Hello world` . It is helpful to remember what happens when you run a Python program. Whenever you _run_ a Python program, it starts at the top of the file and executes each line until it reaches the bottom.

You probably then wondered: Why did we need all this extra stuff if these two programs do the exact same thing? At the time we couldn't give a good answer, but now we are able to justify why these are different and why you should always use the second one.

The case where these two approaches differ is when your program uses `import` statements.

## A Tutorial on Importing

Suppose I have the following three files that did not use the main-method pattern.

```{snippet}
# File: module_a.py

def function_a():
    print('Hello from Function A')

print('I love File A')
```

```{snippet}
# File: module_b.py

def function_b():
    print('Hello from Function B')
```

```{snippet}
# File: module_c.py

import module_a
import module_b

print("Let's call some functions")
module_b.function_b()
module_a.function_a()
```

What would you expect to be the output of `python module_c.py` ? Since we print and call two functions, you would probably expect the following.

```text
Let's call some functions
Hello from Function B
Hello from Function A

```

However, instead, it prints:

```text
I love File A
Let's call some functions
Hello from Function B
Hello from Function A

```

What happened? When you import a file, it runs all statements starting from top to bottom, just like when you run the file! That's why the first thing printed is `I love File A` . When we import `module_a` on Line 3 of `module_c.py` , it goes and runs all statements in that file. Notice it doesn't print `Hello from Function A` at that point because we never called `function_a()` , we just defined it.

What this means is if you have any code outside of just function definitions, that code will get run whenever you import a file! Now, having a few lines of extra output is not the end of the world, but you could imagine it would be really bad if you accidentally started running some kind of data analysis that would take 4 hours to finish just because you wanted to import one function from a module!

## How does the main-method pattern help?

The main-method pattern prevents some of the code in a file from being run on import!

Let's go back and explain the components of the "Hello world" program to understand how this happens. Below, we have annotated the "Hello world" program with comments explaining its components.

```{snippet}
# File: hello_world.py

# This defines a function called main (nothing special here)
def main():
    print('Hello world')

# This if-statement only runs this file is being run via: python hello_world.py
if __name__ == '__main__':
    # If this condition is true, then call the main method (nothing special here)
    main()
```

So in reality, the only "special" part of the main-method pattern is the if-statement `if __name__ == '__main__':` . Python uses the special variable `__name__` to give you information about how your file is being used. All we do in the main-method pattern is only call `main()` if we know this file is being run rather than imported.

- If you are running the module from the command-line (e.g. `python hello_world.py` ), `__name__` will have the value `'__main__'` . This is why our check verifies if `__name__ == '__main__'` before calling the `main` method.

- If you are importing the module from another Python file (e.g. `import hello_world` ), `__name__` will have the value `'hello_world'` (the module that's being imported).

You could imagine making a toy module that just prints out whether it is being run as a program or imported:

```{snippet}
# File: toy_module.py

if __name__ == '__main__':
    print('Runnning program')
elif __name__ == 'toy_module':
    print('Being imported')
else:
    print('Not possible!')
```

## Take-away

The main-method pattern is important and used very commonly in Python to prevent unintended side-effects from importing a module. Your module should only have function definitions, and if you do want the ability to run it, you should use the main-method pattern. There is almost never a case where you want non-function definition lines of code (e.g. `print` statements or reading a file) outside of the main-method pattern.
