#metodo para remover determinado veiculo
class Remove(object):

	def __init__(self,valor):
		self.valor = valor

	def RemoveCarro(self,op):
		abrir = open('Veiculos.txt','r')
		consultas = open('Consulta.txt','r')

		abrir.seek(0)
		consultas.seek(0)

		tam = abrir.read()
		ler = consultas.read()

		pro = op in tam
		if pro  == True:
			abrir.seek(0)
			for linha in abrir:
				if linha.rstrip() == op:
					a = linha.rstrip()
					recebe = tam.replace(a,'')
					a1 = abrir.readline()
					recebe1 = recebe.replace(a1,'')
					a2 = abrir.readline()
					recebe2 = recebe1.replace(a2,'')
					a3 = abrir.readline()
					recebe3 = recebe2.replace(a3,'')
					a4 = abrir.readline()
					recebe4 = recebe3.replace(a4,'')
					a5 = abrir.readline()
					recebe5 = recebe4.replace(a5,'')
					
					abrir = open('Veiculos.txt','w')
					abrir.write(recebe5 + '\n')

			consultas.seek(0)
			for linha in consultas:
				if linha.rstrip() == op:
					a6 = linha.rstrip()
					recebe6 = ler.replace(a6,'')
					a7 = consultas.readline()
					recebe7 = recebe6.replace(a7,'')
					a8 = consultas.readline()
					recebe8 = recebe7.replace(a8,'')

					consultas = open('consulta.txt','w')
					consultas.write(recebe8 + '\n')	
		else:
			print('\n\n--> Sem dados referente ao carro no Sistema!')

		abrir.close()
		consultas.close()

	
