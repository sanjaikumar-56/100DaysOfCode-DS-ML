# Day 26: Understanding Train-Test Split and Cross Validation

import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate sample data
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 3 * X.squeeze() + np.random.randn(100) * 2

# Step 1: Train-Test Split (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate performance
mse = mean_squared_error(y_test, y_pred)
print("Train-Test Split MSE:", round(mse, 2))

# Step 2: K-Fold Cross Validation (k=5)
scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
mean_score = -scores.mean()
print("Cross-Validation Average MSE:", round(mean_score, 2))
