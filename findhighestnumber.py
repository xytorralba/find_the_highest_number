#DEFINE 5 NUMBERS NAMING NUM1, NUM2, NUM3, NUM4, AND NUM5
def find_highest(num1, num2, num3, num4, num5):
    #IF NUM1 IS GREATER THAN NUM2
    if num1 > num2:
        #COMPARE NUM1 TO OTHER NUMBERS
        if num1 > num3:
            return num1
        elif num1 > num4:
            return num1
        elif num1 > num5:
            return num1
        #IF NUM2 IS GREATER THAN NUM1
        else:
            return num2
  
    #IF NUM2 IS GREATER THAN NUM3
    elif num2 > num3:
        #COMPARE NUM2 TO OTHER NUMBERS
        if num2 > num4:
            return num2
        elif num2 > num5:
            return num2
        #IF NUM3 IS GREATER THAN NUM2
        else:
            return num3
        
    #IF NUM3 IS GREATER THAN NUM4
    elif num3 > num4:
        #COMPARE NUM3 TO OTHER NUMBERS
        if num3 > num5:
            return 3
        #IF NUM4 IS GREATER THAN NUM3
        else:
            return num4
    
    else:
        #IF NUM4 IS GREATER THAN NUM5
        if num4 > num5:
            return num4
        #IF NUM5 IS GREATER THAN NUM4
        else:
            return num5

#INPUT FIVE NUMBERS

#PRINT THE HIGHEST NUMBER