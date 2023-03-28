'''
A02
'''
import pandas as pd
from sklearn.linear_model import LinearRegression
from data_extraction import table

# Load the data into a pandas dataframe
df = pd.read_html(str(table))[0]

# Prepare the input and output data
X = df.iloc[:, 1:3]  # Selecting the 'Total Cases' and 'Total Deaths' columns
y = df.iloc[:, 4]    # Selecting the 'Total Recovered' column

# Train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Print the coefficients and intercept of the linear regression model
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)
