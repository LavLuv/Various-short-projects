
print('\n')

print(' '*25 + 'Missing value handling')
print('\n')

import pandas as pd

dataframe = pd.read_csv('C://Users//ASHOK//Desktop//Nirma University//semester-6//Data Mining//practicals//dataset//archive//Asteroid_Updated.csv')

# a dataset of 25000 data samples (asteroids)

df = dataframe.loc[0:24999]

pd.options.display.max_rows = 100
pd.options.display.max_columns = 40

df.drop(labels = ["data_arc", "condition_code", "n_obs_used", "neo", "pha", "diameter", "extent", "GM", "BV", "UB", "IR", "spec_B", "spec_T", "G"], axis = 1, inplace = True)

print('\n')

print('-> Information of dataset attributes') # not for nominal attributes
print('\n')

print(df.info())
print('\n')

print(df.describe())
print('\n')

# Missing value handling

print("-> 'albedo' (19239 values out of 25000) and 'rot_per' (7674 values out of 25000) are the two attributes having missing values")
print('')

# 1. replacing the missing values by mean values of those attributes

print('-> Approach: Replacing the missing values by the mean value of that attribute')
print('')

AlbedoMean = df['albedo'].mean()
print("-> Mean of 'albedo' = %f" %AlbedoMean)
print('')

RotPerMean = df['rot_per'].mean()
print("-> Mean of 'rot_per' = %f" %RotPerMean)
print('')


df['albedo'].fillna(AlbedoMean, inplace = True)
df['rot_per'].fillna(RotPerMean, inplace = True)

print('-> New info. of the dataset:-')
print('\n')

print(df.info())
print('')

print(df.describe())
print('')


# 2. replacing the missing values by median values of those attributes

df1 = dataframe.loc[0:24999]

df1.drop(labels = ["data_arc", "condition_code", "n_obs_used", "neo", "pha", "diameter", "extent", "GM", "BV", "UB", "IR", "spec_B", "spec_T", "G"], axis = 1, inplace = True)

print("-> 'albedo' (19239 values out of 25000) and 'rot_per' (7674 values out of 25000) are the two attributes having missing values")
print('')

print('-> Approach: Replacing the missing values by the median value of that attribute')
print('')

AlbedoMedian = df1['albedo'].median()
print("-> Median of 'albedo' = %f" %AlbedoMedian)
print('')

RotPerMedian = df1['rot_per'].median()
print("-> Median of 'rot_per' = %f" %RotPerMedian)
print('')

df1['albedo'].fillna(AlbedoMedian, inplace = True)
df1['rot_per'].fillna(RotPerMedian, inplace = True)

print('-> New info. of the dataset:-')
print('\n')

print(df1.info())
print('')

print(df1.describe())
print('')

print()