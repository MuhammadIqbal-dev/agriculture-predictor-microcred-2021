import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn import linear_model

coef = -51.36637103
intercept = 111115.3745066
def predict(year):
    predicted_value = coef*year + intercept
    print(predicted_value)
    return predicted_value