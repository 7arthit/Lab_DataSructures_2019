def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0
    while (start <= end):
        print("Subarray in step {}: {}".format(step, str(array[start:end+1])))
        step = step+1
        mid = (start + end) // 2
        if element == array[mid]:
            return mid
        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
element = 49
array = [34, 67, 89, 2, 19, 27, 73, 5, 19, 49]
print("Index of {} : {}".format(element, binary_search_iterative(array, element)))