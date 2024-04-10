#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetro:
medida =  float(input('Digite uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))


