# import math module in order to use math.pi
"""
Problem Statement
The size of a car tire in the United States is
 represented with three numbers like this: 205/60R15. 
 The first number is the width of the tire in millimeters. 
 The second number is the aspect ratio. The third number is 
 the diameter in inches of the wheel that the tire fits. 
 The volume of space inside a tire can be approximated with 
 this formula:

v = 
π w2 aw a + 2,540 d
10,000,000,000
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""


# and math.sqrt
import math

# The following is a brief program description for the user.
print('This program reads from the keyboard three numbers for a tire')
print('The numbers are width in mm,aspect ratio and wheel diameter in inches')
print('computes and outputs the volume of space inside tire')

#Get width,aspect ratio and diameter from the user
width = float(input('enter tire width in mm: '))
aspect_ratio =float(input('whats the aspect ratio: '))
diameter =float(input('Enter diameter of the wheel in inches: '))
#computer the volume of the tire based on size
volume = (((math.pi)*((width**2)*aspect_ratio))*(width*aspect_ratio + (2540*diameter)))/10000000000
#round volume litres into one decimal point

print(f'volume is {volume:.2f} litres')
