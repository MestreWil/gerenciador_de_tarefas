from tarefa import * 
class Usuario:
  def __init__(self, nome, email):
    self._nome = nome
    self._email = email
    self._tarefas = []
  
  @property
  def nome(self):
    return self._nome
  
  @property
  def email(self):
    return self._email
  
  @property
  def tarefas(self):
    return self._tarefas

  
  @nome.setter
  def nome(self, nome):
    self._nome = nome
    
  @email.setter
  def email(self, email):
    self._email = email
     
  @tarefas.setter
  def tarefas(self, tarefas):
    self._tarefas.append(tarefas)
  
  def __str__(self):
    return f'Nome: {self.nome} | E-Mail: {self.email} | Quantidade de tarefa: {len(self.tarefas)}'
  
  def todas_tarefas(self):
    print('-'*30)
    print(f'TAREFAS DO {self.nome}')
    print('-'*30)
    if len(self.tarefas) == 0:
      print(f'Nenhuma TAREFA para {self.nome} no momento!')
    else:
      num = 0
      for tarefas_alocadas in self.tarefas:
        num += 1
        print(f'{num} -> {str(tarefas_alocadas)}')
  
  def receber_tarefa(self, tarefas):
    self.tarefas.append(tarefas)
    print(f"Tarefa {tarefas.titulo} encaminhada para o {self.nome}")
        
  def tarefa_concluida(self):
    if len(self.tarefas) == 0:
      print(f'Nenhuma TAREFA para {self.nome} no momento!')
    else:
      self.todas_tarefas()
      tarefa_concluida = int(input('\nQual tarefa foi concluída? (Digite o número da tarefa)')) - 1
      if tarefa_concluida < len(self.tarefas):
        self.tarefas[tarefa_concluida].atualizar_status_tarefa()
      else:
        print('Não existe a essa tarefa!')
          
    
      
# usuario = Usuario('Will', 'will@gmail.com')
# print(str(usuario))
# tarefa_teste = Tarefa('Foda-se', 'foda-se', '10092024')
# print(str(tarefa_teste)) 
# usuario.receber_tarefa(tarefa_teste)
# usuario.todas_tarefas()
# usuario.tarefa_concluida()
# usuario.todas_tarefas()
# print(str(usuario)) 