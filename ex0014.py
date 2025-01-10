# outra forma de calcular -----  tempF = float((9 * tempC) / 5) + 32

tempC = float(input('Informe a temperatura na sua cidade: '))
tempF = (tempC * 1.8) + 32

print('A temperatura de {}Celsius corresponde a {}F'.format(tempC, tempF))
