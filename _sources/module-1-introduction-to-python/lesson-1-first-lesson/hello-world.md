# Hello World!

In this lesson, we won't learn much Python programming. We'll focus on a deeper introduction to Python starting in Lesson 2. In this lesson, we just want to teach enough such that you can get used to how to run a Python program to follow along with the Python readings.

## Why Python?

Python is one of the most popular languages in the world ([StackOverflow](https://insights.stackoverflow.com/survey/2021#section-most-popular-technologies-programming-scripting-and-markup-languages)), and is one of the most frequently used programming languages by data scientists. In fact, many speculate that Python's explosive growth in popularity in recent years stems from increased interest in the field of data science.

Why do many data scientists use Python? There are two key reasons:

**Simple Syntax**: Python is designed to be very human-readable. Sometimes, writing a Python program feels a lot like writing an English description of how to solve problem. Other languages (e.g., Java), contain a lot of syntactical constructs (i.e., curly brackets) that often make less natural to read. This is not to say that Python is "easier to learn"! Learning programming can be complex, and students of programming generally struggle with concepts of computing (e.g, "what is the idea of a loop") more so than the syntax of computing (e.g., "how to write a loop in Java"). But many data scientists (who might come from non-programming backgrounds) often cite Python's easy-to-approach syntax as a draw to the language for them. See our Hello World program below to get a sense for this.

**Libraries for Data Science**: Python has tools built in it to make it relatively simple to download and use code written by others. Many developers have spent countless hours developing useful pieces of code others can use for data analysis. While the software setup on the last slide might have ran into some hiccups based on how your computer is set up, it is still overall pretty simple in the grand scheme of things: we've taught large Java programming classes and would never dream of trying to set up downloading libraries other programmers have wrote for Java. So the ecosystem of libraries built for data science applications in Python further makes Python an attractive language for data scientists. If they can rely on these libraries to do much of the tedious work, they can focus on their analysis. We will learn many of the most popular libraries for data science in this course!

## Hello World

Conventionally in any first programming course, you learn how to make a computer print out the the text "Hello world!" So let's do that in Python!

```{snippet}
print("Hello world!")
```

That's it! If you just type this in a Python program and run it, it will say "Hello world!" to you!

For comparison, here is how you write "Hello world" in some other popular programming languages that have some more complex syntax. Skimming these, you might begin to see what we mean by Python generally being considered to be more human-readable since it doesn't require a lot of extra syntax these other languages do. Note: we

````{tab-set-code}

```{code-block} java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}
```

```{code-block} c
#include <stdio.h>

int main() {
    printf("Hello World!");
    return 0;
}
```

```{code-block} c++
#include <iostream>

int main()
{
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

```{code-block} go
package main

import "fmt"

func main() {
    fmt.Println("hello world")
}
```

````

## Explore on Your Own!

Consider our "Hello world!" program from above.

```{snippet}
print("Hello world!")
```

Notice that if you hover your mouse over the code above, there is a clipboard icon to copy the code. This is a great way for you to easily copy our code and try it on your own! Now that you've completed the [Software Setup](dev-setup/index), you can make a new Python file (extension: `.py`) in VS Code or whatever editor you use and paste a code snippet there to try it out! Try changing the `print` statement to say something else!

While it might not seem very exciting with our single `print` statement, you will find getting into the practice of running the code you read about to be extremely helpful for learning. You can also gain a huge amount of understanding by trying out your own changes to a new code syntax you've learned to explore how it might work in other situations. We recommend that you always have VS Code up with these readings so you can try out the Python snippets as we show them.
