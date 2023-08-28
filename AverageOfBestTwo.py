print("Enter the marks of three tests: ")
test1 = float(input())
test2 = float(input())
test3 = float(input())
if test1 < test2 and test1 < test3 :
    print("Average of best of two test marks is :", (test2+test3)/2)
elif test2 < test1 and test2 < test3 :
    print("Average of best of two test marks is :", (test1+test3)/2)
else :
    print("Average of best of two test marks is :", (test1+test2)/2) 