#remove duplicates in aset
l = [1,2,2,4,2,13,5,6,1,2,6,45]
l1 =[1,2,2,4,2,13,5,6,1,2,6,45,45]
i=0
u=[]
while i<len(l):
    j = i+1
    while j<len(l):
        if l[i] == l[j]:
            l.pop(j)
            j-=1
        j+=1
    i+=1
print(l)

#+++++++++++++++counting no of pairs in a set++++++++++++++++++++++++++++++++

l1 = [1,2,2,4,2,13,5,6,1,2,6,45]
s = {1,2,2,4,2,13,5,6,1,2,6,45}
print(s)
c = 0
for i in s:
    c = c+l1.count(i)//2
print(c)
#++++++++++++++++++counting no. of times of number in list+++++++++++++++++++
for i in s:
    print(i,end=' ')
    print(l1.count(i))

#+++++++++++++++++++++++printing the pairs +++++++++++++++++++++++++++++++++
for i in s:
    if (l1.count(i)//2)>=1:
            u.append((i,i))
print(u)


'''
********************list given by user choice*********************************
********************printing unique values************************************
n = int(input('range of n:'))
l=[]
i=0
for s in range(1,n):
    l.append(int(input('values :')))
l1 = l.copy()       
while i<len(l):
    j = i+1
    while j<len(l):
        if l[i] == l[j]:
            l.pop(j)
            j-=1
        j+=1
    i+=1
print(l)
print(l1)
**********************printing no. of pairs in the list************************
c = 0
for i in l:
    c = c+l1.count(i)//2
print(c)

'''
