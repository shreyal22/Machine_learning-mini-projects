print('What do you want to pickup from the store?')
print('Enter DONE when finished!')
lst=[]
while True:
    new=input("Enter the item to be purchased: ")
    
    if new=='DONE':
        break
    lst.append(new)
    
print("Your list is as follows: ")
for item in lst:
 print(item)

