def rec_sum(n, current=1):
    
    if current == n:
        print(n, end=" = ")
        return n

    
    print(current, end=" + ")
    return current + rec_sum(n, current + 1)


if __name__ == "__main__":
    n = int(input("enter n: "))
    total = rec_sum(n)
    print(total)