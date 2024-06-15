import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length for the password: "))
        
        if length <= 0:
            print("Password length should be a positive integer.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated Password: {password}")
        
    except ValueError:
        print("Please enter a valid integer for the password length.")

if _name_ == "_main_":
    main()


# Enter the desired length for the password: 12
# Generated Password: 2B1|xjz8HdV_
