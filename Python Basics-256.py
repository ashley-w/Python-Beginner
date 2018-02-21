## 1. Programming And Data Science ##

print(1288)
print(639)
print(1288 + 639)

## 2. Arithmetic Operators ##

print((749 + 371 + 828 + 503 + 1379) / 5)

## 3. Variables ##

albuquerque = 749
anaheim = 371
anchorage = 828
arlington = 503
atlanta = 1379

print(anaheim)

## 4. Data Types ##

atlanta_string = "Atlanta"
atlanta_float = 1379.5

## 5. The Type Function ##

atlanta_string = "Atlanta"
print(type(atlanta_string))

## 6. Using A List To Store Multiple Values ##

cities = []
crime_rates = []

cities.append("Albuquerque")
cities.append("Anaheim")
cities.append("Anchorage")
cities.append("Arlington")
cities.append("Atlanta")

crime_rates.append(749)
crime_rates.append(371)
crime_rates.append(828)
crime_rates.append(503)
crime_rates.append(1379)

print(cities)
print(crime_rates)

## 7. Creating Lists With Values ##

crime_rates = [749, 371, 828, 503, 1379]

## 8. Comments ##

# Before the code
crime_rates = [749, 371, 828, 503, 1379]
print(crime_rates) # After the code

## 9. Accessing Elements In A List ##

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]

anchorage_str = cities[2]
anchorage_cr = crime_rates[2]

## 10. Retrieving The Length Of A List ##

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]
# Add your code here.
two_sum = len(cities) + len(crime_rates)
print(two_sum)

## 11. Slicing Lists ##

cities = ["Albuquerque","Atlanta", "Anaheim", "Anchorage", "Arlington"]
crime_rates = [749, 371, 828, 503, 1379]

cities_end = len(cities)
cities_slice = cities[2:cities_end]

cr_end = len(crime_rates)
cr_slice = crime_rates[3:cr_end]
