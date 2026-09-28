# Pricing A/B Test --- Technical Analysis & Data Quality

## Technical Objective

This document records how the experiment was validated, cleaned, merged,
analyzed, and statistically evaluated. Technical discrepancies remain
visible so the business analysis is auditable.

## Data Sources

`test_results.csv`: `user_id`, `timestamp`, `source`, `device`,
`operative_system`, `test`, `price`, `converted`

`user_table.csv`: `user_id`, `city`, `country`, `lat`, `long`

Experiment definition: `test = 0` corresponds to \$39 and `test = 1` to
\$59; recorded price should match assignment.

## 1. Initial Validation

Original `test_results`: **316,800 records**.

No duplicate `user_id` values were identified in either source table.
Before cleaning, **41,184 test-result users lacked a matching
geographic-table record**, with no reverse unmatched IDs.

## 2. Assignment vs. Price Validation

Observed combinations:

-   test 0 / \$39: **202,517**
-   test 0 / \$59: **210**
-   test 1 / \$39: **155**
-   test 1 / \$59: **113,918**

Total inconsistent records: **365**.

They were exported to `CSVs/mismatched_records.csv` and excluded from
clean pricing analysis. The source data cannot establish whether `test`
or `price` is wrong, so no value was guessed or repaired.

Clean dataset: **316,435 records**.

## 3. Timestamp Validation

Strict parsing:

-   Valid: **311,258**
-   Invalid: **5,177**

Malformed records were exported to `CSVs/invalid_timestamps.csv`. Their
timestamp values were not corrected, inferred, or replaced.

An invalid timestamp does **not** automatically invalidate the entire
record. When the remaining fields are otherwise valid, those records can
still contribute to analyses that do not depend on time, including
applicable overall pricing and conversion calculations. The **5,177
invalid-timestamp records are excluded specifically from analyses
requiring reliable time information**, including monthly trends, weekly
trends, experiment-period calculations, and time-based stability
analysis.

This preserves usable information while preventing unreliable timestamp
values from affecting time-dependent conclusions.

Valid observed period:

-   Start: **2015-03-02 00:04:12**
-   End: **2015-05-31 23:59:45**
-   Duration: **90 days, 23:55:33**

## 4. Geographic Merge

Clean experiment data was left-joined to `user_table` by `user_id`.

-   Before: **316,435**
-   After: **316,435**
-   Shape: **316,435 × 12**

Missing city/country/lat/long after merge: **41,141 each**. These
records remain in primary pricing analysis but not geographic
segmentation.

The pre-clean unmatched-user count in Section 1 and the post-clean
missing-geography count describe different validation stages and are
therefore retained separately rather than silently reconciled.

## 5. Conversion

`conversion rate = sum(converted) / exposed users`

-   \$39: 4,030 / 202,517 = **1.989956%**
-   \$59: 1,772 / 113,918 = **1.555505%**
-   Difference: **0.434452 percentage points**

## 6. Revenue

`observed revenue = price × conversions`

`RPU = total observed revenue / exposed users`

-   \$39 revenue: **\$157,170**
-   \$59 revenue: **\$104,548**
-   \$39 RPU: **\$0.776083**
-   \$59 RPU: **\$0.917748**
-   RPU difference: **+\$0.141665**
-   Relative change: **+18.2538%**

RPU is used because raw totals reflect unequal experimental allocation.

## 7. Statistical Test

Two-proportion z-test:

-   \$39: 4,030 / 202,517
-   \$59: 1,772 / 113,918
-   z: **8.743753**
-   p: **2.2549e-18**

At alpha 0.05, conversion differs significantly. Statistical and
business significance are reported separately.

## 8. Time Stability

Only the **311,258 valid-timestamp records** are used.

Monthly:

-   March: \$39 1.9568%; \$59 1.6166%
-   April: \$39 2.0455%; \$59 1.4890%
-   May: \$39 1.9692%; \$59 1.5582%

Weekly results also maintained \$39 \> \$59 conversion in every
displayed week.

These results describe the observed aggregate time pattern. They do not
by themselves establish why the pattern occurred.

## 9. Sample-Size / Stopping Limitation

The original predetermined sample-size target is not supplied. A sound
pre-test calculation requires significance level, power, expected
variability, and minimum detectable effect, then translates the required
sample into duration using traffic/allocation.

The observed \~91 days are therefore reported as observed duration, not
claimed as the scientifically required stopping point.

## 10. Marketing Segmentation

Conversion was grouped by source and price. Friend referral was highest
observed:

