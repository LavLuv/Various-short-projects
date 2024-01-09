
import math

import matplotlib.pyplot as plt

print('')

print(' '*10 + '##  Grading system')
print('\n')

n = int(input('-> Input the number of students: '))
print('')

while n <= 0 :    
    print('Input a valid value')    
    print('')
    
    n = int(input('-> Input the number of students: '))
    print('')
    
print('')

Scores = []

for i in range(0, n, 1) :
    x = float(input('-> Score[%d] = ' %(i+1)))
    
    while x < 0 or x > 100 :
        print('Enter a valid value')
        print('')
        
        x = float(input('-> Score[%d] = ' %(i+1)))
        
    Scores.append(x)
    
def Grading(x) :
    
    if x >= 85 :
        grade = 'A'
        
    elif x < 85 and x >= 70 :
        grade = 'B'
        
    elif x < 70 and x >= 55 :
        grade = 'C'

    elif x < 55 and x >= 40 :
        grade = 'D'

    else :
        grade = 'E'
        
    return grade


Grades = []

for i in range(0, n, 1) :
    y = Grading(Scores[i])
    
    Grades.append(y)
    
print('\n')

print(' '*10 + 'score and grading:-')
print('')

for i in range(0, n, 1) :
    print('- Score[%d] = %f' %((i+1), Scores[i]))
    print('-- Grade[%d] = %s' %((i+1), Grades[i]))

    print('')
    
print('')

Students = []

for i in range(0, n) :
    Students.append(i+1)

# plotting bar graph (marks of each student)

print(' '*11 + '##  Bar graph for student scores')
print('\n')

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.bar(Students, Scores)

plt.title('student scores')

plt.xlabel('students in serial number')
plt.ylabel('corresponding scores')

plt.show()

# plotting Gaussian distribution (a probability density function)

print('')
print('\n')

print(' '*11 + '##  Gaussian distribution (a probability density function)')
print('\n')

Mean = sum(Scores) / n

DeviationSqr = []

for i in range(0, n) :
    DeviationSqr.append(math.pow((Scores[i] - Mean), 2))

Variance = sum(DeviationSqr) / n

StdDeviation = math.sqrt(Variance)


GaussScores = []

for i in range(0, len(Scores)) :
    elem = Scores[i]
    GaussScores.append(elem)

GaussScores.sort()

Gaussian = []

for i in range(0, n, 1) :
    value = math.exp(-math.pow(GaussScores[i] - Mean, 2) / (2 * Variance)) / (StdDeviation * math.sqrt(2 * math.pi))
    Gaussian.append(value)
    
plt.plot(GaussScores, Gaussian, linewidth = 3, color = 'blue', marker = 'o')

plt.title('Gaussian probability density function')

plt.xlabel('student scores')
plt.ylabel('Gaussian distribution function')

plt.show()

print('\n')

# grading as per seven grades

print('')

print(' '*8 + '##  Grading system as per seven grade scale')
print('\n')

def AltGrading(x) :
    
    if x >= 90 :
        grade = 'A'
        
    elif x < 90 and x >= 80 :
        grade = 'B'
        
    elif x < 80 and x >= 70 :
        grade = 'C+'

    elif x < 70 and x >= 60 :
        grade = 'C'
        
    elif x < 60 and x >= 50 :
        grade = 'C-'
        
    elif x < 50 and x >= 40 :
        grade = 'D'

    else :
        grade = 'E'
        
    return grade


AltGrades = []

for i in range(0, n, 1) :
    y = AltGrading(Scores[i])
    
    AltGrades.append(y)
    
print('')

print(' '*10 + 'score and grading (seven grade scale):-')
print('')

for i in range(0, n, 1) :
    print('- Score[%d] = %f' %((i+1), Scores[i]))
    print('-- Grade[%d] = %s' %((i+1), AltGrades[i]))

    print('')
    
print('\n')

# plotting histogram to show the number of students assigned each grade

print(' '*12 + 'Histogram for grades:-')
print('\n')


A = AltGrades.count('A')
B = AltGrades.count('B')
Cplus = AltGrades.count('C+')
C = AltGrades.count('C')
Cminus = AltGrades.count('C-')
D = AltGrades.count('D')
E = AltGrades.count('E')

NumOfGrades = [A, B, Cplus, C, Cminus, D, E]

Grade = ['A', 'B', 'C+', 'C', 'C-', 'D', 'E']

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.bar(Grade, NumOfGrades)

plt.title('student grades')

plt.xlabel('seven grade scale')
plt.ylabel('number of students assigned each grade')

plt.show()

print('\n')

# Relative Grading

print('')

