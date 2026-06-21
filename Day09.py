#1
age=int(input("Enter your age: "))
if age>=18:
    print("You are old enough to learn to drive")
else:
    print(f"You need {18-age} more years to learn to drive")
    
#2
my_age=30
if my_age>age:
    if my_age-age>1:
        print(f"I am {my_age-age} years older than you")
    else:
        print("I am 1 year older than you")
elif my_age==age:
    print("We have the same age")
else:
    if age-my_age>1:
        print(f"You are {age-my_age} years older than me")
    else:
        print("You are 1 year older than me")

#3
a=int(input("Enter number one "))
b=int(input("Enter number two "))

if a>b:
    print(f"{a} is greater than {b}")
elif a<b:
    print(f"{a} is lower than {b}")
else:
    print(f"{a} is equal to {b}")

#Level 2
#1
score=int(input("Introduce your score "))
if score<=100 and score>=90:
    print("You got A")
elif score<=89 and score>=80:
    print("You got B")
elif score<=79 and score>=70:
    print("You got C")
elif score<=69 and score>=60:
    print("You got D")
elif score<=59 and score>=0:
    print("You got F")

#2
month=input("Introduce the month ")
if month=="September" or month=="October" or month=="November":
    print("The season is Autumn")
if month=="December" or month=="January" or month=="February":
    print("The season is Winter")
if month=="March" or month=="April" or month=="May":
    print("The season is Spring")
if month=="June" or month=="July" or month=="August":
    print("The season is Summer")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit=input("Introduce a fruit ")
if new_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(new_fruit)
    print(fruits)
    
#Level 3
person={
    'first_name': 'Unai',
    'last_name': 'Guerra Matas',
    'age': 20,
    'country': 'Spain',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print(person['skills'][len(person['skills'])//2])
if 'skills' in person:
    if 'Python' in person['skills']:
        print("Python is present")
if 'skills' in person:
    if 'JavaScript' in person['skills'] and 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a fullstack developer")
    elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print("He is a front end developer")
    elif 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a backend developer")
    else:
        print("Unknown title")
if not person['is_married'] and person['country']=='Spain':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is not married.")