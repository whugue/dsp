# Statistics

Read Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) and [Think Bayes](http://greenteapress.com/thinkbayes/) for getting up to speed with core ideas in statistics and how to approach them programmatically. Both books are completely available online, or you can buy physical copies if you would like.

[<img src="img/think_stats.jpg" title="Think Stats"/>](http://greenteapress.com/thinkstats2/)
[<img src="img/think_bayes.png" title="Think Bayes" style="float: left"; />](http://greenteapress.com/thinkbayes/)  

## Instructions

The ThinkStats book is approximately 200 pages in length.  It is recommended you read the entire book, particularly if you are less familiar with introductory statistical concepts.

The stats exercises have been chosen to introduce/solidify some relevant statistical concepts related to data science.  The solutions for these exercises are available in the ThinkStats repository on GitHub.  You should focus on understanding the statistical concepts, python programming and interpreting the results.  If you are stuck, review the solutions and recode the python in a way that is more understandable to you. 

For example, in the first exercise, the author has already written a function to compute Cohen's D.  You could import it, or you could write your own to practice python and develop a deeper understanding of the concept. 

Complete the following exercises along with the questions in this file. They come from Think Stats, and some can be solved using code provided with the book. The preface of Think Stats [explains](http://greenteapress.com/thinkstats2/html/thinkstats2001.html#toc2) how to use the code.  

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

---

### Instructions for cloning the repo 
Using the code referenced in the book, follow the step-by-step instructions below.  

**Step 1. Create a directory on your computer where you will do the prework.  Below is an example:**

```
(Mac):      /Users/yourname/ds/metis/prework  
(Windows):  C:/ds/metis/prework
```

**Step 2. cd into the prework directory.  Use GitHub to pull this repo to your computer.**

```
$ git clone https://github.com/AllenDowney/ThinkStats2.git
```

**Step 3.  Put your ipython notebook or python code files in this directory (that way, it can pull the needed dependencies):**

```
(Mac):     /Users/yourname/ds/metis/prework/ThinkStats2/code  
(Windows):  C:/ds/metis/prework/ThinkStats2/code
```

---

###Required Exercises

*Include your Python code, results and explanation (where applicable).*

###Q1. [Think Stats Chapter 2 Exercise 4](statistics/2-4-cohens_d.md) (effect size of Cohen's d)  
Cohen's D is an example of effect size.  Other examples of effect size are:  correlation between two variables, mean difference, regression coefficients and standardized test statistics such as: t, Z, F, etc. In this example, you will compute Cohen's D to quantify (or measure) the difference between two groups of data.   

You will see effect size again and again in results of algorithms that are run in data science.  For instance, in the bootcamp, when you run a regression analysis, you will recognize the t-statistic as an example of effect size.

###Q2. [Think Stats Chapter 3 Exercise 1](statistics/3-1-actual_biased.md) (actual vs. biased)
This problem presents a robust example of actual vs biased data.  As a data scientist, it will be important to examine not only the data that is available, but also the data that may be missing but highly relevant.  You will see how the absence of this relevant data will bias a dataset, its distribution, and ultimately, its statistical interpretation.

###Q3. [Think Stats Chapter 4 Exercise 2](statistics/4-2-random_dist.md) (random distribution)  
This questions asks you to examine the function that produces random numbers.  Is it really random?  A good way to test that is to examine the pmf and cdf of the list of random numbers and visualize the distribution.  If you're not sure what pmf is, read more about it in Chapter 3.  

###Q4. [Think Stats Chapter 5 Exercise 1](statistics/5-1-blue_men.md) (normal distribution of blue men)
This is a classic example of hypothesis testing using the normal distribution.  The effect size used here is the Z-statistic. 



###Q5. Bayesian (Elvis Presley twin) 

Bayes' Theorem is an important tool in understanding what we really know, given evidence of other information we have, in a quantitative way.  It helps incorporate conditional probabilities into our conclusions.

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin? Assume we observe the following probabilities in the population: fraternal twin is 1/125 and identical twin is 1/300.  

>>We are given the prior probabilities of identical and fraternal twin births in the general population:

>>* `P(IT)=1/300 ~0.0033` (where IT=Identical Twin)
>>* `P(FT)=1/125 =0.0080` (where FT=Fraternal Twin)

>>In order to find the probability of Elvis' twin brother being identical, we need to update P(IT) to include the data that Elvis did, indeed, have a twin brother. Using Bayes theorem, we can calculate:

>>`P(IT|TB) = (P(IT) P(TB|IT))/P(TB)` (where TB=Twin Brothers)

>>`P(TB|IT)` gives the probability of identical twins being a twin brothers (i.e. male). Since identical twins always have to be the same sex, there are two possible identical twin sets: boy-boy and girl-girl. I assume each is equally likely; hence `P(TB|IT)=0.5`

>>`P(TB)=P(IT)P(TB|IT)+P(FT)P(TB|FT)`. `P(TB|FT)` gives the probability of fraternal twins being twin brothers. Since fraternal twins do NOT have the be the same gender, there are four possible fraternal twin sets: boy-boy, boy-girl, girl-boy, girl-girl. I assume each is equally likely; hence `P(TB|FT)=0.25`.

>>So `P(TB)=P(IT)P(TB|IT)+P(FT)P(TB|FT)=(0.0033)(0.5)+(0.008)(0.25)=0.0036`

>>Putting it all together: `P(IT|TB) = (P(IT) P(TB|IT))/P(TB)=((0.0033)(0.5))/(0.0036)=0.458`

>>So, the probability Elvis' twin brother was identical is roughly 46%.


---

###Q6. Bayesian &amp; Frequentist Comparison  
How do frequentist and Bayesian statistics compare?

>>The main difference between frequentist and Bayesian statistics lies in how probabilities are used to make statistical inferences about a specific population. Frequentists only use probabilities to make claims about sample statistics only, while Bayesians use probability more broadly to make claims about the population as a whole.

>>For example, let's say we were interested in determining the average income of all 20-29 year old Crown Heights residents. We draw a sample and compute the sample mean income (i) to use as an estimator of the unobserved population mean (I). Using frequentist statistical inference, we could simulate re-sampling to create a distribution modeling the probability of a specific sample mean occurring over many samplings (i.e. a sampling distribution) and determine the range where 90% of our sample means lie (i.e. the 90% confidence interval).

>>However, using the frequentist statistical inference described above, we could not make any claims about the likelihood of our sample mean (i) being an accurate representation of the actual population mean. To frequentists, probability only represents the proportion of times an observed event occurs (i.e. obtaining a specific sample mean) over many repeated experiments, rather than the level of belief a specific hypothesis might be true. 

>>A Bayesian approach to this same problem would involve creating a prior distribution for I, which models the probability a specific income is the mean for the actual population prior to obtaining any data, and then updating that distribution after analyzing the sample data collected to create a posterior distribution. We could then take the 5th and 95th percentiles of the posterior distribution to create the 90% credible interval, which contains the interval that has a 90% chance of containing I. Note this 90% credible interval is subtly different from the frequentist 90% confidence interval, which only tells us the interval the sample mean occurs in 90% of the time, rather than the interval the population mean is most likely to fall in. Indeed, a common misinterpretation of the confidence interval is that it has the same explanatory power as the credible interval, but this is untrue.


---

###Optional Exercises

The following exercises are optional, but we highly encourage you to complete them if you have the time.

###Q7. [Think Stats Chapter 7 Exercise 1](statistics/7-1-weight_vs_age.md) (correlation of weight vs. age)
In this exercise, you will compute the effect size of correlation.  Correlation measures the relationship of two variables, and data science is about exploring relationships in data.    

###Q8. [Think Stats Chapter 8 Exercise 2](statistics/8-2-sampling_dist.md) (sampling distribution)
In the theoretical world, all data related to an experiment or a scientific problem would be available.  In the real world, some subset of that data is available.  This exercise asks you to take samples from an exponential distribution and examine how the standard error and confidence intervals vary with the sample size.

###Q9. [Think Stats Chapter 6 Exercise 1](statistics/6-1-household_income.md) (skewness of household income)
###Q10. [Think Stats Chapter 8 Exercise 3](statistics/8-3-scoring.md) (scoring)
###Q11. [Think Stats Chapter 9 Exercise 2](statistics/9-2-resampling.md) (resampling)

---

## More Resources

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.







