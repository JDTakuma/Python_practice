operations = ['addition', 'subtraction', 'multiplication', 'division', 'square root']# Create a list
print("This is the list of operations ") #initial message
operations.append('exponent')# New element on the list
for item in range(1): # Elements using a for loop
    print(operations) #result
print("-------------------------------------------------")#Its a division
fruits = ('apple','banana','orange','grape','watermelon','kiwi', 'pineapple') #list of fruits
length = len(fruits)#check the number of fruits on the list
i = 0 #Counter
print("The seven fruits are:")#Message 
while i < length: #loop to be followed until the condition is not met
    print(fruits[i])#will print the 7 fruits in different lines 
    i += 1