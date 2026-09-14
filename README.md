# HACKATHON GROUP 1: PEOPLEPULSE EMPLOYEE ATTRITION ANALYSIS

**Project XYZ** is a comprehensive data analysis tool designed to streamline data exploration, analysis, and visualisation. The tool supports multiple data formats and provides an intuitive interface for both novice and expert data scientists.

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

* Describe your business requirements

## Hypotheses

The hypotheses that we will be examining are:

| **Hypothesis** | **Hypothesis Description** |
| -------------- | -------------------------- |
| **H1** |  |
| **H2** |  |
| **H3** |  |


### How will the hypotheses be validated? 

## Project Plan

* In order to manage this project, we used a shared GitHub Project Kanban Board and assigned specfific features to each other with a dedicated stand up and stand down to go over the board at the start and end of each day. 

* The board was structured with five main workflows stages:
    * **Backlog**: The tickets ready for refinement and discussion
    * **Ready**: Refined tickets that have been discussed and are ready for development
    * **In Progress**: Tickets that are in development with an assignee
    * **Test**: Ticket should be tested for the requirements covered and evidence to be provided for validation
    * **In Review**: Tickets ready for approval for completion
    * **Done**: Tickets approved and merged

## The rationale to map the business requirements to the Data Visualisations

* List your business requirements and a rationale for mapping them to the Data Visualisations

## Analysis techniques used
* List the data analysis methods used and explain limitations or alternative approaches.
* How did you structure the data analysis techniques? Justify your response.
* Did the data limit you, and did you use an alternative approach to meet these challenges?
* How did you use generative AI tools to help with ideation, design thinking and code optimisation?

### ETL Analysis Techniques
* **Descriptive Statistics**: analysed the mean, median, standard deviation of numerical columns using `.describe()`.
* **Data Preparation**: cleaned categorical columns with `.strip()`
* **Visualisation**: performed a quick visualisation of numerical columns with seaborn boxplots and histograms.
* **IQR Analysis**: identified and handled outliers in numerical columns by investigating the interquartile ranges.
* **Feature Engineering**: Extracted new feature columns, `AgeBracket`, `Tenure`, `AnnualIncome`, `SatisfactionScore` and encoded `Attrition` to make a new column `AttritionBinary`.

### EDA and Data Visualisations Analysis Techniques

### Machine Learning Analysis Techniques

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

## Dashboard Design

* Feel free to delete this section if this is a data visualisation only (unit 1 or 2) project submission.
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during project development, you may revisit your dashboard plan to update a feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later you used another plot type).
* How were data insights communicated to technical and non-technical audiences?
* Explain how the dashboard was designed to communicate complex data insights to different audiences. 

## Deployment (optional)

* If this is a Unit 3 Streamlit, Power BI or Tableau Public project, then you can include a link here and explain how you hosted the dashboard.

### Heroku (optional)

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the `.python-version` Python version to a [Heroku-22](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. From the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App at the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the `.slugignore` file.

## Unfixed Bugs

* Please list any unfixed bugs and explain why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
* Did you recognise gaps in your knowledge, and how did you address them?
* If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

## Development Roadmap

* What challenges did you face, and what strategies were used to overcome these challenges?
* What new skills or tools do you plan to learn next based on your project experience? 


## Main Data Analysis Libraries

* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials; however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section into Content and Media, depending on what you include in your project. 

### Content 

- The text for the Home page was taken from the Wikipedia Article A
- Instructions on how to implement form validation were taken from a [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)

* Thank the people who supported this project.
