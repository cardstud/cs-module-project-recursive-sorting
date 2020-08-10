# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    num_elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    a = 0  # pointer in A arry
    b = 0  # pointer in B arry

    while a < len(arrA) and b < len(arrB):
        # check if arrA pointer is less than arrB pointer
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1
    if a < len(arrA):
        # arrA still has leftover elements
        #   so push them all to the merged array
        merged_arr.extend(arrA[a:])

    if b < len(arrB):
        merged_arr.extend(arrB[b:])

    return merged_arr

# test it
arrA = [3, 6, 8, 12, 15]
arrB = [1, 4, 5, 9, 11]
print("Merged array: ", merge(arrA, arrB))





# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case: stop spliting arrays in half when the arrays
    #   reach length of 1 (single element arrays)
    if len(arr) > 1: 
    # otherwise, keep splitting them in half
        left = merge_sort(arr[0 : len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2 : ])
        return merge(left, right)

    return arr 

# test it
arr = [45, 12, 89, 14, 67, 45, 23, 90, 11]
print("Array sorted: ", merge_sort(arr))





# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass 
    

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass 
