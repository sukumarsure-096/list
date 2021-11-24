r = int(input('enter  rows' ))
c = int(input('enter cols '))
m = []
print('---------------first matrix---------------')
for i in range (r) :
    a = []
    for j in range (c):
        a.append(int(input('values :')))
    m.append(a)
#print(m)

for i in range (r):
    for j in range (c):
        print(m[i][j],end=' ')
    print()
print()
##print('----------------second matrix----------')
##m1 = []
##for i in range (r) :
##    a1 = []
##    for j in range (c):
##        a1.append(int(input('values :')))
##    m1.append(a1)
###print(m1)
##for i in range (r):
##    for j in range (c):
##        print(m1[i][j],end=' ')
##    print()
##
##print('----------------add matrix----------')
##add=[]
##for i in range(r):
##    add1=[]
##    for j in range(c):
##        add1.append(m[i][j]+m1[i][j])
##    add.append(add1)
###print(add)
##for i in range(r):
##    for j in range(c):
##        print(add[i][j],end=' ')
##    print()
##print('------subtraction matrix------------')
##sub=[]
##for i in range(r):
##    sub1=[]
##    for j in range(c):
##        sub1.append(m[i][j]-m1[i][j])
##    sub.append(sub1)
###print(add)
##for i in range(r):
##    for j in range(c):
##        print(sub[i][j],end=' ')
##    print()
##
##        
##    
##
