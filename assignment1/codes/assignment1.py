#this is the sample space
space =[1,2,3,-1,-2,-3]
k1=0
k2=0
for i in space :
    #counting no of favourable cases for part 1
    if i > 0 :
        k1 = k1+1
    #counting no of favourable cases for part2
    if i> -3:
        k2=k2+1
#this is sample space length
x=len(space)
#P1 is probability of getting positive integer
P1=k1/x
#p2 is probability of getting integer greater than -3
P2=k2/x
#p3 is the probability of getting the smallest integer
#but there can be onle one smallest no in the sample space
#therefore the no of favourable case is only one
P3=1/x
#printing the probabilities
print("the probability of getting positive integer is :\n",P1)
print("the probability of getting an integer greater than -3 is :\n",P2)
print("the probability of getting the smallest integer is :\n ",P3)