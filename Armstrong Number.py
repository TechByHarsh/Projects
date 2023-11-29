# taking inpiut from user 
number = int(input('Enter the number :'))

# making a function 
def check_armstrong(num):
    if num  in range(1,10):
        return True

    order = len(str(num))
    sum = 0

    original = num
    while num > 0 :
        digit = num % 10
        sum += digit ** order
        num = num // 10
    if sum == original:
        return True
    return False
if check_armstrong(number):
    print("number is Armstrong")
else:
    print("number is  not Armstrong")
    
    