import pandas as pd
from sklearn.linear_model import LinearRegression

# Read the existing data into a Pandas DataFrame
print("Reading input file...")
df = pd.read_csv('dataset.csv')

# Create separate DataFrames for the features (year) and target variables (revenue, expenses, income)
print("Initiating the variables...")
X = df[['year']]
y_revenue = df[['revenue']]
y_expenses = df[['expenses']]
y_income = df[['income']]

# Create a LinearRegression object for each target variable
print("Creating LinearRegression objects...")
lr_revenue = LinearRegression()
lr_expenses = LinearRegression()
lr_income = LinearRegression()

# Fit the models to the existing data
lr_revenue.fit(X, y_revenue)
lr_expenses.fit(X, y_expenses)
lr_income.fit(X, y_income)

# Use the models to predict values for 2023-2028
print("Generating prediction...")
years = [[2023], [2024], [2025], [2026], [2027], [2028]]
predicted_revenue = lr_revenue.predict(years)
predicted_expenses = lr_expenses.predict(years)
predicted_income = lr_income.predict(years)

# Create a new DataFrame for the predicted values
print("Prediction completed. Generating sample_output.csv...")
predicted_df = pd.DataFrame({
    'year': [2023, 2024, 2025, 2026, 2027, 2028],
    'revenue': predicted_revenue.reshape(-1),
    'expenses': predicted_expenses.reshape(-1),
    'income': predicted_income.reshape(-1)
})

# Concatenate the two DataFrames together
df = pd.concat([df, predicted_df], ignore_index=True)

# Write the DataFrame to a new CSV file
df.to_csv('sample_output.csv', index=False)

print("File created.")
