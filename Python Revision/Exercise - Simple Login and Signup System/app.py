# This is a simple login/signup system which stores data in variables. 

print("Welcome to the Simple Login/Signup System") 
print("Please create an account to continue.")

username = input("Enter your username: ") 
password = input("Enter your password: ") 
print("Your account has been created successfully!") 

print("Please login to access your account.") 
username2 = input("Enter your username: ") 
password2 = input("Enter your password: ") 

if ((username == username2) and (password == password2)): 
    print("Logged in successfully!") 
else: 
    print("Invalid username or password. Please try again.") 
    print("Exiting the system...")