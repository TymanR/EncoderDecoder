class Backend:

    ExcelFileName = "EncodingValues.csv"
    Dictionary = {}

    def Decrypt(textToDecrypt):
           arrayChars = []
           arrayChars = Backend.DivideIntoArray(textToDecrypt)     
           
    
    def Encrypt(textToEncrypt):
      parts = []
      Backend.ReadExcelFile(Backend.ExcelFileName)
      chars = list(textToEncrypt)
     # chars = textToEncrypt.split()
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
         lines = line.split('=')
         DictionaryTemp[lines[0]] = lines[1]

       Backend.Dictionary = DictionaryTemp 
        
       
    
