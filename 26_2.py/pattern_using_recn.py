#im taking 5 consecusive nums then decremen the last nuum by 2 two times then increment the latest last num 5 times and print each of the incremented nums and build a pattern
def build_pattern(start, rounds):
    
    if rounds == 0:
        return

  
    for i in range(5):
        print(start + i, end=" ")

    last = start + 4

    last -= 2
    print(last, end=" ")

    last -= 2
    print(last, end=" ")

      

    
    new_start = last + 1

    
    build_pattern(new_start, rounds - 1)



build_pattern(1, 3)