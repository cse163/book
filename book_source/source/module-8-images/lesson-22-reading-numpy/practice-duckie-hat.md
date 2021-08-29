# <i class="fas fa-laptop"></i> Practice: Duckie Hat 🦆🎩

{download}`Download starter code </module-8-images/lesson-22-reading-numpy/practice-duckie-hat.zip>`

Write a function called `duckie_hat` that takes an RGB image of a duck (a `numpy.array` with shape `(Height, Width, Color Channels)` ) and returns a new image with the same pixels but modified so the duck is now wearing a fancy green top-hat.

Our algorithm won't do anything fancy like detect where the duck is. Instead, we will just hard-code where the hat should be.

You should make a hat but setting all the pixels in the following regions to be fully green and the other channels off. The locations below are in terms of `(0, 0)` being the top left and the first dimension going down the image and the second dimension going to the right.

-  The main-hat should be a rectangle with the top-left corner at     `(20, 85)`     and  the bottom-right corner at     `(75, 135)`     .

-  The hat brim should be a rectangle with the top-left corner at     `(75, 60)`     and the bottom-right corner at     `(90, 160)`     .



```{admonition} Warning
:class: warning

**Clarification:**
For simplicity, we intended for the specification of the bottom-right corner to be exclusive but failed to state that explicitly. This means for the main hat, the hat should go up to, but not including the point
`(75, 135)`
.

```

For the duck image from the reading, your output image would look like the following:



```{image} https://static.us.edusercontent.com/files/CafRH3fRgxzSoTdM12aaOzV0
:alt: TODO
:width: 406
:align: center
```

##  Implementation Details

-  Your solution should use no loops or comprehensions to solve this problem.

-  You should not modify the input image. Instead, you should make a copy of it with the     `.copy()`     method provided by     `numpy`     arrays.



```{admonition} Note
:class: note

Credit goes to Mitchell Estberg for coming up with this idea 🦆🎩

```

