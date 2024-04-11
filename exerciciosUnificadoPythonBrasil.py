# Lista21
def calcularMinimoConsumo(carros, consumo):
    indice=consumo.index(max(consumo))
    return f'Carro mais Econômico: {carros[indice]}'
def exibirOrdemConsumo(carros, consumo):    
    consumoEmOrdem=sorted(consumo, reverse=True)
    carroEmOrdem=[]
    stringRetorno='Relatório Final\n'
    for carro in consumoEmOrdem:
        indice=0
        for carroOrdem in consumo:
            if carro==carroOrdem:
                carroEmOrdem.append(carros[indice])
            indice+=1
    indice=0
    for carro in carroEmOrdem:
        stringRetorno+=f'{indice+1} - {carro} - {consumoEmOrdem[indice]}\n'
        indice+=1
    return stringRetorno
# Funçao 7
def valorPagamento(prestacao, atraso):
    valorDevedor = prestacao
    if atraso > 0:
        diaReferenteAtraso = 0
        while diaReferenteAtraso < atraso:
            jurosPorDia = valorDevedor * (0.1 / 100)
            diaReferenteAtraso += 1
            valorDevedor += jurosPorDia
        valorDevedor += prestacao * 0.03
    return valorDevedor

def impressaoGeralValorPagamento():
    valorDevedorTotal = 0
    totalDeParcelas = 0
    
    while True:
        prestacao = float(input("Informe o valor da prestação (0 para encerrar): "))
        
        if prestacao == 0:
            break
        
        atraso = int(input("Informe a quantidade de dias em atraso: "))
        
        valorDevedor = valorPagamento(prestacao, atraso)
        
        valorDevedorTotal += valorDevedor
        totalDeParcelas += 1
        
        print('------------------------------------------------------------------------------------')
        print(f'Valor base: {prestacao}\nDias de atraso: {atraso}\nValor a ser pago: {valorDevedor}')
        print('------------------------------------------------------------------------------------')

    print('Relatório do dia')
    print(f'Quantidade de parcelas pagas: {totalDeParcelas}')    
    print(f'Valor total de prestações pagas no dia: {valorDevedorTotal}')    

# Classe 9

class Ponto:
    def __init__(self, pontoX, pontoY):
        self.pontoX=pontoX
        self.pontoY=pontoY
    def __repr__(self):
        return "This is object of class A"
    def __str__(self):
        return str(self.__dict__)
    def exibirObjetoPonto(objeto):
        return str(objeto.__dict__) 
class Retangulo(Ponto):
    def __init__(self, larguraRetangulo, alturaRetangulo, pontoX, pontoY):
        Ponto.__init__(self, pontoX, pontoY)
        self.larguraRetangulo=larguraRetangulo
        self.alturaRetangulo=alturaRetangulo
    def centroRetangulo(objetoRetangulo):
        return f'({(objetoRetangulo.larguraRetangulo-objetoRetangulo.pontoX)/2},{(objetoRetangulo.alturaRetangulo-objetoRetangulo.pontoY)/2})'
    
#MenuGeral
def menuClasse():
    objetoPonto=[]
    objetoRetangulo=[]
    while True: 
        opcao = input('\n1 - Criar Objeto Ponto\n2 - Criar Objeto Retangulo\n3 - Calcular Centro Retangulo\nSAIR - Para sair\n>>')
        if opcao=='SAIR':
            break
        elif(opcao!='1' and opcao!='2' and opcao!='3'):
            print(opcao)
            print('opcao invalida')
        else:
            if opcao=='1':
                valorX=float(input('Digite o valor de X:\n>>'))
                valorY=float(input('Digite o valor de Y:\n>>'))
                objetoPonto.append(Ponto(valorX, valorY))
            elif opcao=='2':
                largura=float(input('Digite o valor da largura do retângulo:\n>>'))
                altura=float(input('Digite o valor da largura do retângulo:\n>>'))
                valorX=float(input('Digite o valor de X:\n>>'))
                valorY=float(input('Digite o valor de Y:\n>>'))
                objetoRetangulo.append(Retangulo(largura, altura, valorX, valorY))
            elif opcao=='3':
               print(Retangulo.centroRetangulo(objetoRetangulo[-1]))
        
def menuGeral():
    while True:
        opcaoMenu='1 - Lista - 21\n2 - Função - 7\n3 - Classe - 9\nSAIR - Para Sair\n>>'
        opcao=input(opcaoMenu)
        if opcao=='SAIR':
            break
        elif opcao!='1' and opcao!='2' and opcao!='3':
            print('Opcao Invalida')
        elif opcao=='1':
            carros=['Fusca', 'Gol', 'Vectra','Uno', 'Peugeout']
            consumo=[7.0, 10.0, 9.0, 12.5, 14.5]
            print(f'{calcularMinimoConsumo(carros, consumo)}\n')
            print(exibirOrdemConsumo(carros, consumo))
        elif opcao=='2':
            impressaoGeralValorPagamento()
        elif opcao=='3':
            menuClasse()
        print('\n----------------------------------------------------------------\n')
menuGeral()
