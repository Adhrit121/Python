from cryptography.fernet import Fernet
import os

key = b'ObcwFG1Wp9noy1MniE5nN2BzfpwrUO0z10HQKQhYFqE='
fernet = Fernet(key)

def decrypt(message):
    deMessage = fernet.decrypt(message).decode()
    return deMessage
def dir_back():
    current_directory = os.getcwd()
    parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
    os.chdir(parent_directory)
    new_directory = os.getcwd()
    return new_directory

x=True
while x:
    print(" ")
    in_message = input("ENc:").encode()
    print(decrypt(in_message))

if not x:
    print(os.getcwd())
    print(dir_back())
    print(os.getcwd())