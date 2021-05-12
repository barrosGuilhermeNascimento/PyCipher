#Initializing alphabet array

searchArray = "abcdefghijklmnopqrstuvwxyz0123456789"
alphabetArray = "abcdefghijklmnopqrstuvwxyz"


# Getting the string
raw_input = input("Insert your string: ")
rotations = int(input("Insert the rotaions: ")) 
returnString = ''

for i in raw_input:
    if (i.isspace()):
        returnString += ' '
        continue
    elif (i.isnumeric()):
        returnString += i
        continue
    location = searchArray.index(i.lower())
    newLocation = location + rotations
    if (newLocation >= 26):
        newLocation -= 26
    if (i.isupper()):
        returnString += (alphabetArray[newLocation].upper())
    else:
        returnString += (alphabetArray[newLocation])

print("Returned String:", returnString)