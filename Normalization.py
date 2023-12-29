
import pandas as pd

import math

print('\n')

print(' '*25 + 'Data Normalization')
print('\n')

df = pd.read_csv('C://Users//ASHOK//Desktop//Nirma University//semester-6//Data Mining//practicals//dataset//archive//Asteroid_Updated.csv')

pd.options.display.max_rows = 200
pd.options.display.max_columns = 40

dataframe = df.loc[0:999]          # 1000 data samples

dataframe.drop(labels = ["data_arc", "condition_code", "n_obs_used", "neo", "pha", "diameter", "extent", "GM", "BV", "UB", "IR", "spec_B", "spec_T", "G"], axis = 1, inplace = True)

print('\n')

print(dataframe.info())
print('\n')

# filling in missing values of attributes 'albedo' (8 values) and 'rot_per' (10 values)

# replacing the missing values by the mean value of that attribute

AlbedoMean = round(dataframe['albedo'].mean(), 4)
dataframe['albedo'].fillna(AlbedoMean, inplace = True)

RotPerMean = round(dataframe['rot_per'].mean(), 4)
dataframe['rot_per'].fillna(RotPerMean, inplace = True)

print(dataframe.info())
print('\n')

print(dataframe.describe())
print('\n')

print('-> Missing values have been handled')
print('\n')

# dataframe.to_excel('C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 4/Dataset of 1000 samples.xlsx')

# Min = dataframe.iloc[:, 1].min()
# print(Min)

# Max = dataframe.iloc[:, 1].max()
# print(Max)

# print(dataframe.iloc[:, 1].count())

# print(dataframe.iloc[:, 1])

# print(dataframe.loc[0].iat[1])

"""   (a) Min-Max normalization   """

def MinMax(dataframe, attributeIndex, NewMin, NewMax, NumOfDecimalPlaces):
    
    Min = round(dataframe.iloc[:, attributeIndex].min(), NumOfDecimalPlaces)
    Max = round(dataframe.iloc[:, attributeIndex].max(), NumOfDecimalPlaces)
    
    NormalizedColumnData = []
    
    SampleSize = dataframe.iloc[:, attributeIndex].count()
    
    const = ((NewMax - NewMin)/(Max - Min))
    
    for i in range(0, SampleSize):
        Num = round(dataframe.loc[i].iat[attributeIndex], NumOfDecimalPlaces)
        
        # NormNum = ((Num - Min)/(Max - Min))*(NewMax - NewMin) + NewMin
        
        NormNum = (Num - Min)*const + NewMin
        
        NormNum = round(NormNum, NumOfDecimalPlaces)
        
        NormalizedColumnData.append(NormNum)
        
    return NormalizedColumnData
 

"""   normalizing the dataframe (1000 data samples) values   """


# 'name' attribute

a = MinMax(dataframe, 1, 1, 3, 6)

e = MinMax(dataframe, 2, 0, 1, 6)

i = MinMax(dataframe, 3, 0, 10, 6)

om = MinMax(dataframe, 4, 0, 150, 4)

w = MinMax(dataframe, 5, 0, 200, 4)

q = MinMax(dataframe, 6, 1, 3, 6)

ad = MinMax(dataframe, 7, 1, 5, 6)

per_y = MinMax(dataframe, 8, 1, 7, 6)

H = MinMax(dataframe, 9, 1, 10, 2)

# albedo = MinMax(dataframe, attributeIndex, NewMin, NewMax, NumOfDecimalPlaces)
# leaving attribute 'albedo' unnormalized

rot_per = MinMax(dataframe, 11, 1, 100, 3)

moid = MinMax(dataframe, 12, 1, 3, 5)

# attribute 'class' (nominal attribute)

n = MinMax(dataframe, 14, 0, 1, 6)

per = MinMax(dataframe, 15, 500, 2500, 3)

ma = MinMax(dataframe, 16, 50, 200, 4)



# name, albedo, class

name = list(dataframe.iloc[:, 0])

albedo = list(round(dataframe.iloc[:, 10], 3))

Class = list(dataframe.iloc[:, 13])


"""   constructing a dataframe for these normalized attribute values   """

# Normalized dataframe

ZippedColumns = list(zip(name, a, e, i, om, w, q, ad, per_y, H, albedo, rot_per, moid, Class, n, per, ma))

NormalizedDataframe = pd.DataFrame(ZippedColumns, columns = ['name', 'a', 'e', 'i', 'om', 'w', 'q', 'ad', 'per_y', 'H', 'albedo', 'rot_per', 'moid', 'class', 'n', 'per', 'ma'])


# NormalizedDataframe.to_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 4/Normalized datasets/Normalized Dataset (of 1000 samples).xlsx")



"""   (b) Z-score normalization   """

