age = 20
height=1.75
complex_number= 2j

base = float(input("Enter base: "))
height = float(input("Enter height: "))
print ("The area of the triangle is ", 0.5*base*height)

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
print ("The perimeter of the triangle is " ,a+b+c)

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
print ("The area of the rectangle is ", length*width)
print ("The perimeter of the rectangle is ", 2*(length+width))

radius = float(input("Introduce the radius of the circle: "))
print("The area of the circle is ", 3.14*(radius**2))
print("The circumference of the circle is ", 2*3.14*radius)

# y = 2x-2
m=2 #slope
b = -2 #y-intercept

x_intercept = -b / m

print("Slope:", m)
print("X-intercept:", x_intercept)
print("Y-intercept:", b)

x1=2
y1=2

x2=6
y2=10

m2=y2-y1/x2-x1 #slope

print("2nd Slope:", m2)

euclidean_distance=(((x2-x1)**2)+((y2-y1)**2))**0.5
print (m==m2)
print (euclidean_distance)

x=int(input("Value of x?: "))
y=x**2+6*x+9
print(y)

#12
print("Python length:",len("Python"))
print("Dragon length:",len("dragon"))
print (len("Python") > len("dragon"))


#13
print('on' in ('python' and 'dragon') )

#14
print('jargon' in "I hope this course is not full of jargon")

#15
print(not 'on' in ('python' and 'dragon') )

#16
length_python=len("python")
float(length_python)
str(length_python)

#17
number = int(input("Introduce a number to check if it is even"))
if number%2==0:
    print("Yeap, it is even")
else:
    print("Not even, boy")

#18
print((7//3)==int(2.7))

#19
print(type('10')==type(10))

#20
print(int('9.8')==10)

#21
hours= int(input("Enter hours:"))
rate= int(input("Enter rate per hour:"))
print(hours*rate)

#22
years=int(input("Enter number of years you have lived: "))
print("You have lived for ", 31536000*years, " seconds")

#23
for i in range(1,6):
    print(i,1,i,i**2,i**3)
    