#function
#def function_name(parameters):
    #function logic or boay
    #return
#calling function
#Functions with parameters and arguments
#Add 2 numbers
def add(a, b): #a,b are the parameters
    return a + b
print(add(2, 3)) #2,3 are the arguments

def sub(c, d):
    return c - d
print(sub(10, 4))

#Only parameters no arguments
def add(a=3, b=6):
    return a + b
print(add())

#no parameters and arguments
def greet():
    print("Hello")
greet() #function calling

def square(n):
    return n*n
result = square(5)
print(result)

#convert strings to uppercase 
names = ["abc", "def", "ghi"]
result = [name.upper() for name in names]
print(result)

