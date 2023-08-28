# Function to sort the elements using insertion sort 
def insertionSort(L,n) :
    for i in range(1,n) :
        current = L[i]
        j = i-1
        while L[j] > current and j >= 0 :
            L[j+1] = L[j]
            j -= 1
        L[j+1] = current

num = int(input("Enter the number of elements to be sorted :"))
print("Enter the elements to be sorted :")
L = []
for i in range(num) :
    elem = int(input())
    L.append(elem)
insertionSort(L,num)
print("The sorted array is ", L)