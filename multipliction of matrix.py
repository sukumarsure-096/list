'''matrix1 = 2x3
matrix2 = 3X2
In multiplication matrix matrix1 col = matrix2 rows'''
r = int(input('enter  rows' ))
c = int(input('enter cols '))
c_r = int(input('enter equal no. of rows and cols : '))
m = []
print('---------------first matrix---------------')
for i in range (r) :
    a = []
    for j in range (c_r):
        a.append(int(input('values :')))
    m.append(a)
#print(m)

for i in range (r):
    for j in range (c_r):
        print(m[i][j],end=' ')
    print()
print()
print('----------------second matrix----------')
m1 = []
for i in range (c_r) :
    a1 = []
    for j in range (c):
        a1.append(int(input('values :')))
    m1.append(a1)
#print(m1)
for i in range (c_r):
    for j in range (c):
        print(m1[i][j],end=' ')
    print()
print('-------------------')
res=[[0,0],[0,0]]
for i in range(r):
    #mul1=[]
    for j in range(c):
        for k in range(c_r):
            res[i][j]=res[i][j]+(m[i][k]*m1[k][j])
    #mul.append(mul1)
        #print(res[i][j],end=' ')
print()
for i in range(r):
    for j in range(c):
        print(res[i][j],end=' ')
    print()
