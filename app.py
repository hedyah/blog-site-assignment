
import dbcreds
import mariadb


conn = mariadb.connect(
                        user = dbcreds.user,
                        password = dbcreds.password,
                        host = dbcreds.host,
                        port = dbcreds.port,
                        database = dbcreds.database
)

cursor = conn.cursor()

print("Welcome to our Blog !!!")

blog_user =  input("Type your username to post content to Bloogie: ")
print ("Welcome, ", blog_user )


print(blog_user, " Here are some options for you !")
print("1.Write a new blog post?")
print("2.View other blog posts?")

while True:
    
    select = input("Enter your selection ( 1 or 2 ): ")
    
    if select == '1':
            
            print("Hi, ", blog_user)
            new_post=input("Type your content here: ")
            print(new_post , "   Would you like to submit this post?")
            
            insert_statement= ("""INSERT INTO blog_post(username, content)
                            VALUES (?,?)""") 
            data =  blog_user, new_post 
            
            cursor.execute(insert_statement,data)
            conn.commit()
            
            print("Content Posted Successfully!!")
            
    elif select == '2':
            sql = """SELECT * FROM blog_post"""
            cursor.execute(sql)
            result = cursor.fetchone();
            print(result)
            result = cursor.fetchall();
            print(result)
    
    select_next = input("Would you like to exit? (yes/no):  ")
    if select_next == "yes":
        break
    
    else:
        print("Invalid input, try again!")
    

