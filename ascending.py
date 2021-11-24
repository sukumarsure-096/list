s =[-66,9,39,56,-99,69]
print(s)
i = 0
while i<len(s):
    #print('i = ',i) 
    j = i+1
    #print('j = ',j)
    while j<len(s):
        if s[i]>s[j]:
            temp = s[i]
            s[i]=s[j]
            s[j]=temp
        j+=1
    i+=1
print(s)


        
    








    
    

