import sqlite3
import pandas as pd 
import numpy as np
import statistics as sp
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

# Create connection
cnx = sqlite3.connect('basketball.sqlite')
df = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)

#Data cleaning 
def convertible(i):
    try:
        int(i)
        return True
    except (TypeError, ValueError):
        return False
df = df[df.DRAFT_NUMBER.apply(lambda x: x.isnumeric())]
df = df[df.ALL_STAR_APPEARANCES.apply(lambda x : convertible(x))]
del df['PIE']
df.head()
#Further code clean
df['DRAFT_NUMBER']  = df['DRAFT_NUMBER'].astype(int)
df['DRAFT_YEAR']  = df['DRAFT_YEAR'].astype(int)
df['ALL_STAR_APPEARANCES'] = df['ALL_STAR_APPEARANCES'].astype(int)
#del df['PIE']
max(df['DRAFT_YEAR'])

features = ['DRAFT_NUMBER']
Onendone = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
Prendone = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005]



Prendonedata = df[df['DRAFT_YEAR'].isin(Prendone)]
Onendonedata = df[df['DRAFT_YEAR'].isin(Onendone)]

predistance = [2,650, 635, 360, 20, 0, 756, 0, 140, 89, 120, 92, 179, 44, 1770, 800, 470]
postdistance = [0, 364, 48, 3516, 374, 375, 386, 1185, 8, 1417, 58, 2400, 62, 2381, 33, 180, 270, 0, 384, 1160, 643]



    


#random Sample created from data 
predata = Prendonedata[Prendonedata.index % 10 == 0] 
onedata = Onendonedata[Onendonedata.index % 10 == 0] 

#finding unique schools
uniqueschoolspre = []
uniqueschoolspost = []
for i in Prendonedata['SCHOOL']:
    if not i in uniqueschoolspre:
        uniqueschoolspre.append(i);
for i in Onendonedata['SCHOOL']:
    if not i in uniqueschoolspost:
        uniqueschoolspost.append(i);
#test 
len(uniqueschoolspre)
len(uniqueschoolspost)
        
#Set target
target = ['ALL_STAR_APPEARANCES']

#Features and target for linear regression
X = df[features]
y = df[target]
#Split data into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=324)



#Linear regression and fit model

y_prediction = regressor.predict(X_test)
y_prediction

#Caculating RMSE
RMSE = sqrt(mean_squared_error(y_true = y_test, y_pred = y_prediction))

#Decesion tree regression
regressor = DecisionTreeRegressor(max_depth=20)
regressor.fit(X_train, y_train)
#Prediciton 
y_prediction = regressor.predict(X_test)
y_prediction
#Rmse
RMSE = sqrt(mean_squared_error(y_true = y_test, y_pred = y_prediction))
