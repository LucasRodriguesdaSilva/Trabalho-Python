#metodo para devolver o veiculo
class Devolucao(object):

	def __init__(self,codigo,data):
		
		self.codigo = codigo
		self.data = data

	def setCodigo(self,codigo):
		self.codigo = codigo
	def setData(self,data):
		self.data = data

	def getCodigo(self):
		return self.codigo
	def getData(self):
		return self.data
#metodo para liberar o carro lendo o arquivo e depois trocando o conteudo pelo status adequado
	def Libera(self):
		from alugar import Ajeita

		obj1 = Ajeita(0)

		abrir = open('Aluguel.txt','r')

		ler = abrir.read()
		abrir.seek(0)
		op = self.data in ler
		if op == True:
			op = self.codigo in ler
			if op == True:
				carro = 'Carro Nº: '+ self.codigo
				abrir.seek(0)
				for linha in abrir:
					if linha.rstrip() == self.data:
						numero = abrir.readline()
						num = ''.join(numero.split('\n'))
						if num == carro:
							nome = abrir.readline()
							print('\n--> Nome do Cliente: ' + nome)
							prazo = abrir.readline()
							status = abrir.readline()
							procura = 'Alugado' in status
							if procura == True:
								print("--> Carro já alugado!")
								break
							else:
								a = ''.join(status.split('Reservado\n'))
								a1 = status.replace(status,a+'Alugado')
								certo = ler.replace(status,a1+'\n')
								abrir = open('Aluguel.txt','w')
								abrir.write(certo)
								#aux = open('log_de_aluguel.txt','w')
								#aux.write(certo)
								#aux.close()
								obj1.Ajeitar(status,a1)
								print('--> Carro liberado com Sucesso!')
								break

						else:
							print('\n--> Erro 03: Nenhum carro reservado para a data de hoje!')
			else:
				print('\n--> Erro 02: Carro inexistente ou exluido!')		
		else:
			print('\n--> Erro 01: Nenhum carro reservado para a data de hoje!')
		abrir.close()
		
#metodo para devolver o veiculo, lendo e trocando o status por disponivel e calculando o valor a ser pago
	def Devolve(self):
		from alugar import Ajeita
		
		obj1 = Ajeita(0)
		

		abrir = open('Aluguel.txt','r')
		consulta = open('Veiculos.txt','r')
		
		ler = abrir.read()
		abrir.seek(0)
		
		op = self.codigo in ler
		if op == True:
			carro = 'Carro Nº: '+ self.codigo
			for linha in abrir:
				if linha.rstrip() == carro:
					nome = abrir.readline()
					prazo = abrir.readline()
					status = abrir.readline()
					procura = 'Disponivel' in status
					if procura == True:
						print('\n--> Cliente: '+nome)
						print('--> Carro já Disponivel!\n')
						break
					else:
						procura = 'Alugado' in status
						if procura == True:
							a = ''.join(status.split('Alugado\n'))
							a1 = status.replace(status,a+'Disponivel')
							certo = ler.replace(status,a1+'\n')
							abrir = open('Aluguel.txt','w')
							abrir.write(certo)
							obj1.Ajeitar(status,a1)
							tam = consulta.read()
							consulta.seek(0)
							pro = carro in tam
							if pro == True:
								for linha in consulta:
									if linha.rstrip() == carro:
										marca = consulta.readline()
										modelo = consulta.readline()
										ano = consulta.readline()
										valor = consulta.readline()
										cod = int(self.codigo)
										cod = str(cod)
										val = ''.join(valor.split('Valor '+cod+': '))
										print('\n--> Cliente: '+nome)
										newprazo = ''.join(prazo.split('Prazo '+cod+': '))
										prazo = int(newprazo)
										valor = int(prazo) * int(val)
										print('--> Valor a pagar: R$ ', valor)
										print('--> Carro devolvido com sucesso!')
										abrir = open('log_de_aluguel.txt','w')
										

										break
						else:
							procura = 'Reservado' in status
							if procura == True:
								print("Carro está Reservado!")
							else:
								procura = 'Atrasado' in status
								if procura == True:
									a = ''.join(status.split('Atrasado\n'))
									a1 = status.replace(status,a+'Disponivel')
									certo = ler.replace(status,a1+'\n')
									abrir = open('Aluguel.txt','w')
									abrir.write(certo)
									obj1.Ajeitar(status,a1)
									tam = consulta.read()
									consulta.seek(0)
									pro = carro in tam
									if pro == True:
										for linha in consulta:
											if linha.rstrip() == carro:
												marca = consulta.readline()
												modelo = consulta.readline()
												ano = consulta.readline()
												valor = consulta.readline()
												cod = int(self.codigo)
												cod = str(cod)
												val = ''.join(valor.split('Valor '+cod+': '))
												print('\n--> Cliente: '+nome)
												newprazo = ''.join(prazo.split('Prazo '+cod+': '))
												prazo = int(newprazo)
												valor = int(val) + (int(prazo) * int(val)) 
												print('--> Valor a pagar com aumento(atraso): R$ ', valor)
												print('--> Carro devolvido com sucesso!')
												abrir = open('log_de_aluguel.txt','w')
											
												break
		else:
			print('\n ---> Erro: carro não existe!')

		abrir.close()