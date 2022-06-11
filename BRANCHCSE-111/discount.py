"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store's slowest sales days. On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, the store will discount the customer's subtotal by 10%.

Core Requirements¶
1.Your program asks the user for the subtotal but does not ask the user for the day of the week. Your program gets the day of the week from your computer's operating system.
2.Your program correctly computes and prints the discount amount if applicable.
3.Your program correctly computes and prints the sales tax amount and the total amount due.

"""
from datetime import datetime
#to get current date we use datetime from library.

current_date_and_time = datetime.now()
day_of_week =current_date_and_time.weekday()
#compute the subtotal by getting the total &discount from the user
subtotal = float(input('The subtotal of the purchase is : $'))
if subtotal >= 50:
    if day_of_week == 1 or day_of_week == 2:
        discount_amount = subtotal*.1
        print(f'The discount is: ${discount_amount:.2f}')
        subtotal= subtotal-discount_amount

sales_tax = subtotal *.06
total_amount = subtotal + sales_tax
print(f'The sales tax amount is: ${sales_tax:.2f}')
print(f'The total amount is:${total_amount:.2f}')
#print(day_of_week)

