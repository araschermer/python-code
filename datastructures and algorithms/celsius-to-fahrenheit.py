data = [("Berlin", 9), ("Cairo", 33), ("New York", 25), ("Ankara", 2), ("London", 10), ("Tokyo", 14)]
print(data)
# create a lambda function for the conversion
temperature_to_fahrenheit = lambda temp: (temp[0], (9 / 5) * temp[1] + 32)
# map the function to the temperature of the given cities
result = list(map(temperature_to_fahrenheit, data))
print(result)
# use filter function to get the temperatures below average
import statistics

# temperatures = [temp[1] for temp in data]
temperatures = [9, 33, 25, "", 2, 10, 14, ""]
print(temperatures)
# to filter out the empty values, since the data  doesn't contain any zero values'
temperatures = list(filter(None, temperatures))
print(temperatures)
average = statistics.mean(temperatures)
print(average)
# filter temperature above average
cities = list(filter(lambda x: x > average, temperatures))
print(cities)
