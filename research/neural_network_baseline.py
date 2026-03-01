from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd

# 1. Load Data
df = pd.read_csv('data/train.csv').head(1000)  # Small sample for demo
X = df[['onpromotion', 'store_nbr']]
y = df['sales']

# 2. Neural Networks REQUIRE Scaling (Essential for Principal level knowledge)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Define the Multi-Layer Perceptron (Neural Network)
# Using 2 hidden layers with 10 neurons each
nn_model = MLPRegressor(hidden_layer_sizes=(10, 10), max_iter=500, random_state=42)

# 4. Train
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)
nn_model.fit(X_train, y_train)

print(f"Neural Network Training Score: {nn_model.score(X_test, y_test):.4f}")
