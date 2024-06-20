entrada_valores = input()

h,e,a,o,w,x = map(int,entrada_valores.split())

do_bem = h + e + a + x

do_mal = o + w  

if do_bem > do_mal:
    print("Middle-earth is safe.")
if do_bem < do_mal:
    print("Sauron has returned.")
if do_bem == do_mal:
    do_bem += 1
    print("Middle-earth is safe.")    

#1 2 3 10 2 5
#1 2 3 10 2 7

