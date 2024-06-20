
n = float(input())

phi = (1 + 5 ** 0.5) / 2
fibonacci = (phi**n - (-phi)**(-n)) / (5 ** 0.5) 

print(f"{(fibonacci):.1f}")
    