print("*********************************")
print("Variables and Names")
print("*********************************")

#Declaring a cars variable for storing number of cars
cars = 100

#Declaring space_in_a_car variable for storing number of seats
space_in_a_car = 4.0

#declaring drivers variable to store number of drivers
driver = 30

#declaring passenger variable to store number of passengers
passengers = 90

#calculating cars not driven by subtracting drivers available from total number of cars
cars_not_driven = cars - driver

#Calculating total cars driven
cars_driven = driver

#Calculating total number of seats available in all cars
carpool_capacity = cars_driven * space_in_a_car

#calculating average passengers per car
average_passengers_per_car = passengers/cars_driven

print("***************Printing the details*****************")

#printing total number of cars
print("There are", cars, "cars available.")

#printing total drivers available
print("There are only", driver, "drivers available.")

#printing total empty cars today
print("There will be", cars_not_driven, "cars, which will not be driven.")

#printing total passengers that can be travel
print("We can transport", carpool_capacity, "passengers today.")

#total passengers available today
print("We have", passengers, "passengers available today.")

#printing average passengers per car
print("We need to put", average_passengers_per_car, "passengers in each car.")

print("***************End*****************")

