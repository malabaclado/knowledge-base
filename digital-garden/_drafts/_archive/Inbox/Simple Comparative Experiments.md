Two-sample t-test
Paired t-test
## Sample size determination
The estimation approach to determining sample size addresses the question: *"How accurate do you want your estimate to be?"*
## Determining power
We begin this part by defining the power of a hypothesis test. **This also provides another way of determining the sample size.**

**The power is the probability of achieving the desired outcome. **
- *What is the desired outcome of a hypothesis test?* Usually rejecting the null hypothesis.


Therefore, **power is the probability of rejecting the null hypothesis** when in fact the alternative hypothesis is true.
![[Pasted image 20230912153725.png]]

> [!NOTE]
> Before any experiment is conducted you typically want to know how many observations you will need to run. If you are performing a study to test a hypothesis, for instance in the blood pressure example where we are measuring the efficacy of the blood pressure medication, if the drug is effective there should be a difference in the blood pressure before and after the medication. Therefore we want to reject our null hypothesis, and thus we want the power (i.e. the probability of rejecting the $H_{0}$ when it is false) to be as high as possible.


Power depends on the level of the test, $\alpha$, the actual true difference in means, and $n$ (the sample size).

> [!tip]
> When you design a study you usually plan for equal sample size, since this gives the highest power in your results.

Another way to improve power is to use a more efficient procedure - *for example, if we have paired observations we could use a paired t-test.*

> [!important]
> If you can reduce variance or noise, then you can achieve an incredible savings in the number of observations you have to collect. Therefore the benefit of a good design is to get a lot more power for the same cost or much-decreased cost for the same power.

---
See also: [[STAT503 Notes - Design of Experiments]]