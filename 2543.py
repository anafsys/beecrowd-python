while True:
    try:
        n,id1 = map(int,input().split(" "))

        cs = 0
        
        for i in range(n):
            id2,j = map(int,input().split(" "))
            
            if id2 == id1 and j == 0:
                cs += 1
            
        print(cs)
    
    except EOFError:
        break
