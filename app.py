
from select import select


print("Welcome to our Blog")

user =  input("Type your username to post content to Bloogie: ")
print ("Hey, ", user )


print(user, "   Here are some options for you !")
print("1.Would you like to write a new post?")
print("2.Would you like to view other posts?")


while True:
    select = input("Enter selection (1/2): ")
    
    if select in ('1', '2'):
        new_post = input("Would you like to write a new post?: (y/n) ")
        see_post = input( "Would you like to see other posts?: (y/n)")
    
        if select == '1':
            