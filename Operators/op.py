age = 21
height = 5.4 
num = 1 + 5j
# base = input("Enter base:")
# height = input("Enter height:")
# area = 0.5 * float(base) * float(height)
# print("The area of the triangle is ",int(area))

# a = input("Enter side a: ")
# b = input("Enter side b: ")
# c = input("Enter side c: ")
# perimeter = float(a) + float(b) + float(c)
# print("The perimeter of the triangle is ", perimeter)

# length = input("Enter length:")
# width = input("Enter width:")
# area = float(length) * float(width)
# perimeter = 2 * (float(length) + float(width))
# print("The area of the rectangle is ", area)
# print("The perimeter of the rectangle is ", perimeter)

# radius = input("Enter radius:")
# area = 3.14 * float(radius) **2
# circumference = 2 * 3.14 * float(radius)
# print("The area of the circle is ", area)
# print("The circumference of the circle is ", circumference)

slope = 2
c = -2
y_intercept = c
x_intercept = -c/slope
print("The slope of the line is ", slope)
print("The y-intercept of the line is ", y_intercept)
print("The x-intercept of the line is ", x_intercept)

x1=2
y1=2
x2=6
y2=10
m = (y2-y1)/(x2-x1)
print(m)

print(len('python')==len('dragon')) 

print('on' in 'python' and'on'in 'dragon')
a = len('python')
b = float(a)
c = str(b)
print(c)

n = int(input("Enter a number: "))
if(n%2==0):
    print("The number is even")
else:
    print("The number is odd")

if(7//3 == 2.7):
    print("True")

if(type('10')==type(10)):
    print("True")

if(int(float('9.8'))==10):
    print("True")

a = int(input("Enter hours: "))
b = int(input("Enter rate per hour: "))
c = a*b
print("Your weekly earning is ",c)

p = int(input("Enter the number of years you have lived: "))
print("You have lived for ", p * 365 * 24 * 60 * 60, " seconds.")


