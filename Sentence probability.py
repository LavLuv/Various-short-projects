
print('\n')

print(' '*11 + '##  Word-in-sentence probability')
print('\n')

n = int(input('-> Input the number of sentences you are going to enter: '))

while n < 1 :
    print('')
    print('Input a positive integer value')
    print('')
    n = int(input('-> Input the number of sentences you are going to enter: '))
    
print('\n')

print(' '*9 + '---  Enter the sentences  ---')
print('\n')

SentList = []

SentTypeList = []

for i in range(0, n) :
    x = input('--> Enter sentence %d: ' %(i+1))
    SentList.append(x)
       
    print('')
    print('- Input as follows:-   0: positive  and  1: negative')
    
    y = int(input('# Sentence type: '))
    
    while y != 0 and y != 1 :
        print('-- Input as follows:-   0: positive  and  1: negative')
        print('')
        
        y = int(input('# Sentence type: '))
    
    SentTypeList.append(y)
    
    print('')
    
WordListP = []

WordListN = []






















