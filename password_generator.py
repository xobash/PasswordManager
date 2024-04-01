# Creating a simple password generator using Python. Practicing defining functions, & lists. 
import secrets
import string

# Defining the generate password function.
def generate_password(length=12):
  # Defining character types used for the password.
    characters = string.ascii_letters + string.digits + string.punctuation
  # Creating an empty string for the password and returining the generated password. 
    return ''.join(secrets.choice(characters) for _ in range(length))

# Defining main function. 
def main():
    length = int(input("Enter password length (default is 12): "))
    # Defining the variable password as the generated password from the generate_password function.
    password = generate_password(length)
    print(password)

# Checking if the script is being run directly. (This will be built upon in the future.)
if __name__ == "__main__":
    main()
