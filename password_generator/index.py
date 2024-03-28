from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Initialize the Fernet cipher
cipher = Fernet(key)


cipher_text = cipher.encrypt()
# Decrypt the data
decrypted_text = cipher.decrypt(cipher_text)

print("Decrypted:", decrypted_text.decode())
master_pwd = input("What is your master password? ")
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passwrd = data.split("|")
            print("username: " + user + " password: " + passwrd)


def add():
    account_name = input("Enter your account name: ")
    pwd = input("password: ")

    # use a to add to an existing txt file(append)
    # use r to read the file(read)
    # use w to overwrite the content of the file(write)
    #  with helps us to close the text file than the method of (file = open(name.txt) and then file.close())
    with open('password.txt', 'a') as f:
        f.write(account_name + " | "+pwd + "\n")

while True:
    mode = input("Do you want to create new passwords or view existing passwords(Enter View or Add)? Enter q to quit ").lower()

    if mode == "q":
        break
    if mode == "view":
        view()
        continue
    elif mode == "add":
        add()
        continue
    else:
        print("You entered invalid mode")
        continue