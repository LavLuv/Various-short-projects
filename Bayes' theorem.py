
# Bayes' Theorem, Theorem of total probability

# P(A | B) = P(A & B) / P(B)

# P(A & B) = P(A | B) x P(B)

# P(A | B) x P(B) = P(B | A) x P(A)

# Hence, P(B | A) = [ P(A | B) x P(B)] / P(A)

# For an event A related to sample space of E1, E2, E3, ..., En ;
# P(A) = P(A|E1)P(E1) + P(A|E2)P(E2) + P(A|E3)P(E3) + ... + P(A|En)P(En)

print('')
print('\t\t ###  Conditional probability calculator  ###')
print('\n')

n = int(input('--> Enter the number of events: '))

if n <= 0 :
    while n <= 0 :
        print('')
        print('Enter a valid number of events')
        print('')
        n = int(input('--> Enter the number of events: '))       

if n == 1 :
    print('')
    print('The solo event is itself the sample space!')
    
print('\n')
print(' $$ Enter probabilities of the %d events:-' %n)
print('\n')


ProbOfEi = []

# list has to be appended

for i in range(0, n-1) :
    x = float(input('-> P(E%d) = ' %(i+1))) 
    ProbOfEi.append(x)
    print('')
    if ProbOfEi[i] < 0 or ProbOfEi[i] > 1 :        
        while ProbOfEi[i] < 0 or ProbOfEi[i] > 1 :
            print('')
            print('Invalid value')
            print('')
            ProbOfEi[i] = float(input('-> P(E%d) = ' %(i+1)))             
    if sum(ProbOfEi) > 1 :
        print('')
        print('---> Invalid probability value set, run the program again')
    
ProbOfEi.append(1 - sum(ProbOfEi))


print('-> P(E%d) = %f' %(n, ProbOfEi[n-1]))
print('')

print('')
print(ProbOfEi) 
print('')

print('\n')
print(' $$ Enter probabilities of the %d conditional events:-' %n)
print('\n')

ProbOfAEi = []

for i in range(0, n) :
    x = float(input('-> P(A|E%d) = ' %(i+1))) 
    ProbOfAEi.append(x)
    print('')
    if ProbOfAEi[i] < 0 or ProbOfAEi[i] > 1 :        
        while ProbOfAEi[i] < 0 or ProbOfAEi[i] > 1 :
            print('')
            print('Invalid value')
            print('')
            ProbOfAEi[i] = float(input('-> P(A|E%d) = ' %(i+1))) 
                        

if sum(ProbOfAEi) == 0 :
    print('')
    print('---> Invalid probability value set, run the program again')
    
print(ProbOfAEi) 
print('')

ProList = []

for i in range(0, n) :
    x = ProbOfEi[i] * ProbOfAEi[i]
    ProList.append(x)
    
ProA = sum(ProList)

print('')
print('--> P(A) = %f' %ProA)

print('\n')
print('   $$$  Each of the conditional probabilities:-')
print('\n')

ReqList = []

for i in range(0, n) :
    x = ProList[i] / ProA
    ReqList.append(x)
    print('--> P(E%d|A) = %f' %(i+1, ReqList[i]))
    print('')
    
print('')
print('The program has been executed successfully')


