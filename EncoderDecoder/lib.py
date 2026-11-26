class Backend:

    ExcelFileName = "EncodingValues.csv"
    Dictionary = {}

    def Decrypt(textToDecrypt):
           arrayChars = []
           arrayChars = Backend.DivideIntoArray(textToDecrypt)     
           
    
    # need to fix when char doesnt exist in excel ,that program just skipps this char
    def Encrypt(textToEncrypt):
      parts = []
      Backend.ReadExcelFile(Backend.ExcelFileName)
      chars = textToEncrypt.split()
      for char in chars:
        value = Backend.Dictionary.get(char)

        if value is not None:
          parts.append(value)
      return parts
    
              

 

    def DivideIntoArray(textToDivide):
        array = []
        for char in textToDivide:
            array.append(char)
        return array


    def ReadExcelFile(ExcelName):
       DictionaryTemp = {}
       with open(ExcelName, "r") as f1:
        for line in f1:
         lines = line.strip().split('=')
         DictionaryTemp[lines[0]] = lines[1]

       Backend.Dictionary = DictionaryTemp 
        
       


