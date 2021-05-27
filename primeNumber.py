#interface
print("Prime Number Test")
userNumber = int(input("Your number: "))
factors = []

#calculate factors for the users number
for whole_number in range(1, userNumber + 1):
    if userNumber % whole_number == 0:
        factors.append(whole_number)

#get how many factors the users number has
def howManyFactorsNumberHas(factors):
    count = 0
    for element in factors:
        count += 1
    return count

#if/else to print the result
if howManyFactorsNumberHas(factors) > 2:
    print(userNumber, "is not a prime number!")
else:
    print(userNumber, "is a prime number!")