# Day 24: Understanding Regularization (Ridge & Lasso Regression)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate sample data
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 5 * X.squeeze() + np.random.randn(100) * 5

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Linear, Ridge, and Lasso models
linear = LinearRegression()
ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)

linear.fit(X_train, y_train)
ridge.fit(X_train, y_train)
lasso.fit(X_train, y_train)

# Predictions
y_pred_linear = linear.predict(X_test)
y_pred_ridge = ridge.predict(X_test)
y_pred_lasso = lasso.predict(X_test)

# Calculate errors
mse_linear = mean_squared_error(y_test, y_pred_linear)
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
mse_lasso = mean_squared_error(y_test, y_pred_lasso)

# Print results
print("Linear Regression MSE:", round(mse_linear, 2))
print("Ridge Regression MSE:", round(mse_ridge, 2))
print("Lasso Regression MSE:", round(mse_lasso, 2))

# Plot comparison
plt.scatter(X_test, y_test, color='gray', label='Actual Data')
plt.plot(X_test, y_pred_linear, color='blue', label='Linear')
plt.plot(X_test, y_pred_ridge, color='red', label='Ridge')
plt.plot(X_test, y_pred_lasso, color='green', label='Lasso')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regularization: Ridge vs Lasso vs Linear')
plt.legend()
plt.show()
