import random
import string
#1
def random_user_id():
    user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return user_id

print (random_user_id())

#2
def user_id_gen_by_user():
    characters = int(input("Enter number of characters: "))
    ids = int(input("Enter number of IDs: "))
    for _ in range(ids):
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=characters))
        print(user_id)

user_id_gen_by_user()

#3
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

print(rgb_color_gen())

#Level 2
#1
def list_of_hexa_colors(number):
    
    colors=[]
    for n in range(number):
        
        colors.append('#'+''.join(random.choices(string.hexdigits,k=6)))
    return colors

print(list_of_hexa_colors(5))

#2
def list_of_rgb_colors(number):
    colors= []
    for n in range(number):
        colors.append(rgb_color_gen())
    return colors

print (list_of_rgb_colors(3))

#3
def generate_colors(type,number):
    colors=[]
    if type == 'hexa':
        colors.append(list_of_hexa_colors(number))
    elif type == 'rgb':
        colors.append(list_of_rgb_colors(number))
    return colors   

print(generate_colors('hexa',2))

#Level 3
#1
def shuffle_list(list):
    random.shuffle(list)
    return list

print(shuffle_list([1,6,23,7,8]))

#2
def seven_random_nums():
    return random.sample(range(0,9),7)

print(seven_random_nums())
            