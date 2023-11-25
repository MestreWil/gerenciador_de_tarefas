class Usuario:
  def __init__(self, nome, email):
    self._nome = nome
    self._email = email
    self._tarefas = []
    self._projetos = []
    self._gerente = None
  
  @property
  def nome(self):
    return self._nome
  
  @property
  def email(self):
    return self._email
  
  @property
  def gerente(self):
    return self._gerente