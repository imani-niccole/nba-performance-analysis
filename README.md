# NBA Performance Analysis

## Overview

Do star players drive NBA team success or do balanced team-wide contributions matter more?

This project analyzes player and team-level NBA performance data to examine
how scoring, assists, and rebounding patterns relate to team win percentage.

## Tools

- Python
- Selenium
- pandas
- Tableau
- Jupyter Notebook

## Dataset

The analysis contains:
- 30 NBA teams
- 578 player records
- Team performance stats
- Player scoring, assists, and rebound stats

## Analysis Process

1. Collected player and team statistics using Selenium.
2. Cleaned and validated the datasets with pandas.
3. Standardized team identifiers across player and team data.
4. Engineered concentration metrics for scoring, assists, and rebounds.
5. Examined relationships between these metrics and team win percentage.
6. Build an interactive Tableau dashboard to communicate the results. 

## Key Metrics

Scoring Concentration = Top 3 scorers' combined PPG / Top 10 scorers' combined PPG x 100

Assist Concentration = Top 3 leaders' combined APG / Top 10 leaders' combined APG x 100

Reboud Concentration = Top 3 leaders' combined RPG / Top 10 leaders' combined RPG x 100

## Key Findings

- Top 3 scoring concentration has the strongest relationship with team win percentage (r = 0.716).
- Top-scorer PPG had a moderate positive relationship with winning (r = 0.556), noting that an elite scoring core was
more closely associated with success than one leading scorer alone.
- Assist concentration (r = 0.481) was more strongly associated with winning than overall team assists (r = 0.071).
- Overall team rebounding (r = 0.511) was more strongly associated with winning than rebound concentration (r = 0.354).

## Conclusion

The results support the importance of elite contributors, but with a key caveat: 
the relationship between concentrated player production and team success differed
by statistical category (assists vs. rebounds).

Successful teams tended to have scoring concentrated among their top three
contributors, while rebounding showed a stronger relationship with overall
team production.

These findings describe *associations* within the dataset and do not 
establish causation.

## Dashboard

[NBA Performance Analysis Dashboard](https://public.tableau.com/views/NBAPerformanceAnalysis_17889866103190/NBAPerformanceAnalysis?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

[NBA Performance Analysis.pdf](https://github.com/user-attachments/files/32071707/NBA.Performance.Analysis.pdf)

## Repository Structure
- notebook = further analysis & calculate indicator concentrations
- processed = CSV file from combined raw data files 
- raw = outputted data from processing data
- scripts = pipelines used to scrape NBA website
- visuals = PDF of NBA performance dashboard

## Author

Imani Candler

[Portfolio](https://imaniniccole.my.canva.site/portfolio)  

[LinkedIn](http://www.linkedin.com/in/imanicandler)

September 10, 2026
