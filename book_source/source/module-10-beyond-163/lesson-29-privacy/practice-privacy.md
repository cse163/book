# <i class="far fa-edit fa-fw"></i> Practice: Privacy

## Question 0

Consider the following fake dataset showing medical records. The dataset has been fuzzed so that some of the values are not exact. What is the largest value $k$ such that this dataset provides $k$-anonymity? Use the columns "Age", "Sex", and "Zip Code" for the insensitive columns that can identify a person.

Note that a `*` indicates a fuzzed value or part of a value that is a notation to say "any value".

| Name | Age   | Sex    | Zip Code | Diagnosis      |
| ---- | ----- | ------ | -------- | -------------- |
| \*   | 20-30 | Male   | 98\*     | Cardiovascular |
| \*   | 20-30 | Male   | 98\*     | Respiratory    |
| \*   | 20-30 | Male   | 98\*     | None           |
| \*   | 20-30 | Female | 10\*     | Cancer         |
| \*   | 20-30 | Female | 10\*     | None           |
| \*   | 20-30 | Female | 10\*     | Cardiovascular |

**<i class="far fa-edit fa-fw"></i> Your Task**

Write your answer down in your own space.

## Question 1

Suppose we had a series of $\varepsilon$-differntially private algorithms. Order them from the **strongest privacy guarantee** to the **smallest privacy guarantee** .

**<i class="far fa-edit fa-fw"></i> Your Task**

Reorder the following options. Write your answer down in your own space.

_<i class="fas fa-list-ol fa-fw"></i> Option 0_

10-differentially private

_<i class="fas fa-list-ol fa-fw"></i> Option 1_

0-differentially private

_<i class="fas fa-list-ol fa-fw"></i> Option 2_

1-differentially private

_<i class="fas fa-list-ol fa-fw"></i> Option 3_

0.5-differentially private

## Question 2

Consider our discussion of a differential privacy mechanism for jittering published statistics with the Laplace Mechanism. Select all of the following statements that are generally true.

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one or more options. Write your answer down in your own space.

_<i class="far fa-square fa-fw"></i> Option 0_

Providing stronger guarantees for privacy requires adding **more** noise to the result.

_<i class="far fa-square fa-fw"></i> Option 1_

Providing stronger guarantees for privacy requires adding **less** noise to the result.

_<i class="far fa-square fa-fw"></i> Option 2_

Providing stronger guarantees for privacy requires generating noise from a Laplace distribution with a **higher** $\varepsilon$ parameter.

_<i class="far fa-square fa-fw"></i> Option 3_

Providing stronger guarantees for privacy requires generating noise from a Laplace distribution with a **lower** $\varepsilon$ parameter.

_<i class="far fa-square fa-fw"></i> Option 4_

Providing stronger guarantees for privacy requires generating noise from a Laplace distribution that has more likelihood of numbers **close** to 0.

_<i class="far fa-square fa-fw"></i> Option 5_

Providing stronger guarantees for privacy requires generating noise from a Laplace distribution that has more likelihood of numbers **far** to 0.

## Question 3

Consider the randomized response differential privacy mechanism. We will use the procedure described in the reading where the respondent flips a fair coin that is equally likely to show up Heads/Tails.

Suppose after calling everyone in our sample, we reported that 9/20 of the respondents answered "Yes" when following the randomized response mechanism. What is our estimate of the fraction of the population that has "Yes" as their true answer (which they could have truthfully told us "Yes" 3/4 of the time, or told us a wrong answer 1/4 of the time). Enter your number as a probability (e.g., `0.33` precise to 2 decimal places).

**<i class="far fa-edit fa-fw"></i> Your Task**

Write your answer down in your own space.
