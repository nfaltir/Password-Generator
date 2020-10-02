import random

def passGen():

#Asks user to generate bitcoin password
print("\n===============BITCOIN PASSWROD GENERATOR===============")

#asks user to enter password length
passLength = int(input("Enter length of password:"))
<<<<<<< HEAD:pssGen.py
string = "abcdefghijklmnABCoZ!@#$%^xyz012345678MpqrsDLEF0AZ!@#$%^BCODtKuvJwIGHxyz01234567890AZ!@#$%^BCODEFGHNIJKLMNOPQRSTUVWXYZ!@#$%^%^&*()?"
=======

#list of characters
string = "abcdefghijklmnABCoZ!@#$%^MpqrsDLEF0AZ!@#$%^BCODtKuvJwIGHxyz01234567890AZ!@#$%^BCODEFGHNIJKLMNOPQRSTUVWXYZ!@#$%^%^&*()?"

>>>>>>> b094ae17258a546c5ccd9488c7b5be69418860b2:btcPasswordGen.py
#passLength = 20
password =  (("".join(random.sample(string,passLength))

print ("\nNew password: ", password)

passGen()
