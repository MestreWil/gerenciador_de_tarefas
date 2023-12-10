from tarefa import *
from usuario import *
from projeto import *
import json
import os

lista_usuarios = []
lista_projetos = []
# Arquivo que inicia o gerenciador de tarefas, OBS: Crie um usuario ou um projeto antes de criar uma tarefa, 
# pois caso não encaminhe essa tarefa a um usuario ou um projeto essa tarefa será perdida :)

menu = """
=========================================
  Sistema de Gerenciamento de Tarefas
=========================================
    0- Sair
    1- Cadastrar Usuário
    2- Criar Projeto
    3- Criar Tarefa
    4- Lista todos os Usuarios Cadastrados
    5- Lista todos os Projetos Cadastrados 
    6- Marca uma Tarefa como concluída (Usuários)
    7- Marca uma Tarefa como concluída (Projetos)
    8- Mostrar as Tarefas dos Usuários
    9- Mostrar as Tarefas dos Projetos
    """
def salva_json():
  """
  -> Guarda os dados em um arquivo JSON após o encerramento da aplicação
  """
  data = { }

  usuarios = []
  for usuario in lista_usuarios:
    usuario_json = usuario.criar_dicionario()

    tarefas = []
    for tarefa in usuario.tarefas:
      tarefas.append(tarefa.criar_dicionario())

    usuario_json['Tarefas'] = tarefas

    usuarios.append(usuario_json)

  data['usuarios'] = usuarios 
  
  projetos = []
  for projeto in lista_projetos:
    projeto_json = projeto.criar_dicionario()

    tarefas = []
    for tarefa in usuario.tarefas:
      tarefas.append(tarefa.criar_dicionario())

    projeto_json['Tarefas'] = tarefas

    projetos.append(projeto_json)

  data['projetos'] = projetos
  
  json_object = json.dumps(data, indent=2)
  
  with open("database.json", "w") as outfile:
      outfile.write(json_object)
  
def carrega_json():
  '''
  -> Carrega os dados do database.json
  '''
  
  if os.path.isfile("database.json"):
    json_object = {}
    with open('database.json', 'r') as openfile:
      json_object = json.load(openfile)
      
    for usuario_json in json_object['usuarios']:
      usuario = Usuario(usuario_json['Nome'], usuario_json['Email'])

      for tarefa_json in usuario_json['Tarefas']:
        tarefa = Tarefa(tarefa_json['Titulo'], tarefa_json['Descricao'])

        tarefa.carrega_status(tarefa_json['Status'])
        tarefa.carrega_data_criacao(tarefa_json['Data de Criacao'])
        tarefa.carrega_data_conclusao(tarefa_json['Data de Conclusao'])

        usuario.tarefas.append(tarefa)

      lista_usuarios.append(usuario)
      
    for projeto_json in json_object['projetos']:
      projeto = Projeto(projeto_json['Titulo'], projeto_json['Descricao'])

      projeto.carrega_status(projeto_json['Status'])
      projeto.carrega_data_criacao(projeto_json['Data de Criacao'])
      projeto.carrega_data_conclusao(projeto_json['Data de Conclusao'])

      for tarefa_json in projeto_json['Tarefas']:
        tarefa = Tarefa(tarefa_json['Titulo'], tarefa_json['Descricao'])

        tarefa.carrega_status(tarefa_json['Status'])
        tarefa.carrega_data_criacao(tarefa_json['Data de Criacao'])
        tarefa.carrega_data_conclusao(tarefa_json['Data de Conclusao'])

        projeto._tarefas_projeto.append(tarefa)

      lista_projetos.append(projeto)    
    
def novo_usuario():
  """
  -> Cria um novo usuário e joga ele na lista de usuários
  """
  nome = str(input('NOME: '))
  email = str(input('E-MAIL: '))
  print(f'Usuário {nome} Cadastrado')
  return lista_usuarios.append(Usuario(nome, email))
    
def criar_projeto():
  """
  -> Cria um novo projeto e joga ele na lista de projetos
  """
  titulo = str(input('Nome do Projeto: '))
  descricao = str(input('Descrição do Projeto: '))
  data_de_criacao = str(input('Data de Criação (Opcional): '))
  data_de_conclusao = str(input('Data de Conclusão (Opcional): '))   
  print(f'Projeto {titulo} criado')  
  return lista_projetos.append(Projeto(titulo, descricao, data_de_criacao, data_de_conclusao))

def criar_tarefa():
  """
  -> Cria uma nova tarefa
  """
  titulo = str(input('Nome da Tarefa: '))
  descricao = str(input('Descrição da Tarefa: '))
  data_de_criacao = str(input('Data de Criação (dia/mes/ano): '))
  data_de_conclusao = str(input('Data de Conclusão (dia/mes/ano): ')) 
  return Tarefa(titulo, descricao, data_de_criacao, data_de_conclusao)
  
  
def encaminhar_tarefa(tarefa):
  """
  -> Encaminha essa tarefa a um usuário ou a um projeto
  """
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
  """
  -> Lista todos os usuários na lista de usuários
  """
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
  """
  -> Lista todos os projetos na lista de projetos
  """
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
  """
  -> Conclui a tarefa de um usuário na lista de usuários
  """
  listar_usuarios()
  num =  int(input('\nDigite o número do USUÁRIO correspondente: ')) - 1
  lista_usuarios[num].tarefa_concluida()
  
def tarefa_concluida_projeto():
  """
  -> Conclui a tarefa de um projeto na lista de projetos
  """
  listar_projetos()
  num =  int(input('\nDigite o número do USUÁRIO correspondente: ')) - 1
  lista_projetos[num].concluir_tarefa()

def tarefas_dos_usuarios():
  """
  -> Mostra todas as tarefas de um usuário da lista de usuários 
  """
  listar_usuarios()
  num =  int(input('\nDigite o número do USUÁRIO correspondente: ')) - 1
  lista_usuarios[num].todas_tarefas()
  
def tarefas_dos_projetos():
  """
  -> Mostra todas as tarefas de um projeto da lista de projetos
  """
  listar_projetos()
  num =  int(input('\nDigite o número do PROJETO correspondente: ')) - 1
  lista_projetos[num].mostrar_tarefas_no_projeto()

def menu_principal():
  """
  -> Menu que controla a aplicação 
  """ 
  carrega_json()            
  while True:
    print("\n"*10)
    escolha = input(menu + "Escolha: ")
    if escolha == "0":
      salva_json()
      break
    elif escolha == "1":
      novo_usuario()
    elif escolha == "2":
      criar_projeto()
    elif escolha == "3":
      encaminhar_tarefa(criar_tarefa())
    elif escolha == "4":
      listar_usuarios()
    elif escolha == "5":
      listar_projetos()
    elif escolha == "6":
      tarefa_concluida_usuario()
    elif escolha == "7":
      tarefa_concluida_projeto()
    elif escolha == "8":
      tarefas_dos_usuarios()
    elif escolha == "9":
      tarefas_dos_projetos()    
if __name__ == "__main__":
    menu_principal()