# HACKATHON GROUP 1: PEOPLEPULSE EMPLOYEE ATTRITION ANALYSIS

This project explores what drives employee attrition, using exploratory data analysis, hypothesis testing and machine learning to identify key patterns of behaviour to predict at-risk employees. The findings for this project are presented in a data app with a user interface (UI). This project will perform critical data analysis, generate useful insights, and deliver data-driven recommendations.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Dataset

### Data Governance

The dataset we have chosen is [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) sourced from Kaggle. It is a *synthetic dataset* made up of 1,470 rows of employee data (therefore does *not* represent real employees). It is a public domain dataset under an [Open Data Commons](https://opendatacommons.org/licenses/dbcl/1-0/) license.

### Dataset Content

The raw data includes the following columns:

| **Column Name** | **Description** |
| --------------- | ---------------- |
| `Age` | The age of the employee |
| `Attrition` | Whether an employee has left their company or not |
| `BusinessTravel` | Whether an employee travels regularly for work |
| `DailyRate` | Daily rate |
| `Department` | The department that the employee works for |
| `DistanceFromHome` | The distance that someone's job is from their home, measured in an unspecfied unit |
| `Education` | An employee's education level, where 1 = Below College, 2 = College, 3 = Bachelor, 4 = Master, 5 = Doctor |
| `EducationField` | The specific field an employee studied in |
| `EmployeeCount` | A column that seems to identify each row as "1 employee" |
| `EmployeeNumber` | An index list |
| `EnvironmentSatisfaction` | An employee's satisfaction level, where 1 = Low, 2 = Medium, 3 = High, 4 = Very High |
| `Gender` | The employee's gender |
| `HourlyRate` | Hourly rate |
| `JobInvolvement` | How involved an employee is in their job, where 1 = Low, 2 = Medium, 3 = High, 4 = Very High |
| `JobLevel` | The level an employee is at in the company, unspecified what the numbers relate to |
| `JobRole` | The named job role an employee holds |
| `JobSatisfaction` | How satisfied an employee feels in their job, where 1 = Low, 2 = Medium, 3 = High, 4 = Very High |
| `MaritalStatus` | The marital status of the employee |
| `MonthlyIncome` | The monthly income of an employee, with no specified currency unit |
| `MonthlyRate` | Monthly rate |
| `NumCompaniesWorked` | Number of companies that an employee has worked for |
| `Over18` | Is an employee aged over 18? |
| `OverTime` | Does the employee work overtime? |
| `PercentSalaryHike` | The percentage salary increase an employee has received |
| `PerformanceRating` | An employee's performance rating, where 1 = Low, 2 = Good, 3 = Excellent, 4 = Outstanding |
| `RelationshipSatisfaction` | Ralationship satisfaction level between employee and organisation, where 1 = Low, 2 = Medium, 3 = High, 4 = Very High |
| `StandardHours` | Standard hours worked by employee |
| `StockOptionLevel` | Stock Option |
| `TotalWorkingYears` | Number of years the employee has worked in total |
| `TrainingTimesLastYear` | Number of times an employee tok part in training last year |
| `WorkLifeBalance` | Work-life balance, where 1 = Bad, 2 = Good, 3 = Better, 4 = Best |
| `YearsAtCompany` | Number of years an employee has been at the company |
| `YearsSinceLastPromotion` | Number of years since an employee's last promotion |
| `YearsWithCurrManager` | Number of years an employee has worked with their current manager |

## Business Requirements

* This project addresses the following business problem: A company is experiencing employee attrition, but has no systematic way of identifying what’s driving it or where it’s concentrated. Without this insight, HR can only react to resignations individually, rather than addressing the underlying factors causing them or focusing retention efforts where they’re needed most.

* The business requirements are as follows:

| **Business Requirement** | **Description** |
| ------------------------ | --------------- |
| **BR1 - Reduce Employee Attrition** | Identify the key factors associated with employees leaving the organisation to support the development of effective employee retention strategies. |
| **BR2 - Improve Employee Retention in High-Risk Departments and Job Roles** | Identify departments and job roles with relatively higher attrition rates so that HR can prioritise targeted retention initiatives. |

## Hypotheses

The hypotheses that we will be examining are:

| **Hypothesis** | **Hypothesis Description** |
| -------------- | -------------------------- |
| **H1** | **Job Role and Employee Attrition**: Attrition differs significantly between job roles  |
| **H2** | **Promotion History and Employee Attrition**: Employees with limited promotion history have higher attrition |
| **H3** | **Monthly Income and Employee Attrition**: Lower-income employees have higher attrition rates |
| **H4** | **Overtime and Employee Attrition**: Employees who work overtime have a higher attrition rate than employees who do not |
| **H5** | **Lower Job Satisfaction and Employee Attrition**: Employees with lower job satisfaction have higher attrition rates than employees with higher job satisfaction |
| **H6** | **Business Travel and Employee Attrition**: Attrition differs by travel frequency, with frequent travelers having higher attrition |
| **H7** | **Distance from Home and Employee Attrition**: Employees who leave live farther from work |
| **H8** | **Years at Company and Employee Attrition**: Employees in their first few years at the company have higher attrition than long-serving employees |
| **H9** | **Stock Options and Employee Attrition**: Employees with fewer stock options are more likely to leave |
| **H10** | **Department and Employee Attrition**: Attrition differs significantly between departments |


### How will the hypotheses be validated? 

| **Hypothesis** | **How Validated?** |
| -------------- | -------------------------- |
| **H1** | Horizontal Bar Chart and Chi-Squared Test of Independence |
| **H2** | Boxplot and Mann-Whitney U Test |
| **H3** | Bar Chart and Mann-Whitney U test |
| **H4** | Heatmap and Chi-Squared Test of Independence |
| **H5** | Bar Chart and Chi-Squared Test of Independence |
| **H6** | Bar Chart and Chi-Squared Test of Independence |
| **H7** | Boxplot and Mann-Whitney U Test |
| **H8** | Boxplot and Mann-Whitney U Test |
| **H9** | Bar Chart and Chi-Squared Test of Independence |
| **H10** | Bar Chart and Chi-Squared Test of Independence |

## Project Plan

* In order to manage this project, we used a shared GitHub Project Kanban Board and assigned specfific features to each other with a dedicated stand up and stand down to go over the board at the start and end of each day. 

* The board was structured with five main workflows stages:
    * **Backlog**: The tickets ready for refinement and discussion
    * **Ready**: Refined tickets that have been discussed and are ready for development
    * **In Progress**: Tickets that are in development with an assignee
    * **Test**: Ticket should be tested for the requirements covered and evidence to be provided for validation
    * **In Review**: Tickets ready for approval for completion
    * **Done**: Tickets approved and merged

## Analysis techniques used

### ETL Analysis Techniques
* **Descriptive Statistics**: analysed the mean, median, standard deviation of numerical columns using `.describe()`.
* **Data Preparation**: cleaned categorical columns with `.strip()`
* **Visualisation**: performed a quick visualisation of numerical columns with seaborn boxplots and histograms.
* **IQR Analysis**: identified and handled outliers in numerical columns by investigating the interquartile ranges.
* **Feature Engineering**: Extracted new feature columns, `AgeBracket`, `Tenure`, `AnnualIncome`, `SatisfactionScore` and encoded `Attrition` to make a new column `AttritionBinary`.

### EDA and Data Visualisations Analysis Techniques
* **Descriptive Statistics**: analysed the mean, median, min, max
* **Hypothesis Testing**: carried out different statistical tests (Mann-Whitney U test and Chi-Squared test) and assessed the appropriate coefficient alongside the p-value to reject or uphold the null hypothesis in each case.
* **Visualisation**: created a number of visualisation types to assist in exploratory data analysis and hypothesis testing:
    * horizontal bar chart
    * bar chart
    * heatmap
    * boxplot

### Machine Learning Analysis Techniques
* **Classification Model**: trained Logistic Regression classification model to how effective it was in predicting the target variable `AttritionBinary`.
* **Train Test Split**: split the dataset into training and test sets using `scikit-learn`.
* **Preprocessing**:
    * for numerical columns: `SimpleImputer(strategy="median")` and `StandardScaler`
    * for categorical columns: `SimpleImputer(strategy="most_frequent")` and `OneHotEncoder`
* **Pipeline**: combined the preprocessing step with the `LogisticRegression` model in a pipeline, before fitting this pipeline to the training data
* **Evaluation**: evaluated the model using four metrics
    * Accuracy
    * ROC-AUC
    * Recall
    * Precision
    * F1 Score

## Ethical Considerations
Despite this being a synthetic dataset, there are still ethical considerations we need to take into consideration:
* The predictive model created is for educational purposes only and **should not be used on real employee data**. Were a similar prediction mode to be created in a real-world setting, a full audit would need to be completed including impact and fairness testing.
* The dataset contains real demographic categories (`Gender`, `MaritalStatus`, `Age`, `EducationField`) alongside an `Attrition` outcome. Any model that is built is learning patterns from these categories, even if the underlying people are not real.
* Synthetic data can still contain biases from however it was generated.

## Social Implications
* Even if this attrition model is created for educational purposes, we must acknowledge that the methodology is transferable even if the current dataset isn't real - *transferability carries responsibility*. 
* How a prediction model is used matters. A well-intentioned tool could shift organisational culture towards treating retention as a data problem to optimise rather than a relationship to build. 
* It might lead to manageriable bias: if a manager knows who has been flagged as "high attrition risk", that knowlegde could change how employees are treated.

## Data Privacy
* Fields in this dataset would be considered **personal data** under UK GDPR; several would be flagged as being linked to **protected characteristics** under the Equality Act 2010.
* If this were a dataset with real employees, combining several fields of data (even if the employee wasn't named) could lead to the ability to identify specific employees. 

## Legal Implications
* **Equality Act 2021**: If a real-life attrition model were found to disadvantage a protected characteristic group, even unintentionally, this would be discrimination.
* **Proxy Bias**: Even if you were to remove protected characteristics out of a prediction model, there might be correlations that allow a model to essentially develop biases without explicitly being trained with these characteristics as features.
* **UK GDPR and Data Protection Act 2018**: Were this real employee data, processing would fall under UK GDPR and the Data Protection Act 2018. The organisation would be requried to inform employees of how their data is used (the right to be informed), collect only what's genuinely necessary for the stated purpose, retain the data no longer than needed, and give employees the right to object to decisions made about them through automated processing. 

## Dashboard

* The **PeoplePulse** dashboard brings historical workforce patterns and model-generated risk signals into one place. It helps stakeholders decide where to investigate first, what questions to ask, and which retention themes may need attention.

### Overview Page
* The overview page provides an organisation-level summary and helps users identify workforce hotspots.

| **Visualisation** | **What Does This Show?** | **Description** |
| ------------------ | ----------------------- | --------------- |
| **KPI Card** | Employees | The number of employee records currently represented in the dataset. |
| **KPI Card** | Historical Attrition | The proportion of records where AttritionBinary indicates that the employee left. This describes the historical dataset, not a forecast. |
| **KPI Card** | High-Risk Profiles | The number of records with a model probability at or above the configured high-risk threshold. |
| **KPI Card** | Risk Bands | Shows the viewer what the different risk banks are. |
| **Bar Chart** | Hotspot Chart - Attrition by Job Role | Compare historical attrition rates across job roles to decide where deeper investigation may be useful. | 
| **Bar Chart** | Hotspot Chart - Attrition by Department | Compare historical attrition rates across departments to decide where deeper investigation may be useful. | 

### Risk Triage Page

* Risk Triage lets **authorised** users narrow the dataset using three filters.

| **Filter** | **What It Changes** | **Example Questions** |
| ---------- | ------------------- | --------------------- |
| Department | Limits records to one department. | Which profiles should HR review within Sales? |
| Job Role | Limits roles available within the chosen department. | Is a pattern concentrated in a particular role? |
| Risk Band | Low, Medium, or High model-risk groups. | How many high-risk profiles are in this selection? |

* Once the filters have been selected, it shows three KPI cards with high-level summaries on the data selected, as well as a searchable table of all matching employees. 

| **Visualisation** | **What Does This Show?** | **Description** |
| ------------------ | ----------------------- | --------------- |
| **KPI Card** | Matching Employees | Number of records matching the current filters. |
| **KPI Card** | Average Predicted Risk | Average model probability for the current selection. |
| **KPI Card** | High-Risk in Selection | Count of records in the High band within the filtered selection. |

### Hypotheses and Retention Actions Page

* This page connects observed data patterns to practical questions and possible retention actions.

#### Job Role
* Compare role-level attrition rates and investigate workload, onboarding, leadership, and progression differences.

#### Income and Fariness
* Use pay patterns to prompt benchmarking and transparent reward discussions. Do not infer personal performance from income.

#### Progression
* Explore whether limited promotion opportunities may justify career check-ins, mentoring, or development pathways.

#### Sustainable Work
* Use overtime patterns to investigate staffing, workload, flexibility, and work-life balance.

*The page presents hypotheses, not proven causes. Treat each result as a reason to investigate with qualitative evidence.*

### Deployment

* The app has been deployed via Heroku and the link is: https://people-pulse-3f8aa97595aa.herokuapp.com/

## Unfixed Bugs
* In the Jupyter Notebooks, we have found that sometimes the visualisations don't show up if you click *Run All*. If this happens, please manually run the cell again and the plots should appear.

## Development Roadmap

* This project was an excellent opportunity to understand how to collaborate on a project.
* We learnt how to use feature branches merged into main once tested. That way, we could make sure we could collaborate without overwriting each other’s work.

## Main Data Analysis Libraries

### ETL
* os
* numpy
* pandas
* matplotlib
    * .pyplot
* seaborn

### EDA
* os
* numpy
* pandas
* matplotlib
    * .pyplot
* seaborn
* scipy
    * .stats

### Visualisation Features
* joblib
* numpy
* pandas
* plotly
    * .express
    * .graph_objects

### Machine Learning
* joblib
* pandas
* matplotlib
    * .pyplot
* seaborn
* sklearn
    * .compose - ColumnTransformer
    * .impute - SimpleImputer
    * .linear_model - LogisticRegression
    * .metrics - accuracy_score, classification_report, roc_auc_score
    * .model_selection - train_test_split
    * .pipeline - Pipeline
    * .preprocessing - OneHotEncoder, StandardScaler

## Credits

### Use of Generative AI
* Generative AI was used in this project as a support troubleshooting, for unfamiliar processes and for content suggestions.

### Content 

* Credit to Rory from Code Institute for the **D-I-S-H** acronym and for taking us through a step-by-step process for ETL, particularly with regards to IQR analysis for handling outliers.
* Credit to the Code Institute LMS and Rory for support with the Machine Learning section.
* Heroku has enabled us with Student account to deploy our PeoplePulse App.
* Project Kanban Board provided by GitHub for project management. 
* Discord for enabling group discussion. 

### Media

* The image used in this README.md is from Code Institute.

## Acknowledgements

* Thank you to Code Institute and to our great cohort!