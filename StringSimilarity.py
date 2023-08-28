# Function to compare two strings for similarity
def compare(str1, str2) :
    length = min(len(str1),len(str2))
    count = 0
    for i in range(length):
        if str1[i] == str2[i] :
            count += 1
    return count

str1 = input("Enter the first string")
str2 = input("Enter the second string")
count = compare(str1, str2)
maximum = max(len(str1), len(str2))
print("Number of letters matched : ", count)
print("String similarity is ", count/maximum * 100, "%")