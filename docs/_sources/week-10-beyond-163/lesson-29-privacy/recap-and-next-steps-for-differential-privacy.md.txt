# Recap and Next Steps for Differential Privacy

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/78e30ed8485a4f2698629d65523124c4?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

So we have seen a lot in this lesson! They are all terms that we think you should know and are likely ones you will hear more prominently in your work as people working with data as you move into the future! We start this last slide of the reading by recapping some of the terms we introduced in this lesson and the most important takeaways, highlighting an important reason differential privacy is used in practice, and showing some current and next steps for differential privacy.  
##  Recap  

-  We started this lesson by introducing the notion of     **k-anonymity**     which is the requirement that any published dataset must ensure that any combination of insensitive features (e.g., sex, date of birth, zip code) narrows down the data to at least $k$ people. In other words, you should never be able to uniquely identify anyone from a dataset but are limited to narrowing down to at least $k$ people.  
    -  We saw that this approach was a great first step, but had some downsides when it came to making guarantees when you were working with multiple datasets (sometimes called         **composability**         ).  

-  We then saw a video on this concept called     **differential privacy**     and how it would be used for the first time on the US Census this past year to ensure the privacy of individuals who took the Census. We then defined differential privacy as the guarantee that you can't tell if an individual's data was used or not in a data analysis. We didn't show how you get differential privacy at first, just that it's a requirement that the result of an analysis looks "similar" whether or not you removed a particular individual.  
-  We showed the first differentially private mechanism called     **jittering**     or the     **Laplace Mechanism**     which is the process of adding random noise to published statistics to make it harder to work backward and find if an individual's data was used in the data. There were specifics of how the noise has to follow a specific distribution known as the Laplace Distribution, but we only cared about the relationship between the noise and guarantees of privacy.  
-  We then looked at the case when we don't trust the party gathering data and a mechanism called     **randomized response**     that can ensure differential privacy without trust. The respondents of a (potentially embarrassing) poll flip a coin that dictates how they respond. This allows us to analyze general trends about the population, but lose the ability to say with certainty if an individual told the truth or a lie.  

##  Why Differential Privacy?  

While we saw that differential privacy doesn't solve every privacy problem, it does make some strong guarantees as long as you use mechanisms that we know are differentially private (e.g., jittering with Laplace or random response). There are other, more complicated mechanisms that achieve differential privacy, but the mechanisms exist so we can use them.  
One of the most important reasons differential privacy is used is how it handles **composability** . When we talked about k-anonymity, we said we throw out all privacy guarantees once we talk about combining two separate datasets (even if they are both k-anonymous individually). This is important for something like the US Census where they might publish multiple statistics and we would want to make sure that the composition of many individual privacy guarantees doesn't break down privacy guarantees.  
It turns out, that differential privacy handles composability quite well. If you have two differentially private algorithms, you can run them both and the result will still be differentially private. So for example, if you publish one statistic about your dataset that is 2-differentially private and another that is 3-differentially private, you can think about that as one output with a total of 5-differential privacy guaranteed in the worst case. The power here is you can analyze the privacy of complex systems by breaking them down into simpler differential privacy "building blocks" and looking at how they compose.  
This is sometimes referred to as a "privacy budget". That you might want to have a guarantee of 10-differential privacy in the entirety of your published statistics, so that limits you to a tradeoff between:  
-  Many small statistics with small $\varepsilon$ guarantees. Remember small $\varepsilon$-differential privacy has a high guarantee of privacy, but may not be very accurate.  
-  A few statistics with larger $\varepsilon$ guarantees. This allows them to be more accurate, but at the cost of less privacy per statistic requires allowing to publish fewer of them.  

##  Optional: Next and Current Steps for Differential Privacy  

We hope you found something interesting here in our discussion of differential privacy. We expect this is only a term you will hear more frequently moving into the future so it's good you get a chance to see it now. Before you go, we wanted to provide a completely optional section on where differential privacy is used now and where it might go in the future.  
-  We saw it being used in the most recent US Census.  
-  Differentially private systems have been implemented in large organizations like Google and Apple since 2014 and 2016 respectively to gather usage statistics on their devices. They chose to mostly operate using randomized response to ensure privacy "locally". It's unclear how much of their systems use differential privacy, but they have started rolling it out in at least some systems (it's likely they implemented these systems for new data sources rather than data they were already collecting).  
-  The interface between machine learning and differential privacy will become more and more studied. There is already a lot of work showing it's theoretically possible, but improvements there will need to be a stronger emphasis on using it as common practice in the ML community where necessary.  
-  The intersection of differential privacy can be quite complicated when unexpected events like the COVID-19 pandemic arise. There are lots of real-world policy debates happening right now on the tradeoff between utility and privacy when it comes to something like, contact tracing or creating government-run systems to contact trace automatically through apps.  
-  Communication with people about how differential privacy is used and what it means will be an increasingly important point of practice for computer scientists and data scientists alike in the future.  

If you want to learn more about the theory of differential privacy, Cynthia Dwork and Aaron Roth wrote a book on that is a formal introduction to differential privacy: https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf  
 
