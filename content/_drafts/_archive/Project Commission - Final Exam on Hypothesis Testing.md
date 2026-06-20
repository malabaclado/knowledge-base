> [!NOTE]- **Problem 1: E-commerce Conversion Rates**
> **Scenario:** An e-commerce website introduces a new user interface design, claiming that it will improve the conversion rate (the percentage of visitors who make a purchase). The historical conversion rate is known to be 3%.
> **Hypotheses:** Null Hypothesis (H0​): The new design has no effect on the conversion rate (p=0.03).Alternative Hypothesis (Ha​): The new design increases the conversion rate (p>0.03).
> **Data:** A sample of 500 visitors using the new design results in 20 purchases.
> **Test:** Conduct a hypothesis test at a 5% significance level to determine if the new design has a significant impact on the conversion rate.

%% One-sample test of proportion (p-value approach) %%
Hypotheses:
- $H_{0}: p=0.03$ The new design has no effect on the conversion rate
- $H_{A}: p>0.03$ The new design increases the conversion rate

Significance level: $\alpha = 0.05$
Critical z-score: $z_{\alpha} = -1.645$

Test: Reject $H_{0}$ if $z \geq z_{\alpha}$

Computing the z-score:
$$Z =\frac{\frac{X}{n} - p_{0}}{\sqrt{ \frac{(p_{0}) (1-p_{0})}{n} }}$$
where X=20, n=500


---

> [!NOTE]+ Problem 2: Product Preference
> **Scenario:** A marketing team wants to know if there is a significant relationship between customer preferences for a product (Option A, Option B, Option C) and their age group (18-25, 26-35, 36-45).
> **Hypotheses:** Null Hypothesis (H0​): Product preference and age group are independent.Alternative Hypothesis (Ha​): Product preference and age group are associated
> **Data:** A survey of 500 customers and their preferences and age groups.Product Preference: Option A (150), Option B (200), Option C (150)Age Group: 18-25 (180), 26-35 (200), 36-45 (120)
> **Test:** Conduct a chi-square test at a 1% significance level to determine if there is a significant relationship between product preference and age group.


Hypotheses:
- $H_{0}$ Product preference and age group are independent.
- $H_{A}$ Product preference and age group are associated

Significance level: $\alpha = 0.01$
Critical Z-score:
Test:Chi-square Test of Independence

Test statistic:
$$Q_{1} = \sum^{2}_{i=1} \frac{(Y_{i} - np_{i})^2}{np_{i}}$$
