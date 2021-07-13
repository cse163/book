# Recap and Next Steps for Differential Privacy

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/share/78e30ed8485a4f2698629d65523124c4?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

So we have seen a lot in this lesson! They are all terms that we think you should know and are likely ones you will hear more prominently in your work as people working with data as you move into the future! We start this last slide of the reading by recapping some of the terms we introduced in this lesson and the most important takeaways, highlighting an important reason differential privacy is used in practice, and showing some current and next steps for differential privacy.

## Recap

<Element 'list' at 0x7fcd237603b0>
## Why Differential Privacy?

While we saw that differential privacy doesn't solve every privacy problem, it does make some strong guarantees as long as you use mechanisms that we know are differentially private (e.g., jittering with Laplace or random response). There are other, more complicated mechanisms that achieve differential privacy, but the mechanisms exist so we can use them.

One of the most important reasons differential privacy is used is how it handles
**composability**
. When we talked about k-anonymity, we said we throw out all privacy guarantees once we talk about combining two separate datasets (even if they are both k-anonymous individually). This is important for something like the US Census where they might publish multiple statistics and we would want to make sure that the composition of many individual privacy guarantees doesn't break down privacy guarantees.

It turns out, that differential privacy handles composability quite well. If you have two differentially private algorithms, you can run them both and the result will still be differentially private. So for example, if you publish one statistic about your dataset that is 2-differentially private and another that is 3-differentially private, you can think about that as one output with a total of 5-differential privacy guaranteed in the worst case. The power here is you can analyze the privacy of complex systems by breaking them down into simpler differential privacy "building blocks" and looking at how they compose.

This is sometimes referred to as a "privacy budget". That you might want to have a guarantee of 10-differential privacy in the entirety of your published statistics, so that limits you to a tradeoff between:

<Element 'list' at 0x7fcd2603c7c0>
## Optional: Next and Current Steps for Differential Privacy

We hope you found something interesting here in our discussion of differential privacy. We expect this is only a term you will hear more frequently moving into the future so it's good you get a chance to see it now. Before you go, we wanted to provide a completely optional section on where differential privacy is used now and where it might go in the future.

<Element 'list' at 0x7fcd260399f0>
If you want to learn more about the theory of differential privacy, Cynthia Dwork and Aaron Roth wrote a book on that is a formal introduction to differential privacy: https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf



