
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
