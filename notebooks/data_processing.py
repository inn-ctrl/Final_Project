#list out string columns and their corresponding encodings
def encoding(df):
  df.replace({'Attrition': {'Yes': 0, 'No': 1}}, inplace=True)
  df.replace({'BusinessTravel': {'Non-Travel': 0, 'Travel_Rarely': 1, 'Travel_Frequently': 2}}, inplace=True)
  df.replace({'Department': {'Sales': 0, 'Research & Development': 1, 'Human Resources': 2}}, inplace=True)
  df.replace({'EducationField': {'Life Sciences': 0, 'Medical': 1, 'Marketing': 2, 'Technical Degree': 3, 'Other': 4, 'Human Resources': 5}}, inplace=True)
  df.replace({'Gender': {'Male': 0, 'Female': 1}}, inplace=True)
  df.replace({'JobRole': {'Sales Executive': 0, 'Research Scientist': 1, 'Laboratory Technician': 2, 'Manufacturing Director': 3, 'Healthcare Representative': 4, 'Manager': 5, 'Sales Representative':6, 'Research Director': 7, 'Human Resources': 8}}, inplace = True)
  df.replace({'MaritalStatus': {'Single': 0, 'Married': 1, 'Divorced': 2}}, inplace = True)
  df.replace({'Over18': {'Y': 1, 'N': 0}}, inplace=True)
  df.replace({'OverTime': {'Yes': 1, 'No': 0}}, inplace=True)