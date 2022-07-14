def selectionSort(arr):
    
    for i in range(len(arr)):
        min_x = i

        for item in range(i+1, len(arr)):
            if arr[item] < arr[min_x]:
                min_x = item

        arr[i], arr[min_x] = arr[min_x], arr[i]
        
        print(arr)
        

arr = [8, 7, 6, 5, 4]
selectionSort(arr)

print(arr)