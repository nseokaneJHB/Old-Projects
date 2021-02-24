import sklearn
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.utils import shuffle


data = pd.read_csv('student-mat.csv', sep=';')
print(data)