alimento = int(input('Quantos alimentos ingeriu no dia?'))
caloria = 0

for x in range(alimento):
    caloria += float(input('informar quantidade de calorias do alimento:'))

print(f'a quantidade de calorias ingeridas foi de {caloria} cal')
