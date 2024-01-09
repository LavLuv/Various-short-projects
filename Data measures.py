
import math

print('\n')

print(' '*16 + '##  Data measures:-')
print('\n')

m = int(input('-> Input an even positive number: '))

while m <= 0 or m % 2 != 0 :
    while m % 2 != 0 :
        if m <= 0 :
            break
        print('')
        print('The number should be even')
        print('')
        m = int(input('-> Input an even positive number: '))
    if m > 0 :
        break
    print('')
    print('The number should be positive')
    print('')
    m = int(input('-> Input an even positive number: '))
    

Data = []

print('\n')

print('--> Input the %d observations:- ' %m)

x = float(input(' 1st Obsv. = '))
Data.append(x)

x = float(input(' 2nd Obsv. = '))
Data.append(x)

x = float(input(' 3rd Obsv. = '))
Data.append(x)

for i in range(3, m, 1) :
    x = float(input(' %dth Obsv. = ' %(i+1)))
    Data.append(x)
    
print('\n')

print('# These observations will now be grouped into two data sets of %d values each' %(m/2))
print('')

DataA = []

DataB = []

for i in range(0, int(m/2), 1) :
    DataA.append(Data[i])

for i in range(int(m/2), m, 1) :
    DataB.append(Data[i])

print('')
print('Data set A: ')

print(DataA)

print('')
print('Data set B: ')

print(DataB)

print('\n')

print(' '*16 + '#  Mean')
print('\n')

MeanA = sum(DataA)/int(m/2)

MeanB = sum(DataB)/int(m/2)

print('Mean (Data set A) = %f' %MeanA)
print('')

print('Mean (Data set B) = %f' %MeanB)
print('')

DevA = []

DevB = []

for i in range(0, int(m/2), 1) :
    DevI = DataA[i] - MeanA
    DevA.append(DevI)
    
for i in range(0, int(m/2), 1) :
    DevI = DataB[i] - MeanB
    DevB.append(DevI)

DevSqrA = []

DevSqrB = []

for i in range(0, int(m/2), 1) :
    DevSqrI = math.pow(DevA[i], 2)
    DevSqrA.append(DevSqrI)

for i in range(0, int(m/2), 1) :
    DevSqrI = math.pow(DevB[i], 2)
    DevSqrB.append(DevSqrI)
    
VarianceA = sum(DevSqrA)/int(m/2)

VarianceB = sum(DevSqrB)/int(m/2)

print('\n')

print(' '*16 + '#  Variance')
print('\n')

print('Variance (Data set A) = %f' %VarianceA)
print('')

print('Variance (Data set B) = %f' %VarianceB)
print('')

StdDeviationA = math.sqrt(VarianceA)

StdDeviationB = math.sqrt(VarianceB)

print('\n')

print(' '*16 + '#  Standard Deviation')
print('\n')

print('Standard Deviation (Data set A) = %f' %StdDeviationA)
print('')

print('Standard Deviation (Data set B) = %f' %StdDeviationB)
print('')

# Z-score (of an observation) = (observation value - mean) / standard deviation

# Z-score is also known as Standard score

print('\n')

print(' '*14 + '##  Z-scores of each observation:-')
print('\n')

Z_scoreA = []

Z_scoreB = []

for i in range(0, int(m/2), 1) :
    Z_A = DevA[i] / StdDeviationA
    Z_scoreA.append(Z_A)
    
for i in range(0, int(m/2), 1) :
    Z_B = DevB[i] / StdDeviationB
    Z_scoreB.append(Z_B)

print(' '*12 + '# of Data set A')
print('')

for i in range(0, int(m/2), 1) :
    print('-> Z-score (obsv. %d) = %f' %((i+1), Z_scoreA[i]))
    print('')
    
print('')

print(' '*12 + '# of Data set B')
print('')

for i in range(0, int(m/2), 1) :
    print('-> Z-score (obsv. %d) = %f' %((i+1), Z_scoreB[i]))
    print('')

# Scatter plot between Data set A and Data set B

import matplotlib.pyplot as plt

print('\n')

print(' '*6 + '##  Scatter plot between Data set A and Data set B')
print('\n')

plt.scatter(DataA, DataB)

plt.title('Scatter Plot')

plt.xlabel('Data set A observations')
plt.ylabel('Data set B observations')

plt.show()

print('\n\n')

# Histogram

print(' '*15 + '##  Histogram')
print('')

import numpy as np

n = int(input('-> Input the number of bins to be plotted in histogram: '))

print('\n')

plt.hist(Data, bins = n, range = (math.floor(min(Data)), math.ceil(max(Data))), ec = 'black', color = 'lime')       

plt.xticks(np.arange(math.floor(min(Data)), math.ceil(max(Data))+1, (math.ceil(max(Data)) - math.floor(min(Data)))/n))

plt.title('Histogram for the entire Data set')

plt.xlabel('Class ranges of observation values')
plt.ylabel('Frequency of values in class range')

plt.show()

print('\n\n')


# Mean, Variance and Standard Deviation of the entire Data set

Mean = (MeanA + MeanB) / 2

Variance = ((VarianceA + VarianceB) / 2) + math.pow((MeanA - MeanB) / 2, 2)

StdDeviation = math.sqrt(Variance)


# Gaussian probability density function

print(' '*11 + '##  Gaussian probability density function')
print('\n')


# Gaussian = math.exp(-math.pow(Data - Mean, 2) / (2 * Variance)) / (StdDeviation * math.sqrt(2 * math.pi))                                  

Data.sort()

Gaussian = []


for i in range(0, m, 1) :
    value = math.exp(-math.pow(Data[i] - Mean, 2) / (2 * Variance)) / (StdDeviation * math.sqrt(2 * math.pi))
    Gaussian.append(value)


plt.plot(Data, Gaussian, linewidth = 3, color = 'blue', marker = 'o')

plt.title('Gaussian probability density function')

plt.xlabel('Data set')
plt.ylabel('Gaussian function (PDF)')

plt.show()

print('\n')


