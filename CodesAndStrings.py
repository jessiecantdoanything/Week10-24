# strings

# concatenation

firstName = "Jesus"
lastName = "Monte"

print(firstName + " " + lastName)

name = firstName + " " + lastName
lastFirst = lastName + ", " + firstName

print(lastFirst)

# repition

print("uh "*2 + "AAAAAAAAA")

def imTiredofSchool():
    print("me, "*3 + "young Jessie,")
    print("is extremely exhausted")
    print("Why must you ask?")
    print("school "*3)

imTiredofSchool()

# indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)

middleCharIndex = len(name) // 2
print(middleCharIndex)
print(name[middleCharIndex])
print(name[-3])

for i in range(0, len(name)):
    print(name[i])

#slicing and dicing

print(name[0:3])

for i in range(0, len(name)+1):
    print(name[0:i])

# searching

print("biv" in name)
print("y" not in name)


    # String Methods to investigate:
    # Method        Use Example         Explanation
    # center        aStr.center(w)
    # ljust         aStr.ljust(w)
    # rjust         aStr.rjust(w)
    # upper         aStr.upper()
    # lower         aStr.lower()
    # index         aStr.index(item)
    # rindex        aStr.rindex(item)
    # find          aStr.find(item)
    # rfind         aStr.rfind(item)
    # replace       aStr.replace(old, new)

    # Be sure to include multiple examples of all of them in use

# Character functions


from mapper import *

print(letterToIndex('M'))

print(indexToLetter(24))
from crypto import *


print(scramble2Encrypt("THE MEETING IS AT FIVE OCLOCK"))
print(scramble2Decrypt("H ETN SA IEOLCTEMEIGI TFV COK"))

