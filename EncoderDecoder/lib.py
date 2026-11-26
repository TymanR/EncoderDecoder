class Backend:

    ExcelFileName = "EncodingValues.csv"
    Dictionary = {}
    ValueToChar = {}


    def Decrypt(textToDecrypt):
           Backend.ReadExcelFile(Backend.ExcelFileName)
           originalText = []
           arrayNumbers = []
           arrayNumbers = Backend.DivideIntoArray(textToDecrypt)
           for numbers in arrayNumbers:
            char = Backend.ValueToChar.get(numbers)
            if char is not None:
             originalText.append(char)

           return originalText
    
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
    
    
              




    def ReadExcelFile(ExcelName):
       DictionaryTemp = {}
       with open(ExcelName, "r") as f1:
        for line in f1:
         lines = line.strip().split('=')
         key = lines[0]
         if key == "SPACE":
            key = " "
         DictionaryTemp[key] = lines[1]

        
       Backend.Dictionary = DictionaryTemp 
       Backend.ValueToChar = {v: k for k, v in DictionaryTemp.items()}

       
    
 

    def DivideIntoArray(textToDivide):
        array = []
        line = textToDivide.split()
        for numbers in line:
           array.append(numbers)
            
        return array
