num = input("Enter the number to check if it is pallindrome or not :")
if num == num[::-1] :
    print("The entered number is pallindrome")
    for i in range(10) :
        if num.count(str(i)) > 0 :
            print(i, " appears ", num.count(str(i)), " times")
else :
    print("The entered number is not a pallindrome")