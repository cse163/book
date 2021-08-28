# 📚 Lesson 29: Privacy

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/1891cb98018b4f84b843803bb6371e62?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

In the last lesson, we talked about fairness. Fairness is a crucial area (albeit a more recent area) being examined by data and computer scientists alike. We saw that defining something abstract like fairness is very difficult, and requires clear statements of values; this emphasized the importance of people in decision-making processes related to fairness in data science.

Another key area of research applicable to data science is regarding the notion of **privacy** when it comes to user's data. This is both in work defining what privacy even means and mechanisms to make sure definitions of privacy can be met. In this lesson, we will provide an overview of some of the foundational work in the field of defining and ensuring privacy.

Do note that a lot of these definitions require a rigorous mathematical definition and proof of correctness, that we don't have the background material to tackle. So you'll have to trust me that the guarantees we make are true since we cannot include a proof of their correctness (but proofs do exist).

```{admonition} Note
:class: note

This lesson is heavily inspired by The Ethical Algorithm by Michael Kearns and Aaron Roth. I highly recommend you check out their fantastic book!

```

## Concepts

- k-anonymity

- Differential Privacy

- Jittering Numbers (specific example: Laplace Mechanism)

- Randomized Response

## Table of Contents

```{toctree}
:maxdepth: 1
:caption: Contents

is-your-data-anonymous
privacy-in-practice-the-census
differential-privacy
jittering-laplace-mechanism
randomized-response
recap-and-next-steps-for-differential-privacy
pause-and-think
practice-privacy
```
