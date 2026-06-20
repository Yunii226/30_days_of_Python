# Day 2:30 Days of python programming

first_name = 'Unai'
last_name = 'Guerra Matas'
country = 'España'
city = 'Toledo'
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = True

birth_date, birth_year, birth_month, birth_day = "2005-06-22", 2005, 6, 22
# Level 2
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(birth_date))
print(type(birth_year))
print(type(birth_month))
print(type(birth_day))

print("Length of first name:", len(first_name))
print("Length of last name:", len(last_name))

print ("Is first name longer than last name?", len(first_name) > len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle=3.14159*(radius**2)
circumference_of_circle= 2*3.14159*radius
print ("Area: ",area_of_circle, " Circumference ", circumference_of_circle)

radius_input = float(input("What is your radius?: "))
print ("Area of circle: " , 3.14159*(radius_input**2))

first_name = input("What is your first name?")
last_name = input("What is your last name?")

help('keywords')