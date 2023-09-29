# hasing can be achive in python by using python dictionay

# just replace all the int inputs to normal string input for string hashing

inList = [ ]
length = int(input("Enter how many elements you want in array : "))

hashDic = {}
for i in range(0, length):
    value = int(input(f"Enter {i+1}th element : "))
    inList.append(value)

# this loop can be avoid by replacing the logic inside the above loop
# hashing the inputs 

for i in inList:
    if i in hashDic:
        hashDic[i] += 1
    else:
        hashDic[i] = 1

# inputing the number how many times numbers will be checked 
checking = int(input("Enter how many times you want to check : "))

for i in range(0, checking):
    num = int(input(f"Enter the {i+1}th number to check occerence : "))

    if num in hashDic:
        print(hashDic[num])
    else:
        print(0)
