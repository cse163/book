# <i class="fas fa-book fa-fw"></i> Lesson 28: Fairness

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/0a6ffbc982844cd09cfca4923fd00c46?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

## Concepts

Last time we looked into case studies of how data science could go wrong (intentionally or unintentionally). In particular, when talking about the COMPAS example, we talked a bit about how a model can exhibit biased behavior. In this lesson, we want to dive more into what does fairness or bias even mean, and some work in trying to require that learned models are fair.

In this lesson, we will be focusing on an example of using various factors to predict admission to college. We are using this example, **not** because this is a system we endorse, but because it's very relevant for student's near college-age. We will vastly oversimplify the example too, but this is to make the concepts of fairness much easier, rather than trying to perfectly reflect all of the complexities of the world.

For example, we will talk about race being a binary construct (either one race or another) for simplicity. Obviously, this is not how we actually think about race in the real world but we do this to simplify the example to highlight ideas of fairness. All of the ideas we talk about in this lesson can be extended to more complicated situations in the real-world (e.g., more nuanced notions of race and intersectional identities).

```{admonition} Note
:class: note

This lesson is heavily inspired by The Ethical Algorithm by Michael Kearns and Aaron Roth. I highly recommend you check out their fantastic book!

```

## Table of Contents

```{toctree}
:maxdepth: 1
:caption: Contents

defining-fairness
tradeoff-between-accuracy-and-fairness
worldview-limitations-of-fairness
pause-and-think
practice-fairness-concepts
```
