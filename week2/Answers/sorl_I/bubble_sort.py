def bubbleSort(arr):
    n = len(arr)
    for i in range(0, n):
        # for optimization
        isSwaped = False
        for j in range(0, n-1-i):
  
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSwaped = True
        if isSwaped == False:
            return arr
      

    return arr


# arr = [1, 2,3,4,5]  #best case
arr = [1, 4, 2, 7, 3, 9, 2]  #wrost and average case
sorted_arr = bubbleSort(arr)
print("Sorted Array is : ",sorted_arr)

'''
[3,2,1]  n =3
[2,3,1] i = 0, j= 0 , n-i-1 -> 3-1-0 = 2 times that is  0 and 1
[2,1,3] i = 0, j= 1 

[2,1,3] 
[1,2,3] i = 1, j= 0
[1,2,3] i = 1, j= 1

so i will go till n-1 and j will loop n-i-1

'''