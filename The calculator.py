import math
#all functions here
help = ("For addition type addition or add\nFor subtraction type sutraction or minus\nFor multiplication type multiplication or times\nFor division type division or divide\nFor exponents type exponents or power\nFor square root type square root or sqrt\nFor area type area\nFor volume type volume\nFor sales tax type sales tax or tax")

def title():
 print("---------------------------")
 print("Welcome to my calculator")
 print("If you need help type help")
 print("---------------------------")

def end():
 print("--------------------------------------------")
 print("Thank you for using my calculator program :D")
 print("--------------------------------------------")
 print("Credits")
 print("Ryan for making the flowchart planing sheet")
 print("Ryan for making the funtions")
 print("Ryan for doing the coding")
 print("Ryan for qa testing and bug fixing")
 print('last but not least Ryan for leading the "group"')
 
def addition(a,b): 
  print(a+b)

def subtraction(a,b): 
  print(a-b)

def squareroot(a):
    print(round(math.sqrt(a),2))

def multiplication(a,b):
    print(round(a*b,2))

def division(a,b):
    print(round(a/b,2))

def powering(a,b):
    print(round(a**b,2))

def squarearea(a):
    print(round(a**2,2))

def recarea(a,b):
    print(round(a*b,2))

def triarea(a,b):
    print(round((a*b)/2,2))
    
def circlearea(a):
    print(round((a**2)*math.pi,2))
    
def taxtime(a,b):
    b = b/100
    
    print(round((a*b)+a,2))

def cubevol(a):
    print(round(a**3,2))
    
def recvol(a,b,c):
    print(round(a*b*c,2))

def trivol(a,b,c):
    print(round((a*b*c)/2,2))
    
def cirvol(a):
    print(round((4/3)*math.pi*(a**3),2))
    
def adding():
    try:
     numbers = float(input("What's the first number you are adding:"))
     numbers2 = float(input("What's the second number you are adding:"))
     addition(numbers,numbers2)
    
    except:
        print("Error please enter single numbers only")
 
def sqrt():
    try:
     numbers= float(input("What number are you square rooting:"))
     squareroot(numbers)
     
    except:
        print("Error please enter a single positive number")   

def subing():
    try:
     numbers = float(input("What's the first number you are subtracting:")) 
     numbers2 = float(input("What's the second number you are subtracting:"))
     subtraction(numbers,numbers2)
    
    except:
        print("Error please enter single numbers only") 

def xing():
    try:
     numbers = float(input("What's the first number you are multiplying:"))
     numbers2 = float(input("What's the second number you are multiplying:"))
     multiplication(numbers,numbers2)
    except:
        print("Error please enter single numbers only")

def divi():
    try:
     numbers = float(input("What's the first number you are dividing:"))
     numbers2 = float(input("What's the second number you are dividing:"))
     division(numbers,numbers2)
    except:
        print("Error please enter single numbers only")

def expo():
    try:
     numbers = float(input("What's the first number you are dividing:"))
     numbers2 = float(input("What's the second number you are dividing:"))
     division(numbers,numbers2)
    except:
        print("Error please enter single numbers only")

def are():
     shape = input("Are you looking for the area of a square, rectangle, circle or triangle?: ") 
     shape=shape.casefold()
     
     if shape == "square":
       try:
         numbers = float(input("What's the side lenth of the square:"))
         squarearea(numbers)
       except:
           print("Error please enter single numbers only")
     if shape == "rectangle":
        try:
         numbers = float(input("What's the lenth of the rectangle:"))
         numbers2 = float(input("What's the width of the rectangle:"))
         recarea(numbers,numbers2)
        except:
            print("Error please enter single numbers only")
     if shape == "triangle":
        try: 
         numbers = float(input("What's the base of the triangle:"))
         numbers2 = float(input("What's the hight of the triangle:"))
         triarea(numbers,numbers2)
        except:
            print("Error please enter single numbers only")
     if shape == "circle":
        try:
         numbers = float(input("What's the radius of the circle:"))
         circlearea(numbers)
        except:
            print("Error please enter single numbers only")
            
def nottheirs():
     try:
         numbers = float(input("What's the price of what you're buying:"))
         numbers2 = float(input("What's the tax percent (don't add the '%' sign):"))
         taxtime(numbers, numbers2)
     except:
         print("Error please enter single numbers only")

def turnup():
     shape = input("Are you looking for the volume of a cube, rectangular prism, triangular prism or sphere?: ") 
     shape=shape.casefold()
     
     if shape == "cube":
       try:
         numbers = float(input("What's the side lenth of the cube:"))
         cubevol(numbers)
       except:
           print("Error please enter single numbers only")
     if shape == "rectangular prism":
        try:
         numbers = float(input("What's the lenth of the prism:"))
         numbers2 = float(input("What's the width of the prism:"))
         numbers3 = float(input("What's the hight of the prism:"))
         recvol(numbers,numbers2,numbers3)
        except:
            print("Error please enter single numbers only")
     if shape == "triangular prism":
        try: 
         numbers = float(input("What's the base of the prism:"))
         numbers2 = float(input("What's the hight of the prism:"))
         numbers3 = float(input("What's the length of the prism:"))
         triarea(numbers,numbers2,numbers3)
        except:
            print("Error please enter single numbers only")
     if shape == "sphere":
        try:
         numbers = float(input("What's the radius of the sphere:"))
         cirvol(numbers)
        except:
            print("Error please enter single numbers only")
#------------------

#body

calculating = True
stop = ""

while calculating == True:

 title()
 doing = input("Enter what you're doing:")
 doing=doing.casefold()

 if doing == "help":
     print(help)

 if doing=="square root" or doing == "sqrt":
     sqrt()
     stop = input("Do you want to stop? (yes or no):")
     
 if doing=="addition" or doing == "add":
     adding()
     stop = input("Do you want to stop? (yes or no):")
     
 if doing=="subtraction" or doing == "minus":
     subing()
     stop = input("Do you want to stop? (yes or no):")
     
 if doing=="times" or doing == "multiplication":
     xing()
     stop = input("Do you want to stop? (yes or no):")
     
 if doing=="division" or doing == "divide":
     divi
     stop = input("Do you want to stop? (yes or no):")
     
 if doing=="exponents" or doing == "power":
     expo()
     stop = input("Do you want to stop? (yes or no):")
     
 if doing=="area":
     are()
     stop = input("Do you want to stop? (yes or no):")  
              
 if doing == "sales tax" or doing == "tax":
     nottheirs()         
     stop = input("Do you want to stop? (yes or no):") 
             
 if doing=="volume":
     turnup()
     stop = input("Do you want to stop? (yes or no):") 
        
 if stop == "yes":
     break
 
end()
