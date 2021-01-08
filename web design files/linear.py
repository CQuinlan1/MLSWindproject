import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression # importing my tools in python 
from sklearn.metrics import r2_score
from scipy import stats


data = pd.read_csv(r'C:\Users\35387\Desktop\Galway\python\powerproduction.csv',usecols= ['Speed','Power'])# importing the data

#df = pd.DataFrame(data, columns= ['Speed','Power'])

X = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array # adapted from https://towardsdatascience.com/linear-regression-in-6-lines
Y = data.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
lin = LinearRegression() 
C = data.iloc[:, 0]  # values converts it into a numpy array # adapted from https://towardsdatascience.com/linear-regression-in-6-lines
D = data.iloc[:, 1] 
 
  
lin.fit(X, Y) 

user = input("value")

mymodel = np.poly1d(np.polyfit(C, D, 1))

linelec = mymodel(value)
print ('with wind speeds of 'value' using linear function we get',+linelec)


user = input("value")

mymodel = np.poly1d(np.polyfit(C, D, 2))

polelec = mymodel(value)
print ('with wind speeds of 'value' using linear function we get',+elepol)