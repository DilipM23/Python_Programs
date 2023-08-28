# Program to count the number of words, uppercase letters, lowercase letters and digits in the sentence
sentence = input("Enter the sentence")
wordcount = sentence.split()
upcount = lowcount = digitcount = 0
for ch in sentence :
    if ch >= '0' and ch <= '9' :
        digitcount += 1
    if ch >= 'a' and ch <= 'z' :
        lowcount += 1
    if ch >= 'A' and ch <= 'Z' :
        upcount += 1

print("Number of words in sentence :",len(wordcount) )
print("Number of uppercase letters :", upcount)
print("Number of lowercase letters : ", lowcount)
print("Number of digits : ", digitcount)