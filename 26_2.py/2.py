# def rec(val):
#     if val>=10:
#         print("stopping the iteration{}.format(val)")
#     else:
#         print("at the iteration{}".format(val))
#         val+=1
#         print("changing the value to {}".format(val))
#         print("*******************")
#         rec(val)

def summation(n):
    if n == 0:
        return 0
    else:
        return n + summation(n-1)


if __name__ == "__main__":
    i = int(input("enter n: "))
    print(summation(i))
