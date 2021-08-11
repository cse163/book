# Default Parameters


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/f3ceb3d5100b4bbbabf4eb591c2a2b5f?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Last time, we saw how to call functions by using keyword arguments (also called named parameters or pass by name). We mentioned briefly that one motivation for having this feature is it allows libraries to define methods that take many parameters and you can pass them in by name without needing to memorize the order the parameters were defined. We also mentioned that they also have some functionality for specifying **default values** for parameters not passed. That's what we are going to see today!  
When defining a function that takes parameters, you can use the syntax `param=value` in the parameter list to give the parameter `param` the default value of `value` when it was not specified by the client. See the following snippet for an example which you can run to see the output.  
```python
def div(a=10, b=1):
    return a / b


print('div(2, 3)', div(2, 3))
print('div(2)', div(2))
print('div(b=3)', div(b=3))
print('div()', div())
```

Notice that on many of the calls, we omit passing one of `a` or `b` . This does not cause an error because `a` and `b` were defined in the function to have default values! If you look at the function definition at the top of the snippet, you can see we have defined the default value of `a` to be `10` and the default value of `b` to be `1` .  
Notice that the features for default parameters and keyword arguments are *orthogonal* . What this means is you could have one without the other, but the fact that Python provides both allows library writers to write some truly flexible code!  
You'll see that in the library we learn today, we will commonly always pass in keyword arguments to the functions. The functions take many possible parameters and it helps to be explicit with what we are passing in rather than relying on the order the parameters were defined! What we mean by that is even though you could call the `div` function above with `div(1, 2)` , we will commonly be more explicit and write out the parameter names as in `div(a=1, b=2)` when calling library functions that take many parameters.  
