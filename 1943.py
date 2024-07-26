k = int(input())

if k == 1:
    print("Top 1")
elif k == 2 or k == 3:
    print("Top 3")
elif k == 4 or k == 5:
    print("Top 5") 
elif k >= 6 and k <= 10:
    print("Top 10")
elif k >= 11 and k <= 25:
    print("Top 25")
elif k >= 26 and k <= 50:
    print("Top 50")
elif k >= 51 and k <= 100:
    print("Top 100")