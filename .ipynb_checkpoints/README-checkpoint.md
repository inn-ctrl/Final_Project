# Final_Project

0. PROJECT INTRODUCTION
Employee attrition vs employee turnover:
While the two terms gets intertwined sometimes, undrestanding their difference is key in human resources. Similalry, confusing them is too detrimental.

Simply put, employee turnover refers to a number of employees who leave a company over a period of time. 
employee attrition refers to a number of employees who leave a company unprecedently or due to uncontrolable reasons

One of the impact employee attrition causes over employee turnover are the following: 

- employees leaves role unfilled long-term
- sometimes roles can be eliminated 

Business invest a lot of resources to understand the reasons behind employees attrition, with an understanding there has to be some factors at play. There surely are. And the assumption is that if those factors would be delt with adequately, employee attrition would be reduced considerably. This project assumes that role. By gathering data that satisfy the factors that contribute the most to employee turnover, I use machine learning to build a model that detect those models and predict whether an employee will stay with a company over a periond of time or not.

Dataset: 

Pre-assumptions:
   * Factors at play:
     
  b. Position
     - JobRole
     - JobLevel
     - YearsAtCompany'
     - YearsInCurrentRole
     - YearsWithCurrManager
     - YearsSinceLastPromotion
       
  c. Education and experience factors 
     - Education
     - TotalWorkingYears':
     
  d. Job satisfaction
     - RelationshipSatisfaction
     - WorkLifeBalance
     - EnvironmentSatisfaction
     -  DistanceFromHome
     
  d. demographics
     - MaritalStatus
     - Gender
     - Age
     
  e. Past experience
     - NumCompaniesWorked

  f. Financial security: 
     - MonthlyIncome'
     - MonthlyRate
     - StockOptionLevel

Factors applicability: The above factors can be applied to both new and existing company employees and potential employees as long as there is historical records of that employee or potential employee. 
     
Attrition time assumed: Due to the highlighted differences with attrition and retention mentioned above, there is no time assigned to the attrition analysis in this project. It rather flags a certain individual as more or less likely to leave the company and then further actions can be taken. 
     
4. PROJECT ACCESS
This project is made of the following components:
- data related files are found in the data folder
- notebooks includes all jupyter notebooks used to handle the data, build the model, and carry out evaluation and analysis
    - the individual notebooks are numbered from 1 to 6 in their order
    - functions separation: to come up with a more organized code, the functions used in cleaning are separated in file
    - After model evaluation and hyper-parameter tuning, the best model is also dumped in requirements folder
 
- 4.model_eval_and interpretation notebook is dedicated to testing the saved model on a new dataset. 
- 
5. PREPROCESSING
The sourced data needs to be encoded in order to be standardized and used in the model. However, other cleanings are not needed since it is already cleaned. Further observations show that there is a huge class imbalance where a big number of employees ended up staying with the company, and a small number left.  Instead of dealing with this imbalance directly, I rather left it as it is since it represent the nature of the data distribution. I will resolt to using a model that handle such an imbalance.

6. EDA

From understanding the data distribution through numbers, I used different visualization to see how this is. I also tried to quantify the class imbalances which gives me an idea of how I should prepare for selecting the right model and how I should interpret it well.

From the findings, we can see that there are more employees who stayed with the company than those who left

8. MODEL-SELECTION

- Random Forest classification: Will handle imbalances in left employees without the need to apply other techniques such as oversampling and undersampling
- After splitting the data in train and test splits, we will use RandomClassifier algolrithm. Before using it though, it will be necessary to select the most suitable parameters to so that we come up with the best posible model parameters by using GridSearchCV. Then next, we fit the model to the best performing parameters to come up with the best possible results.

- Model evaluation: We evaluate the performance of our model with its accuracy and looking at the classification report.
  - Accuracy: the accuracy of the hyper-tuned model is 0.85. it is a good score if we combine this with other metrics such as precison and recall 
  - Classification report: a detailed classfication report is in file 3. model_selection found in the notebooks folder

9. Interpretation: There is always the current model performance interpretation in the file 3. model_selectin found in the notebooks folder

# References 
S. Flowers (1974), Why Employees Stay. Retrieved from: https://hbr.org/1973/07/why-employees-stay
Dataset: Link: https://www.kaggle.com/datasets/thedevastator/employee-attrition-and-factors
