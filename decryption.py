import pyAesCrypt
import os


# Function for encryption file

def decryption(file, password):
    # buffer size
    buffer_size = 512 * 1024

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    print("File " + str(os.path.splitext(file)[0] + " decrypted"))

    #delete original file
    os.remove(file)

#function for scaning directories


def walking_by_dirs(dir, password):
    # creating for loop
    for name in os.listdir(dir):
        path = os.path.join(dir, name) #join directory path with files

        # if we found any type of File we need to decrypt
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)

        else:
            walking_by_dirs(path, password)

password = input("Passwrord for decryption: ")

data = r"" #decryption path

walking_by_dirs(data, password)
