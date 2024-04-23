# Hw_03
# Prob 1
# part a lines 3-34
list1 = [-3, 0, 3, 6]
for i in list1:
    print(str(i) + " ",end = ' ')
print()

# Part b
list1 = []
for numbers in range(1,5):
    print(numbers)
    list1.append( '%5d' %  (3*numbers-6))
    print(list1)

# part c
list2 = []
temp = 'y'
while temp== 'y' or temp== 'Y':
    print("enter a nummber:" , end= '')
    n = int(input())
    list2.append(n)
    print("Do you whish to continue? (Type'Y for yes 'N for no): " ,end= '')
    temp = input()
for i in list2:
    print(str(i) + " " , end= '')
print()
    
# part D
arr = []
for i in reversed(range(len(list2))):
    arr.append(list2[i])
for i in arr:
    print(str(i) + " " ,end= ' ')
    

# prob 2 lines 38-54
# List1 given
List1 = [0.2802, -0.1103, -0.2584, -0.0961, -0.4036
         -0.3681, 0.4420, 0.4561, 0.0752, -0.4403
         -0.2653, -0.1469, 0.3211, -0.4846, -0.4570
         -0.3311, 0.1491, 0.2317, 0.1477, -0.0491]
print(List1)
# List created using List2
List2 = []
sum_values = 0
# making a loop through List1
for i in range(len(List1)):
    # add values in List1 to sum_values
    sum_values+=List1[i]
    List2.append(sum_values) 
    # appending values to get to List2
for num in List2:
    print('{:.4f} '.format(num))
   
# prob 3 lines 56-63 
# connected to part on prob 2
# looping through list, while printing 5 num per row
for i in range(len(List2)):
    print('{:8.4f}'.format(List2[i]), end='')
    if (i+1)%5==0:
        print()
print()

# prob 4 lines 66-69
mydict= {0:'Barnarain', 1:'Bard', 2:'Cleric', 
         3:'Durid', 4:'fighter', 5:'Monk',
         6:'Paladin', 7:'Ranger', 8:'Rogue',
         9:'Sorcer', 10:'Wizard', 11:'Aberration'}
   
print('mydict=%s'% mydict)
