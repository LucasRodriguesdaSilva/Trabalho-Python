# Metodo para cadastrar veiculos no sistema
class AdicionarVeiculos(object):

	def __init__(self,marca,modelo,ano,valor):
	
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.valor = valor
		


	def setMarca(self,marca):
		self.marca = marca

	def setModelo(self,modelo):
		self.modelo = modelo
	
	def setAno(self,ano):
		self.ano = ano

	def setValor(self,valor):
		self.valor = valor


	def getMarca(self):
		return self.marca

	def getModelo(self):
		return self.modelo

	def getAno(self):
		return self.ano

	def getValor(self):
		return self.valor

	#metodo que salva os veiculos em um arquivo de texto
	def Arquivo(self,num,cont):
		arq = open("Veiculos.txt","a")
		arquivo = open("Consulta.txt","a")
		if cont < 10:
			arq.write('Carro Nº: 00'+(str(num)))
		else:
			arq.write('Carro Nº: 0'+(str(num)))
		if cont < 10:
			arquivo.write('Carro Nº: 00'+(str(num)))
		else:
			arquivo.write('Carro Nº: 0'+(str(num)))

		arq.write('\nMarca ' +(str(num))+': ' + self.marca)
		arq.write('\nModelo ' + (str(num)) + ': ' + self.modelo)
		arquivo.write('\nModelo ' + (str(num)) + ': ' + self.modelo)
		arq.write('\nAno ' + (str(num)) + ': ' + self.ano)
		arq.write('\nValor ' + (str(num)) + ': ' + self.valor)
		arq.write('\nStatus ' + (str(num)) + ': '  + 'Disponivel\n\n')
		arquivo.write('\nStatus ' + (str(num)) +': ' + 'Disponivel\n\n')

		arq.close()
		arquivo.close()
