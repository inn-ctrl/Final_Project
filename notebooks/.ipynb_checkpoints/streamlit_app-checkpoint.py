import streamlit as st
import pandas as pd

# Model imports
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from joblib import dump

# dataset
data = pd.read_csv('../data/data.csv')

# Spliting dataset
X = data.drop('Attrition', axis=1)
y = data['Attrition']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# pipeline with a random forest classifier
pipeline = Pipeline([
    ('rf', RandomForestClassifier(random_state=42))
])

# grid of hyperparameters to search
param_grid = {
    'rf__n_estimators': [100, 200, 300],
    'rf__max_depth': [None, 5, 10],
    'rf__min_samples_split': [2, 5, 10],
    'rf__min_samples_leaf': [1, 2, 4]
}

# Create the grid search object
grid_search = GridSearchCV(pipeline, param_grid=param_grid, cv=5)

# Fit the grid search object to the data
grid_search.fit(X_train, y_train)

# Get the best model from grid search
best_model = grid_search.best_estimator_

# Define a function to make predictions
def predict_attrition(model, input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return prediction[0]

# Streamlit app
st.title('Predicting Employee Attrition')

# Defining input parameters using Streamlit widgets
with st.expander("Input Parameters", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider('Age', 18, 65, 25)
        total_working_years = st.slider('Total Working Years', 0, 40, 10)
        job_level = st.slider('Job Level', 1, 5, 1)
        years_at_company = st.slider('Years at Company', 0, 40, 1)
        monthly_income = st.slider('Monthly Income', 1000, 20000, 3000)
        years_in_current_role = st.slider('Years in Current Role', 0, 20, 1)
        years_with_curr_manager = st.slider('Years with Current Manager', 0, 20, 1)
        years_since_last_promotion = st.slider('Years since Last Promotion', 0, 15, 1)
    with col2:
        job_role = st.selectbox('Job Role', ['1', '2', '3', '4', '5'])
        education = st.selectbox('Education', ['1', '2', '3', '4', '5'])
        marital_status = st.selectbox('Marital Status', ['1', '2', '3'])
        num_companies_worked = st.slider('Number of Companies Worked', 0, 10, 2)
        gender = st.selectbox('Gender', ['0', '1'])
        stock_option_level = st.slider('Stock Option Level', 0, 3, 1)
        relationship_satisfaction = st.slider('Relationship Satisfaction', 1, 4, 4)
        work_life_balance = st.slider('Work Life Balance', 1, 4, 3)
        monthly_rate = st.slider('Monthly Rate', 1000, 30000, 19200)
        distance_from_home = st.slider('Distance from Home', 1, 30, 1)
        environment_satisfaction = st.slider('Environment Satisfaction', 1, 4, 4)

# Preparing input parameters dictionary
input_params = {
    'TotalWorkingYears': total_working_years,
    'JobLevel': job_level,
    'YearsAtCompany': years_at_company,
    'MonthlyIncome': monthly_income,
    'YearsInCurrentRole': years_in_current_role,
    'YearsWithCurrManager': years_with_curr_manager,
    'YearsSinceLastPromotion': years_since_last_promotion,
    'Age': age,
    'JobRole': int(job_role),  # Convert to integer
    'Education': int(education),  # Convert to integer
    'MaritalStatus': int(marital_status),  # Convert to integer
    'NumCompaniesWorked': num_companies_worked,
    'Gender': int(gender),  # Convert to integer
    'StockOptionLevel': stock_option_level,
    'RelationshipSatisfaction': relationship_satisfaction,
    'WorkLifeBalance': work_life_balance,
    'MonthlyRate': monthly_rate,
    'DistanceFromHome': distance_from_home,
    'EnvironmentSatisfaction': environment_satisfaction
}

# Display the input parameters
with st.expander("Factors", expanded=True):
    st.write(pd.DataFrame(input_params, index=[0]))

# Predict button
if st.button('Predict'):
    prediction = predict_attrition(best_model, input_params)
    if prediction == 1:
        st.subheader('Prediction')
        st.write('The model predicts that the employee is likely to leave.')
    else:
        st.subheader('Prediction')
        st.write('The model predicts that the employee is likely to stay.')
