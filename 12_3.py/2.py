def head(n):
    if n == 0:
        return
    
    head(n-1)
    print(n) #wont call anything or print anything