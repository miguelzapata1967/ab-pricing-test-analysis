**# Pricing A/B Test — Business & Data Analysis**



**## Executive Summary**

Company XYZ tested increasing its software price from ****$39 to $59****. The experiment assigned approximately 66% of users to the original $39 price and 33% to the $59 price.



After data validation, ****316,435 clean experiment records**** were available for the primary pricing analysis. The $39 group converted at ****1.990%****, compared with ****1.556%**** for the $59 group. However, revenue per exposed user was ****$0.776 at $39**** and ****$0.918 at $59****, meaning the $59 treatment generated approximately ****18.25% more revenue per exposed user**** in the observed experiment.



The conversion-rate difference was statistically significant (two-proportion z-test: ****z = 8.744, p = 2.25e-18****). The direction was also consistent across the observed months and weeks: $39 converted at a higher rate throughout the valid time periods examined.



The central business tradeoff is clear: ****$39 produces more conversions, while $59 produces more revenue per exposed user.**** Because the supplied data contains revenue but no product costs, customer lifetime value, churn, refunds, or implementation costs, this analysis does not claim that either price is more profitable in a net-profit sense.



**## Analytical Approach**

This project uses a comprehensive review of the experiment. Expected findings, unexpected patterns, data-quality problems, missing information, statistical results, segment behavior, and analytical limitations are all reported. Records are not silently repaired when the source data does not provide enough evidence to determine the correct value.



**## Question 1 — Purpose**

The experiment evaluates whether increasing the software price from $39 to $59 improves the company's business outcome. The analysis considers both conversion and revenue and also investigates behavioral segments and stability over time.



**## Question 2 — Control and Test**

- ****Control:**** `test = 0`, expected price ****$39****

- ****Test:**** `test = 1`, expected price ****$59****



Users were randomly assigned to see a price, so the analysis refers to users as assigned/shown a price rather than saying they chose it.



**## Question 3 — Primary Metrics**

****Conversion rate**** measures the percentage of exposed users who purchased. ****Revenue per exposed user (RPU)**** is observed revenue divided by exposed users. They answer different questions: conversion measures purchase frequency; RPU incorporates the price paid.



**## Question 4 — Conversion Calculation**

`conversion rate = conversions / users exposed`



A conversion is `converted = 1`. Rates are compared between $39 and $59 and then explored across behavioral segments.



**## Question 5 — Conversion by Price**

| Price | Users | Conversions | Conversion Rate |

|---|---:|---:|---:|

| $39 | 202,517 | 4,030 | 1.990% |

| $59 | 113,918 | 1,772 | 1.556% |



The $39 price produced a conversion rate ****0.434 percentage points higher****. Relative to $39, the $59 conversion rate is about ****21.8% lower****.



****Finding:**** Raising the price reduced conversion in the observed experiment.



**## Question 6 — Revenue**

| Price | Users | Conversions | Observed Revenue | Revenue/User |

|---|---:|---:|---:|---:|

| $39 | 202,517 | 4,030 | $157,170 | $0.776 |

| $59 | 113,918 | 1,772 | $104,548 | $0.918 |



Raw total revenue is not directly comparable because allocation was unequal. RPU normalizes for exposure. $59 generated approximately ****$0.142 more per exposed user****, or ****18.25% more RPU****.



****Finding:**** The higher price lost conversions but more than offset the decline in observed RPU.



****Limitation:**** Revenue is not profit; cost information is absent.



**## Question 7 — Statistical Significance**

Two-proportion z-test:

- ****z = 8.7438****

- ****p = 2.2549e-18****



At alpha 0.05, the conversion-rate difference is statistically significant. Statistical significance does not by itself determine whether a change is economically worthwhile.



**## Question 8 — Duration and Monthly Stability**

After malformed timestamps were separated, ****311,258 records**** were available for time analysis.



- Start: ****2015-03-02 00:04:12****

- End: ****2015-05-31 23:59:45****

- Duration: ****90 days, 23:55:33****



| Month | $39 | $59 |

|---|---:|---:|

| March | 1.957% | 1.617% |

| April | 2.045% | 1.489% |

| May | 1.969% | 1.558% |



$39 converted higher in every observed month.



****Limitation:**** The original predetermined sample-size target and assumptions are not supplied. We can describe the observed ~91-day period and stability, but cannot claim 91 days was the scientifically required duration. A pre-test sample-size plan requires significance level, power, expected variability, and minimum effect size, then translates sample requirements into duration using traffic and allocation.



**## Question 9 — Weekly Stability / Early Stopping**

Weekly analysis showed $39 conversion above $59 in every displayed week from March 2 through May 31, although exact rates fluctuated.



****Finding:**** The direction was stable despite normal week-to-week variation. A planned test should not be stopped simply because a favorable result appears temporarily.



**## Question 10 — Business Significance**

- $39 RPU: ****$0.776****

- $59 RPU: ****$0.918****

- Difference: ****+$0.142/user****

- Relative increase: ****+18.25%****



The revenue effect is meaningful in the metric measured here. Stakeholders still need to consider implementation costs and longer-term effects absent from the dataset.



**## Question 11 — Marketing Source**

| Source | $39 | $59 |

|---|---:|---:|

| Friend referral | 4.169% | 3.348% |

| SEO Bing | 3.010% | 1.350% |

| Facebook Ads | 2.365% | 1.686% |

