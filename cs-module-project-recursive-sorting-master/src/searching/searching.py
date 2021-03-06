# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    
    if end >= start:
        mid = start + (end - start) // 2
        
        # if found at mid, return mid
        if arr[mid] == target:
            return mid
        
        # search the left half
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
            # search the left half
        else:  # arr[mid] < target
            return binary_search(arr, target, mid + 1, end)
    
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target, start, end):
    
#     # start = 0
#     # end = len(arr)-1
    
#     if start > end:
#         return -1
#     mid = start + (end - start) // 2
#     if arr[mid] == target:
#         return mid
        
#     # update left and right
#     if arr[start] == arr[mid] and arr[end] == arr[mid]:
#         start += 1
#         end -= 1
        
#         if arr[start] <= arr[mid]:
            
#             # sorted subarray
#             if arr[start] <= target and arr[mid] >= target:
#                 return agnostic_binary_search(arr, target, start, mid-1)
            
#             # no target in first half
#             return agnostic_binary_search(arr, target, mid+1, end)
        
#     if arr[mid] <= target and arr[end] >= target:
#         return agnostic_binary_search(arr, target, mid+1, end)
    
#     return agnostic_binary_search(arr, target, start, mid-1)

def agnostic_binary_search_solution(arr, target):
    # $%$Start
    start = 0
    end = len(arr) - 1
    if arr[start] == arr[end]:
        if target == arr[start]:
            return start    
        else:
            return -1
    # we'll need a boolean to keep track of whether array is
    # ascending or descending 
    is_ascending = arr[start] < arr[end]
    # if the array is ascending, then perform a "normal" binary search
    if is_ascending:
        return binary_search(arr, target, 0, len(arr)-1)
    # if the array is descending, then perform a "reverse" binary search 
    else:
        return descending_binary_search(arr, target, 0, len(arr)-1)

def descending_binary_search(arr, target, start, end):
    if start > end:
        return -1
    else:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return descending_binary_search(arr, target, mid + 1, end)
        else:
            return descending_binary_search(arr, target, start, mid - 1)
    # $%$End


array = [-3, 0, 4, 7, 77, 89]
target = 4
result = binary_search(array, target, 0, len(array)-1)
print(f'target index: {result}')
