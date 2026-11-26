class Backend:

    ExcelFileName = "EncodingValues.csv"


    def Decrypt(textToDecrypt):
          
        Backend.ReadExcelFile(Backend.ExcelFileName)

        return 0
    

 

    def TransformToDecimal(char):
          x = 0
          
        
          return x



    def DivideIntoArray(textToDivide):
        array = []
        for char in textToDivide:
            array.append(char)
        return array


    def ReadExcelFile(ExcelName):
       Dictionary = {}
       with open(ExcelName, "r") as f1:
        for line in f1:
         lines = line.split('=')
         Dictionary[lines[0]] = lines[1]
         print(Dictionary["A"])



"""  
  my_array = []

my_array.append(10)       # Add element
my_array.insert(0, 5)    # Insert at index 0
my_array.remove(10)      # Remove element by value
my_array.pop()           # Remove last element

print(len(my_array))     # Get number of elements
print(my_array[0])       # Access first element



   def Encrypt(textToEncrypt):
     arrayChars = []
     arrayChars = Backend.DivideIntoArray(textToEncrypt)     
     for char in arrayChars:
        if char == 
     
     return arrayChars

"""