print(' '*12 + '##  Relative Grading')
print('')

a = float(input('-> Enter the step of range relating mean and standard deviation: '))
print('')

print('As per step of %f, the relative grading scheme will be as follows:-' %a)
print('\n')

print('''
      score  >=  Mean + %f StdDev                       :  A
      Mean + %f StdDev  <=  score  <  Mean + %f StdDev  :  B
      Mean + %f StdDev  <=  score  <  Mean + %f StdDev  :  C
      Mean              <=  score  <  Mean + %f StdDev  :  D
      Mean - %f StdDev  <=  score  <  Mean              :  E
      Mean - %f StdDev  <=  score  <  Mean - %f StdDev  :  F
      score  <  Mean - %f StdDev                        :  G           

      ''' %((3*a), (2*a), (3*a), (a), (2*a), (a), (a), (2*a), (a), (2*a)))


def RelativeGrading(x) :
    
    if x >= (Mean + (3 * a * StdDeviation)) :
        grade = 'A'
        
    elif x < (Mean + (3 * a * StdDeviation)) and x >= (Mean + (2 * a * StdDeviation)) :
        grade = 'B'
        
    elif x < (Mean + (2 * a * StdDeviation)) and x >= (Mean + (1 * a * StdDeviation)) :
        grade = 'C'

    elif x < (Mean + (1 * a * StdDeviation)) and x >= (Mean) :
        grade = 'D'

    elif x < (Mean) and x >= (Mean - (1 * a * StdDeviation)) :
        grade = 'E'
        
    elif x < (Mean - (1 * a * StdDeviation)) and x >= (Mean - (2 * a * StdDeviation)) :
        grade = 'F'
        
    else :
        grade = 'G'
        
    return grade
    

RelativeGrades = []

for i in range(0, n, 1) :
    y = RelativeGrading(Scores[i])
    
    RelativeGrades.append(y)
    
print('\n')

print(' '*9 + 'scores and relative grading (using mean and standard deviation):-')
print('')

for i in range(0, n, 1) :
    print('- Score[%d] = %f' %((i+1), Scores[i]))
    print('-- Grade[%d] = %s' %((i+1), RelativeGrades[i]))

    print('')
    
print('\n')

# plotting histogram to show the number of students assigned each relative grade

print(' '*12 + 'Histogram for relative grades:-')
print('\n')


A = RelativeGrades.count('A')
B = RelativeGrades.count('B')
C = RelativeGrades.count('C')
D = RelativeGrades.count('D')
E = RelativeGrades.count('E')
F = RelativeGrades.count('F')
G = RelativeGrades.count('G')

NumOfRelativeGrades = [A, B, C, D, E, F, G]

RelativeGrade = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.bar(RelativeGrade, NumOfRelativeGrades)

plt.title('relative grades')

plt.xlabel('relative grade scale')
plt.ylabel('number of students assigned each relative grade')

plt.show()

print('\n')
print('')

# taking input of the number of grades and the number of students being 
# assigned each grade

print(' '*10 + '##  Number of grades and the number of students being assigned each grade:-')
print('\n')

print('The maximum number of grades can be 25')
print('')

g = int(input('-> Input the number of grades being assigned: '))
print('')

while g <= 0 or g > 25 :
    print('Input again')
    print('')    
    g = int(input('-> Input the number of grades being assigned: '))
    print('')

print('')

GradeList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

Scores.sort(reverse = True)

GradeNumbersList = []

for i in range(0, g) :
    
    print('   The number of students left to be allotted grades: %d' %(n - sum(GradeNumbersList)))
    print('')
    
    num = int(input('-> Input the number of students for grade %s : ' %GradeList[i]))
    
    while num > (n - sum(GradeNumbersList)) :
        print('')
        print('---> Input a smaller number of students')
        print('')
        num = int(input('-> Input the number of students for grade %s : ' %GradeList[i]))
        
    GradeNumbersList.append(num)
    print('')
    
    print(' The total number of grade-allotted students = %d' %sum(GradeNumbersList))
    print('')
    
    if sum(GradeNumbersList) == n :
        break
    
    print(' The number of types of grades left to be allotted = %d' %(g - (i+1)))
    print('')


print('\n')

print(' '*6 + 'The grade classification is as follows:-')
print('')

count = 0

for i in range(0, len(GradeNumbersList)) :
    for j in range(0, GradeNumbersList[i]) :
        count = count + 1
        
        print('-- Score[%d] = %f' %(count, Scores[count-1]))
        print(' - Grade: %s' %(GradeList[i]))

        print('')

print('')

print('The entire grade assignment has been completed successfully')
print('')

