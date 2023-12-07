from tarefa import * 
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
  
  @property
  def tarefas(self):
    return self._tarefas
  
  @property
  def projetos(self):
    return self._projetos
  
  @nome.setter
  def nome(self, nome):
    self._nome = nome
    
  @email.setter
  def email(self, email):
    self._email = email
    
  @gerente.setter
  def gerente(self, gerente):
    self._gerente = gerente
     
  @tarefas.setter
  def tarefas(self, tarefas):
    self._tarefas.append(tarefas)
    
  @projetos.setter
  def projetos(self, projetos):
    self._projetos.append(projetos)
    
  def status_gerente(self):
    if self.gerente is True:
      return 'GERENTE'
    return 'USUÁRIO'
  
  def virar_gerente(self):
    self.gerente = True
    print(f'O {self.nome} se torno GERENTE')
  
  def __str__(self):
    return f'Status: {self.status_gerente()} | Nome: {self.nome} | Quantidade de tarefa: {len(self.tarefas)} | Quantidade de Projetos: {len(self.projetos)}'
  
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
  
  def todos_projetos(self):
    print('-'*30)
    print(f'PROJETOS DO {self.nome}')
    print('-'*30)
    if len(self.tarefas) == 0:
      print(f'NENHUM PROJETO para {self.nome} no momento!')
    else:
      num = 0
      for projetos_alocadas in self.projetos:
        num += 1
        print(f'{num} -> {str(projetos_alocadas)}')
  
  def receber_tarefa(self, tarefas):
    self.tarefas.append(tarefas)
    print(f"Tarefa {tarefas.titulo} encaminhada para o {self.status_gerente()}: {self.nome}")
    
  def receber_projeto(self, projeto):
    self.projetos.append(projeto)
    print(f'Projeto')
        
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
          
             
  def criar_tarefas(self):
    if self.gerente is True:
      titulo = str(input('Digite o Título da Tarefa: '))
      descricao = str(input('Descreva sua Tarefa: '))
      conclusao = input('Data de Conclusão (Opcional): ').strip()
      objeto_tarefa = Tarefa(titulo, descricao, conclusao)
      print(f'Tarefa {titulo} criada com SUCESSO!')
      return objeto_tarefa  
    print('Seu Status é de USUÁRIO. Por tanto, não tem autorização para criar TAREFAS')
    
  def criar_projetos(self):
    if self.gerente is True:
      titulo = str(input('Digite o Título da Tarefa: '))
      descricao = str(input('Descreva sua Tarefa: '))
      conclusao = input('Data de Conclusão (Opcional): ').strip()
      objeto_projeto = Projeto(titulo, descricao, conclusao)
      print(f'Projeto {titulo} criada com SUCESSO!')
      return objeto_projeto
    print('Seu Status é de USUÁRIO. Por tanto, não tem autorização para criar PROJETOS')
      
usuario = Usuario('Will', 'will@gmail.com')
print(str(usuario))
tarefa_teste = Tarefa('Foda-se', 'foda-se', '10092024')
print(str(tarefa_teste)) 
usuario.receber_tarefa(tarefa_teste)
usuario.todas_tarefas()
usuario.tarefa_concluida()
usuario.todas_tarefas()
usuario.virar_gerente()
print(str(usuario)) 