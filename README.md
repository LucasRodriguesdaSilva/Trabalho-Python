# TRABALHO PRÁTICO PYTHON
Trabalho prático de Python sobre locação (aluguel) de veículos.

# <strong>MANUAL DO USUÁRIO</strong>

<strong>ATENÇÃO!!!</strong>

<p> Como se trata de um programa para locação de veículos e de
operações relacionadas (Versão 0.00.1), então pode surgir eventuais bugs no
programa, então sugiro que tente seguir à risca as instruções dadas nesse
manual para evitar eventuais erros.</p>


<h3> MANUAL DO USUÁRIO </h3>

<h4><strong>Atenção:</strong><em> O programa ler e salva os dados em um arquivo de texto que pode ser visto na própria pasta do codigo baixado, e como eles estão salvo no arquivo, se o usuário sair do programa e voltar de novo todo o seu "Progresso" vai estar salvo, a não ser que este o exclua, assim perdendo todos os dados. Com isso exclua somente, se necessário, o conteúdo dos arquivos, e <strong>NÃO</strong> exclua os arquivos de texto.</em></h4>
  
<p> Ao entrar no repositório no site do github, clicaremos em em clonar or download e depois clicaremos em download .zip 
  e assim baixaremos o arquivo .zip
  
  ![baixar](https://user-images.githubusercontent.com/43484645/48741699-2efb8680-ec43-11e8-9e7f-9771efa56644.PNG)

Logo após baixar o arquivo vamos extrair-lo (podendo ser em qualquer lugar que você quiser), com isso vamos entrar na pasta e copiar o caminho do arquivo onde se encontra o codigo.

![caminho](https://user-images.githubusercontent.com/43484645/48741947-25265300-ec44-11e8-8397-1ad5d4604230.PNG)

Assim que copiar o caminho, vamos abrir o Prompt de Comando (cmd) do Windows, e vamos digitar esse trecho de código e apertar em enter:

~~~CMD
cd C:\Users\Jarvis\Desktop\Python-master
~~~

onde C:\Users\Jarvis\Desktop\Python-master é o caminho que você copiou. 

![tela prompt](https://user-images.githubusercontent.com/43484645/48742443-235d8f00-ec46-11e8-818d-e1cee0ada2c9.PNG)

Assim que estivermos dentro da pasta vamos digitar principal.py para iniciar o nosso sistema para locação de carros

![principal](https://user-images.githubusercontent.com/43484645/48742465-33756e80-ec46-11e8-9ff9-05e4c14f6f6b.PNG)

Logo após dar enter em principal.py vai exibir a tela principal do nosso sistema

![tela principal](https://user-images.githubusercontent.com/43484645/48742525-691a5780-ec46-11e8-8b6a-40642ac69d3d.PNG)

Essa tela exibe a data atual conforme a data do sistema operacional do computador, vai exibir a quantidade de veículos cadastrados,
a quantidade de veículos alugados e a quantidade de veículos atrasados. Também vai conter as opções básicas para escolher.

Se escolhermos a opção 1 de consulta de veículos e não tiver nenhum carro cadastrado vai exibir uma mensagem dizendo nenhum carro cadastrado, e assim vai voltar ao inicio do modulo.

![consulta sem dadoos](https://user-images.githubusercontent.com/43484645/48742654-f65dac00-ec46-11e8-9823-7ad2dc497bd7.PNG)

Com isso vamos cadastrar os veículos, digitando a opção 2 iremos para o modulo de cadastro, onde você ira ter que digitar a marca, o modelo, o ano do carro e o valor da diária do carro, e assim que tiver tudo completo vai exibir uma mensagem dizendo que o cadastro foi efetuado com sucesso, como na imagem abaixo.

![cadastro carro](https://user-images.githubusercontent.com/43484645/48743383-07f48300-ec4a-11e8-893a-e6549c90587e.PNG)

Tomando como exemplo dois carros cadastrados, voltamos ao inicio do módulo e logo notaremos que vai estar dizendo que a quantidade de veículos cadastrados vai estar em 002. Assim vamos digitar a opção 1 para consultar os veículos cadastrados.

![consulta com dados](https://user-images.githubusercontent.com/43484645/48743588-d5975580-ec4a-11e8-97cb-bcc277b409a2.PNG)

No modulo vai conter a consulta simples, e logo depois vai exibir uma mensagem perguntando se deseja uma consulta mais detalhada se o usuário digitar S ou s ele vai exibir todos os carros ja cadastrados, se o usuário digitar N ou n o programa volta a tela principal.

Agora vamos digitar a opção 3 para Alugar/Reservar veículos, e vamos reservar um veículo para uma certa data

![reserva](https://user-images.githubusercontent.com/43484645/48743726-75ed7a00-ec4b-11e8-9896-622c14ee6d24.PNG)

Como na imagem acima, o módulo vai pedir o nome do cliente, o prazo, a data para reserva, tendo que digitar o dia, mes e ano e no final o módulo pedi o código do carro para reserva, assim que tiver tudo completo vai aparecer uma mensagem dizendo que a reserva foi feita com sucesso e o programa irá retorna a tela principal.

Com isso vamos escolher a opção 6, assim avançando a data atual para o dia da reserva do carro anteriormente mencionado.

![data adiante](https://user-images.githubusercontent.com/43484645/48743913-59057680-ec4c-11e8-8f66-9da52b69c20d.PNG)

<em>Note que ainda não está constando veículos alugados, isso porque o que fizemos foi uma reserva, agora vamos liberar o carro para ser alugado.</em>

Com o programa no dia que queremos, vamos liberar o veículo e assim ele vai ficar com status de alugado, como na imagem abaixo, escolhemos a opção 4 para liberar/devolver veículos, e logo após digitar a opção, vai aparecer mais duas opções do modulo, um para liberar o carro com reserva, e outra devolver um carro ja alugado. Digitando a primeira opção e digitando o código do carro a ser liberado o sistema ira exibir o nome do cliente e que ele foi liberado com sucesso, e também ao voltar a tela inicial ele vai exibir a quantidade de veículos alugados.

![allugado](https://user-images.githubusercontent.com/43484645/48744096-fd87b880-ec4c-11e8-9e16-19bc1f12b7eb.PNG)

Se caso o módulo liberar/dovolver for escolhido e não tiver nenhuma reserva para a data vai exibir uma mensagem de erro dizendo que não existe nenhuma reserva para tal dia.

![erro](https://user-images.githubusercontent.com/43484645/48744319-ec8b7700-ec4d-11e8-9833-3bec9d852a27.PNG)

E se caso o programa tiver no dia que tiver reserva para tal carro e quando o usuário escolher o módulo liberar/devolver e escolher um carro que nao consta no sistema ele vai exibir uma mensagem de erro dizendo que nao existe tal carro ou ele foi excluido.

![erro nao exite_li](https://user-images.githubusercontent.com/43484645/48744390-36745d00-ec4e-11e8-9ba6-a6eb80749c64.jpg)

E caso o usuário tiver no módulo alugar/reservar e tente alugar um carro para a data atual ele vai ser alugado automaticamente.

![alugado para hoje](https://user-images.githubusercontent.com/43484645/48744444-6e7ba000-ec4e-11e8-8fbb-be57834ed417.PNG)

Caso o cliente queira devolver o veículo alugado, o usuário ira no módulo devolver / liberar, e assim escolher a opção de devolver o programa ira pedir o código do carro, e logo irá exibir o nome do cliente e o valor a pagar, e assim vai exibir que o carro foi devolvido com sucesso.

![devolhj](https://user-images.githubusercontent.com/43484645/48744742-9f100980-ec4f-11e8-8040-e7b530261171.PNG)

Caso o carro alugado passe do prazo que foi digitado no modulo alugar/reservar o sistema irá considerar o veículo como atrasado, se dermos uma consulta o sistema ira mostrar o carro com status atrasado.

![atrasado](https://user-images.githubusercontent.com/43484645/48744839-1b0a5180-ec50-11e8-8bf4-8f3fcb196a46.PNG)

Se ocorrer a devolução com o veículo atrasado o programa irá mostrar o nome do cliente e o valor a pagar com um acréscimo por conta do atraso.

![devolucao com aumento](https://user-images.githubusercontent.com/43484645/48744782-d67eb600-ec4f-11e8-9024-a04217887eb1.PNG)

Em todos os dois casos de devolução o sistema ira deixar o status do carro como disponivel novamente.

![devolvido disponivel](https://user-images.githubusercontent.com/43484645/48744883-42f9b500-ec50-11e8-91d0-6868833d50f1.PNG)

Se o usuário optar por excluir um carro do sistema, ele devera escolher a opção 5.

![excluir](https://user-images.githubusercontent.com/43484645/48744920-74728080-ec50-11e8-9ab8-cbceb8e0530d.PNG)

<em>Note que a quantidade de carros cadastrados diminuiu, isso porque quando o usuário exluir um carro o sitema ja detecta que não tem mais dois carros cadastrados, e sim somente um.</em>

Assim por final se a opção de sair for escolhida o sistema ira mostrar que o programa foi encerrado com sucesso.

![sair](https://user-images.githubusercontent.com/43484645/48744988-c4e9de00-ec50-11e8-918c-132ed8afa095.PNG)

### <strong>REFERÊNCIAS</strong>

https://pythonhelp.wordpress.com/2012/07/10/trabalhando-com-datas-e-horas-em-python-datetime/
https://pt.stackoverflow.com/questions/296286/encontrar-determinado-texto-em-uma-string
https://pt.stackoverflow.com/questions/210225/ler-arquivo-de-texto-e-gerar-listas-para-cada-linha-com-separa%C3%A7%C3%A3o-de-elementos
https://pt.stackoverflow.com/questions/120389/como-remover-caracteres-de-uma-string
https://pt.stackoverflow.com/questions/296286/encontrar-determinado-texto-em-uma-string
## AUTOR: LUCAS RODRIGUES DA SILVA – MATRICULA 428787
