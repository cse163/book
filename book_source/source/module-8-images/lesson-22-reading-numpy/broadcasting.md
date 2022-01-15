# Broadcasting

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/ff84cc52b01b42f1a7465093aa65d932" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

In the last slide, we saw that you can do element-wise arithmetic with `numpy.array`s. We showed that you could do something like `x + 3` and it would add 3 to each value in the array. While this did work, it also seems reasonable that this cause an error since the shapes of `x` and `3` disagree. The reason it is not an error is that `numpy` has a well-defined series of rules to transform values that disagree in shape for these operations. These rules form what is known as **broadcasting**. In other words, broadcasting is a procedure `numpy` uses to transform values that disagree in shape so that the result is well defined.

Before we state the rules, let us point out that this is in some sense an arbitrary decision on `numpy`'s part. They could have very easily said that if any shapes disagree, it causes an error. They chose the following set of rules to do some automatic transformations. If you want anything outside of these transformations provided, you would have to write the code yourself. We will start by stating the rules, and then do a worked example which should hopefully clear up what is going on.

## Broadcasting Rules

Consider some element-wise operation like `x + y` that operates on two `numpy.arrays`. This operation is well-defined if both `x` and `y` have the shape. If `x` and `y` disagree on their shape, `numpy` will run the following steps in order to make the shapes match up.

- If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded on it’s left side.

- If the shape of two arrays does not match on any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape. This will happen for all dimensions that don't match and one has a shape equal to 1.

- If in any dimension the sizes disagree and neither is equal to 1, an error is raised.

The process of broadcasting doesn't actually modify `x` or `y` , but rather creates a temporary structure with the shape described in this algorithm to do the operation.

## Broadcasting Example

Consider the code snippet. We print out the resulting shape and then explain using the rules of broadcasting why this is the case.

```{snippet}
import numpy as np

m = np.ones((2, 3))  # Shape: (2, 3)
v = np.arange(3)     # Shape: (3,)
result = m + v
print(result)
print(result.shape)
```

It helps to see that originally our data is

```text
m (2, 3)
[[1, 1, 1],
 [1, 1, 1]]

v (3,) # Notice the extra set of []!
[0, 1, 2]
```

### Step 1: Pad Dimensions

The first rule of broadcasting says:

> If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded on it’s left side.

Since `m` has 2 dimensions and `v` has 1, we will need to pad `v` with dimensions of shape 1 on the left of its shape. After this step, we will be working with the following shape/values.

```text

m (2, 3)
[[1, 1, 1],
 [1, 1, 1]]

v (1, 3)
[[0, 1, 2]]
```

```{admonition} Warning
:class: warning

Important: While we are saying that `v.shape` is now a `(1,3)`, this is a bit of a lie since `v`'s shape never actually changes. Broadcasting makes a temporary copy that starts with the value of `v` and transforms that. For simplicity we refer to it as `v`'s shape. If you go to the snippet above and print out `v`'s shape at the end, you'll see it's the same as it started.

```

### Step 2: Stretch Dimensions

The second rule of broadcasting says:

> If the shape of two arrays does not match on any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape. This will happen for all dimensions that don't match and one has a shape equal to 1.

We can see after Step 1, that the first dimension of `m` and `v` disagree since `m` 's first dimension has shape 2 and `v` 's first dimension has shape 1. This means we will stretch `v` along its first dimension so that it becomes a `(2,2)` . Semantically, this means we will add a new row (since first dimension is rows) to `v` with the exact same values as the first row. This is because we "stretch" the values along that dimension.

After this step, we will be working with the following shape/values.

```text

m (2, 3)
[[1, 1, 1],
 [1, 1, 1]]

v (2, 3)
[[0, 1, 2],
 [0, 1, 2]]
```

Importantly, we **only** do this stretching in the case of a mismatch for the array that has shape 1 for that dimension.

### Step 3: Check for Errors

The third rule of broadcasting says:

> If in any dimension the sizes disagree and neither is equal to 1, an error is raised.

After step 2, our shapes match so there is not an error.

You might be wondering, how could an error occur with this algorithm? Consider trying to add a shape `(1, 3)` to a `(2, 6)`. According to Step 1, we wouldn't need to pad since there is the same number of dimensions. In Step 2 when we stretch, we would only stretch the first dimension of the first array since that's the only one that has shape 1. This means you cannot stretch the second dimension from 3 to 6 since the rule says it will only stretch dimensions with shape 1 if it disagrees. Then we would get to Step 3 and see that we have a `(2, 3)` and a `(2, 6)` which disagree on a dimension and neither are one.
