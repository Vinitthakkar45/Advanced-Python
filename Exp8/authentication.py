import hashlib
import logging

sha256 = hashlib.sha256()
logging.basicConfig(filename='authentication.log', level=logging.INFO)

file="user_data.txt"
while(True):
    print("Menu :")
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Exit")
    
    try: 
        choice = int(input("Enter your choice : "))
    except ValueError:
        logging.error("Invalid choice. Please try again.")
        print("Invalid choice. Please try again.")
        continue
    if choice == 1:
        username = input("Enter username : ")
        if(username.__contains__(' ')):
            print("Username cannot contain spaces. Please try again.")
            logging.error("Username cannot contain spaces. Please try again.")
            continue
        flag=True
        with open(file, 'r') as f:
            for row in f.readlines():
                row=row.split(" ")
                if row[0] == username:
                    logging.error("Username already exists. Please try again.")
                    print("Username already exists. Please try again.")
                    flag=False
                    break
        if(flag==False):
            continue
        password = input("Enter password : ")
        
        sha256 = hashlib.sha256()
        sha256.update(password.encode())
        password_hash = sha256.hexdigest()
        
        with open (file, 'a') as f:
            f.write(username + " " + password_hash)
            f.write("\n")
            logging.info("Sign Up successful for username : "+ username)
        print("Sign Up successful for username : ", username)
        
    elif choice == 2:
        username = input("Enter username : ")
        password = input("Enter password : ")
        
        sha256 = hashlib.sha256()
        sha256.update(password.encode())
        password_hash = sha256.hexdigest()
        
        with open(file, 'r') as f:
            for row in f.readlines():
                row=row.split(" ")
                if row[0] == username and row[1].strip() == password_hash:
                    logging.info("Sign In successful for username : "+ username)
                    print("Sign In successful for username : "+ username)
                    break
            else:
                print("Invalid username or password")
                logging.error("Invalid username or password for username : "+ username)
       
    elif choice == 3:
        break

    else:
        print("Invalid choice. Please try again.")
        logging.error("Invalid choice. Please try again.")