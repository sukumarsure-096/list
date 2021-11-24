'''
list function
1.append       9.copy
2.extend       10.index
3.insert       11.count
4.remove       12.len
5.pop
6.reverse
7.sort
8.clear'''
s=[]
for i in range (1,10):
        s.append(i)
#print(s)
s.extend([1,6,3,9])
print(s)
#s.remove(96)
#print(s)
#s.pop(1)
#print(s)
#s.sort(reverse=True)
#print(s)
s.count(9)
print(s)
