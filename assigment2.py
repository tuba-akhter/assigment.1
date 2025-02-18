#Write a Python program to solve quadratic equation.
import math
a=int(input("Enter first coefficent a : "))
b=int(input("Ener second coefficent b : "))
c=int(input("Enter third coefficent c : "))
discriminant=4**2-4*a*c
if discriminant > 0:
 root1 = (-b + math.sqrt(discriminant)) / (2*a)
 root2 = (-b - math.sqrt(discriminant)) / (2*a)
 print(f"the root1 is: {root1}")
 print(f"the root2 is: {root2}")
elif discriminant==0:
  root= -1/(2*a)
  print(f"root is: {root}")
else:
  real_part = -b / (2*a)
imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
print(f"Root 1: {real_part} + {imaginary_part}i")
print(f"Root 2: {real_part} - {imaginary_part}i")
 

 

 #Write a Python program to swap two variables without temp variable.
a=5
b=10
a,b=b,a
print("swapped values are: ")
print(f"a={a}")
print(f"b={b}")




#Write a Python Program to Check if a Number is Positive, Negative or Zero.
num=int(input("Enter a number to check that the number is positive,negtive or neutral: "))
if num > 0:
  print(" the number is positive ")
elif num==0:
  print("the number is zero")
else:
  print("number is negtive")




#Write a Python Program to Check if a Number is Odd or Even.
num=int(input("Enter a number to check the number is even or odd: "))
if num%2==0:
 print("The number is even")
else:
 print("The number is odd")



#Write a Python Program to Check Leap Year.
year=int(input("enter a year: "))
if (year%400==0) and (year%100==0):
  print("{0}This year is leap year".format(year))
elif (year%4==0) and (year%100==0):
  print("{0}  this year is a leap year".format(year))
else:
  print("{0}  is not a leap year".format(year))



#Write a Python Program to Check Prime Number.
num=int(input("Enter a num to check the prime number: "))
flag = False
if num==1:
  print(f"{num} is not a prime number")
elif num > 1:
  for i in range(2, num):
    if(num%i)==0:
      flag = True
    break
  if flag:
    print(f"{num}, is not a prime number")
else:
 print(f"{num}, is a prime number")

#Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
lower = 1
upper = 10
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
 if num > 1:
     for i in range(2, num):
       if (num % i) == 0:
          break
     else:
      print(num)

#Write a Python Program to Find the Factorial of a Number.
num = int(input("Enter a number to find the fictorial: "))
factorial = 1
if num <0:
 print("Factirial does not exist for negative numbers")
elif num == 0:
 print("Factorial of 0 is 1")
else:
 for i in range(1, num+1):
  factorial = factorial*i
 print(f'The factorial of {num} is {factorial}')


 #Write a Python Program to Display the multiplication Table.
 num=int(input("Enter a number that u want to print a table for "))
 for i in range(1, 11):
  print(f"{num} X {i} = {num*i}")



#Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.
def add(x, y):
 return x+y
def substraction(x, y):
  return x-y
def multiplicationa(x, y):
  return x*y
def division(x, y):
  return x/y

  print("please select an operator")
  print("1.add")
  print("2.substraction")
  print("3.multplication")
  print("4.division")

  while True:
    choice= input("please enter choice(1/2/3/4): ")
    if choice in('1', '2', '3', '4'):
     Try
    num1=int(input("enter first number: "))
    num2=int(input("enter 2nd number: "))
     except ValueError:
     print("Invalid input. Please enter a number.")
    continue
    if choice == '1':
          print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
   

      
