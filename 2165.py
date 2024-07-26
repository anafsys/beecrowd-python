T = input()

for char in T:
    caracteres = len(T)
    
if caracteres <= 140:
    print("TWEET")
else:
    print("MUTE")