import mpld3
import sys
from scipy.stats import pearsonr
from scipy.stats import spearmanr 
from scipy.stats import kendalltau 
import pandas as pd
import numpy as np
import io
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64

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

#received_variable_type_1 = "VRP"
#received_variable_type_2 = "Trud"
#received_variable_region = "Липецкая область"

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

corr_1 = pearsonr(values_1, values_2)
corr_2 = spearmanr(values_1, values_2)
corr_3 = kendalltau(values_1, values_2)


#print(values_1)
#print(values_2) 
#print(corr_1)
#print(corr_2)
#print(corr_3)
'''
fig, ax = plt.subplots()
ax.scatter(values_1, values_2)  # добавляем данные на график

# Создаем объект BytesIO для сохранения рисунка
buf = io.BytesIO()

# Сохраняем график в buf в формате PNG
plt.savefig(buf, format='png')

# Перемещаем указатель на начало буфера
buf.seek(0)

# Теперь buf содержит изображение в формате PNG, которое можно отобразить или переслать.
# Если вам нужно преобразовать его в строку base64 для встраивания в HTML или JSON:
import base64
data = base64.b64encode(buf.read()).decode('utf8')

# график в формате base64, готовый для встраивания в HTML
#print('data:image/png;base64,' + data)

# Не забудьте закрыть buf, чтобы освободить ресурсы
buf.close()'''
# Создание графика
fig = Figure()
axis = fig.add_subplot(1, 1, 1)
axis.scatter(values_1, values_2)
axis.set_xlabel(received_variable_type_1)
axis.set_ylabel(received_variable_type_2)
axis.set_title('Диаграмма рассеивания между Показателем 1 и Показателем 2')

# Преобразование графика в PNG изображение в кодировке base64 для вставки в HTML
pngImage = io.BytesIO()
FigureCanvas(fig).print_png(pngImage)
pngImageB64String = "data:image/png;base64,"
pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
