class Backend:
    def Decrypt(textToDecrypt):
          
        

        return 0
    

    def Encrypt(textToEncrypt):
     arrayNew = []
     arrayNew = Backend.DivideIntoArray(textToEncrypt)     

     return arrayNew



    def DivideIntoArray(textToDivide):
        array = []
        for char in textToDivide:
            array.append(char)
        return array




"""  
  my_array = []

my_array.append(10)       # Add element
my_array.insert(0, 5)    # Insert at index 0
my_array.remove(10)      # Remove element by value
my_array.pop()           # Remove last element

print(len(my_array))     # Get number of elements
print(my_array[0])       # Access first element

"""