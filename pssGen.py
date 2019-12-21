import random

#Asks user to generate bitcoin password
print("\n===============BITCOIN PASSWROD GENERATOR===============")
#asks user to enter password length
passLength = int(input("Enter length of password:"))
string = "abcdefghijklmnABCoZ!@#$%^MpqrsDLEF0AZ!@#$%^BCODtKuvJwIGHxyz01234567890AZ!@#$%^BCODEFGHNIJKLMNOPQRSTUVWXYZ!@#$%^%^&*()?"
#passLength = 20
password =  "".join(random.sample(string,passLength))
print ("\nNew password: ", password)