-   \$39: **4.1689%**
-   \$59: **3.3479%**

Segment comparisons are exploratory. Testing many segments creates
multiple-comparison concerns: as more groups are examined, the chance of
observing apparently unusual differences through random variation
increases. Segment findings are therefore treated as investigation leads
rather than automatically as confirmed effects unless supported by
appropriate statistical testing or independent validation.

## 11. Device / OS Segmentation

Device:

-   Mobile: \$39 **1.9872%**, \$59 **1.6146%**
-   Web: \$39 **1.9940%**, \$59 **1.4744%**

At \$39, mobile and web conversion were nearly identical. At \$59,
mobile showed a somewhat higher observed conversion rate than web. The
supplied data does not establish why.

Unusual OS result:

-   Linux/\$39: 2,204 users, 34 conversions, **1.5427%**
-   Linux/\$59: 1,926 users, 0 conversions, **0%**

The Linux/\$59 result is treated as an **identified anomaly requiring
further investigation, not as an identified cause or proof that Linux
users reject the \$59 price**.

The available dataset does not contain sufficient technical or
behavioral evidence---such as browser-level events, checkout failures,
payment errors, application logs, or detailed funnel events---to
determine why zero conversions were recorded. Possible explanations
therefore remain hypotheses rather than conclusions.

The anomaly remains an **open investigation item**. Additional technical
or behavioral data would be required to determine whether it reflects
customer behavior, a technical issue, tracking behavior, experiment
implementation, or another factor.

## 12. Geographic Segmentation

Available: **275,294 records**.

Missing geography: **41,141**.

City/price aggregation: **1,832 rows**.

A sample-size table identified **923 cities**:

-   Median \$39 group: **103**
-   Median \$59 group: **58**
-   25th percentile \$39: **51**
-   25th percentile \$59: **26**

Exploratory flag: fewer than 100 users in either price group.

-   Flagged: **686 / 923 cities = 74.3%**

The `<100` rule is descriptive and exploratory, **not a statistically
derived minimum sample-size requirement, power calculation, or proof
that observations above 100 users are statistically reliable**. No
geographic records were deleted solely because of this flag.

City-level comparisons should therefore be treated as exploratory
signals requiring stronger evidence before supporting geographic pricing
conclusions.

## 13. Novelty Limitation

Aggregate monthly direction is stable, but available fields do not
provide new-versus-existing-user information or other customer-history
evidence needed to isolate novelty.

The analysis can describe aggregate stability or variation over time,
but **novelty cannot be proved or ruled out from the supplied fields**.

## 14. Audit Trail

Preserved audit files:

-   `CSVs/mismatched_records.csv`
-   `CSVs/invalid_timestamps.csv`

Questionable source records are separated rather than overwritten,
preserving traceability for later data-owner investigation.

The technical approach follows the principle:

**Detected → examined → resolved when evidence permits → explicitly
documented as unresolved when available evidence cannot support a
defensible resolution.**

## 15. Technical Limitations

-   Original sample-size target unavailable.
-   **365** assignment/price mismatches were isolated; the source cannot
    establish which field is incorrect.
-   **5,177** malformed timestamps limit time-dependent analysis but do
    not automatically invalidate otherwise usable fields in those
    records.
-   **41,141** clean records lack geography and cannot contribute to
    geographic segmentation.
-   Most cities are small under the exploratory `<100` flag; **686 of
    923 cities** were flagged.
-   Segment comparisons create multiple-testing concerns and should
    generally be treated as exploratory unless appropriately validated.
-   The Linux/\$59 zero-conversion anomaly remains unresolved because
    the supplied dataset lacks the technical and behavioral evidence
    needed to determine root cause.
-   Novelty cannot be isolated.
-   Revenue is measurable; net profit is not.
-   Churn, lifetime value, refunds, costs/margins, retention, customer
    satisfaction, and other long-term outcomes are absent.

## Reproducibility

The Python workflow is stored in `A_B_Testing_P1.py` and performs
validation, cleaning, timestamp separation, geographic merge,
conversion/revenue calculations, significance testing, time analysis,
and segmentation.

## Power BI Deliverables

The final analytical dataset was used to develop the project's Power BI dashboard.

Project deliverables include:

- `Pricing_AB_Test_Dashboard.pbix` — original Power BI project file
- `Docs/Pricing_AB_Test_Dashboard.pdf` — exported dashboard presentation

➡️ **[View the Power BI Dashboard Presentation (PDF)](Docs/Pricing_AB_Test_Dashboard.pdf)**
