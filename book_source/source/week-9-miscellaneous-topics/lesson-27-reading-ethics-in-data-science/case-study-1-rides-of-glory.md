# Case Study 1: "Rides of Glory"
In 2012 Uber (a ride-sharing company) wrote an engineering blog post outlining an analysis that one of their data scientists performed for fun titled "Rides of Glory." They looked user's data for requesting rides on the app, along with the time the user ordered them to make maps of locations in San Francisco where "hookups" were more common. Many people reacted negatively to this blog post and argued that it was inappropriate for Uber to analyze this. Uber has since deleted the post. We want to tackle the following question: Was it unethical for Uber to do (and publish) an analysis like this?  
We should emphasize the point that the blog post didn't leak any personal identifying information. Uber never revealed individually that person A hooked up with person B since all the data was presented in aggregate (X people in this area of the city). This situation wasn't a privacy violation in that respect since no one knew who's data was used.  
However, this does bring up an essential question of consent. When users use applications, they usually consent to share some of their data with the application writer in that terms of service no one reads. You could argue that the user agreed to give up their data, so they have no right to complain about Uber using it in this type of analysis. However, it's not clear to users that they consent to any possible use of their data for all time. Generally, people expect that companies respect the data that they provide and that companies use that data for the service they provided the information for (or used to improve the service overall).  
Apple does a pretty good job of thinking about user consent. In fact, in all the interviews I've done in my life, Apple is the only one that has asked me questions about how developers should use user data in a way that follows what they consented Apple to use it for. For example, a user might permit to share their location data with Apple to help improve the Apple Maps service. Since the consent they gave was narrow to that one application, it would be inappropriate to use that data to enhance say the Messaging app. So Apple doesn't just do something with user data because they think they can, they think about respecting the user as a guiding principle. This doesn't mean Apple is a perfect company (they are no way are), but it is one of their strengths.  
When writing an application or doing data analysis, it helps at least to ask the following questions as a quick check so that you don't make the same mistake that Uber made:  
-  What consent was given by the user when the data was collected?  
-  Would the user want their data to be private or used in your application in that way? Would they be happy to know you used it in this way?  

##  Data Science Principles  

-  Keep user data anonymized and secure.  
-  Know where the data came from and what permission we have to use it.  

##  Further Resources  

-  Read the     [None](https://www.amazon.com/Ethical-Algorithm-Science-Socially-Design/dp/0190948205)   
    -  k-anonymity  
    -  Differential privacy  

-  Look into Security, a  sub-field of Computer Science  

