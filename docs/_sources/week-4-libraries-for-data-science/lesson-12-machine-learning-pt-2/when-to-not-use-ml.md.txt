# When to Not Use ML

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/bdf5663bbb434ab4bc3c98a40240a8c1?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

So in the past two lessons, we have introduced to you the awesome ability to learn from data to make predictions about the future. In Lesson 11 we introduced the concepts and the basics of how to train a model. In Lesson 12, we introduced how to handle some other types of data (e.g., categorical data) and outlining the common problem of model's overfitting and how to assess their performance. One of the points of discussions we have been putting off, but we are now a bit better equipped to tackle is: Should we even apply ML to a particular task?

So take for example the last slide where we were training a model on credit card data. Is that something we should endorse as Computer/Data Scientists in training, or should we be more hesitant to use a system like that? What does it mean to think critically about how an ML system is used?

ML has both an awesome potential to solve problems that we didn't think would be possible before, but it also has a terrifying risk of creating new problems on its own in how it is applied. Unfortunately, there is no "easy answer" to what tasks you should/shouldn't apply ML. It requires critical thought and careful consideration of the benefits and harms the model might produce and think of how the ML model will be used in the greater system as a whole.

We won't be able to provide an easy answer in this lesson or this course, but it's important to pause and bring up some questions and things to consider before applying ML to a task at hand. In a later class, we will talk about some concrete case studies that can help serve as "anchors" for comparison, but here we outline some key things to think about:

<Element 'list' at 0x7fcd236cf4a0>
In most of these questions, we will be talking about the credit card example in the last slide, but these ideas can be applied more generally. Importantly,
**these are not the only questions that you should ask**
, but they do serve as a good starting point for your consideration. They also aren't questions that you can necessarily ask in a linear order, since your thoughts on one might affect your thoughts on another.

We also want to highlight that we don't necessarily have answers to all of these questions but, they serve as a way to start discussions. But these are all things you should surely at least start thinking about before trying to apply ML to some particular task. The fact that these questions are tough to answer should hopefully make it clear that you should carefully consider what you apply ML to solving.

## Use


**How will the model be used?**


In trying to answer "Should we use a model to predict credit card churn?" or "Is it ethical to use a model that predicts credit card churn?", an incredibly important thing to ask is: "How will the model ultimately be used?"

For this credit card churn example, here are two wildly different ways this ML system could be used by a credit card agency.

<Element 'list' at 0x7fcd26039090>
Notice that the question of "Should I use a model for this task" might vastly depend on how that model is used. The benefits/drawbacks of using that model depend on the context in that it is used. Is there something different between those cases that might make us think it's more okay to use the model in one case over the other? Is it okay to use the model in both or neither? Why?

## Impact of Errors


**What is the impact the model will have on individuals or groups of people? What is the cost of an error?**


One fact you must know about ML is that
<Element 'italic' at 0x7fcd26039720>
. A "perfect predictor" is nearly impossible to achieve and no one tries actually tries to reach perfection but just tries to approach it. What level of accuracy would you require before feeling comfortable using a model in our credit card example? Does that accuracy requirement depend on the use case where we are trying to give special offers before someone leaves vs. whether or not they can get a credit card in the first place?

Importantly, consider the cost of making an error. Note, this is not asking "what if an error happens?" Errors are guaranteed to happen, so you must have a good idea of what the negative impact is when errors happen. In our credit card example, the error of the first use case (e.g., not giving someone special offers and they churn) seems much less harmless than the second use case (e.g., not giving someone access to a line of credit).

When considering bias in the data in the next section, is there a risk that biases present will disproportionally incur the cost of an error onto a particular group or demographic?

## Biases 


**What biases might be present in the data?**


A common phrase in ML is "Garbage in $\rightarrow$ Garbage out" when discussing the quality of data you use to train a model. Most people refer to garbage being the ability for features to describe the data, but there is usually a much more insidious notion of garbage behind the scenes.

Data comes from the real world, and the real world is not equally fair to all people. There are systematic and individual biases that have caused a disproportionate impact on historically and presently marginalized communities. These biases can find their way into our datasets because the data is drawn from the real world where these biases are present and this encoded bias in the data could then be perpetuated by what the model learns from the data. When you hear in the news of ML models exhibiting biased behavior, it normally comes from the fact that they are mirroring the biases found in the data fed to them.

So to think a little more concretely about our credit card example, we might question why do people churn their credit cards, and do we have reason to believe that some implicit or systematic bias can affect the trends seen in the data? Will those biases have an impact on the overall outcomes and potentially negatively hurt particular groups or individuals? Is churn the result of affluent individuals trying to "game" the credit card system, or is churn the sign of economic hardship and losing the ability to afford a line of credit? Is it possible for something like someone's race or gender (something they have no control over) impact either of these causes of churn (short answer: yes)? And this definitely relates back to how the model might be used since the impact of the model depends on the context it is used in.

Another potential source of bias is the structure of the data itself might exclude certain populations. Either in how the data was collected (forms customers fill out), or what the dataset publisher decides to publish, data is always a reduction of reality to something we try to use in computation. For example, the data presents a Gender column that shows a binary choice between M and F, when in reality, gender is a much more complicated notion. There is a tension between simple data we can analyze (something categorical like M/F) and something more open-ended that can account for the diversity of human experience. You should think carefully about who is represented and who is excluded in your data.

## Feedback Loops


**How will the model's use reinforce these biases?**


A very pernicious way these biases can sneak into an ML system and how it's used can come in the form of what is known as a "feedback loop". This is a bit harder to see in our credit card example, so we will switch the example to this section to something known as "predictive policing". The idea is to better allocate police resources by having more police patrol in areas with higher reported incidences of crime, in an effort to prevent more violent crimes from happening.

While it sounds great in theory to try to not waste police resources (since there is probably money that we could put into other resources than just policing), this can create very large unintended side effects. Cathy O'Neil describes this phenomenon well in her book
<Element 'italic' at 0x7fcd26039e00>
where she highlights that a well-intended system to reduce violent crimes (e.g., burglaries, assault, murder) can reinforce systems of oppression when the models the police used include all crime data, including low-level or "nuisance crimes". Cathy writes:

<Element 'blockquote' at 0x7fcd260391d0>
How the model is used can create a feedback loop, which can further exacerbate biases found in the data when the results of the model affect the results in the future. In the presence of bias in the data originally, feedback loops have the potential to quickly amplify them. Even if the bias is small to start, this feedback loop can make it into a completely broken system.

