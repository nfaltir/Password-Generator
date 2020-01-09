import random

# Asks user to generate bitcoin password
print("\n===============BITCOIN PASSWROD GENERATOR===============")
# asks user to enter password length
passLength = int(input("Enter length of password:"))


string = "abcdefghijklmnABCoZ!@#$%^xyz012345678MpqrsDLEF0AZ!@#$%^BCODtKuvJwIGHxyz01234567890AZ!@#$%^BCODEFGHNIJKLMNOPQRSTUVWXYZ!@#$%^%^&*()?"
#passLength = 20
passwordCount = int(input("Enter how many passwords you want to generate?:"))
password = "".join(random.sample(string, passLength))

#controlls how many iterations
for password in range(passwordCount):
    password = "".join(random.sample(string, passLength))
    print("\nNew password: ", password)


#print ("\nNew password: ", password)
