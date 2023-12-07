from tarefa import *

lista_usurarios = []

menu = """
=========================================
  Sistema de Gerenciamento de Tarefas
=========================================
    0- Sair
    1- Criar Usuário
    2- 
    3-  
    4- 
    5- 
    """
    
    
def entrada():
  titulo = str(input('Digite o Título da Tarefa: '))
  descricao = str(input('Descreva sua Tarefa: '))
  conclusao = input('Data de Conclusão (Opcional): ').strip()
  tarefas = Tarefa(titulo, descricao, conclusao)
  return tarefas
  
  
def ver_tarefa():
  import json
  print(f'Temos armazenado as seguintes tarefas:')
  for x in lista_tarefas:
    tarefas_armazenadas = json.loads(x)
  for y in tarefas_armazenadas["Titulo"]:
    print(f'{y}')    
    
def menu_principal():            
  while True:
    print("\n"*10)
    escolha = input(menu + "Escolha: ")
    if escolha == "0":
      break
    elif escolha == "1":
      lista_tarefas.append(entrada())
    elif escolha == "2":
      print(f'Existem {len(lista_tarefas)}')
      ver_tarefa()
    elif escolha == "3":
      pass
    elif escolha == "5":
      pass
    
if __name__ == "__main__":
    menu_principal()