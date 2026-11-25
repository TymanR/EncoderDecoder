from lib import Backend


print("Write 1 for Decrypt 2 for Encrypt")

Task  =  input()

if Task == "1":
    print("Write text u want to decrypt")
    text = input()
    Backend.Decrypt(text)

elif Task == "2":
    print("Write text u want to encrypt")
    text = input()
    arrayToPrint = []
    arrayToPrint = Backend.Encrypt(text)
    print(arrayToPrint)
    

print("scs")
