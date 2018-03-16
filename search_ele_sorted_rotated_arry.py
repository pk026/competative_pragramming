# We can search an element in one pass of Binary Search. The idea is to search
# 1) Find middle point mid = (l + h)/2
# 2) If key is present at middle point, return mid.
# 3) Else If arr[l..mid] is sorted
#     a) If key to be searched lies in range from arr[l]
#        to arr[mid], recur for arr[l..mid].
#     b) Else recur for arr[mid+1..r]
# 4) Else (arr[mid+1..r] must be sorted)
#     a) If key to be searched lies in range from arr[mid+1]
#        to arr[r], recur for arr[mid+1..r].
#     b) Else recur for arr[l..mid]
def search (arr, l, h, key):
    if l > h:
        return -1
     
    mid = (l + h) // 2
    if arr[mid] == key:
        return mid
 
    # If arr[l...mid] is sorted 
    if arr[l] <= arr[mid]:
 
        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half 
        if key >= arr[l] and key <= arr[mid]:
            return search(arr, l, mid-1, key)
        return search(arr, mid+1, h, key)
 
    # If arr[l..mid] is not sorted, then arr[mid... r]
    # must be sorted
    if key >= arr[mid] and key <= arr[h]:
        return search(a, mid+1, h, key)
    return search(arr, l, mid-1, key)