import pandas
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from pandas import DataFrame

df = DataFrame.pandas.read_csv('C:\\Users\\Администратор\\Desktop\\iq.csv')
years_of_education = df['years_of_education'][:, np.newaxis]
x_train, x_test, y_train, y_test = train_test_split(
    years_of_education, df['iq'], test_size=0.3
)
model = linear_model.LinearRegression()
model.fit(x_train, y_train)
print('first = ' + str(model.coef_[0]) + 'second = '
                       + str(model.intercept_))
y_predicted = model.predict(x.test)
score = r2_score(y_test, y_predicted)
print('Точность: %s' % score)