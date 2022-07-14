def bubbleSort(arr):
    for iter in range(len(arr)):
        for index in range(0, len(arr) - 1 - iter):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
        print(arr)
        
arr = [8, 7, 6, 5, 4]
bubbleSort(arr)

print(arr)
