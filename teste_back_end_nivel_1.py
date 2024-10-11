#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS

#Faça o teste abaixo 100% sozinho, sem a ajuda de CHAT GPT, amigos, familiares, professores ou etc.. conseguimos facilmente identificar

#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico

#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra
response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]


for loja in response:
    loja["produtos"] = [produto for produto in loja["produtos"] if produto["preço"] < 30]

print(response[0])

# Eu escolhi essa solução, porque esse laço for faz a iteração das lojas e através da compressão da lista de produtos com a condição if, loja["produtos"] recebe a lista com os dicionários  dos produtos que custam menos de 30 reais. Portanto, essa solução é otimizada e eficiente.


#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}


for produto in responsejson["produtos"]:
    if produto["nome"] == "Produto B":
        preco_produto_b = produto["preço"]
        break

# Eu escolhi essa solução, porque utilizando esse laço for, é possível iterar cada produto dentro da lista do JSON e se os houverem mais produtos no JSON, o código verifica o preço de um Produto X, no  caso dessa questão é o Produto B. Ao encontrar o preço desejado, o break interrompe o laço for para evitar verificações desnecessárias.


#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]

lista.sort()

# Escolhi usar o método sort(), porque esse método altera a lista original e é mais eficiente em relação a memória comparado a outra possível solução: a função sorted() que não altera a lista original, apenas retorna uma nova lista ordenada.


#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela

lista = ["   joao   ","   maria   ","  joana  "]

lista_nova = []
for nome in lista:
    lista_nova.append(nome.strip())


#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]

lista.pop(1)
print(lista)


#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

for i in range(len(lista)):
    if lista[i] == "joao":
        lista[i] = "maria"


#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]
i = 0

while i < len(lista) and i <= 5:
    print(lista[i])
    i += 1

# Eu escolhi essa solução, porque com o while verificando se o índice é menor que o tamanho da lista e menor ou igual a 5, não é necessário utilizar uma condição if e aumentar o código. Dessa forma, o código fica mais simplificado e eficiente.


#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra

import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")

if response.status_code == 200:
    tasks = response.json()
    completadas = 0
    nao_completadas = 0
    total_tasks = {}
    
    for task in tasks:
        if task['completed']:
            completadas += 1
        else:
            nao_completadas += 1
    
    total_tasks['completadas'] = completadas
    total_tasks['nao completadas'] = nao_completadas

    print(f"Tasks completadas: {total_tasks['completadas']}")
    print(f"Tasks pendentes: {total_tasks['nao completadas']}")

else:
    print(f"Erro: {response.status_code}")


# Eu escolhi essa solução, pois esse laço for permite que ele itere em todos as chaves e verifique se a task o 'completed' é verdadeiro ou falso. Essa foi a solução mais eficiente e otimzada que cosnegui desenvolver.  


#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if  response.status_code == 200:
    usuarios = response.json()
    
    dados_usuarios = []
    
    for usuario in usuarios:
        dados_usuarios.append(
            {
                "nome": usuario["name"],
                "username": usuario["username"],
                "email": usuario["email"],
                "rua": usuario["address"]["street"],
                "numero": usuario["address"]["suite"]
            }
        )

# Eu escolhi essa solução, pois com esse laço for iterando pelos usuários e armazenando os dados em um dicionário, permite posteriomente uma simples manipulação dos dados, além de facilitar a adição de campos no futuro e garantir que não haja conflitos com os dados do JSON. 


#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

cores = []
cores.append("azul")
cores.append("verde")
cores.append("vermelho")
cores.append("amarelo")

cores.pop(0)


#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO

cores = []
cores.append("azul")
cores.append("verde")
cores.append("vermelho")
cores.append("amarelo")

cores.pop()


#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta

class Conta():
    cont_id = 1
    
    def __init__(self, nome='', cpf=0):
        self.id = Conta.cont_id
        Conta.cont_id += 1
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        
        
    def depositar(self, valor=0):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso. O seu novo saldo é R${self.saldo:.2f}.')
        else:
            print('Erro! O valor de depósito deve ser positivo.')


    def sacar(self, valor=0):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'\nSaque de R${valor:.2f} realizado com sucesso. O seu novo saldo é R${self.saldo:.2f}.')
        else:
            print('\nErro! Verifique o valor.')

    
    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, CPF: {self.cpf}, Saldo: R$ {self.saldo:.2f}"


class Banco():
    
    def __init__(self):
        self.contas = []
        
        
    def verificarInteiro(self, valor=0):
        try:
            return int(valor)
        
        except ValueError:
            print('\nErro! O valor deve ser um número inteiro.')
            return None
        
                
    def criarConta(self, nome='', cpf=0):
        nova_conta = Conta(nome, cpf)
        self.contas.append(nova_conta)
        print('\nConta criada com sucesso!')
        
    
    def buscarConta(self, id_conta=0):
        id_conta_int = self.verificarInteiro(id_conta)
        if id_conta_int is not None:
            for conta in self.contas:
                if conta.id == id_conta_int:
                    return conta
            return None


def main():
    
    banco = Banco()
    
    menu = 1 # ligado

    while menu == 1:
        
        print('\n')
        print("-=" * 20)
        print("\n'SISTEMA DO BANCO X'\n")
        print('[1] - Criar Conta')
        print('[2] - Depositar')
        print('[3] - Sacar')
        print('[4] - Sair\n')
        print("-=" * 20)

        opcao = input('\nEscolha uma opção: ')
        
        escolha_int = banco.verificarInteiro(opcao)
        if 0 < escolha_int <= 4 and escolha_int is not None:
            print('\nOpção escolhida válida!')
            
        opcao_int = banco.verificarInteiro(opcao)
        
        match opcao_int:
            case 1: # criar conta
                nome = input('\nDigite seu nome: ')
                cpf = input('Digite seu CPF: ')
                banco.criarConta(nome, cpf)
                
            case 2: # depostiar
                id_conta = int(input("\nDigite o ID da conta: "))
                conta = banco.buscarConta(id_conta)
                if conta:
                    valor = float(input("Digite o valor do depósito: "))
                    conta.depositar(valor)
                else:
                    print("\nErro! Conta não encontrada.")
                    
            case 3: # sacar
                id_conta = input("\nDigite o ID da conta: ")
                
                conta = banco.buscarConta(id_conta)
                if conta:
                    valor = float(input("Digite o valor do saque: "))
                    conta.sacar(valor)
                else:
                    print("\nErro! Conta não encontrada.")
                
            case 4: # sair
                print('\nFechando o sistema...')
                break
                
            case _:
                print('\nErro! Digite uma opção válida.')

if __name__ == "__main__":
    main()








