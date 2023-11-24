class Usuario:
  def __init__(self, nome, email):
    self.__nome = nome
    self.__email = email
    self.__tarefas = []
    self.__projetos = []
    self.__gerente = None
  
  