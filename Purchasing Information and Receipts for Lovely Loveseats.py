lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'
lovely_loveseat_price = 254.00
stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'
stylish_settee_price = 180.50
luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'
luxurious_lamp_price = 52.15
#Sales 8.8%
sales_tax = .088

customer_one_total = 0
customer_one_itemization = ''

#First customer bought Lovely Loveseat
customer_one_total += 254.00
#We keep track of the items our customer purchased.
customer_one_itemization = lovely_loveseat_description
#Our customer had also decided to purchas the Luxurious Lamp
customer_one_total += 52.15
#We keep tracking the items
customer_one_itemization += luxurious_lamp_description

#Check out! I'll begin to calculate sales tax
customer_one_tax = customer_one_total * sales_tax
#Add the sales tax to the customer's total cost
customer_one_total += customer_one_tax

print('Customer One Items:')
print(customer_one_itemization)
print('Customer One Total:')
print(customer_one_total)