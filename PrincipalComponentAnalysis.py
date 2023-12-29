
import pandas as pd

import numpy as np

print('\n')

print(' '*25 + 'Principal Component Analysis')
print('\n')

df = pd.read_csv('C://Users//ASHOK//Desktop//Nirma University//semester-6//Data Mining//practicals//dataset//archive//Asteroid_Updated.csv')

pd.options.display.max_rows = 200
pd.options.display.max_columns = 40

dataframe = df.loc[0:999]          # 1000 data samples

dataframe.drop(labels = ["condition_code", "n_obs_used", "neo", "pha", "extent", "GM", "IR", "spec_B", "spec_T", "G"], axis = 1, inplace = True)

print('\n')

print(dataframe.info())
print('\n')

# replacing the missing values by the mean value of that attribute

DiameterMean = round(dataframe['diameter'].mean(), 3)
dataframe['diameter'].fillna(DiameterMean, inplace = True)

AlbedoMean = round(dataframe['albedo'].mean(), 4)
dataframe['albedo'].fillna(AlbedoMean, inplace = True)

RotPerMean = round(dataframe['rot_per'].mean(), 4)
dataframe['rot_per'].fillna(RotPerMean, inplace = True)

BVMean = round(dataframe['BV'].mean(), 3)
dataframe['BV'].fillna(BVMean, inplace = True)

UBMean = round(dataframe['UB'].mean(), 3)
dataframe['UB'].fillna(UBMean, inplace = True)

print(dataframe.info())
print('\n')

print(dataframe.describe())
print('\n')

print('-> Missing values have been handled')
print('\n')


NumericalDataframe = dataframe.drop(labels = ["ar", "class"], axis = 1, inplace = False)

print(NumericalDataframe.info())
print('\n')


# Covariance matrix

CovarianceMatrix = NumericalDataframe.cov()           # in dataframe format

print(type(CovarianceMatrix))
print('')

print(CovarianceMatrix)


np.set_printoptions(formatter={'float_kind':'{:f}'.format})


CovarianceMatrixArray = CovarianceMatrix.to_numpy()
print(CovarianceMatrixArray)

print('\n')

EigenValues, NormalizedEigenVectors = np.linalg.eig(CovarianceMatrixArray)

EigenValuesList = []

for eigen in EigenValues:
    EigenValuesList.append(round(eigen, 6))

print(EigenValuesList)
print('\n')

# chosen values: 46020263.477648, 3024.625602, 33.359531, 0.674639, 0.000287
# value indices: 0, 6, 7, 8, 14

eigen = [46020263.477648, 3024.625602, 33.359531, 0.674639, 0.000287]

NormalizedEigenVectorsList = []

NEV = []

for EigenVector in NormalizedEigenVectors[:, 0]:
    NEV.append(round(EigenVector, 6))
    
NormalizedEigenVectorsList.append(NEV)

NEV = []

for EigenVector in NormalizedEigenVectors[:, 6]:
    NEV.append(round(EigenVector, 6))
    
NormalizedEigenVectorsList.append(NEV)

NEV = []

for EigenVector in NormalizedEigenVectors[:, 7]:
    NEV.append(round(EigenVector, 6))
    
NormalizedEigenVectorsList.append(NEV)

NEV = []

for EigenVector in NormalizedEigenVectors[:, 8]:
    NEV.append(round(EigenVector, 6))
    
NormalizedEigenVectorsList.append(NEV)

NEV = []

for EigenVector in NormalizedEigenVectors[:, 14]:
    NEV.append(round(EigenVector, 6))
    
NormalizedEigenVectorsList.append(NEV)


print(NormalizedEigenVectorsList)
print('\n')

# Principal Component Analysis (PCA) values for the 1000 data samples, 19 attributes each:-

AttributeMeans = []

for i in range(0, 19):
    AttributeMeans.append(round(NumericalDataframe.iloc[:, i].mean(), 6))
    
print(AttributeMeans)
print('\n')


PrincipalComponentsForEigenValues = []

for NormalizedEigenVector in NormalizedEigenVectorsList:
    PrincipalComponentsOfSamples = []
    for i in range(0, 1000):
        PrincipalComponent = 0
        for j in range(0, 19):
            value = round(NumericalDataframe.loc[i].iat[j], 6)
            mean = AttributeMeans[j]
            
            PrincipalComponent = PrincipalComponent + (NormalizedEigenVector[j] * (value - mean))
            
            PrincipalComponent = round(PrincipalComponent, 6)
            
        PrincipalComponentsOfSamples.append(PrincipalComponent)
            
    PrincipalComponentsForEigenValues.append(PrincipalComponentsOfSamples)
    

# print(PrincipalComponentsForEigenValues)

print('\n')

"""   constructing a dataframe for these Principal Component values   """
    
PCAforEigenValue1 = PrincipalComponentsForEigenValues[0]
PCAforEigenValue2 = PrincipalComponentsForEigenValues[1]
PCAforEigenValue3 = PrincipalComponentsForEigenValues[2]
PCAforEigenValue4 = PrincipalComponentsForEigenValues[3]
PCAforEigenValue5 = PrincipalComponentsForEigenValues[4]

name = list(dataframe.iloc[:, 0])

ZippedColumns = list(zip(name, PCAforEigenValue1, PCAforEigenValue2, PCAforEigenValue3, PCAforEigenValue4, PCAforEigenValue5))

PCA = pd.DataFrame(ZippedColumns, columns = ['name', 'Eigen value = 46020263.477648', 'Eigen value = 3024.625602', 'Eigen value = 33.359531', 'Eigen value = 0.674639', 'Eigen value = 0.000287'])

# PCA.to_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 5/PCA.xlsx")

print('\n')


