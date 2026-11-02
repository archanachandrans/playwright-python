#Defines a decorator that accepts function as an argument
def logger(func):
#Defines an inner func that adds extra behaviour
    def wrapper():
        print("Function started")
        func() #calls original fn, which is greet()
        print("function ended")
    return wrapper #returns wrapper fn 
@logger #applies decorator to greet
def greet():
    print("Welcome to python playwright")
greet() #greet = logger(greet)
#func() - greet()

#Login Authentication
def login_required(func):
    def wrapper(is_logged_in):
        if not is_logged_in: #if not true = false
            print("Access denied, Please login again")
            return
        return func(is_logged_in) #func dashboard
    return wrapper
@login_required
def dashboard(is_logged_in):
    print("Welcome to dashboard")
dashboard(True) #login required of dashboard(true)
dashboard(False)

#Lambda function
#Anonymous, single line functions
def squares(x):
    return x * x
print(squares(5))

square = lambda x : x*x 
print(square(5))

def add(a, b):
    return a + b
print(add(3,6))

add = lambda a, b: a + b
print(add(3,6))

# import pandas as pd 
# live_transactions = [
#     {"user": "Vikas" , "amount": 1250, "status": "completed"},
#     {"user": "Vikas" , "amount": 1950, "status": "pending"},
#     {"user": "Vikas" , "amount": 2250, "status": "completed"}
# ]
# #Flag VIP orders
# df = pd.DataFrame(live_transactions)
# df[is_vip] = df['amount'].apply(lambda x:True if x > 500 else False)
# #Anonymize user name for privacy
# df['user'] = df['user'].apply(lambda name: name[0] + "***")
# print(df)

