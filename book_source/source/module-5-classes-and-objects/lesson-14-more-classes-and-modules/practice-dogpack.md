# <i class="fas fa-laptop"></i> Practice: DogPack

{download}`Download starter code </module-5-classes-and-objects/lesson-14-more-classes-and-modules/practice-dogpack.zip>`

This practice problem has two parts. The first modifies the `Dog` class we worked on in the lesson last time and the second writes a new class called `DogPack` that stores multiple `Dog` s.

All the files have been included in the provided starter code. To run the program run `python main.py` in the terminal.

## Problem 0: Modify `Dog`

In the module `dog.py` we have the same `Dog` class that we defined last time. Rename the `name` field to make it private! Since you are changing the name of the field, you will need to change how it's accessed in all methods!

After fixing this, you should pass the test labelled "Problem 0".

## Problem 1: Write `DogPack`

In the module `dog_pack.py` write a class called `DogPack` . The `DogPack` should have a field called `dogs` (remember to make it private though) that will be of type `list` . The `DogPack` should have the following methods:

- An initializer that should set up the state of the `DogPack` . The field for the dogs should start out as the empty `list` .

  - _Hint: Remember the initializer is just like any other method, except that it has a special method name._

- A method named `add_dog` that takes a `Dog` as a parameter and adds it to the end list of `Dog` s in the `DogPack` .

- A method called `all_bark` that goes to each `Dog` in the `DogPack` and has them bark.

For example, after running `main.py` (command: `python main.py` ), your program should produce the following output. We first show the relevant part of `main` for context.

```python
pack = DogPack()
pack.add_dog(Dog('Chester'))
pack.add_dog(Dog('Scout'))
pack.add_dog(Dog('Bella'))
pack.all_bark()
```

```text
Chester: Woof
Scout: Woof
Bella: Woof
```

## A Note on Testing

Even though we are asking you to make your fields private, we do a bad thing and access the private fields of your class. This is so we can test your implementation matches our specification. We make this decision for its pedagogical benefit, despite its poor style.

## A Note About Naming Convention

Python uses `snake_case` for almost everything. All your functions, variables, fields, and even file names should use `snake_case` . The one major exception is class names which should be `CapitalCase` (where the first letter of each word is capitalized). This is why we will call the class `DogPack` but the file name will be `dog_pack.py` .
