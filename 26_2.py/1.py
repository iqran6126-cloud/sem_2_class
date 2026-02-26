# def show(n):
#     if (n==0):
#         return 1
#     print(n)
#     show(n-1)
#     n=int(input("enter n"))
#     print(show(n))

def rec(val):
    if val==10:
        print("stoping the iterration{}".format(val))
    else:
        print("at the itertion{}".format(val))
        print("*******************")
        rec(val)