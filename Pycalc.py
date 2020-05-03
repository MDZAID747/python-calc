def add():
    a=input("Enter the first number")
    b=input("Enter the second number")
    a=float(a)
    b=float(b)
    c=a+b
    c=float(c)
    print("The addition of two number is %0.02f"%(c))
    
def sub():
    a=input("Enter the first number")
    b=input("Enter the second number")
    a=float(a)
    b=float(b)
    c=a-b
    c=float(c)
    print("The substraction of two number is %0.02f"%(c))
    
def mul():
    a=input("Enter the first number")
    b=input("Enter the second number")
    a=float(a)
    b=float(b)
    c=a*b
    c=float(c)
    print("The multiplication of two number is %0.02f"%(c))
    
def div():
    a=input("Enter the first number")
    b=input("Enter the second number")
    a=float(a)
    b=float(b)
    c=a/b
    c=float(c)
    print("The division of two number is %0.02f"%(c))
    
def fact():
    a=input("Enter a number to find factorial")
    a=int(a)
    s=1
    for i in range(0,a):
        
        s=s*(a)
        a=a-1
    print("The factorial of the given number is ",s)

def square():
    a=input("Enter a number to find square ")
    a=int(a)
    b=a*a
    b=int(b)
    print("The square of the given number is ",b)
    
def sqroot():
    a=input("Enter a number to find square root")
    a=float(a)
    b=a**0.5
    b=float(b)
    print("Square root of the given number is %0.02f"%(b))
    

try:
    print("            PYTHON CALCULATOR              ")
    print("PRESS\n   1)for ADDITION\n   2)for SUBSTRACTION\n   3)for MULTIPLCATION\n   4)for DIVISION\n   5)for FACTORIAL\n   6)for SQUARE\n   7)for SQUAREROOT\n")   
    z=input("Enter Your Choice") 
    z=int(z)
except:
    print("Invaliind Option")
finally:
    if(z==1):
        add()
    elif(z==2):
        sub()
    elif(z==3):
        mul()
    elif(z==4):
        div()
    elif(z==5):
        fact()
    elif(z==6):
        square()
    elif(z==7):
        sqroot()
    else:
        print("Error in program")
        