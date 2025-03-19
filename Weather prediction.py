import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model iimport LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

np.random.seed(0)
n_samples = 1000

humiditiy = np.random.uniform(0,100,n_samples)
pressure = np.random.uniform(980,1050, n_samples)
wind_speed = np.random.uniform(0,30, n_samples)
temprature = 20 + 0.5 * humiditiy - 0.02 * pressure + 0.1 * wind_speed + np.random.normal(0,2,n_samples)

weather_data = pd.DataFrame({'humidity':humiditiy,'pressure':pressure,
                               'wind_speed':wind_speed, 'temprature':temprature})
        

plt.figure(figsize = (12,6))
plt.subplot(2,2,1)
plt.scatter(weather_data['pressure'],weather_data['temprature'],alpha=0.5)
plt.xlabel('Pressure')
plt.ylable('Temprature')
plt.title('Wind speed Vs. Temprature')


x = weather_data[['humidity','pressure','wind_speed']]
y = weather_data['temprature']

x_train , x_test , y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')

plt.tight_layout()
plt.show()

new_data = pd.DataFrame({'humidity':[65],'pressure':[1005],'wind_speed':[15]})
prediction = model.predict (new_data)

print(f'Predicted Temprature: {prediction[0]}')
