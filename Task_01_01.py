input =input("Input the Filename: ")
index= input.find(".")
x=input[int(index)+1:]
if x== "py":
    Result= "python"
else:
    Result= "Other type"
print('The extension of the file is:', Result)
