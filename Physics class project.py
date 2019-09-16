train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
#We test our function
f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
#Same thing as above
c0_in_fahrenheit = c_to_f(0)

#Define a function that takes in mass and acceleration
def get_force():
  result_force = train_mass*train_acceleration
  return result_force
#Save the result in a variable
train_force = get_force()

print('The GE train supplies '+str(train_force)+ ' Newtons of force.')

#Define a function that takes in mass and c
def get_energy():
  c = 3*10**8
  result_energy = bomb_mass*c
  return result_energy
#Save the result in a variable
bomb_energy = get_energy()

print('A 1kg bomb supplies '+str(bomb_energy)+ ' Joules')

#Define a function that takes in mass, acceleration and distance
def get_work():
  result_work = train_force*train_distance
  return result_work
#Save the result in a variable
train_work = get_work()

print('The GE train does '+str(train_work)+ ' Joules of work over '+str(train_distance)+ ' meters.')
  