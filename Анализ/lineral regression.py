# Линейная регрессия
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Загрузка данных
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/LKOH.csv')

# Обработка данных
data = data.dropna()
data["<DATE>"] = data.index
data = data.drop('<TIME>', axis=1)



# задание столбца с датой в качестве индекса
data.set_index('<DATE>', inplace=True)

# построение линейного графика временного ряда
plt.plot(data.index, data['<CLOSE>'])

# настройка меток на оси x
plt.xticks(rotation=45)

# добавление заголовка графика и меток на оси x и y
plt.title('Title of the plot')
plt.xlabel('Date')
plt.ylabel('Value')

# отображение графика
plt.show()



# Расчет количества пропущенных значений в каждом столбце
missing_values = data.isnull().sum()

# Вывод информации о количестве пропущенных значений
print(missing_values)

# Визуализация количества пропущенных значений в каждом столбце
plt.figure(figsize=(12,6))
plt.bar(missing_values.index, missing_values.values)
plt.xticks(rotation='vertical')
plt.title('Missing Values')
plt.xlabel('Columns')
plt.ylabel('Number of missing values')
plt.show()

# Разделение данных на обучающую и тестовую выборки
X = data.drop('<CLOSE>', axis=1)
y = data['<CLOSE>'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Прогнозирование на тестовых данных
y_pred = model.predict(X_test)

# Оценка модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

sns.set_style('whitegrid')
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs. Predicted Prices')
plt.show()

print('Mean Squared Error (MSE):', mse)
print('Coefficient of Determination (R2 Score):', r2)


