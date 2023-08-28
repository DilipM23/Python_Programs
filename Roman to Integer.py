def roman_integer(roman) :
    roman_dict = {'I':1 , 'V':5 , 'X':10, 'L':50 , 'C':100, 'D':500, 'M':1000}
    romanBack = list(roman)[::-1]
    value = 0
    rightval = roman_dict[romanBack[0]]
    for numeral in romanBack :
        leftval = roman_dict[numeral]
        if leftval < rightval :
            value -= leftval
        else :
            value += leftval
        rightval = leftval
    return value

roman = input("Enter the roman number : ")
value = roman_integer(roman)
print("Integer equivalent of ",roman, " is ", value)