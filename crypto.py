#Encription

import pyAesCrypt
import os


# Function for encryption file

def encryption(file, password):
    # buffer size
    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )
    print("File " + str(os.path.splitext(file)[0] + " encrypted"))

    #delete original file
    os.remove(file)

#function for scaning directories


def walking_by_dirs(dir, password):
    # creating for loop
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # if we found any type of Fyle we need to encrypyit
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)

        else:
            walking_by_dirs(path, password)

password = input("Passwrord for encryption: ")

data = r""  #Directoy for encrypting files

walking_by_dirs(data, password)
