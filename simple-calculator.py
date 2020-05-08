# Simple calculator python program
# Author: Monaheng Ntai
# Date: 28 April 2020

# Function definitions

def add(a,b):
    """This function adds two numbers"""
    return a+b

def subtract(a,b):
    """This function subtracts two numbers"""
    return a-b


def multiply(a,b):
    """This function multiplys two numbers"""
    return a*b

def divide(a,b):
    """This function divides two numbers"""
    
def power(a,b):
    """This function gives power"""
    return pow(a,b)

# User Input
print("\t\tCALCULATOR. \n\n")
num1=int(input("Enter first number:"))

while(True):
    
    print("\n +  - ADD")
    print(" -  - SUBTRACT")
    print(" *  - MULTIPLY")
    print(" /  - DIVIDE")
    print(" ** - POWER")

    operator=input("\nSelect Operation:")
    if(operator=='+' or operator=='-' or operator=='*' or operator=='/' or operator=='**'):
        break
    
num2=int(input("\nEnter Second number:"))

if(operator=='+'):
    print("\n\t=  ",add(num1,num2))
    
elif(operator=='-'):
    print("\n\t=  ",subtract(num1,num2))
elif(operator=='*'):
    print("\n\t=  ",multiply(num1,num2))
elif(operator=='/'):
    print("\n\t=  ",divide(num1,num2))
else:
    print("\n\t=  ",power(num1,num2))

print("DOne")

