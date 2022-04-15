x=[]
k1=0
k2=0
for i in range(-3,4,1):
    if(i!=0):
        x.append(i)  #generating the required sample space
    
for i in x:
    if i>0:
        k1=k1+1      #counting the no of favourable cases for case1
    if i>-3:
        k2=k2+1      #counting the no of favourable cases for case2
        
#length of sample space
x1=len(x)   

#probability for case1
p1=k1/x1    


 #probability for case2
p2=k2/x1             
#there can be only one smallest no.,so no. of favourable case=1
#probability for case3
p3=1/x1

print("the probability of getting a positive no. is : ",p1)
print("the probability of getting an integer greater than -3 is : ",p2)
print("the probability of getting the smallest no. is : ",p3)

