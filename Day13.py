#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives = [i for i in numbers if i<=0]
print (negatives)

#2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
single_list = [x for lst in list_of_lists for l in lst for x in l]
print(single_list)

#3
tuplas = [(i,i**0,i,i**2,i**3,i**4,i**5) for i in range(10)]
print(tuplas)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lst_countries= [[country[0].upper(), country[0][:3].upper(), country[1].upper()] for item in countries for country in item]
print(lst_countries)

#5
lst_dictionaries= [{'country': country[0], 'city': country[1]} for item in countries for country in item]
print(lst_dictionaries)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lst_names = [name[0] + " " + name[1] for i in names for name in i]

print (lst_names)