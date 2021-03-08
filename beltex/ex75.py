import pandas as pd
from pandas import concat
import pandas


df = pd.DataFrame({'name': ['Earth', 'Moon', 'Mars'], 'mass_to_earth': [1, 0.606, 0.107]})
sf = pd.DataFrame({'name': ['Jupiter'], 'mass_to_earth': [5]})
# print(df)
# print(sf)

zf = concat([df, sf])
# print(zf)

# 2. Сгрупируйте датафрейм из csv файла https://drive.google.com/open?id=1kzDXgDS5_ZTtPlOppYuIatjgXB3-Spvn
# по колонке 'job'. Посчитайте средний возраст у каждой професии.
#


ef = pandas.read_csv('C:\\Users\\Администратор\\Desktop\\data.csv')
ff = ef.sort_values('job')
x = ef['age'].sum()
y = ef.shape[0]
# print(x/y)

# 3. Отсортируйте датафрейм из пункта 2 по колонке age
d = ef.sort_values('age')
# print(d)
#
# 4. Получите только тех людей возраст которых 20 и 25 лет. Использовать isin

w = ef[ef['age'].isin([20, 25])]
print(w)