## 1. Overview ##

m = open("movie_metadata.csv", "r")
data = m.read()
split_data = data.split("\n")

movie_data = []

for row in split_data:
    final_data = row.split(",")
    movie_data.append(final_data)
    
print(movie_data[0:5])

## 3. Writing Our Own Functions ##

def first_elts(input_lst):
    first = input_lst[0]
    return first

movie_names = []

for movie in movie_data:
    names_list = first_elts(movie)
    movie_names.append(names_list)
    
print(movie_names[0:5])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(film_lst):
    if film_lst[6] == 'USA':
        return True
    else:
        return False
    
wonder_woman_usa = is_usa(wonder_woman)

type(movie_data)

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False
    
def index_equals_str(lst_input, index_input, str_input):
    if lst_input[index_input] == str_input:
        return True
    else:
        return False
    
wonder_woman_order = index_equals_str(index_input = 1, lst_input = wonder_woman, str_input = 'Patty Jenkins')
    
wonder_woman_in_color = index_equals_str(wonder_woman, 2, 'Color')

## 6. Optional Arguments ##

# A function that checks a list index for a value
def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False

# A funtion that counts everything in the list except for the header
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

def feature_count(input_lst, index, input_str, header_row = False):
    num_elmt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elmt = num_elmt + 1
    return num_elmt

num_of_us_movies = feature_count(movie_data, 6, 'USA', header_row = True)

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(input_lst):
    num_japan_films = feature_counter(input_lst,6,"Japan",True)
    num_color_films = feature_counter(input_lst,2,"Color",True)
    num_films_in_english = feature_counter(input_lst,5,"English",True)
    summary_dict = {"japan_films" : num_japan_films, "color_films" : num_color_films, "films_in_english" : num_films_in_english}
    return summary_dict
summary = summary_statistics(movie_data)