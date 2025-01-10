peso = float(input('Qual o seu peso? (KG):'))
altura = float(input('Qual a sua altura em metros?: '))
IMC = peso / (altura * altura)

print('O seu IMC é de {:.1f}'.format(IMC))

if IMC <= 18.49:
    print('Você está magro, seria bom ganhar alguns musculos!')

elif IMC <= 24.9:
    print('Você está com o IMC NORMAL!')

elif IMC <= 29.9:
    print('Você está com sobrepeso, é melhor se cuidar.')

elif IMC <= 39.9:
    print('Você está em estado de obesidade, deveria procurar um médico.')

else:
    print('Você está com obesidade GRAVE! Deveria agendar uma consulta imediatamente.')
