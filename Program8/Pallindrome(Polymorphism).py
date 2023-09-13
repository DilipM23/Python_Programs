class StringPallindrome:
    def __init__(self):
        self.ispali = False
    
    def checkPallindrome(self,mystr):
        if mystr == mystr[::-1]:
            self.ispali = True
        else :
            self.ispali = False 
        return self.ispali
    
class IntegerPallindrome(StringPallindrome):
    def chechPallindrome(self,val):
        temp = val
        rev = 0
        while temp != 0 :
            dig = temp % 10
            rev = (rev*10) + dig
            temp = temp // 10
        
        if val == rev :
            self.ispali = True 
        else :
            self.ispali = False
        return self.ispali
    
mystr = input("Enter the string to check if it is pallindrome or not")
str = StringPallindrome()
if str.checkPallindrome(mystr):
    print("Enter string is a pallindrome")
else :
    print("It is not a pallindrome")
myint = int(input("Enter the number to check if it is pallindrome or not"))
inte = IntegerPallindrome()
if inte.chechPallindrome(myint):
    print("Enter integer is a pallindrome")
else :
    print("It is not a pallindrome")