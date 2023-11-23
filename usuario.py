import json
from tarefa import *

class Usuario:
  def __init__(self, nome, email, tarefas):
    self.__nome = nome
    self.__email = email
    self.__tarefas = [tarefas]
  
  def nova_tarefa(self):
    nome_tarefa = str(input('Digite o título da nova tarefa: '))
    descricao_tarefa = str(input('Digite a descrição da tarefa: '))
    data_criação = int(input('Digite a data de '))