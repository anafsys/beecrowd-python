while True:
    try:
        n = int(input())

        if 1001 <= n <= 9998:
            print(n - 1)
    
        if n == 9999:
            print(n - 1)
                
    except EOFError:
        break