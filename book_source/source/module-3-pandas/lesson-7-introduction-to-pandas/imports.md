# Imports

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/a47eaf00be10430c844fb210b33e91c7?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

When you write a Python file (like `my_file.py` ) you are defining a Python **module** . You can think of using the words module and file interchangeably. A Python module can do one (or both) of the following:

- Be run as a program (e.g., `python my_file.py` ).

- Be **imported** so that another module can use the values defined in it.

```{admonition} Note
:class: note

As a bit of a preview, the reason the main-method pattern is necessary is to make sure these behaviors don't get mixed up! If you don't include the main-method pattern, all the things you want to run in a module as a script will aslo be run when you import it! We'll give a complete explanation in a later lesson.

```

We use importing to get values or functions defined inside one module so they can be used in another module. You have already been using this on your homework! We defined a module `cse163_utils` and in order to use the function `assert_equals` defined in that module, you had to import it.

There are 2 (and a half, sort of) main ways to import in Python that we will explore in this slide. For the following examples, assume we have defined the module `module_a` with the file `module_a.py` as shown below.

```python
# Contents of: module_a.py
def fun1():
    print("Calling a's fun1")
    print("Ending a's fun1")


def fun2():
    print("Calling a's fun2")
    fun1()
    print("Ending a's fun2")
```

Our goal is to call `fun2` inside another module, `module_b` . To do this, we need to import the module to use its functions.

## Option 1) `import module_a`

The simplest syntax simply uses the `import` statement to import a module. The following snippet shows a short program that uses `fun2` defined in `module_a` .

```python
# Contents of: module_b.py
import module_a


def fun1():
    print("Calling b's fun1")
    print("Ending b's fun1")


def fun2():
    print("Calling b's fun2")
    print("Ending b's fun2")


def main():
    fun2()
    module_a.fun2()


if __name__ == '__main__':
    main()
```

When you import a module, you are importing the whole thing (including all values defined inside of it). In some sense, when you `import` a module, you are running all of the code defined in that module.

However, to keep things manageable for you, Python keeps all these values defined in `module_a` in a different scope (sometimes called a "namespace"). This helps prevent confusion if `module_b` also defines a function with the same name, as we did in this example. That means to call `fun2` from `module_a` , you have to write `module_a.fun2()` to make it clear you want the one from `module_a` .

To double-check your understanding: **What is the output of running `python module_b.py`** as defined above? Take a second to make a prediction
before expanding the answer below.

````{admonition} Output
:class: dropdown

```text
Calling b's fun2
Ending b's fun2
Calling a's fun2
Calling a's fun1
Ending a's fun1
Ending a's fun2
```
Notice that `module_a` 's `fun2` behaves exactly the same as it was defined, even though we defined our own `fun1` and `fun2` in `module_b` (the scopes are different).
````

### Option 1.5) `import module_a as m`

This syntax has the exact same semantics as the one before, but it lets you define a shorthand name for the module. In this case, we essentially renamed `module_a` to `m` in our module so in our code, we can just say `m.f2()` . Semantically, these are really the same ways to import a module, but this one has an extra step to "rename" it.

Here, we show the complete `module_b` that uses the syntax. The output and behavior of the program are exactly the same.

```python
# Contents of: module_b.py
import module_a as m


def fun1():
    print("Calling b's fun1")
    print("Ending b's fun1")


def fun2():
    print("Calling b's fun2")
    print("Ending b's fun2")


def main():
    fun2()
    m.fun2()  # Notice m instead of module_a


if __name__ == '__main__':
    main()
```

## Option 2) `from module_a import fun2`

Sometimes, it is very tedious to import a whole module and prefix every function call with `module_name.function_name` . Python provides another syntax that lets you import a specific function from another module. When you say `from module_a import fun2` you are importing just the function `fun2` from `module_a` . When this syntax is used, Python just adds `fun2` to your current scope. This means you don't need to call it with `module_a.f2()` , you can just say `f2()` .

The following snippet shows how to use this syntax.

```python
# Contents of: module_b.py
from module_a import fun2


def main():
    fun2() # Calling module_a's fun2


if __name__ == '__main__':
    main()
```

This syntax is nice when you know exactly which function you want from `module_a` and you know you will call it often.

You might wonder what would happen if I defined a `fun2` in `module_b.py` (since we removed that from the previous examples). How would Python know which `fun2` to call if there was one that came from `module_a` and one from `module_b` and both are in the same scope? It turns out, if you define two functions with the same name, it will always use the one most recently defined. This is because by defining a function, you essentially are storing it in a variable with that function name. If you redefine, it will just update which function is stored at that variable name (just like updating a plain-old variable). That means if we defined a `fun2` after importing it from `module_a` using this syntax, we would essentially lose the value we imported.
