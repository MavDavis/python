from cryptography.fernet import Fernet
# Generate a key

# def write_key():

#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)


def load_key():
    with open("./key.key", "rb") as file:
        key = file.read()
        return key
# master_pwd = input("What is your master password? ")
# key = load_key() + master_pwd.encode()
key = load_key()
fer = Fernet(key)
print(fer, key)
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passwrd = data.split("|")
            print("username: " + user + " password: " + fer.decrypt(passwrd.encode()).decode())


def add():
    account_name = input("Enter your account name: ")
    pwd = input("password: ")

    # use a to add to an existing txt file(append)
    # use r to read the file(read)
    # use w to overwrite the content of the file(write)
    #  with helps us to close the text file than the method of (file = open(name.txt) and then file.close())
    with open('password.txt', 'a') as f:
        f.write(account_name + " | "+ fer.encrypt(pwd.encode()).decode() + "\n")

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