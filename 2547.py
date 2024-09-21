while True:
    try:
        n, alt_min, alt_max = map(int,input().split(" "))
        count = 0
        for i in range(n):
            alturas = int(input())
            if alt_min <= alturas <= alt_max:
                count += 1

        print(count) 

    except EOFError:
        break