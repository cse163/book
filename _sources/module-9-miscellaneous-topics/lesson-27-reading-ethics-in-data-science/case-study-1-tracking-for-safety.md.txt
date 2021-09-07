# Case Study 1: Tracking for Safety

## Task

Read both of the readings below. Reading 1 is article and Reading 2 are some tweets about the use of phone apps to track the potential spread of COVID-19. Then read the section below for {ref}`content:module9:lesson27:case-study-1:things-to-consider`. For context, this article was written relatively early during the pandemic (April 4, 2020) when quarantining was fairly ubiquitous and we didn't have a vaccine available yet to protect people at risk.

**Reading 1**

[Read this article](https://www.cnn.com/2020/04/04/tech/location-tracking-florida-coronavirus/index.html)

**Reading 2**

Tectronix, one of the companies involved with making this map, posted the following [tweet](https://twitter.com/tectonixgeo/status/1242628347034767361?lang=en) about it on Twitter:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Want to see the true potential impact of ignoring social distancing? Through a partnership with <a href="https://twitter.com/xmodesocial?ref_src=twsrc%5Etfw">@xmodesocial</a>, we analyzed secondary locations of anonymized mobile devices that were active at a single Ft. Lauderdale beach during spring break. This is where they went across the US: <a href="https://t.co/3A3ePn9Vin">pic.twitter.com/3A3ePn9Vin</a></p>&mdash; Tectonix (@TectonixGEO) <a data-dnt="true" href="https://twitter.com/TectonixGEO/status/1242628347034767361?ref_src=twsrc%5Etfw">March 25, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

When another user pointed out a concern about a potential violation of the user's privacy (tweet since deleted), Textronix [replied](https://mobile.twitter.com/TectonixGEO/status/1243004792932368385).

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Understand the concern, but every point of data we used here is completely anonymized and collected with user consent! We realize the implications of data collection at this scale, but used responsibly with privacy in mind, it can have massive positive effect!</p>&mdash; Tectonix (@TectonixGEO) <a data-dnt="true" href="https://twitter.com/TectonixGEO/status/1243004792932368385?ref_src=twsrc%5Etfw">March 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

(content:module9:lesson27:case-study-1:things-to-consider)=

## Things to Consider

This case study sets up an interesting tension between utility (i.e. public safety) and user's privacy. On one hand, we want to have accurate information to inform policy-makers on the general behaviors of people so they can make better informed policy decisions. But in some cases, this utility can come at the cost of someone's personal privacy.

Now, Tectronix claims (see tweet above) that there is no privacy concerns here since they collected the data with users' consent and kept the data anonymous. While we assume this is true, there are still a couple potential gray-areas here.

1. **Anonymous data sometimes isn't**: In the [next module](/module-10-beyond-163/lesson-29-privacy/index), we'll discuss the challenges of keeping anonymous data truly anonymous. You'll find that it's surprisingly easy, given enough information, to narrow down a large dataset with anonymous data, down to a single individual that you are looking for. In that lesson, we will talk about some techniques to ensure anonymity, but the key point is that it's challenging and rarely sufficient to just remove the users' name from the data. You can also see an example linked in {ref}`content:module9:lesson27:case-study-1:further-resources` below on how the New York Times could identify individuals from a large, anonymous dataset.
2. **What did the users consent to?** While the users might have consented to the collection of their data, the details of that consent are fairly important for us to consider whether using their data in this way is appropriate.

   <br />

   Many of us have probably had the experience of downloading the new app, and clicking through the "Terms of Conditions" as fast as we can just so we can get to the good stuff. This usually means by clicking the "I agree" button, you are (usually) consenting to the company using your data in a very generous manner without many restrictions. While we aren't lawyers, we assume many uses of data, including publishing anonymous maps like this, do not pose any _legal_ complications. So if it's legal, does that make it totally fine? Many privacy experts agree that legality is not enough, since our current laws might not accurately reflect the impact and importance of data. In fact, the European Union recently overhauled their data privacy laws with the introduction of [GDPR](https://gdpr-info.eu/); a move that vastly increased user's privacy rights that companies with European customers must abide by.

   <br />

   There is an additional question here of exactly what the scope of consent users agree to. An example (mentioned in the New York Times article linked below): If a user downloads a weather app, and consents that the company use their location data to improve their ability to provide a better service for the customer, is it allowed for that weather app to sell location data to advertisers? Some might claim that the advertising brings in money, that lets the developers of the app improve the software they use. But others might claim that the user was really giving a much narrower consent that might make it an _ethical_ issue for companies to use that data in scopes where consent was not provided.

(content:module9:lesson27:case-study-1:further-resources)=

## Further Resources

- Read [this New York Times piece](https://www.nytimes.com/interactive/2018/12/10/business/location-data-privacy-apps.html) on the use of "anonymous" location data to identify particular individuals and learn about their regular habits.
- See [](/module-10-beyond-163/lesson-29-privacy/index) for more information on concepts of privacy.
