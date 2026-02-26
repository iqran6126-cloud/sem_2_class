#wapp to check whether a num is odd or even using subtraction method
def check_even_odd(n):
    
    if n < 0:
        n = -n

    
    if n == 0:
        return "Even"
    if n == 1:
        return "Odd"

    
    return check_even_odd(n - 2)


num = int(input("Enter a number: "))
result = check_even_odd(num)
print(result)