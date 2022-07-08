
def binarySearch(my_array, target):
    cnt=0
    left = 0
    right = len(my_array) - 1

    while left <= right:
        cnt= cnt+1
        middle = (left + right) // 2
        middle_element = my_array[middle]

        if target == middle_element:
            return cnt
        elif target < middle_element:
            right = middle - 1
        else:
            left = middle + 1
    return cnt

### Test 1 ###
print(binarySearch(a, 99999))

### Test 2 ###
print(binarySearch([5, 10, 15, 20, 25], 15))