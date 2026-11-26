from lib import Backend


print("Write 1 for Decrypt 2 for Encrypt")

Task  =  input()

if Task == "1":
    print("Write text u want to decrypt")
    text = input()
   
    arrayToPrint =  Backend.Decrypt(text)
    print("".join(str(value) for value in arrayToPrint))

elif Task == "2":
    print("Write text u want to encrypt")
    text = input()
    arrayToPrint = []
    arrayToPrint = Backend.Encrypt(text)
    print(" ".join(str(value) for value in arrayToPrint))
    

print("script ended")
