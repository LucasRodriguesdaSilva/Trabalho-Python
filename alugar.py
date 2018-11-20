#metodo para alugar veiculos
class Alugar(object):

	def __init__(self,nome,prazo,dia,mes,ano,carro):
		super(Alugar,self).__init__()
		self.nome = nome
		self.prazo = prazo
		self.dia = dia
		self.mes = mes
		self.ano = ano
		self.carro = carro
	

	def setNome(self,nome):
		self.nome = nome
	def setPrazo(self,prazo):
		self.prazo = prazo
	def setDia(self,dia):
		self.dia = dia
	def setMes(self,mes):
		self.mes = mes
	def setAno(self,ano):
		self.ano = ano
	def setCarro(self,carro):
		self.carro = carro
	
	
	def getNome(self):
		return self.nome
	def getPrazo(self):
		return self.prazo
	def getDia(self):
		return self.dia
	def getMes(self):
		return self.mes
	def getAno(self):
		return self.ano
	def getCarro(self):
		return self.carro
	#salvando em arquivo de texto cada dado passado pelo usuario
	def Save(self,status,cod):
		abrir = open('Aluguel.txt','a')
		new = open('log_de_aluguel.txt','a')
		data = '{}/{}/{}'.format(self.dia,self.mes,self.ano) 
		abrir.write(data + '\n' + self.carro + '\n' + self.nome + '\nPrazo ' + cod +': ' + str(self.prazo) + '\n' + status + '\n\n')
		new.write(data + '\n' + self.carro + '\n' + self.nome + '\nPrazo ' + cod +': ' + str(self.prazo) + '\n' + 'Status ' + cod +': Alugado\n\n')
		new.close()
		abrir.close()
		#return data
#função para trocar os status do carro, esse metodo é chamado em devolução
class Trocar(Alugar):

	def __init__(self,valor):
		self.valor = valor


	def Alterar(self,status,valor):
		abrir = open('Veiculos.txt','r')
		consulta = open('Consulta.txt','r')

		tam = abrir.read()
		abrir.seek(0)

		ler = consulta.read()
		consulta.seek(0)

		pro = valor in tam

		if pro == True:
			for linha in abrir:
				if linha.rstrip() == valor:
					abrir.readline()
					abrir.readline()
					abrir.readline()
					abrir.readline()
					quinta_linha = abrir.readline()
					recebe = tam.replace(quinta_linha,status+'\n')
					abrir = open('Veiculos.txt','w')
					abrir.write(recebe + '\n')
			for linha in consulta:
				if linha.rstrip() == valor:
					consulta.readline()
					terceira_linha = consulta.readline()
					recebe = ler.replace(terceira_linha,status+'\n')
					consulta = open('Consulta.txt','w')
					consulta.write(recebe + '\n')


		consulta.close()
		abrir.close()
#
class Ajeita(Alugar):
	def __init__(self,valor):
		self.valor = valor

	def Ajeitar(self,a,troca):
		abrir = open('Veiculos.txt','r')
		consulta = open('Consulta.txt','r')
		
		tam = consulta.read()
		ler = abrir.read()
		
		
		teste = ''.join(a.split('\n'))

		pro = teste in ler
		if pro == True:
			abrir.seek(0)
			for linha in abrir:
				if linha.rstrip() == teste:
					j =linha.rstrip()
					recebe = ler.replace(j,troca)
					abrir = open('Veiculos.txt','w')
					abrir.write(recebe)
			consulta.seek(0)
			for linha in consulta:
				if linha.rstrip() == teste:
					j = linha.rstrip()
					recebe = tam.replace(j,troca)
					consulta = open('Consulta.txt','w')
					consulta.write(recebe)

		consulta.close()
		abrir.close()

	






