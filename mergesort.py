# Python program for implementation of MergeSort 

# Merges two subarrays of arr[]. 
# First subarray is arr[l..m] 
# Second subarray is arr[m+1..r] 
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = []
    R = []

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted 
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h

        m = round((l + (r - 1)) / 2)

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# Driver code to test above 
# arr = [12, 11, 13, 5, 6, 7]
# n = len(arr)
# print ("Given array is")
# print (arr)

# mergeSort(arr, 0, n - 1)
# print ("\n\nSorted array is")
# print (arr),

# This code is contributed by Mohit Kumra


def mer(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = a[i + l]

    for j in range(0, n2):
        R[j] = a[j + 1 + m]
    print(L)
    print(R)
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
    	if L[i] <= R[j]:
    		a[k] = L[i]
    		i +=1
    	else:
    		a[k] = R[j]
    		j+=1
    	k +=1

    while i < n1:
    	a[k] = L[i]
    	i+=1
    	k+=1
    	
    while j < n1:
    	a[k] = R[j]
    	j+=1
    	k+=1
    
    print(a)
    



def merS(a, l, r):
    if l < r:
        m = int((l + (r - 1)) / 2)
        merS(a, l, m)
        merS(a, m+1, r)
        mer(a, l, m, r)


a = [83, 45, 99, 46, 23, 74, 75, 35]

merS(a, 0, len(a) - 1)