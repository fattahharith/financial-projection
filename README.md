Introduction

This program uses the Python programming language and the scikit-learn machine learning library to predict the revenue, expenses, and income of a corporation for the years 2023-2028, based on the existing financial data of the company.


Requirements

To run this program, you need to have the following software installed on your computer:
```
Python 3
NumPy
Pandas
scikit-learn
```
You can install NumPy, Pandas, and scikit-learn by running the following commands in your terminal or command prompt:
```
pip install numpy
pip install pandas
pip install scikit-learn
```
Usage

To use this program, follow these steps:

- Download the "dataset.csv" file, which contains the existing financial data of SKS Corporation.
- Save the file in the same directory as the "prediction.py" file.
- Open a terminal or command prompt and navigate to the directory where the files are located.


Run the following command:
```
python prediction.py
```
- The program will generate a new file named "sample_output.csv" in the same directory, which contains the predicted financial data for the years 2023-2028.
Code Explanation

Here's a breakdown of what the code does:

- Imports the necessary libraries: Pandas and scikit-learn.
- Reads the existing financial data from the "sample_output.csv" file into a Pandas DataFrame named "df".
- Creates separate DataFrames for the features (year) and target variables (revenue, expenses, income).
- Creates a LinearRegression object for each target variable.
- Fits the models to the existing data.
- Uses the models to predict values for the years 2023-2028.
- Next, we create a separate DataFrame for the features (year) and target variables (revenue, expenses, income). We will use these DataFrames to train our Linear Regression models.
- We then create a LinearRegression object for each target variable and fit the models to the existing data.
- We use the fitted models to predict the values for the years 2023-2028 and create new columns in the DataFrame for the predicted values.
- Finally, we write the DataFrame to a new CSV file.


In summary, this Python code reads financial data from a CSV file, uses Linear Regression to predict financial values for future years, and saves the predicted values in a new CSV file.
