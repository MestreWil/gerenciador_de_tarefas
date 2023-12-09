from tarefa import *
from usuario import *

lista_usuarios = []
lista_projetos = []

menu = """
=========================================
  Sistema de Gerenciamento de Tarefas
=========================================
    0- Sair
    1- Cadastrar Usuário
    2- Criar Projeto
    3- Criar Tarefa 
    4- Marca uma Tarefa como concluída (Usuários)
    5- Marca uma Tarefa como concluída (Projetos)
    6- Mostrar as Tarefas dos Usuários
    7- Mostrar as Tarefas dos Projetos
    """
    
    
def novo_usuario():
  nome = str(input('NOME: '))
  email = str(input('E-MAIL: '))
  print(f'Usuário {nome} Cadastrado')
  return lista_usuarios.append(Usuario(nome, email))
    
def criar_projeto():
  titulo = str(input('Nome do Projeto: '))
  descricao = str(input('Descrição do Projeto: '))
  data_de_criacao = str(input('Data de Criação (dia/mes/ano): '))
  data_de_conclusao = str(input('Data de Conclusão (dia/mes/ano): '))   
  print(f'Projeto {titulo} criado')  
  return lista_projetos.append(Projeto(titulo, descricao, data_de_criacao, data_de_conclusao))

def criar_tarefa():
  titulo = str(input('Nome da Tarefa: '))
  descricao = str(input('Descrição da Tarefa: '))
  data_de_criacao = str(input('Data de Criação (dia/mes/ano): '))
  data_de_conclusao = str(input('Data de Conclusão (dia/mes/ano): ')) 
  return Tarefa(titulo, descricao, data_de_criacao, data_de_conclusao)
  
  
def encaminhar_tarefa(tarefa):
  para_user = input('Essa tarefa está direcionada a algum usuário? [S/N] ').strip()[0]
  if para_user in 'Ss':
    listar_usuarios()
    num = int(input('\nDigite o número do USUÁRIO correspondente: ')) - 1
    lista_usuarios[num].receber_tarefa(tarefa)
  else:
    para_projetos = input('Essa tarefa está direcionada a algum projeto? [S/N] ').strip()[0]
    if para_projetos in 'Ss':
      listar_projetos()
      num = int(input('\nDigite o número do Projeto correspondente: ')) - 1
      lista_projetos[num].receber_tarefa(tarefa)
      
def listar_usuarios():
  if len(lista_usuarios) == 0:
    print('Nenhum Usuário Cadastrado até o momento!')
  else:
    num = 0
    print('-'*23)
    print('| USUÁRIOS CADASTRADOS |')
    print('-'*23)
    for usuarios in lista_usuarios:
      num += 1
      print(f'{num} -> {str(usuarios)} ')

def listar_projetos():
  if len(lista_projetos) == 0:
    print('Nenhum Projeto Criado até o momento!')
  else:
    num = 0
    print('-'*23)
    print('| PROJETOS CADASTRADOS |')
    print('-'*23)
    for projeto in lista_projetos:
      num += 1
      print(f'{num} -> {str(projeto)} ')
      
def tarefa_concluida_usuario():
  listar_usuarios()
  num =  int(input('\nDigite o número do USUÁRIO correspondente: ')) - 1
  lista_usuarios[num].tarefa_concluida()
  
def tarefa_concluida_projeto():
  listar_projetos()
  num =  int(input('\nDigite o número do USUÁRIO correspondente: ')) - 1
  lista_projetos[num].concluir_tarefa()

def tarefas_dos_usuarios():
  listar_usuarios()
  num =  int(input('\nDigite o número do USUÁRIO correspondente: ')) - 1
  lista_usuarios[num].todas_tarefas()
  
def tarefas_dos_projetos():
  listar_projetos()
  num =  int(input('\nDigite o número do PROJETO correspondente: ')) - 1
  lista_projetos[num].mostrar_tarefas_no_projeto()

def menu_principal():            
  while True:
    print("\n"*10)
    escolha = input(menu + "Escolha: ")
    if escolha == "0":
      break
    elif escolha == "1":
      novo_usuario()
    elif escolha == "2":
      criar_projeto()
    elif escolha == "3":
      encaminhar_tarefa(criar_tarefa())
    elif escolha == "4":
      tarefa_concluida_usuario()
    elif escolha == "5":
      tarefa_concluida_projeto()
    elif escolha == "6":
      tarefas_dos_usuarios()
    elif escolha == "7":
      tarefas_dos_projetos()    
if __name__ == "__main__":
    menu_principal()