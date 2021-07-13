# Recap of Machine Learning
We have lightly discussed the topic of machine learning in this course so far. As a reminder, machine learning uses **features** of a dataset and a **learning algorithm** to learn a target concept to **predict the label** for a given example. As a reminder of some terminology we used:  
-  A     **model**     (created by a learning algorithm), is a concrete set of rules to take an example (maybe from the dataset) and predict the label.  
    -  We might train a         `DecisionTreeClassifier`         on a dataset about surviving the Titanic to create a specific model that can predict survival for data of that type.  
    -  The term model is often overloaded when discussed by machine learning practitioners. They sometimes refer to the specific model learned after training (e.g. this specific         `DecisionTreeClassifier`         that is the result of training on this data). Other times, they refer to the type of models you are considering (e.g. we are looking over the space of all         `DecisionTreeClassifiers`         of height at most 5 to find which one is best for this specific task). It is often confusing to figure out if they are talking about a specific model or a class of models. We commonly use the terminology of "model" to refer to a specific model and "         **model class**         " to refer to the class of all models of some type.  

-  A dataset that has     **features**     and     **labels**     .  
    -  We always split a dataset into a         **training set**         and a         **test set**         . The training set is used by the learning algorithm to train the model. The test set is used to assess the model's performance on data it did not train on, in order to get an unbiased estimate of its future performance.  
    -  So far, we have just used CSV data for machine learning since we could simply just use the values in each column as the various features. In this section, we will learn how to use another type of data: images.  

-  Slightly new terminology: The     **parameters**     of a model are the details of how a particular model is specified. For example, the parameters of a decision tree model are all of the split points and stop points in the tree. An alternative way of phrasing the learning algorithm is an algorithm that tries to find the optimal setting of the parameters (e.g. what the split and stop points should be) to maximize the accuracy. The     **hyperparameters**     of a model are the parameters you specify as a programmer to control which models can be selected. For example, setting the maximum height of the decision tree is a hyperparameter you choose that then effect which parameterization is chosen by the learning algorithm.  


```{admonition} Tip
:class: tip

You should remember that parameters are things learned by the learning algorithm while hyperparameters are things you specify.

```

