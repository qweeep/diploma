# Градиентный бустинг
import pandas as pd
import numpy as np
import xgboost as xgb
import plotly.express as px
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Загрузка данных
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/LKOH.csv')

# Очистка данных
data = data.dropna()
data.rename(columns={'<DATE>': 'DATE'}, inplace=True)
data.rename(columns={'<CLOSE>': 'CLOSE'}, inplace=True)
data.rename(columns={'<OPEN>': 'OPEN'}, inplace=True)
data.rename(columns={'<HIGH>': 'HIGH'}, inplace=True)
data.rename(columns={'<LOW>': 'LOW'}, inplace=True)
data.rename(columns={'<VOL>': 'VOL'}, inplace=True)
data["DATE"] = data.index
data = data.drop('<TIME>', axis=1)

# Разделение данных на обучающую и тестовую выборки
X = data.drop('CLOSE', axis=1)  
y = data['CLOSE']  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели градиентного бустинга
model = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 5, alpha = 10, n_estimators = 100)


model.fit(X_train, y_train)

# Прогнозирование на тестовых данных
y_pred = model.predict(X_test)

# Оценка модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Визуализация результатов
fig = px.scatter(x=y_test, y=y_pred, labels={'x': 'Actual', 'y': 'Predicted'})
fig.add_shape(type='line', x0=y_test.min(), y0=y_test.min(), x1=y_test.max(), y1=y_test.max(), line=dict(color='black', width=2, dash='dash'))
fig.update_layout(title='Actual vs. Predicted Prices', xaxis_title='Actual', yaxis_title='Predicted')
fig.show()

# Важность признаков
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': model.feature_importances_})
feature_importance = feature_importance.sort_values('importance', ascending=False).reset_index(drop=True)
fig = px.bar(feature_importance, x='importance', y='feature', orientation='h', labels={'x': 'Importance', 'y': 'Feature'})
fig.update_layout(title='Feature Importance')
fig.show()

print('Mean Squared Error (MSE):', mse)
print('Coefficient of Determination (R2 Score):', r2)