
print('\n')

print(' '*25 + 'Data, Similarity and Dissimilarity matrices of the dataset')
print('\n')

# loading data from the 'csv' dataset file to a 'pandas' data structure

import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import math

# df : data frame of the dataset

df = pd.read_csv('C://Users//ASHOK//Desktop//Nirma University//semester-6//Data Mining//practicals//dataset//archive//Asteroid_Updated.csv')

# print(pd.options.display.max_rows)
# print(df)

# change the maximum number of rows displayed

# pd.options.display.max_rows = 200

# print(pd.options.display.max_rows)
# print(df)

# to view the complete row details of 1 particular sample/tuple/object of index 'i'
# df.loc[i]

# print(df.loc[12])

# to return multiple such rows: df.loc[[indices(i, j, k, ...)]]

# print(df.loc[[6, 19, 35, 68]])

# to give particular names to the indices
# df.index = ["NameOfIndex0", "NameOfIndex1", "NameOfIndex2", ...]

# to return a row with a particular index name
# print(df.loc["NameOfTheParticularRowIndex"])

# removing rows with any empty cells (missing info.):
# new_df = df.dropna()          makes a new data frame altogether
# print(new_df.to_string())       

# df.dropna(inplace = True)       to change the original data frame itself,
                                # removes all the rows with missing data
    
# to display the dataset in entirety: print(df.to_string())

# replacing all the null values with a specific value: df.fillna(value, inplace = True)
# null values: missing data/info., rows with empty cells

# replacing empty values for a specific column
# df["column name"].fillna(value, inplace = True)

# deleting specific columns from the data frame:
#
    
# displaying only a section of rows of the entire dataset in data frame:
#

# deleting rows/specific rows from the data frame:
#

# creating a sub data-frame from a data-frame:

dataframe = df.loc[0:200]

pd.options.display.max_columns = 40

# deleting rows and columns

dataframe.drop(labels = ["data_arc", "condition_code", "n_obs_used", "neo", "pha", "diameter", "extent", "GM", "BV", "UB", "IR", "spec_B", "spec_T", "G"], axis = 1, inplace = True)

# finding the number of null values in each column

print('\n')

print('-> A brief statistical summary of the numeric data attributes') # not for nominal attributes
print('\n')

print(dataframe.describe())

print('\n')

print("-> 'albedo' ( values out of 201) and 'rot_per' ( values out of 201) are the two attributes having missing values")
print('')

# Missing value handling

# Approach: Replacing the missing values by the mean value of that attribute

# mean of 'albedo': 0.19774  
# mean of 'rot_per': 23.997678

# df["column name"].fillna(value, inplace = True)

# dataframe['albedo'].fillna(0.19774, inplace = True)
# dataframe['rot_per'].fillna(23.997678, inplace = True)

# all the missing values in these two columns have now been filled in

print(dataframe.describe())

print('\n')

print(dataframe.info())

# New means

# new mean of 'albedo': 0.197740 
# new mean of 'rot_per': 23.997678

# means have remain unchanged


#               Dissimilarity matrix

# ---> dissimilarity matrices for all the numeric attributes (15 numeric attributes)


# 1. dissimilarity matrix for 'a' (semi-major axis)

# dissimilarity(i, j) = |value(i)-value(j)| / value(max)-value(min)

Matrix = []

max = dataframe.loc[dataframe['ma'].idxmax()].iat[16]
min = dataframe.loc[dataframe['ma'].idxmin()].iat[16]


for i in range(0, 201):
    DissMatrixRow = []
    for j in range(0, 201):
        dis = abs(dataframe.loc[i].iat[16] - dataframe.loc[j].iat[16]) / (max - min)
        DissMatrixRow.append(dis)
        print([i, j])
    Matrix.append(DissMatrixRow)
    

Columns = []

for k in range(0, 201):
    Columns.append(k)


data = pd.DataFrame(Matrix, Columns)

print(data)

data.to_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/16. attribute 'ma'.xlsx")



# ---> dissimilarity matrices for all the nominal attributes (1 nominal attribute)

#-> nominal attribute: 'class' (asteroid class)

# 13. dissimilarity matrix for 'class'

# dissimilarity(i, j) = (p-m)/p    (p: total no. of nominal attributes, m: no. of matching/similar/equal nominal attributes)

