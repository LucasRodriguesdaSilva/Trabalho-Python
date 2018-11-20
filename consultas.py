#metodo para consultas de dados dos carros salvos
class ConsultarCarros(object):

	def __init__(self,valor):
		self.valor = valor

	def setValor(self,valor):
		self.valor = valor

	def getValor(self):
		return self.valor

	def ConsultaSimples(self):
		ler = open("Consulta.txt","r")
		ler.seek(0)
		tam = ler.read()
		print('\n -----------------\n Consulta Simples \n -----------------\n')
		print('------------------------------\n\n'+tam+'\n------------------------------')
		ler.close()


	def ConsultaAvancada(self):
		ler = open('Veiculos.txt','r')
		ler.seek(0)
		tam = ler.read()
		print('\n ------------------\n Consulta Avançada \n ------------------\n')
		print('------------------------------\n\n'+tam+'\n------------------------------')
		ler.close()

class Atrasos(ConsultarCarros):
	
	def __init__(self,val):
		self.val = val

	def Atrasados(self,data):
		#print(data)
		from alugar import Ajeita
		obj1 = Ajeita(0)

		abrir = open('log_de_aluguel.txt','r')
		ler = abrir.read()
		abrir.seek(0)

		for linha in abrir:
			if linha.rstrip() < data:
				#print(linha.rstrip())
				if linha.rstrip() != '':
					#print(linha.rstrip())
					carro = abrir.readline()
					newcar = ''.join(carro.split('Carro Nº:'))
					
					i = int(newcar)
					newcar = str(i)
					#print(i)
					nome = abrir.readline()
					prazo = abrir.readline()
					#print(prazo)
					newprazo = ''.join(prazo.split('Prazo '+ newcar +': '))
					#print(newprazo)
					#prazoint1 = int(newprazo) - 1
					prazoint = int(newprazo) - 1
					#prazo1 = str(prazoint)
					
					
					nw = str(prazoint) 
					new = ler.replace(prazo,'Prazo '+newcar+': '+nw+'\n')
					#print (ler)
					if prazoint < 0:
						#print('entrou no if prazo')
						newopen = open('Aluguel.txt','r')
						ler = newopen.read()
						newopen.seek(0)

						status = abrir.readline()
						#print(status)
					
						procurar = 'Alugado' in status
						#print(procurar)
						if procurar == True:
						#print(status)
							a = ''.join(status.split('Alugado\n'))

							#print(a)
							a1 = status.replace(status,a+'Atrasado')
							#print(a1)
							certo = ler.replace(status,a1+'\n')
							#print('----\n\n {} \n-----------\n'.format(ler))
							#print(status)
							#print(certo)
					
							abrir = open('Aluguel.txt','w')
							abrir.write(certo)
							obj1.Ajeitar(status,a1)

							break
					else:
						abrir = open('log_de_aluguel.txt','w')
						abrir.write(new)
						
				else:
					pass
		abrir.close()




		