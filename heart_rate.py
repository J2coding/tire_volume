"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
"""
The prepare content for this lesson explains how to write code to do the following:

Get input from a user
Convert user input from a string to a number
Calculate results
Display results for the user to see
"""
first_name = input('Please enter your name?' )#name of the user
print(first_name)#print out
age =int(input('Your age please?'))#age of the user
print(age)
#compute slowest and fastest heart rate
maximum_heart_rate = int(input('220-46'))
slowest = maximum_heart_rate * .65
fastest = maximum_heart_rate * .85
# use f-string to create and print user message to see
print('when you exercise to strengthen your heart, you should')
print(f"keep your heart rate between {slowest:.0f} and {fastest:.0f}")
print("beats per minute.")

