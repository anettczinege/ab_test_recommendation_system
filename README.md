# A/B Test: Recommendation System Algorithm Update for a Streaming Platform

## Project Overview
Recommendation systems play a critical role in driving user engagement and content discovery on streaming platforms. Algorithms are frequently updated to improve relevance, increase interaction with recommended content, and prevent stagnation in user behavior over time.

This project analyzes an A/B test designed to evaluate a new recommendation algorithm against an existing system of a streaming platform (movies, TV shows, or music). The goal is to assess whether the updated algorithm meaningfully changes user engagement metrics while accounting for experimental design challenges commonly encountered in algorithmic experimentation.

Users are randomly assigned to one of two groups:
- **Control group:** existing recommendation algorithm
- **Treatment group:** updated recommendation algorithm

The analysis focuses on identifying statistically significant differences in engagement outcomes and translating those results into actionable business insights.

## Algorithm Variants
**Control Algorithm (Existing System):**
- Optimized primarily for historical user similarity
- Strongly favors familiar and previously consumed content
- Stable ranking logic with limited exploration

**Treatment Algorithm (Updated System):**
- Re-weights recommendations toward recent engagement signals
- Incorporates trending content and short-term behavioral data
- Introduces a modest exploration factor for content discovery

The platform’s long-term objective is to improve sustained engagement and retention.  
The hypothesis behind the update is that enhancing short-term interaction signals may positively influence long-term user behavior.

## Business Question
Should the updated recommendation algorithm be rolled out platform-wide based on statistically and practically meaningful improvements in user engagement?

## Hypotheses
This is a **two-sided A/B test (α = 0.05)**, as the algorithm update could either improve or worsen user behavior.
- **Null Hypothesis (H₀):** There is no statistically significant difference in engagement metrics between the control and treatment groups.
- **Alternative Hypothesis (Hₐ):** A statistically significant difference exists in engagement metrics between the control and treatment groups.

## Primary Metrics (Formal Hypothesis Testing)
- **Click-Through Rate (CTR):**  
  Proportion of recommended items clicked by users.
- **Return Rate:**  
  Proportion of users who return to the platform within 7 days.

## Secondary Metrics (Supporting Analysis)
- **Completion Rate:**  
  Share of started content watched at least 80%.
- **Average Minutes Watched per Session:**  
  Average time a user spends consuming content per session.

## Experiment Design
- **Experiment duration:** January 1, 2026 – January 21, 2026 (21 days)
- **Total users:** 24,500
  - Control group: 12,250 users
  - Treatment group: 12,250 users
- **Unit of analysis:** User (all engagement metrics aggregated at the user level prior to inference)
- **Randomization:** Users randomly assigned to control or treatment at the user level
- **Exposure rule:** Each user is exposed to only one recommendation algorithm throughout the experiment
- **Observation window:** All user sessions occurring within the experiment period

## Data Source
The dataset is **simulated** to replicate realistic user behavior patterns commonly observed in recommendation systems.  
Simulation allows:
- Full control over experimental assumptions  
- Reproducibility  
- Demonstration of experimental design and statistical rigor  
Intentional imperfections (e.g., missing values, duplication) are included to replicate real-world data challenges

## Methodology
1. **Data Acquisition / Simulation:** Generate a realistic session-level dataset representing user interactions with a recommendation system, including randomized assignment to control and treatment groups.
2. **Data Cleaning & Validation:** Perform structured data quality checks, including logical consistency validation, correction of inconsistent categorical values, missing value handling, duplicate removal, and schema enforcement to ensure analytical reliability before inference.
3. **Exploratory Data Analysis (EDA):** Examine engagement distributions, compare control and treatment groups descriptively, and construct user-level metrics for inference.  
4. **Statistical Testing:** Apply appropriate two-sample hypothesis tests to evaluate differences in primary and secondary metrics. Estimate confidence intervals and quantify effect sizes. 
5. **Visualization:** Create publication-quality visualizations to communicate metric distributions and experimental differences clearly.  
6. **Insights & Recommendations:** Interpret statistical findings in a business context and provide a data-driven rollout recommendation.

## Final Results Summary
The statistical analysis reveals mixed but meaningful effects of the updated recommendation algorithm:

| Metric | Control | Treatment | Absolute Difference | Relative Lift | 95% CI | Statistically Significant? |
|--------|---------|-----------|-----------------|---------------|--------|----------------------------|
| **Click-Through Rate (CTR)** | 15.03% | 15.97% | +0.94 pp | +6.25% | 0.84 to 1.03 pp | Yes |
| **7-Day Return Rate** | 85.57% | 85.97% | +0.40 pp | 0.47% | -0.48 to 1.27 pp | No |
| **Completion Rate** | 59.93% | 59.10% | −0.83 pp | −1.38% | -1.19 to -0.47 pp | Yes |
| **Average Watch Time (Minutes)** | 38.89 | 39.56 | +0.67 min | +1.73% | 0.39 to 0.95 min | Yes |

### Key Takeaways
- The treatment algorithm significantly increased **Click-Through Rate** (+0.94 pp).
- **7-day return rate** showed no statistically significant change.
- **Completion Rate** declined slightly (-0.83 pp), and this decrease is statistically significant.
- **Average Minutes Watched per Session** increased modestly (+0.67 minutes per user).

### Business Interpretation
The updated algorithm increases short-term engagement, as reflected by a statistically significant lift in CTR and average watch time. However, the decline in completion rate suggests a shift toward broader exploration rather than deeper content consumption.

From a strategic perspective:
- If the primary objective is to maximize interaction volume and platform activity, the treatment algorithm is a strong candidate for rollout.
- If long-term engagement and content depth are prioritized, further refinement may be required before full deployment.

The decision should align with the platform’s broader growth and monetization strategy.

## Tools & Technologies
- Python 3.13
- Python Libraries (pandas, numpy, matplotlib, seaborn, scipy, statsmodels)
- JupyterLab/Notebook (via Anaconda Navigator)   
- Git & GitHub  

## Project Status
- **Day 0:** Technical environment setup, project folder structure creation completed
- **Day 1:** Project concept, hypothesis, and metrics finalized
- **Day 2-3:** Dataset simulation completed
- **Day 4-5:** Data Cleaning completed
- **Day 6-7:** Exploratory Data Analysis completed
- **Day 8-9:** Statistical testing and visualizations completed
- **Day 10:** Summarized findings and GitHub portfolio submission