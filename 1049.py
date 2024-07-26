grupo =  {'vertebrado':{'ave': {'carnivoro':'aguia', 'onivoro': 'pomba'}, 
                        'mamifero': {'onivoro': 'homem', 'herbivoro': 'vaca'}}, 
                        'invertebrado': {'inseto': {'hematofago': 'pulga','herbivoro': 'lagarta'}, 
                        'anelideo': {'hematofago': 'sanguessuga', 'onivoro': 'minhoca'}}}

palavra1 = input()
palavra2 = input()
palavra3 = input()

print(grupo[palavra1][palavra2][palavra3])