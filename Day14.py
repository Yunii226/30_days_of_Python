from functools import reduce
from countries_data import countries_data
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Level 1 
#1
print("Map applies a function to a whole iterable, Filter applies a function to the elements of the iterable that passes the condition defined, Reduce applies the function to the iterable and returns a single element")

#2
print(" A higher order function is a function that takes a function as an argument or returns a function, a closure is a function that \"remembers\" variables from the scope where it has been implemented, a decorator is a modification added to a function ")

#4
for country in countries:
    print (country)

#5
for name in names:
    print(name)
    
#6
for number in numbers:
    print(number)
    
#Level 2
#1
upper_countries=map(lambda i: i.upper(),countries)
print (list(upper_countries))

#2
sqrd_numbers=map(lambda x:x**2, numbers)
print(list(sqrd_numbers))

#3
names=list(map(lambda i:i.upper(),names))
print(names)


#4
def has_land(word):
    if 'land' in word:
        return True
    else:
        return False
lands=filter(has_land,countries)
print(list(lands))

#5
def six_chars(word):
    if len(word) == 6:
        return True
    else:
        return False
six_country=filter(six_chars,countries)
print(list(six_country))

#6
def six_more_chars(word):
    if len(word) >= 6:
        return True
    else:
        return False
six_more_country=filter(six_more_chars,countries)
print(list(six_more_country))

#7
def starts_with_E(word):
    if word[0] == 'E':
        return True
    else:
        return False
country_starts_with_E = filter(starts_with_E,countries)
print(list(country_starts_with_E))

#8

def countries_to_upper(word):
    return(word.upper())
print(list(filter(starts_with_E,list(map(countries_to_upper,countries)))))

#9
def get_strings_list(word):
    if isinstance(word,str):
        return True
    else:
        return False
    
print(list(filter(get_strings_list,countries)))

#10
def add_two_numbers(a,b):
    return a+b

print(reduce(add_two_numbers,numbers))

#11
def concatenate_strings(a,b):
    return a + ' ' + b

print(reduce(concatenate_strings,countries))

#12
def categorize_countries(word):
    if 'land' in word:
        return 'land'
    elif 'ia' in word:
        return 'ia'
    elif 'is' in word:
        return 'is'
    else:
        return 'other'
    
print(list(map(categorize_countries,countries)))

#13
def count_countries_by_starting_letter(countries):
    starting_letter_count = {}
    for country in countries:
        starting_letter = country[0].upper()
        if starting_letter in starting_letter_count:
            starting_letter_count[starting_letter] += 1
        else:
            starting_letter_count[starting_letter] = 1
    return starting_letter_count

print(count_countries_by_starting_letter(countries))

#14
def get_first_ten_countries(countries):
    return countries[:10]
print(get_first_ten_countries(countries))

#15
def get_last_ten_countries(countries):
    return countries[-10:]
print(get_last_ten_countries(countries))
    
#Level 3
def sort_name(countries):
    return sorted(countries)

print (sort_name([country['name'] for country in countries_data]))

def sort_population(countries):
    return sorted(countries, key=lambda x: x['population'], reverse=True)

print(sort_population(countries_data))

def sort_capital(countries):
    return sorted(countries, key=lambda x: x['capital'])
print(sort_capital(countries_data))

def get_most_populated_countries(countries, n=10):
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:n]

print(get_most_populated_countries(countries_data, 10))

def get_most_spoken_languages(countries, n=10):
    language_count = {}
    for country in countries:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]

print(get_most_spoken_languages(countries_data, 10))