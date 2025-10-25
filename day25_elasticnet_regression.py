# Day 25: Understanding ElasticNet Regression (Combination of L1 and L2)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate sample data
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 4 * X.squeeze() + np.random.randn(100) * 4

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize models
linear = LinearRegression()
ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)
elastic = ElasticNet(alpha=0.1, l1_ratio=0.5)  # l1_ratio balances L1 vs L2

# Train models
linear.fit(X_train, y_train)
ridge.fit(X_train, y_train)
lasso.fit(X_train, y_train)
elastic.fit(X_train, y_train)

# Predictions
y_pred_linear = linear.predict(X_test)
y_pred_elastic = elastic.predict(X_test)

# Calculate MSE
mse_linear = mean_squared_error(y_test, y_pred_linear)
mse_elastic = mean_squared_error(y_test, y_pred_elastic)

print("Linear Regression MSE:", round(mse_linear, 2))
print("ElasticNet Regression MSE:", round(mse_elastic, 2))

# Plot comparison
plt.scatter(X_test, y_test, color='gray', label='Actual Data')
plt.plot(X_test, y_pred_linear, color='blue', label='Linear')
plt.plot(X_test, y_pred_elastic, color='red', label='ElasticNet')
plt.xlabel('X')
plt.ylabel('y')
plt.title('ElasticNet Regression (Combination of L1 + L2)')
plt.legend()
plt.show()
