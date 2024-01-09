
import math

print('')

print(' '*10 + '##  Wrestling Match Probability')
print('\n')

m = int(input('-> Input the number of matches till date: '))

while m <= 0 :
    print('')
    print('invalid')
    print('')
    m = int(input('-> Input the number of matches till date: '))

print('')

print(' '*6 + 'Outcome of the previous %d bouts' %m)
print('')

BoutOut = []

print(' ##  Input "W" for victory in bout and "L" for defeat in bout')
print('')

for i in range(0, m) :
    x = input('-> Outcome of bout %d: ' %(i+1))
    print('')
    
    while x != 'W' and x != 'L' :
        print('Input either "W" (capital "w") or "L" (capital "l")')
        print('')
        x = input('-> Outcome of bout %d: ' %(i+1))
        print('')

    BoutOut.append(x)

Vic = BoutOut.count('W')
Def = BoutOut.count('L')

VicProb = Vic / m
DefProb = Def / m


n = int(input('-> Input the number of upcoming wrestling matches: '))
print('')

while n <= 0 :
    print('invalid')
    print('')
    n = int(input('-> Input the number of upcoming wrestling matches: '))
    print('')

print('')

print(' '*12 + '##  Upcoming %d wrestling bouts' %n)
print('\n')

x = int(input('-> Input the number of bouts for which you want to find the probability of winning: '))
print('')

while x < 0 or x > n :
    print('invalid')
    print('')
    x = int(input('-> Input the number of bouts for which you want to find the probability of winning: '))
    print('')


def BoutVic(n, r, p, q) :
    return (math.comb(n, r) * math.pow(p, r) * math.pow(q, (n-r)))

ListVicProb = []

for i in range(0, n+1) :
    prob = BoutVic(n, i, VicProb, DefProb)
    ListVicProb.append(prob)
    
print('')

print('--  The probability of winning %d bouts in the upcoming %d matches = %f' %(x, n, BoutVic(n, x, VicProb, DefProb)))
print('\n')

y = int(input('-> Probability of winning atleast ___ bouts. Input the number of bouts: '))
print('')

while y <= 0 or y > n :
    print('invalid')
    print('')
    y = int(input('-> Probability of winning atleast ___ bouts. Input the number of bouts: '))
    print('')

print('')

print('--  The probability of winning atleast %d bouts in the upcoming %d bouts = %f' %(y, n, sum(ListVicProb[y:])))
print('')

