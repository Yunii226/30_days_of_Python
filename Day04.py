#1
single_string='Thirty'+' '+'Days'+' '+'Of'+' '+'Python'
print(single_string)

#2
single_string='Coding'+' '+'For'+' '+'All'
print(single_string)

#3
company="Coding For All"

#4
print(company)

#5
print(len(company))

#6
print(company.upper())

#7
print(company.lower())

#8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9
print(company[0:6])

#10
print(company.index('Coding'))
print(company.find('Coding'))

#11
print(company.replace('Coding','Python'))

#12
print("Python for Everyone".replace("Everyone","All"))

#13
print("Python for Everyone".split())

#14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

#15
print(company[0])

#16
print(len(company)-1)

#17
print(company[10])

#18
sentence="Python For Everyone".split()
print(f"{sentence[0][0]}{sentence[1][0]}{sentence[2][0]}")

#19
name="Coding For All".split()
print(f"{name[0][0]}{name[1][0]}{name[2][0]}")

#20
print("Coding For All".index("C"))

#21
print("Coding For All".index("F"))

#22
print("Coding For All People".rfind("l"))

#23
sentence="You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))

#24
sentence="You cannot end a sentence with because because because is a conjunction"
print(sentence.rindex("because"))

#25
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace("because because because",""))

#28
print("Coding For All".startswith("Coding"))

#29
print("Coding For All".endswith("Coding"))

#30
print('   Coding For All      '.strip())

#31
print(f'''{"30DaysOfPython".isidentifier()}
{"thirty_days_of_python".isidentifier()}''')

#32
libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(libraries))

#33
print("I am enjoying this challenge.\nI just wonder what is next.")

#34
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

#35
print("radius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is 314 meters square.")

#36
print(f'''8 + 6 = {8+6}
      8 - 6 = {8-6}
      8 * 6 = {8*6}
      8 / 6 = {8/6:.2f}
      8 % 6 = {8%6}
      8 // 6 = {8//6}
      8 ** 6 = {8**6}
      ''')