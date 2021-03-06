# Randomized Response

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/cae22f5a50404b05bef82d70392673a7?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

---

When discussing notions of privacy, one important point to bring up that we have not addressed yet relates to issues of _trust_ . Who do we trust to take our data and ensure it is differentially private? We might have trust in the Census Beurua to safeguard our data and follow the procedure they set up to ensure differential privacy (in fact, census takers are sworn for life to protect information that may identify individuals). Would we trust Facebook to make sure privacy is guaranteed in our data if they promised some notion of differential privacy?

Implicit in discussions of privacy are discussions of trust. To use a differentially private mechanism like Jittering, we have to trust the data gatherer and statistics publisher to not do wrong with our data. What if we don't trust this party with our data? Is it possible to have another mechanism to ensure differential privacy such that we don't have to trust some central data aggregator? It turns out that yes! It is possible to come up with a differentially private system in case you don't trust the party collecting data.

## Randomized Response

To accomplish this, we will use an approach to a "decentralized" differential privacy called the randomized response. This is, in some sense, in opposition to the jittering mechanism discussed in the last slide where we had accurate data and added noise to the summary statistic to ensure privacy. Instead, we will now add randomness in the collection of data gathering to protect individual's privacy.

To understand the mechanism, let's consider the task of polling the population about an embarrassing topic. Suppose I wanted to find out what percentage of people have cheated on their spouse. To conduct a poll, I would call up a random sample of the population, ask them if they have cheated on their spouse, and record the yes/no answers to get an estimate of the overall population that has.

There is kind of an large problem with this approach though: people might not trust us to answer truthfully! Even if we are doing this "for science", individuals might be nervous about divulging such private information since that can have real impacts on their life. The incentive to tell the truth is low, and the incentive to lie is high. If we were to actually run this polling experiment, we would probably report that near 0% of respondents have cheated on their spouse! This is probably due to a response bias, in most people not telling a random stranger on the phone such a private aspect of their life.

Even if we told the people we called that we were using differential privacy, they are still unlikely to trust us that the data we collected would never get out (you probably have never heard of differential privacy before this lesson). Remember, differential privacy is a property of published statistics. We probably still need to record the data somewhere, so it's still possible there is a data breach and privacy can be broken in that way.

So our goal is to ensure privacy in how people answer the question so they feel comfortable answering us. It turns out there is a very simple way to ensure differential privacy while not requiring the individuals to trust us with their data. We call this approach **randomized response** and it follows this very simple algorithm each individual we call will follow on their own:

- Flip a coin (don't tell us how it landed).

  - If the coinflip is a Heads, tell us the truth on whether or not you cheated (e.g., if you have cheated, report "Yes").

  - If the coinflip is a Tails, flip the coin again.

    - If the second flip comes up Heads, report "Yes"

    - If the second flip comes up Tails, report "No"

The clever part about this approach and the secret to why it guarantees privacy: if they never tell us what that original coinflip was we have no way to tell if they are answering honestly or randomly. So we can assure them that if they flip the coin on their own, there is no way we get an accurate read on if they individually have cheated or not. Even if we had a data leak from the collected data (e.g., a hacker stole all the data), every individual in the dataset has plausible deniability that their response was from the random coin flips instead of the truth!

The key to this though, is the data that we gather from this approach lets us estimate the true percentage of the population that has cheated, even if we aren't able to say with certainty if an individual person cheated or not! How is that possible? The trick is that the individual responds truthfully 3/4 of the time. Half the time, they tell us the truth, and half of the remaining time they give us a random answer that might line up with the truth by chance (leaving 1/4 of the time where they lie).

To understand how this is possible, let's think of the "forward process" of what the result we will look like if we knew before-hand the true percentage of people that have cheated. So suppose 1/3 of the population has cheated on their spouse. What would we expect the result of a poll to look like if that's the case? Recall that result of our poll is the fraction of people we call that say "Yes".

- We would expect 1/3 of the people we called to actually have cheated on their spouse. We said earlier that each time someone responds truthfully 3/4 of the time, so we would expect $1/3 \times 3/4 = 1/4$ of the people we call to truthfully report yes if they had cheated.

- But truthful cheaters are not the only places that we get "Yes" counts from. We would expect 2/3 of the people we called to not have cheated. Since we said they tell the truth 3/4 of the time, that means they would randomly tell us "Yes" 1/4 of the time even though that is not truthful to them not cheating. So we would expect $2/3 \times 1/4 = 1/6$ of the population to report "Yes" even though they haven't cheated.

- That means in total, we expect $1/4 + 1/6 = 5/12$ of the population to report "Yes" (but again, we don't know if they are from the truthful group or they just said "Yes" by chance even though they didn't cheat).

So understanding how this forward process works, we can now understand how to do this backward. If we found that 5/12 of our respondents responded "Yes", we can work backward using the logic above to arrive at an estimate that 1/3 of the population has cheated on their spouse. Note, that this is just an estimate though since all of these fractions are "we expect" statements, and you could imagine slight deviations from this since it is a random procedure. This deviation from what we expect should be unlikely when we are sampling a lot of people by this process called "the law of large numbers".

## Randomized Response and Differential Privacy

Although this process is relatively simple (flipping coins and asking them to sometimes not tell us the truth), it provides strong privacy guarantees without any need to trust the pollster! In the data we gather, we can't say for certain whether an individual cheated on their spouse or not, but we are able to gather the data we want in aggregate.

This randomized response protocol was introduced in 1965, long before the invention of differential privacy. It turns out though, that the randomized response is differentially private even though it wasn't designed with differential privacy in mind! To be specific, the protocol as described is $\ln(3)$-differentially private. It turns out there is nothing special about that constant in particular, you could provide stronger privacy guarantees by asking respondents to respond truthfully with a lower probability (e.g., rolling a die and responding truthfully 1/6 of the time). The strength in privacy tends to make your estimate in the true probability less accurate unless you poll many more people.
