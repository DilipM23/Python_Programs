def fn(N) :
    if N == 1 :
        return 0
    elif N == 2 :
        return 1
    else :
        return fn(N-1) + fn(N-2)

N = int(input("Enter a number greater than zero :"))
if N > 0 :
    print("The value after evaluation is ",fn(N))
else :
    print("The entered number is greater than or equal to zero")   