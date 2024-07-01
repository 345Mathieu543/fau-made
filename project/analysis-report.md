# Analysis Report
<!-- generate pdf with the following command -->
<!-- pandoc analysis-report.md -o analysis-report.pdf -V papersize:a4 -V geometry:margin=2cm -->

## Introduction
<!-- Introduces and motivates the question you answer in the report -->
Do temperature and rainfall negatively correlate with the number of people walking through the pedestrian zone in Erlangen?
Are there any other factors that have a significant impact on the number of pedestrians?

## Used Data
<!-- Describe the used data you used for the analysis (the output of your data pipeline). Briefly discuss the structure and meaning of the data (such as domain-specific value types), and implement the obligations to comply with the data licenses of your data sources if necessary. -->

## Analysis
<!-- Present the executed analysis: method, result, and interpretation. This section doesn’t need to show code, but the reader should understand what you did and why it is appropriate what you’ve done to answer the question. Focus on the results (positive and/or negative) but leave out any failed attempts. -->

Steps:

1. Median per Weekday
2. Select the days with more than 10 % difference to the Median of that weekday
3. Remove the days that are a public holiday or within an event taking place in Erlangen
4. For the remaining days, calculate the correlation between the number of pedestrians and the temperature and rainfall

## Conclusions
<!-- Explicitly answer the question you posed to yourself. Critically reflect whether the question could be answered completely and if there are any remaining uncertainties or limitations. -->

- Social Events (positively) and Sundays (negatively) have more effect on the number of pedestrians in the city rain or temperature
- 
