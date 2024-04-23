# Hw_02.py
# prob 1 lines (2-15)
import math
import numpy as np
th1 = float(input("Enter first angle in degrees: "))
th2 = float(input("enter second angle in degrees: "))
t1 = th1*np.pi/180;
t2 = th2*np.pi/180;
cs1 = math.cos(t1);
cs2 = math.cos(t2);
if (cs1 > cs1):
    print("Max is", cs2, ", corresponding in degrees is", th1)
elif(cs2 > cs1):
    print("Max is", cs1, ", corresponding angle is", th2)
else:
     print("Both are equal and value is", cs1)

#prob 2 (lines 18-45)
classnum = int(input('enter value: '))
if classnum > 0 and classnum <=11:
    if classnum == 0:
        print('Barbarian')
    elif classnum == 1:
        print('Bard')
    elif classnum == 2:
        print('Cleric')
    elif classnum == 3:
        print('Durid')
    elif classnum == 4:
        print('Fighter')
    elif classnum == 5:
        print('Monk')
    elif classnum == 6:
        print('Paladin')
    elif classnum == 7:
        print('Ranger')
    elif classnum == 8:
        print('Rogue')
    elif classnum == 9:
        print('Sorcere')
    elif classnum ==  10:
        print('Wizard')
    elif classnum == 11:
        print('Aberration')
    else:
        print('Error: value out of range')

# prob 3 lines 48-57
start = 0
final = 40
#loop irates from 0 to 40
while start <= final:
    # multiples of 5
    if start%5 == 0:
        print(start)
        #display multiples of 5
    #start with 5
    start +=1


#prob 4 lines 61-63
for i in range(0,45, 5):
    print(i)
    
# Prob 5 lines 64-78
# change value of Maxval
Maxval = 100
# input in any integer that is between 1 to 10
x=int(input("enter value between 1 and 10: "))
if x >= 1 and x <= 10:
    print("multiples of", x, ", are", end= "")
    # inclusive so Maxval +1
    for i in range(1,Maxval+1):
        # is it a ,ultiple of x?
        if(i%x==0):
            print(i, end= "")
else: 
    # input is greater than 10
    print("Error, value is greater than 10")
    
# prob 6 lines 81-95
import math
import numpy as np
th1 = float(input("Enter first angle in degrees: "))
th2 = float(input("enter second angle in degrees: "))
t1 = th1*np.pi/180;
t2 = th2*np.pi/180;
cs1 = math.cos(t1);
cs2 = math.cos(t2);
if (cs1 > cs1):
    print("Max is", cs2, ", corresponding in degrees is", th1)
elif(cs2 > cs1):
    print("Max is", cs1, ", corresponding angle is", th2)
else:
     print("Both are equal and value is", cs1)
response = input("Do another(y/n)?")

