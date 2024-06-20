# função zip para iterar sobre os dois intervalos simultaneamente.
for i, j in zip(range(1,40,3), range(60,-1,-5)):
    print(f"I={i:<1} J={j:<1}")

    ''' 
    O :2 na string de formatação é usado para garantir que haja pelo menos dois espaços 
    alocados para cada número, proporcionando uma aparência mais organizada quando os 
    números têm apenas um dígito
    
    usei < para alinhar à esquerda cada número em sua respectiva coluna, e 1 para indicar 
    a largura máxima de cada campo. Isso deve manter as colunas alinhadas e eliminar o espaço 
    extra após o sinal de igual.
    '''
      

    #print("J=" + str(j), end=' ')