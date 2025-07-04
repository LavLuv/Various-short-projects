
"""                            Plane fitting                       """

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# dataframe: contains the training dataset (data samples comprising of features and label value)

# model parameter theta: θ

# summation symbol (sigma): Σ

def PlaneFitting(dataframe):
    x1_data = dataframe.iloc[:, 0]
    x2_data = dataframe.iloc[:, 1]
    y_data = dataframe.iloc[:, 2]
    
    N = len(dataframe)
    
    x1 = np.array(x1_data)
    x2 = np.array(x2_data)
    y = np.array(y_data)
    
    x1_squared = np.power(x1, 2)
    x2_squared = np.power(x2, 2)
    
    x1x2 = x1 * x2
    x1y = x1 * y
    x2y = x2 * y
    
    # 8 arrays: x1, x2, y, x1_squared, x2_squared, x1x2, x1y, x2y
    
    Σx1 = np.sum(x1)
    Σx2 = np.sum(x2)
    Σy = np.sum(y)
    Σ_x1_squared = np.sum(x1_squared)
    Σ_x2_squared = np.sum(x2_squared)
    Σx1x2 = np.sum(x1x2)
    Σx1y = np.sum(x1y)
    Σx2y = np.sum(x2y)
    
    square_Σx1 = np.power(Σx1, 2)
    square_Σx2 = np.power(Σx2, 2)
    
    Σx2x1 = Σx1x2
    
    θ1_numerator = (Σ_x2_squared * ((Σx1 * Σy) - (N * Σx1y)) 
                    - Σx1x2 * ((Σx2 * Σy) - (N * Σx2y)) 
                    + Σx2 * ((Σx2 * Σx1y) - (Σx1 * Σx2y)))
    
    θ1_denominator = (Σ_x2_squared * ((square_Σx1) - (N * Σ_x1_squared)) 
                      - Σx1x2 * ((Σx2 * Σx1) - (N * Σx2x1)) 
                      + Σx2 * ((Σx2 * Σ_x1_squared) - (Σx1 * Σx2x1)))
    
    θ1 = θ1_numerator / θ1_denominator
    
    θ2_numerator = (θ1 * ((Σx1 * Σx2) - (N * Σx1x2)) 
                    - ((Σx2 * Σy) - (N * Σx2y)))
    
    θ2_denominator = ((N * Σ_x2_squared) - (square_Σx2))
    
    θ2 = θ2_numerator / θ2_denominator
    
    θ0 = ((Σy) - (θ1 * Σx1) - (θ2 * Σx2)) / N
    
    return θ0, θ1, θ2


