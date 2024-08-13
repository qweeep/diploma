# Cлучайный лес
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/LKOH.csv')

data = data.dropna()
data.rename(columns={'<DATE>': 'DATE'}, inplace=True)
data.rename(columns={'<CLOSE>': 'CLOSE'}, inplace=True)
data.rename(columns={'<OPEN>': 'OPEN'}, inplace=True)
data.rename(columns={'<HIGH>': 'HIGH'}, inplace=True)
data.rename(columns={'<LOW>': 'LOW'}, inplace=True)
data.rename(columns={'<VOL>': 'VOL'}, inplace=True)
data["DATE"] = data.index
data = data.drop('<TIME>', axis=1)


# Определение признаков и целевой переменной
features = ['OPEN', 'HIGH', 'LOW', 'VOL']
target_column = 'CLOSE'
X = data[features]
y = data[target_column]

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание модели случайного леса
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Обучение модели на обучающих данных
model.fit(X_train, y_train)

# Оценка производительности модели на тестовых данных
score = model.score(X_test, y_test)
print("R-squared score:", score)
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error (MSE):', mse)

# Прогнозирование цен на тестовых данных
y_pred = model.predict(X_test)

# Визуализация результатов
plt.scatter(y_test, y_pred)
plt.xlabel("True Prices")
plt.ylabel("Predicted Prices")
plt.title("True Prices vs Predicted Prices")
plt.show()

# Важность признаков
importances = model.feature_importances_
plt.bar(features, importances)
plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Feature Importance")
plt.show()