#assign cars with the total number of available cars
cars = 100
#assign cars with the number of people that can fit inside the car
space_in_a_car = 4.0
#assign drivers with the number of drivers available
drivers = 30
#assign passengers with the total number of passengers
passengers  = 90
#assign cars_not_driven with the number of unmanned cars
cars_not_driven = cars - drivers
#assign cars_driven with the number of manned cars
cars_driven = drivers
#assign carpool_capacity with the total number of people who can be carpooled
carpool_capacity = cars_driven * space_in_a_car

#assign average_passengers_per_car with the actual number of people in one car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
