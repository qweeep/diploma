import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import sys
import pandas as pd
import base64
from io import BytesIO


if len(sys.argv) > 1:  # Проверяем, что был передан хотя бы один аргумент
    received_variable_type_1 = sys.argv[1]
    received_variable_type_2 = sys.argv[2]
    received_variable_region = sys.argv[3]
    received_variable_link = sys.argv[4]
else:
    with open('data.txt', 'r') as f:
        received_variable_type_1 = f.readline().strip()
        received_variable_type_2 = f.readline().strip()
        received_variable_region = f.readline().strip()
        received_variable_link = f.readline().strip()


match received_variable_type_2:
        case "VRP":
           csv_file_2 = 'tables/VRP.csv'
        case "innovation":
           csv_file_2 = 'tables/innovation.csv'
        case "iznos":
           csv_file_2 = 'tables/iznos.csv'
        case "RabSila":
           csv_file_2 = 'tables/RabSila.csv'
        case "Trud":
           csv_file_2 = 'tables/Trud.csv'
        case "VredProizv":
           csv_file_2 = 'tables/VredProizv.csv'
        case "ZP":
           csv_file_2 = 'tables/ZP.csv'
        case "Bezrabotica":
           csv_file_2 = 'tables/Bezrabotica.csv'

match received_variable_type_1:
        case "VRP":
           csv_file_1 = 'tables/VRP.csv'
        case "innovation":
           csv_file_1 = 'tables/innovation.csv'
        case "iznos":
           csv_file_1 = 'tables/iznos.csv'
        case "RabSila":
           csv_file_1 = 'tables/RabSila.csv'
        case "Trud":
           csv_file_1 = 'tables/Trud.csv'
        case "VredProizv":
           csv_file_1 = 'tables/VredProizv.csv'
        case "ZP":
           csv_file_1 = 'tables/ZP.csv'
        case "Bezrabotica":
           csv_file_1 = 'tables/Bezrabotica.csv'
# Загрузка данных
try:
    df_1 = pd.read_csv(csv_file_1, index_col=0, sep=';') 
    df_2 = pd.read_csv(csv_file_2, index_col=0, sep=';')  
except Exception as e:
    print(f"Произошла ошибка при чтении файла: {e}")
    exit()


region_name = received_variable_region
data_1 = df_1.loc[region_name]
data_2 = df_2.loc[region_name]
data_1 = data_1.dropna()
data_2 = data_2.dropna()
data_1 = data_1.to_dict()
data_2 = data_2.to_dict()
values_1 = [float(value.replace(" ", "").replace(",", ".")) if isinstance(value, str) else value for value in data_1.values()]
values_2 = [float(value.replace(" ", "").replace(",", ".")) if isinstance(value, str) else value for value in data_2.values()]





if len(values_1) > len(values_2):
    values_1 = values_1[:len(values_2)]
elif len(values_2) > len(values_1):
    values_2 = values_2[:len(values_1)]
# Преобразуем список X в форму, пригодную для scikit-learn (массивы вида [[x1], [x2], ...])
X = np.array(values_1).reshape(-1, 1)
y = values_2

model = LinearRegression()
model.fit(X, y)

# Получаем коэффициенты модели
slope = model.coef_[0]
intercept = model.intercept_

reg_ur = f"y = {slope:.2f}x + {intercept:.2f}"
print(reg_ur)

# Создаем данные для линии регрессии
x_range = np.linspace(X.min(), X.max(), 100)
y_range = model.predict(x_range.reshape(-1, 1))

# Вывод оценки R² модели
r_squared = model.score(X, y)
print(f"R²: {r_squared}")


# Получаем коэффициенты модели
slope = model.coef_[0]
intercept = model.intercept_


# Создаем данные для линии регрессии
x_range = np.linspace(X.min(), X.max(), 100)
y_range = model.predict(x_range.reshape(-1, 1))

# Визуализация результатов
plt.scatter(X, y, color='blue', label='Исходные данные')
plt.plot(x_range, y_range, color='red', label='Линия регрессии')
plt.legend()
plt.xlabel('X')
plt.ylabel('y')
plt.title(f'Линейная регрессия\nR²: {round(r_squared, 2)}')

# Создаем PNG изображение из графика в base64
buffer = BytesIO()
plt.savefig(buffer, format='png')
plt.close() # закрываем контекст, чтобы избежать утечек памяти
buffer.seek(0) # перемещаем указатель в начало буфера
img_png_base64 = base64.b64encode(buffer.getvalue()).decode('utf8')

# Встроенное изображение можно использовать в HTML следующим образом:
html_img = f'data:image/png;base64,{img_png_base64}'
