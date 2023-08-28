# Function to convert binary number to decimal number
def bin_dec(num) :
    rev = num[::-1]
    i=0
    dec = 0
    for dig in rev :
        dec += int(dig) * 2**i
        i += 1
    return dec

# Function to convert octal number to hexa decimal number
def oct_hex(num) :
    num1 = str(num)
    rev = num1[::-1]
    i = 0
    dec = 0
    for dig in rev :
        dec += int(dig) * 8 ** i
        i += 1
    digits = "0123456789ABCDEF"
    X = dec % 16
    res = dec // 16
    if res == 0 :
        return digits[X]
    return oct_hex(res) + digits[X]

bin = input("Enter the binary number to convert it into decimal: ")
res = bin_dec(bin)
print("Decimal equivalent of ", bin, " is ", res )
oct = input("Enter the octal number to convert it into hexa decimal: ")
res = oct_hex(oct)
print("Hexa Decimal equivalent of ", oct, " is ",res )