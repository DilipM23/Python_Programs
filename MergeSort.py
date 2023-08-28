def mergeSort(L1) :
    if len(L1) > 1 :
        mid = len(L1)//2
        left = L1[:mid]
        right = L1[mid:]
        mergeSort(left)
        mergeSort(right)
        i = k = j = 0
        while i < len(left) and j < len(right) : 
            if left[i] < right[j] :
                L1[k] = left[i]
                i += 1
                k += 1
            else :
                L1[k] = right[j]
                j += 1
                k += 1
        while i < len(left) :
            L1[k] = left[i]
            i += 1
            k += 1
        while j < len(right) :
            L1[k] = right[j]
            j += 1
            k += 1

num = int(input("Enter the number of elements to be sorted :"))
print("Enter the elements to be sorted :")
L1 = []
for i in range(num) :
    elem = int(input())
    L1.append(elem)
mergeSort(L1)
print("The sorted array is ", L1)