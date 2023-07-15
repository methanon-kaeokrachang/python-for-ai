
import numpy as np
import matplotlib.pyplot as plt

# Sample data for days since the outbreak and corresponding number of COVID-19 cases
days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
cases = np.array([10, 15, 20, 30, 45, 60, 75, 90, 105, 120])

# Plotting the dataset
plt.scatter(days, cases, color='blue', label='Actual Cases')
plt.xlabel('Days since outbreak')
plt.ylabel('Number of COVID-19 cases')
plt.title('COVID-19 Dataset')
plt.legend()
plt.show()


########################################
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data for days since the outbreak and corresponding number of COVID-19 cases
days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
cases = np.array([10, 15, 20, 30, 45, 60, 75, 90, 105, 120])

# Reshape the data to fit the sklearn LinearRegression model
X = days.reshape(-1, 1)
y = cases.reshape(-1, 1)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict the number of cases for future days
future_days = np.array([11, 12, 13, 14])
future_cases = model.predict(future_days.reshape(-1, 1))

# Plotting the data and regression line
plt.scatter(days, cases, color='blue', label='Actual Cases')
plt.plot(days, model.predict(X), color='red', label='Regression Line')
plt.scatter(future_days, future_cases, color='green', label='Predicted Cases')
plt.xlabel('Days since outbreak')
plt.ylabel('Number of COVID-19 cases')
plt.title('COVID-19 Linear Regression')
plt.legend()
plt.show()
