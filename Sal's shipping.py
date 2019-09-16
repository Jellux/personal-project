#First off, I need to know how much it costs to ship a package of given weight by normal ground shipping. 
# So I wrote a function for the cost of ground shipping.
def shipping_cost_ground(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return 20 + (price_per_pound * weight)
#Print the cost of ground shipping 
print(shipping_cost_ground(8.4))

#Create a variable for the cost of premium ground shipping
shipping_cost_premium = 125.00

#I need a function for the cost of drone shipping
def shipping_cost_drone(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  return (price_per_pound * weight)
#Print the cost of drone shipping
print(shipping_cost_drone(1.5))

#Now I need a function that tell the user the following things: 
#The shipping method that is cheapest
#How much it would cost to ship a package of said weight using this method
def print_cheapest_shipping_method(weight):
  
  ground = shipping_cost_ground(weight)
  premium = shipping_cost_premium
  drone = shipping_cost_drone(weight)
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone
  print(
    "The cheapest option avaible is $%.2f with %s shipping."
  %(cost, method)
  )
  
#This is an example 
print_cheapest_shipping_method(4.8)
print_cheapest_shipping_method(41.5)
   
 
    
