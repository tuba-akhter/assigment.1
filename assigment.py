print("hello world")
print("hey")
print('tooba')
print("its me")
#addition
num1=int(input("Enter ypur first number:"))
num2=int(input("Enter your second number:"))
result=num1+num2
print(f"the result of num1 and num2 is: {result}")
#divsion
num3=int(input("Enter your number for divdion:"))
num4=int(input("enter your 4th number: "))
if num4==0:
  print("divison by zero isnt allowed")
else:
 div_result=num3/num4
print(f"the result of divsion: {div_result}")
#Write a Python program to find the area of a triangle.
base=int(input("enter the base of the triangle: "))
height=int(input("enter the height of the triangle: "))
area=0.5*base*height
print(f"the area of the triangle is: {area}")
#Write a Python program to swap two variables.
a=int(input("enter a number to swap: "))
b=int(input("enter 2nd number to swap: "))
temp=a
a=b
b=temp
print(f"the swaped values of a is {a} and b is {b} ")
#Write a Python program to generate a random number.
#import random 
#print(f"the random numbers are random.randtint{(1,100)}")
#Write a Python program to convert kilometers to miles.
kilometer=int(input("enter distance to find the kilometer: "))
conversion_factor=0.621371
meters=kilometer*0.621371
print(f"the kilometer in distance is {meters} meters.")
#Write a Python program to convert Celsius to Fahrenheit.
celsius=int(input("enter a number to covert the celsius into fahrenheit "))
fahrenheit= (celsius * 9/5) + 32
print(f"the coversion of celsius into fahrenheit is {fahrenheit} ")
#create a calculator
import calendar
month=int(input("Enter month: "))
year=int(input("Enter year: "))
cal=calendar.month(year,month)
print(cal)


