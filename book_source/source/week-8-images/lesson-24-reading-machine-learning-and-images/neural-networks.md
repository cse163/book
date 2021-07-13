# Neural Networks
To introduce yourself to Neural Networks, we want you to watch a video from a YouTube channel called 3Blue1Brown. 3Blue1Brown is one of Nicole's favorite YouTube channels about mathematics and their videos are very accessible and well done.  
You can find a link to the video below, but first, we want to highlight some things we really want you to get out of the video and some things you can skim over and not focus on as much. You should read these lists first even though they won't make much sense yet. Then after watching the video, review these key points to make sure you got what we wanted you from it.  

```{admonition} Warning
:class: warning

In their video, 3Blue1Brown uses grayscale images with pixel values between 0.0 (black) and 1.0 (white) instead of our 0 to 255. These are equivalent, just different scales that are both commonly used!

```

##  Things to Pay Attention To  

-  The general structure of a neural network and how it is used to make predictions.  
    -  How many input neurons will there be for the digit recognition? Why that number?  
    -  Why are there 10 output neurons for the digit recognition task?  
    -  What is a hidden layer?  

-  How does the information go from one layer to the next?  
-  What is the intuition for why organizing the nodes in layers helps?  
-  How does a node determine its output value from its inputs?  

##  Things to Skim  

-  The specific formula for the "squishing function" called the Sigmoid. All you really need to know is the general idea that it squishes the input to output between 0 and 1.  
-  13:30 - 15:00 talks a bit about representing this process using matrices and vectors which is more complex than we care about. You should still watch the part after that since it shows a quick application of     `numpy`     and gives some more high-level motivation!  

There is a whole series of videos that you are welcome to watch if you're interested, but we will only focus on the first one.  

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

 