def Zscore(dataframe, attributeIndex, NumOfDecimalPlaces):
    
    Mean = round(dataframe.iloc[:, attributeIndex].mean(), NumOfDecimalPlaces)
    StdDev = round(dataframe.iloc[:, attributeIndex].std(), NumOfDecimalPlaces)
    
    NormalizedColumnData = []
    
    SampleSize = dataframe.iloc[:, attributeIndex].count()
    
    for i in range(0, SampleSize):
        Num = round(dataframe.loc[i].iat[attributeIndex], NumOfDecimalPlaces)
        
        Zscore = round(((Num - Mean) / StdDev), NumOfDecimalPlaces)
        
        NormalizedColumnData.append(Zscore)
        
    return NormalizedColumnData


"""   normalizing the dataframe (1000 data samples) values   """
        
    
# 'name' attribute

a = Zscore(dataframe, 1, 6)

e = Zscore(dataframe, 2, 6)

i = Zscore(dataframe, 3, 6)

om = Zscore(dataframe, 4, 4)

w = Zscore(dataframe, 5, 4)

q = Zscore(dataframe, 6, 6)

ad = Zscore(dataframe, 7, 6)

per_y = Zscore(dataframe, 8, 6)

H = Zscore(dataframe, 9, 2)

albedo = Zscore(dataframe, 10, 3)

rot_per = Zscore(dataframe, 11, 3)

moid = Zscore(dataframe, 12, 5)

# attribute 'class' (nominal attribute)

n = Zscore(dataframe, 14, 6)

per = Zscore(dataframe, 15, 3)

ma = Zscore(dataframe, 16, 4)


# name, class

name = list(dataframe.iloc[:, 0])

Class = list(dataframe.iloc[:, 13])


"""   constructing a dataframe for these normalized attribute values   """

# Normalized dataframe (Z-score)

ZippedColumns = list(zip(name, a, e, i, om, w, q, ad, per_y, H, albedo, rot_per, moid, Class, n, per, ma))

NormalizedDataframeZscore = pd.DataFrame(ZippedColumns, columns = ['name', 'a', 'e', 'i', 'om', 'w', 'q', 'ad', 'per_y', 'H', 'albedo', 'rot_per', 'moid', 'class', 'n', 'per', 'ma'])


# NormalizedDataframeZscore.to_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 4/Normalized datasets/Normalized Dataset (Z-score).xlsx")



"""   (c) Decimal-scaling normalization   """

def DecimalScale(dataframe, attributeIndex, NumOfDecimalPlaces):
    Data = list(dataframe.iloc[:, attributeIndex])
    
    AbsData = []
    
    for data in Data:
        AbsData.append(abs(data))
        
    MaxAbsValue = max(AbsData)
    
    n = len(str(int(MaxAbsValue)))
    
    NormalizedColumnData = []
    
    SampleSize = dataframe.iloc[:, attributeIndex].count()
    
    for i in range(0, SampleSize):
        Num = round(dataframe.loc[i].iat[attributeIndex], NumOfDecimalPlaces)
        
        NormVal = round((Num / int(math.pow(10, n))), NumOfDecimalPlaces)
        
        NormalizedColumnData.append(NormVal)
        
    return NormalizedColumnData


"""   normalizing the dataframe (1000 data samples) values   """
        
    
# 'name' attribute

a = DecimalScale(dataframe, 1, 6)

e = DecimalScale(dataframe, 2, 6)

i = DecimalScale(dataframe, 3, 6)

om = DecimalScale(dataframe, 4, 4)

w = DecimalScale(dataframe, 5, 4)

q = DecimalScale(dataframe, 6, 6)

ad = DecimalScale(dataframe, 7, 6)

per_y = DecimalScale(dataframe, 8, 6)

H = DecimalScale(dataframe, 9, 2)

albedo = DecimalScale(dataframe, 10, 3)

rot_per = DecimalScale(dataframe, 11, 3)

moid = DecimalScale(dataframe, 12, 5)

# attribute 'class' (nominal attribute)

n = DecimalScale(dataframe, 14, 6)

per = DecimalScale(dataframe, 15, 3)

ma = DecimalScale(dataframe, 16, 4)


# name, class

name = list(dataframe.iloc[:, 0])

Class = list(dataframe.iloc[:, 13])


"""   constructing a dataframe for these normalized attribute values   """

# Normalized dataframe (Decimal scaling)

ZippedColumns = list(zip(name, a, e, i, om, w, q, ad, per_y, H, albedo, rot_per, moid, Class, n, per, ma))

NormalizedDataframeDecimalScaling = pd.DataFrame(ZippedColumns, columns = ['name', 'a', 'e', 'i', 'om', 'w', 'q', 'ad', 'per_y', 'H', 'albedo', 'rot_per', 'moid', 'class', 'n', 'per', 'ma'])


# NormalizedDataframeDecimalScaling.to_excel("C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 4/Normalized datasets/Normalized Dataset (Decimal scaling).xlsx")


