letter = '''Dear <|Name|>,
i am happy to tell you about your self
                  you are selected!
           Date :      <|Date|> '''
name = input("Enter your Name\n")
date = input("Enter Date\n")  
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)    
print(letter)                  