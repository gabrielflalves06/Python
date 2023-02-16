import random;

menor = 10
maior = 0


for i in range(10): 
    r = random.randint(0,10) 

    if r > maior:
        maior = r
    elif r <= menor:
        menor = r
    
    print(f'{i + 1}º: {r}')


print(f'Maior: {maior}')
print(f'Menor: {menor}')
