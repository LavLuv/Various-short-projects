
print('\n')

print(' '*16 + '##  Account management system')
print('\n')


fileOb = open("C:\\Users\\ASHOK\\Desktop\\Nirma University\\semester-4\\Programming for Scientific Computing\\lab\\prac-5 files\\UserDetails.txt", "w+")

nu = int(input("-> Input the number of accounts: ")) 
print('')
    
ud = []

unam = []

up = []

hl = []

rl = []

for x in range(nu):
    print("Enter user id:") 
    ud.append(str(input()))
    
    print("Enter User Name:")
    unam.append(str(input()))
    
    print("Enter Password:")
    up.append(str(input()))
    
    print("Home Loan Amount:") 
    hl.append(float(input())) 
    
    print("Enter Remaining Home Loan:")
    rl.append(float(input()))
    
for x in range(nu):
    fileOb.write(str(ud[x])+"|"+str(unam[x])+"|"+str(up[x])+"|"+str(hl[x])+"|"+str(rl[x])+"\n")

fileOb.close()



def check(ud) :
    ch = 0 
    f = open("C:\\Users\\ASHOK\\Desktop\\Nirma University\\semester-4\\Programming for Scientific Computing\\lab\\prac-5 files\\UserDetails.txt",'r')
    r = f.readline()
    while r and ch == 0:
        r1 = r.split("|") 
        
        if r1[0] == ud:
            ch = 1 
            break
        
        r = f.readline()
    
    if ch :
        return True
    return False
    f.close()
    

l = open("C:\\Users\\ASHOK\\Desktop\\Nirma University\\semester-4\\Programming for Scientific Computing\\lab\\prac-5 files\\LoanPaymentDetails.txt", "a") 

ap = []

des = []

dom = []

mon = []

ye = []
    
print("Enter number of loan payment details: ")
lu = int(input())
    
for x in range(lu) :
    while True :
        print("Enter user id: ") 
        uid = str(input())
        if not check(uid) :
            print("Invalid User id.") 
        else :
            break
        
    print("Enter Amount Paid:")
    ap.append(int(input()))
        
    print("Enter Description:") 
    des.append(str(input()))
        
    print("Enter Day of Month of Payment:") 
    dom.append(int(input()))
        
    print("Enter Month of Payment:")
    mon.append(int(input()))
        
    print("Enter Year of Payment:")
    ye.append(int(input()))
        
    l.write(uid+"|"+str(ap[x])+"|"+des[x]+"|"+str(dom[x])+"|"+str(mon[x])+"|"+str(ye[x])+"\n")

l.close()
    
    
f1 = open("C:\\Users\\ASHOK\\Desktop\\Nirma University\\semester-4\\Programming for Scientific Computing\\lab\\prac-5 files\\UserDetails.txt",'r')

r1 = f1.readline()

while r1 :
    uid = r1.split("|")[0]
    
    print(uid) 
    
    f2 = open("C:\\Users\\ASHOK\\Desktop\\Nirma University\\semester-4\\Programming for Scientific Computing\\lab\\prac-5 files\\LoanPaymentDetails.txt",'r')
    r2 = f2.readline()
    
    res = 0
    
    while r2 :
        if uid == r2.split('|')[0] :
            res = res + int(r2.split('|')[1])
            print(" ") 
            print("Name:\t\t\t\t", uid) 
            print("Fullname:\t\t\t", r1.split("|")[1])
            print("Home Loan Amount:\t\t", r1.split("|")[3])
            print("Current remaining loan amount:\t", r1.split("|")[4],end='') 
            print("Given Loan amount in year:\t", r2.split("|")[-1],res)
        
        r2 = f2.readline() 
    
    r1 = f1.readline()
    f2.close()

f1.close()


f3 = open("C:\\Users\\ASHOK\\Desktop\\Nirma University\\semester-4\\Programming for Scientific Computing\\lab\\prac-5 files\\UserDetails.txt",'r')
r3 = f3.readline()

while r3:
    f4 = open("LoanPaymentDetails.txt",'r') 
    r4 = f4.readline()
    
    print("\nUser Deatils:", r3.split("|")[0])
    print("Year\tMonth\tRepaymentLoan")
    print("."*25) 
    
    while r4 :
        r4 = r4[:-1]
        
        if r3.split("|")[0]==r4.split("|")[0]:
            print(r4.split("|")[-1],"\t",r4.split("|")[2].split(" ")[0],"\t",r4.split("|")[1])
        r4 = f4.readline()
    
    r3 = f3.readline()
    f4.close()

f3.close()

