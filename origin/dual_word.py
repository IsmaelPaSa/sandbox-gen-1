import random

palabras = [
            'quetzal',
            'library'
            ]

counter = 10000
salto = 1000
buscador = True
abc = 'quet'
limitador = False
limite = 8
mostrador = False
pseudomostrador = True

combinaciones = 0
resultado = ''
elementos = 0
resultados = []
finales = []
totales = []
i = 0
z = 0
y = 0
u = 0
w = 0

for p in palabras:
    combinaciones = combinaciones + len(p)
elementos = len(palabras)
combinaciones = elementos * combinaciones * elementos * combinaciones

while(i < combinaciones):
    i = i + 1
    w = w + 1
    resultado = ''
    for j in range(elementos):
        alpal = random.choice(palabras)
        rango = (len(alpal))
        mir = round(rango / (rango + 1))
        mar = round((rango + rango) - 1)
        alpal = alpal[(random.randrange(mir)):(random.randrange(mar))]
        resultado = resultado + alpal
    if not resultado in totales:
        totales.append(resultado)
        z = z + 1
        if buscador:
            if abc in resultado:
                resultados.append(resultado)
                y = y + 1
                print('encontrado en', i, 'de', combinaciones)
            else:
                combinaciones = combinaciones + 1
    else:
        combinaciones = combinaciones + 1
    if i > counter:
        break
    if w > salto:
        print(i)
        w = 0

if pseudomostrador:
    print('\n ---------- \n')
    for b in range(elementos * elementos * elementos * elementos):
            print(b, totales[b])

if mostrador:
    print('\n ---------- \n')
    for b in range(z):
            print(b, totales[b])

print('\n ---------- \n')
for a in range(z):
        c = totales[a]
        if limitador:
            if len(c) <= limite:
                print(a, c)

if buscador:
    print('\n ---------- \n')
    for b in range(y):
            print(b, resultados[b])

print('\n ---------- \n')
print('combinaciones:', combinaciones)
print('intentos:', i)
print('totales:', z)
print('esperado:', y)