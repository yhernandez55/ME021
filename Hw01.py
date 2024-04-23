# Hw01 
# problem: 1 view lines 5-18
# view table for values ao a-x and x,y

a=1296**0+216**1+36**2+6**3+1**4
print(a)

b=6**2+(5*2**4)+(3*2**(2*3**2))+7**2
print(b)

c=(4*3**(2*1))+(2*1**(4*3))+(1*4**(3*2))
print(c)
# last two factorial problems view 14-18 lines
import math
x=(math.factorial(12)/math.factorial(11)/math.factorial(3))
print(x)
y=(math.factorial(16)/math.factorial(14)/math.factorial(5))
print(y)

# problem: 2 view lines 22-59 for sin and 61-101 for tan
print('starting with the sin function')
import math
theta=0
# -sin(0)
print((-math.sin(math.pi/180 *theta)), 'left                                 ', end='   ')
# sin(-0)
print((math.sin(math.pi/180 *-theta)), 'right','    theta:',theta)

theta=30
# -sin(30)
print((-math.sin(math.pi/180 *theta)), 'left', end='   ')
# sin(-30)
print((math.sin(math.pi/180 *-theta)), 'right','    theta:',theta)

theta=90
# -sin(90)
print((-math.sin(math.pi/180 *theta)), 'left                                ', end='   ')
# sin(-90)
print((math.sin(math.pi/180 *-theta)), 'right','    theta:',theta)

theta=135
# -sin(135)
print((-math.sin(math.pi/180 *theta)), 'left  ', end='   ')
# sin(-135)
print((math.sin(math.pi/180 *-theta)), 'right','    theta:',theta)

theta=270
# -sin(270)
print((-math.sin(math.pi/180 *theta)), 'left                                  '  , end='   ')
# sin(-270)
print((math.sin(math.pi/180 *-theta)), 'right','    theta:',theta)

theta=321
# -sin(321)
print((-math.sin(math.pi/180 *theta)), 'left    ',end='   ')
# sin(-321)
print((math.sin(math.pi/180 *-theta)), 'right','    theta:',theta)

# the first part is done
 
# finding out if tan(pi-theta)=-tan(theta)
print('tan equation'    )

theta=0
# tan(pi-0) 
print((math.tan(math.pi - math.pi/180 *theta)), 'left               ', end='  ' )
# -tan(0)
print((-math.tan(math.pi/180 *theta)), 'right','   theta:', theta)
 
theta=30
# tan(pi-30) 
print((math.tan(math.pi - math.pi/180 *theta)), 'left', end='      ' )
# -tan(30)
print((-math.tan(math.pi/180 *theta)), 'right','   theta:',theta)

theta=90
# tan(pi-90) 
print((math.tan(math.pi - math.pi/180 *theta)), 'left', end=' ' )
# -tan(90)
print((-math.tan(math.pi/180 *theta)), 'right','   theta:', theta)

theta=135
# tan(pi-135) 
print((math.tan(math.pi - math.pi/180 *theta)), 'left       ', end=' ' )
# -tan(135)
print((-math.tan(math.pi/180 *theta)), 'right','   theta:', theta)

theta=270
# tan(pi-270) 
print((math.tan(math.pi - math.pi/180 *theta)), 'left', end='   ' )
# -tan(270)
print((-math.tan(theta*math.pi/180)), 'right','   theta:', theta)

theta=321
# tan(pi-321)  
print((math.tan(math.pi - math.pi/180 *theta)), 'left ', end='        ')
# -tan(321)
print((-math.tan(math.pi/180 *theta)), 'right','   theta:', theta)
# tan is finished 

      
# problem: 3 view lines 103-110
# Calulate for J
# d=inner diameter
# D=outer diameter
import math
D=5
d=2
J=math.pi*(D**4-(d**4))/32
print(J)

#problem: 4 view lines 112-to end
# Hw01_04.py
# Calculate the extension (stretch) of a simple uniform steel rod
# of circular cross section when subject to a constant tension
# force. Assume that we are given 
#  d = the rod diameter (milimeters)
#  l = the rod length (meters)
#  F = the force on the rod (Newtons)

# User may adjust these values
d=25.0          # mm
l=1.0           # m
F= 1000.0       # N
# some constants(are the units correct?)
E = 200*10**6# 200 GPa (elastic modulus of steel)
from math import pi # the circular constant (this line is correct)

d_m = d/1000.0      # convert units
A = pi*d_m**2/4.0  # cross-sectional area

delta = (l*F)/(A*E)  # The stretch, in meters
 # Show results
# instead of ^ put ** for line 131
# 
