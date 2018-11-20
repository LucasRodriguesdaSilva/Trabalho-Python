def main():
	#importando os metodos de cada arquivo!
	from consultas import ConsultarCarros
	from consultas import Atrasos
	from datetime import date #importa a data de hoje
	from adicionar import AdicionarVeiculos
	from remover import Remove
	from alugar import Alugar
	from alugar import Trocar
	from devolucao import Devolucao
	from alugar import Ajeita

	hoje = date.today()
	dia = hoje.day
	mes = hoje.month
	ano = hoje.year
	
	#instanciando os metodos
	obj1 = AdicionarVeiculos('marca', 'modelo', 1900, 00000)
	obj2 = ConsultarCarros(0)
	obj3 = Remove(0)
	obj4 = Alugar(0,0,0,0,0,0)
	obj5 = Trocar(0)
	obj6 = Devolucao(0,0)
	obj7 = Ajeita(0)
	atr = Atrasos(0)

	
	

	cont = 0
	op = 1
	avancar = 0
	alugados = 0
	
	
	ler = open('logs1.txt','r')
	ler.seek(0)
	leitura = ler.readline()
	num = open('log.txt','w')
	num.write(leitura)
	ler.close()
	num.close()

	while op < 7 and op > 0:

		contar = open('log.txt','r+')

		contar.seek(0)
		if contar.readline() == '':
			pass

		else:
			contar.seek(0)
			cont = contar.readline()
			contar = open('log.txt','w')
		#abrindo arquivos e contando quantos carros alugados e carros cadastrados tem no arquiv de aluguel e consulta
		dt = open('Aluguel.txt','r')
		quant = dt.read()
		qt = quant.count('Alugado')
		dt = open('Consulta.txt','r')
		quant = dt.read()
		ct = quant.count('Carro')
		dt.close()

		print('\n\n ------------------------------\n Sistema para Locação de Carros \n ------------------------------\n ------------------------------\n Autor: Lucas Rodrigues \n ------------------------------\n\n')


		dataatual = '{}/{}/{}'.format(dia,mes,ano)

		atr.Atrasados(dataatual)

		dt = open('Aluguel.txt','r')
		at = dt.read()
		atrds = at.count('Atrasado')
		dt.close()



		print('\n Data atual:',dataatual)
		if ct < 10:
			print(' Quantidade de veículos cadastrados: 00{}'.format(ct))
		else:
			print(' Quantidade de Veiculos cadastrados: 0{}'.format(ct))
		if qt < 10:
			print(' Quantidade de veículos alugados: 0{}'.format(qt))
		else:
			print(' Quantidade de veículos alugados: ',qt)
		if atrds < 10:
			print(' Quantidade de veículos atrasados: 0{}'.format(atrds))
		else:
			print(' Quantidade de veículos atrasados: ',atrds)


		print('\n Escolha uma opção abaixo digitando o seu numero correspondente!')
		print('\n 1 - Consultar Veiculos', '\n 2 - Adicionar Veiculos', '\n 3 - Alugar / Reservar Veiculos', '\n 4 - Devolver / Liberar Veiculos', '\n 5 - Excluir Veiculos', '\n 6 - Avançar data atual', '\n 7 - Sair')

		op = (int(input('\n Digite a opção desejada: ')))



		if op == 1:
			if (cont == '0') or (cont == 0) or (cont == 00) or (cont == 000) or (cont == ''):
				print('\n\n--> Nenhum carro cadastrado!\n')
			else:

				print('\n')
				obj2.ConsultaSimples()
				aux = (str(input('\nRealizar consulta mais detadalhada S/N: ')))
				if aux == 'S' or aux == 's':
					print('\n')
					obj2.ConsultaAvancada()
				else:
					print('\n')
					pass

		if op == 2:
			cont = int(cont) + 1
			print('\n\n -------------------\n Adicionar Veiculos \n -------------------\n\n')
			obj1.setMarca((input('Digite a marca: ')))
			obj1.setModelo((input('Digite o modelo: ')))
			obj1.setAno((input('Digite o ano: ')))
			obj1.setValor((input('Digite o valor: ')))
			print('\n')
			obj1.Arquivo(cont,ct)
			if ct < 10:
				contar.write('00'+(str(cont)))
			else:
				contar.write('0'+(str(cont)))
			print('\n ------------------------------\n Carro cadastrado com Sucesso! \n ------------------------------\n\n')

		if op == 3:
			obj4.setNome(input('Nome: '))
			prazo = 31

			while prazo > 30:
				prazo = int(input('Digite o prazo de locação: '))
			obj4.setPrazo(prazo)
			print("Digite a data para a reserva/locação do carro(max 30 dias apartir de hoje)!\n")
			obj4.setDia(input('digite o dia: '))
			obj4.setMes(input('digite o mes: '))
			obj4.setAno(input('digite o ano: '))
			cod1 = int(input("digite o codigo do carro: "))
			cod = 'Carro Nº: 00' + str(cod1)
			obj4.setCarro(cod)
			comp = '{}/{}/{}'.format(obj4.getDia(),obj4.getMes(),obj4.getAno())
			
			if comp == dataatual:
				
				objeto = ('Status ' + str(cod1) + ': ' + 'Alugado')
				obj4.Save(objeto,str(cod1))
				obj5.Alterar(objeto,cod)
				print("\nCarro Alugado com Sucesso!")
				
			else:
				
				objeto = ('Status ' + str(cod1) + ': ' + 'Reservado')
				obj4.Save(objeto,str(cod1))
				obj5.Alterar(objeto,cod)
				print("\nCarro Reservado com Sucesso!")
			#comp = obj4.Save()

		if op == 4:
			print('\n1 - Liberar\n2 - Devoluções')
			escolher = int(input('\n Digite a opção desejada: '))
			if escolher == 1:
				a1 = input('Digite o codigo do carro a ser liberado (Somente para carros reservados): ')
				obj6.setCodigo(a1)
				obj6.setData(dataatual)
				obj6.Libera()

			else:
				a1 = input('Digite o codigo do carro a ser devolvido (Somente para carros ja alugados): ')
				obj6.setCodigo(a1)
				obj6.setData(dataatual)
				obj6.Devolve()

		if op == 5:
			i = str(input('Digite o código do carro a ser exluido: '))
			i = 'Carro Nº: ' + i
			obj3.RemoveCarro(i)
			#cont = int(cont) - 1
			#cont = '00'+str(cont)

	
		if op == 6:
			avancar += 1
			futuro = date.fromordinal(hoje.toordinal()+avancar)
			dia = futuro.day
			mes = futuro.month
			ano = futuro.year

			# = '{}/{}/{}'.format(dia,mes,ano)

			


								
		aux = open('logs1.txt','w')
		aux.write(str(cont))
		aux.close()
		contar.close()
	print('\n\n -----------------------------\n Programa fechado com Sucesso! \n -----------------------------\n\n')
		

main()