| Google Ads | 2.257% | 1.963% |

| SEO Yahoo | 1.951% | 1.046% |

| SEO Other | 1.752% | 1.248% |

| SEO Google | 1.750% | 1.600% |

| SEO Facebook | 1.746% | 1.360% |

| Yahoo Ads | 1.683% | 1.124% |

| Other Ads | 1.542% | 1.239% |

| Direct Traffic | 1.351% | 1.011% |

| Bing Ads | 1.337% | 0.958% |



****Finding:**** Friend referrals show the highest observed conversion at both prices. Google and Facebook ads are also relatively strong. These are associations, not causal proof. Multiple segment comparisons also raise a multiple-testing issue.



**## Question 12 — Device and Operating System**

**### Device**

| Device | $39 | $59 |

|---|---:|---:|

| Mobile | 1.987% | 1.615% |

| Web | 1.994% | 1.474% |



At $39, mobile and web are nearly identical. At $59, mobile is somewhat higher.



**### Operating System**

| OS | $39 | $59 |

|---|---:|---:|

| Android | 1.634% | 1.236% |

| iOS | 2.359% | 1.999% |

| Linux | 1.543% | 0.000% |

| Mac | 2.545% | 2.124% |

| Other | 1.403% | 1.106% |

| Windows | 1.870% | 1.401% |



Mac and iOS have the highest observed rates among listed OS groups.



****Additional finding:**** Linux at $59 has ****1,926 users and zero conversions****. This is unusual and should be investigated rather than explained without evidence.



**## Question 13 — Geography**

Geography was available for ****275,294 records****. ****41,141 clean experiment records**** lack city/country/latitude/longitude and remain in the primary analysis but not geographic segmentation.



**### Geographic Sample-Size Finding**

The sample-size table identified ****923 cities****.



| Statistic | $39 Users | $59 Users |

|---|---:|---:|

| Mean | 190.94 | 107.32 |

| 25th percentile | 51 | 26 |

| Median | 103 | 58 |

| 75th percentile | 177 | 101 |

| Maximum | 16,559 | 9,159 |



Using ****fewer than 100 users in either group as an exploratory flag****, ****686 of 923 cities (74.3%)**** were flagged.



The 100-user threshold is ****not a statistically derived reliability guarantee****. It is an exploratory reporting rule to expose percentages driven by very small groups.



Examples:

- Yorba Linda: 69 at $39; 8 at $59

- Yuba City: 21 at $39; 4 at $59

- Yucaipa: 130 at $39; 44 at $59

- Yuma: 137 at $39; 77 at $59



****Finding:**** Strong city-specific pricing claims are not supported without additional statistical work and/or more observations. No records were deleted because of this finding.



**## Question 14 — Stability and Novelty**

Monthly conversion showed no directional reversal. However, the dataset does not provide the new-versus-existing-user information needed to isolate novelty directly.



****Finding:**** Aggregate time stability is observable; novelty cannot be proved or ruled out from the supplied fields.



**## Question 15 — Final Evidence and Business Conclusion**

**### Evidence**

- $39 conversion: ****1.990%****

- $59 conversion: ****1.556%****

- $39 advantage: ****0.434 percentage points****

- $39 RPU: ****$0.776****

- $59 RPU: ****$0.918****

- $59 RPU increase: ****18.25%****

- Conversion difference statistically significant

- Monthly and weekly direction consistent

- Data-quality and segmentation limitations documented



**### Business Interpretation**

For the specific objective of ****maximizing observed revenue per exposed user among the two tested prices****, the experiment supports the ****$59 treatment on that metric****, with the explicit tradeoff of significantly lower conversion.



This is not proof that $59 maximizes ****profit****, because costs are not supplied, nor does it establish long-term retention, lifetime value, satisfaction, or churn effects.



**### Stakeholder Decision Context**

****$39 protects conversion volume. $59 increases observed revenue per exposed user.****



Stakeholders should combine this evidence with costs and longer-term customer metrics before a permanent pricing decision.

If the business intends to pursue the **$59 price point**, the next phase should focus on improving customer acceptance of the higher price while protecting its observed RPU advantage. That means testing value proposition and messaging, examining acquisition and funnel behavior, investigating unresolved anomalies such as Linux/$59, and defining conversion/RPU guardrails before broader rollout. The purpose of that next phase would be to determine **whether, and under what conditions, $59 can become a viable strategy**—not to assume in advance that it will succeed.



**## Complete Findings & Discrepancies Register**

1\. ****365 test/price assignment mismatches**** were isolated from clean analysis.

2\. ****5,177 malformed timestamps**** were preserved separately and excluded only from time analysis.

3\. ****41,141 clean records lack geographic information.****

4\. ****686 of 923 cities (74.3%)**** have fewer than 100 users in at least one group under the exploratory flag.

5\. ****Linux/$59 has zero conversions among 1,926 users****, requiring investigation rather than speculation.

6\. The ****original predetermined sample-size target is unavailable****, so ~91 days cannot be labeled the scientifically required stopping point.

7\. ****Novelty cannot be isolated directly**** with supplied fields.

8\. Segment analysis involves ****multiple comparisons****; isolated differences should not be treated as confirmatory tests without correction.

9\. The dataset measures ****revenue, not net profit****.

10\. The central observed tradeoff is ****higher conversion at $39 versus higher RPU at $59****.
