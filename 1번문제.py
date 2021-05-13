# price :원가, grade : 회원등급
def soulution(price, grade):
    reduced_price = 0
    if grade == "S":
        reduced_price = price * 0.05
    elif grade == "G":
        reduced_price = price * 0.1
    elif grade == "V":
        reduced_price = price * 0.15
    return price - reduced_price

price1 = 2500
grade1= "V"
ret1 = soulution(price1, grade1)
print("solution : return value of the function is", ret1)

price2 = 96900
grade2= "S"
ret2 = soulution(price2, grade2)
print("solution : return value of the function is", ret2, ".")

