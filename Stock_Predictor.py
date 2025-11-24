import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


file_path = "stock_data.csv"   
data = pd.read_csv(file_path)

print("✅ Dataset Loaded Successfully")
print(data.head())


X = data[['Open', 'High', 'Low', 'Volume']]
y = data['Close']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LinearRegression()
model.fit(X_train, y_train)


predictions = model.predict(X_test)


accuracy = model.score(X_test, y_test)
print("✅ Model Accuracy:", accuracy)


plt.plot(y_test.values, label="Actual Price")
plt.plot(predictions, label="Predicted Price")
plt.title("Stock Price Prediction")
plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()
plt.show()

new_data_values = np.array([[205, 208, 203, 3700000]])
new_data = pd.DataFrame(new_data_values, columns=X.columns)
future_price = model.predict(new_data)

print("✅ Predicted Future Stock Price:", future_price[0])