Matrix = []

for i in range(0, 201):
    DissMatrixRow = []
    for j in range(0, 201):
        if dataframe.loc[i].iat[13] == dataframe.loc[j].iat[13]:
            dis = 0
        else:
            dis = 1
        DissMatrixRow.append(dis)
        print([i, j])
    Matrix.append(DissMatrixRow)


Columns = []

for k in range(0, 201):
    Columns.append(k)

data = pd.DataFrame(Matrix, Columns)

print(data)

data.to_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/13. attribute 'class'.xlsx")



#  #   Column   Non-Null Count  Dtype  
# ---  ------   --------------  -----  
#  0   name     201 non-null    object 
#  1   a        201 non-null    float64
#  2   e        201 non-null    float64
#  3   i        201 non-null    float64
#  4   om       201 non-null    float64
#  5   w        201 non-null    float64
#  6   q        201 non-null    float64
#  7   ad       201 non-null    float64
#  8   per_y    201 non-null    float64
#  9   H        201 non-null    float64
#  10  albedo   201 non-null    float64
#  11  rot_per  201 non-null    float64
#  12  moid     201 non-null    float64
#  13  class    201 non-null    object 
#  14  n        201 non-null    float64
#  15  per      201 non-null    float64
#  16  ma       201 non-null    float64
# dtypes: float64(15), object(2)


###          Dissimilarity matrix of the dataset (Asteroid dataset)

# -> each value of this dissimilarity matrix: mean of the corresponding values of each attribute's dissimilarity matrix

# therefore, D(i, j) = sum[d(i, j)] / 16         (16 attributes)

DataframeList = []

df1 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/1. attribute 'a'.xlsx", index_col = 0)
DataframeList.append(df1)

df2 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/2. attribute 'e'.xlsx", index_col = 0)
DataframeList.append(df2)

df3 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/3. attribute 'i'.xlsx", index_col = 0)
DataframeList.append(df3)

df4 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/4. attribute 'om'.xlsx", index_col = 0)
DataframeList.append(df4)

df5 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/5. attribute 'w'.xlsx", index_col = 0)
DataframeList.append(df5)

df6 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/6. attribute 'q'.xlsx", index_col = 0)
DataframeList.append(df6)

df7 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/7. attribute 'ad'.xlsx", index_col = 0)
DataframeList.append(df7)

df8 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/8. attribute 'per_y'.xlsx", index_col = 0)
DataframeList.append(df8)

df9 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/9. attribute 'H'.xlsx", index_col = 0)
DataframeList.append(df9)

df10 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/10. attribute 'albedo'.xlsx", index_col = 0)
DataframeList.append(df10)

df11 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/11. attribute 'rot_per'.xlsx", index_col = 0)
DataframeList.append(df11)

df12 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/12. attribute 'moid'.xlsx", index_col = 0)
DataframeList.append(df12)

df13 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/13. attribute 'class'.xlsx", index_col = 0)
DataframeList.append(df13)

df14 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/14. attribute 'n'.xlsx", index_col = 0)
DataframeList.append(df14)

df15 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/15. attribute 'per'.xlsx", index_col = 0)
DataframeList.append(df15)

df16 = pd.read_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/16. attribute 'ma'.xlsx", index_col = 0)
DataframeList.append(df16)


DissimilarityMatrix = []

for i in range(0, 201):
    DissimilarityMatrixRow = []
    for j in range(0, 201):
        sum = 0
        for k in range(0, 16):
            DataFrame = DataframeList[k]
            sum = sum + DataFrame.loc[i].iat[j]
        avg = sum / 16
        DissimilarityMatrixRow.append(avg)
    DissimilarityMatrix.append(DissimilarityMatrixRow)


Columns = []

for k in range(0, 201):
    Columns.append(k)
    
DisMatrix = pd.DataFrame(DissimilarityMatrix, Columns)

# print(DisMatrix)
# print('\n')

# print(DisMatrix.info())

DisMatrix.to_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 2/Dissimilarity Matrices of 201 samples of the Asteroid dataset/Dissimilarity Matrix/Dissimilarity Matrix for Asteroid dataset.xlsx")

print('\n')
print('Done')













