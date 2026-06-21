#1
empty_tuple= ()

#2
brothers=("Alex", "Bro2", "Bro3")
sisters=("Sis1", "Sis2", "Sis3")

#3
siblings = brothers+sisters

#4
print(f"I have {len(siblings)} siblings")

#5
family_members= siblings + ("Oscar","Silvia")

print(family_members)

#Level 2
#1
*siblings,father,mother= family_members
print(siblings)
print(father)
print(mother)

#2
fruits=("Pear","Apple","Orange","Banana")
vegetables=("Lettuce", "Onion", "Potato")
animal_products=("Milk","Meat","Eggs")

food_stuff_tp= fruits+vegetables+animal_products
print(food_stuff_tp)

#3
food_stuff_lt=list(food_stuff_tp)

#4
print(food_stuff_tp[len(food_stuff_tp)//2 - 1])

#5
print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
