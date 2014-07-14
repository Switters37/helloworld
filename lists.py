
#print range(10)
#for x in range (3):
#    print 'x=',x
    
#names = [['dave',23,True],['jeff',24,False],['mark',21,True]]
#for x in names:
#    print x
        
#print names [1][1]
#numbers in square brackets above will index over in the list.  So in this case, the list will index over 1 list, and then 1 space in the second list.
# thus giving 24, which is the second value in the second list. 

#use a number sign to comment out stuff....

#for x in range (3):
#    y = x**2
#    print y

# for-loops:
# so for the range(4) [0, 1, 2, 3], for i = the range(4), it will loop and produce the array of [0, 1, 4, 9]
#x = range (4)    
#y = [i**2 for i in x]
#print y


y = list()
for x in range(3):
    y.append(x**2)
print y

y = [i+3 for i in y]
print y

