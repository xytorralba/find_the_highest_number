#DEFINE 5 NUMBERS NAMING NUM1, NUM2, NUM3, NUM4, AND NUM5
def find_highest(num1, num2, num3, num4, num5):  
    #IF NUM1 IS GREATER THAN ALL NUMBERS
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5 and num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5:
        return num1
    #IF NUM3 IS GREATER THAN ALL NUMBERS
    elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5 and num3 == num1 or num3 == num2 or num3 == num4 or num3 == num5:
        return num3
    #IF NUM4 IS GREATER THAN ALL NUMBERS
    elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5 and num4 == num1 or num4 == num2 or num4 == num3 or num4 == num5:
        return num4    
    #IF NUM5 IS GREATER THAN ALL NUMBERS
    elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4 and num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
        return num5
    #IF NUM2 IS GREATER THAN ALL NUMBERS:
    else:
        if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5 and num2 == num1 or num2 == num3 or num2 == num4 or num5 == num5:
            return num2
        
#INPUT FIVE NUMBERS
res = find_highest(100,100,2,3,4)
#PRINT THE HIGHEST NUMBER
print(f"Highest number: {res}")