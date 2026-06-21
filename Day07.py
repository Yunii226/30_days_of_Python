# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print(len(it_companies))

#2
it_companies.add("Twitter")
print(it_companies)

#3
it_companies.update(["OpenAI","NVIDIA","Anthropic"])
print(it_companies)

#4
it_companies.remove("Microsoft")
print(it_companies)

#5
#it_companies.remove("Microsoft") This would fail, remove only works with existent elements, else it raise an exception.
it_companies.discard("Microsoft") # Discard do works with not existing elements
print(it_companies)

#Level 2
#1

print(A.union(B))

#2
print(A.intersection(B))

#3
print(A.issubset(B))

#4
print(A.isdisjoint(B))

#5
print(A.union(B))
print(B.union(A))

#6
print(A.symmetric_difference(B))

#7
del A
del B

#Level 3
#1
ages_st=set(age)
print("List length", len(age))
print("Set length", len(ages_st))
if len(age)>len(ages_st):
    print("The list is larger")
elif len(ages_st)>len(age):
    print("The set is larger")
else:
    print("They are equal large")
    
#2
print ("""
String: Immutable text. 
List: Mutable ordered collection. 
Tuple: Immutable ordered collection. 
Set: Mutable unordered unique elements.
       """)

#3
words=set("I am a teacher and I love to inspire and teach people".split(" "))
print(len(words))