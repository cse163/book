# Privacy in Practice: The Census

Before trying to more formally define this more complex notion of privacy and how to achieve it, we want to let our friends at Minute Physics show a recent example of how it is used in practice. We do this because they provide a very good intuition for what this notion of privacy tries to capture and how applicable it is to real-world problems like the US Census. Watch the video below to find out more! It's okay if you slow down the Youtube video a bit since the Minute Physics guy can sometimes talk a bit fast.  

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.youtube.com/watch?v=pT19VwBAqKA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

##  Recap  

-  The goal of differential privacy is to prevent the leak of confidential information about an individual. The context is slightly different than the one we tackled in the last slide, where here we are publishing statistics about demographics rather than a database of (hopefully) anonymous individual data. The overall concern is the same though, where we are concerned that potential linkage of different datasets might reveal private information about an individual.  
-  The thought process behind it is thinking about the possible databases that could result in the published summary statistics and how likely they might be. So this definition of privacy is a probabilistic one, trying to make the probability of a single unambiguous option for the data unlikely.  
-  One way of achieving this guarantee in privacy is "Jittering" the data to provide some uncertainty in the published values. This jittering can ensure privacy (if done carefully) at the loss of accuracy (since we have less precise numbers).  
-  This notion of privacy is composable. That means if you publish two separate $\varepsilon$-private statistics, you can still guarantee $2\varepsilon$-privacy. This is commonly phrased as having a fixed "privacy budget" and controlling for what level of accuracy you provide across statistics you do publish, without going over that "privacy budget". So for example if you want your overall set of statistics published to ensure 10-differential privacy, you can only release 20 statistics, each with individual 0.5-differential privacy.  

