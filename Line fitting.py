
"""                            Line fitting                       """

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# dataframe: contains the training dataset (data samples comprising of features and label value)

# model parameter theta: θ

# summation symbol (sigma): Σ

def LineFitting(dataframe):
    x_data = dataframe.iloc[:, 0]
    y_data = dataframe.iloc[:, 1]
    
    N = len(dataframe)
    
    x = np.array(x_data)
    y = np.array(y_data)
    
    xy = x * y
    
    x_squared = np.power(x, 2)
    
    # 4 arrays: x, y, xy, x_squared
    
    Σx = np.sum(x)
    Σy = np.sum(y)
    Σxy = np.sum(xy)
    Σ_x_squared = np.sum(x_squared)
    
    square_Σx = np.power(Σx, 2)
    
    θ1 = ((Σx * Σy) - (N * Σxy)) / ((square_Σx) - (N * Σ_x_squared))
    
    θ0 = ((Σx * Σxy) - (Σy * Σ_x_squared)) / ((square_Σx) - (N * Σ_x_squared))
    
    return θ0, θ1


