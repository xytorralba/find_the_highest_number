#DEFINE 5 VARIABLES
print("Input five numbers please")
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))
num3 = int(input("3rd number: "))
num4 = int(input("4th number: "))
num5 = int(input("5th number: "))

#IF NUM1 IS GREATER THAN ALL
if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5 and num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5:
    print (f"Highest number is: {num1}")
#IF NUM3 IS GREATER THAN ALL
elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5 and num3 == num1 or num3 == num2 or num3 == num4 or num3 == num5:
    print (f"Highest number is: {num3}")
#IF NUM4 IS GREATER THAN ALL
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5 and num4 == num1 or num4 == num2 or num4 == num3 or num4 == num5:
    print (f"Highest number is: {num4}") 
#IF NUM5 IS GREATER THAN ALL
elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4 and num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
    print (f"Highest number is: {num5}")  
#IF NUM2 IS GREATER THAN ALL
else:
    if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5 and num2 == num1 or num2 == num3 or num2 == num4 or num5 == num5:
        print (f"Highest number is: {num2}")