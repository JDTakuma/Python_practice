operations = ['addition', 'subtraction', 'multiplication', 'division', 'square root']#create a list
print("This is the list of operations:") #initial message
operations.append('exponent')#new element on the list
for item in range(1): #elements using a for loop
    print(operations) #result
print("-------------------------------------------------")#Its a division
fruits = ('apple','banana','orange','grape','watermelon','kiwi', 'pineapple') #list of fruits
length = len(fruits)#check the number of fruits on the list
i = 0 #counter
print("The seven fruits are:")#Message 
while i < length: #loop to be followed until the condition is not met
    print(fruits[i])#will print the 7 fruits in different lines 
    i += 1 #
print("-------------------------------------------------")#division

fruitDir = { #dictionary with characteristics of an fruit
"name": "apple",#name of the fruit 
"color": "red", #color of the fruit
"taste": "sweet"#taste of the fruit
}
print("This is the firts Dictionary of characteristics:")
print(fruitDir)
fruitDir["color"] = "green"# modify one of the properties
print("Its is the new list with the change of color:")# print the updated dictionary
print(fruitDir) #final result