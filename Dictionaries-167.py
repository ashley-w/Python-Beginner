## 1. The Data Set ##

# Weather has been loaded in.

first_element = weather[0]
print(first_element)

last_element = weather[364]
print(last_element)

## 3. Practice Populating a Dictionary ##

['superhero_ranks = {}\n\nsuperhero_ranks["Aquaman"] = 1\nsuperhero_ranks["Superman"] = 2']

## 4. Practice Indexing a Dictionary ##

president_ranks = {}
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3

# Look up FDR and assign to new variable
fdr_rank = president_ranks["FDR"]
lincoln_rank = president_ranks["Lincoln"]
aquaman_rank = president_ranks["Aquaman"]

## 5. Defining a Dictionary with Values ##

random_values = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}
print(random_values)

# Create a dictionary named animals with a variety of kes and values

animals = {
    7: "raven",
    8: "goose",
    9: "duck"
}

times = {
    "morning": 9,
    "afternoon": 14,
    "evening": 19,
    "night": 23
}
    

## 6. Modifying Dictionary Values ##

students = {
    "Tom": 60,
    "Jim": 70
}

students["Ann"] = 85
students["Tom"] = 80
students["Jim"] = students["Jim"] + 5

## 7. The In Statement and Dictionaries ##

planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}

jupiter_found = "jupiter" in planet_numbers
earth_found = "earth" in planet_numbers

## 9. Practicing with the Else Statement ##

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []

for planet in planet_names:
    if len(planet) > 5:
        long_names.append(planet)
    else:
        short_names.append(planet)

## 10. Counting with Dictionaries ##

pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts = {}

for item in pantry:
    if item in pantry_counts:
        pantry_counts[item] +=1
    else:
        pantry_counts[item] = 1

        

## 11. Counting the Weather ##

weather_counts = {}

for weather_type in weather:
    if weather_type in weather_counts:
        weather_counts[weather_type] += 1
    else:
        weather_counts[weather_type] = 1
        
print(weather_counts)