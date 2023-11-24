class Tarefa:
    
    def __init__(self, titulo, descricao, data_criacao = '',   data_conclusao = ''):
        self._titulo =  titulo
        self._descricao = descricao
        self._status = False
        self._data_criacao = data_criacao
        self._data_conclusao =  data_conclusao
        
    @property
    def titulo(self):
      return self._titulo.title()
    
    @property
    def descricao(self):
      return self._descricao
    
    @property
    def status(self):
      return self._status
    
    @property
    def data_conclusao(self):
      return self._data_conclusao
    
    @property
    def data_criacao(self):
      return self._data_criacao
    
    @titulo.setter
    def titulo(self, titulo):
      self._titulo = titulo
      
    @descricao.setter
    def descricao(self, descricao):
      self._descricao = descricao
    
    @status.setter
    def status(self, status):
      self._status = status
    
    @data_criacao.setter
    def data_criacao(self, data_criacao):
      self._data_criacao = data_criacao
        
    @data_conclusao.setter
    def data_conclusao(self, data_conclusao):
      self._data_conclusao = data_conclusao
      
    def informa_status(self):
      if self.status is True:
        return 'Concluido'
      return 'Pendente'
    
    def _formatar_data_conclusao(self):
      if self._data_conclusao != '':
        dia = self._data_conclusao[0:2]
        mes = self._data_conclusao[2:4]
        ano = self._data_conclusao[4:]
        return f'{dia}/{mes}/{ano}'
      return 'Nao Informado'

    def _formatar_data_criacao(self):
      if self._data_criacao != '':
        dia = self._data_criacao[0:2]
        mes = self._data_criacao[2:4]
        ano = self._data_criacao[4:]
        return f'{dia}/{mes}/{ano}'
      return 'Nao Informado'
    
    def criar_tarefa(self):
      status = 'Concluido' if self.status is True else 'Pendente'
      return {"Titulo": self.titulo, "Descricao": self.descricao, "Status": status, "Data de Criacao": self._formatar_data_criacao(), "Data de Conclusao": self._formatar_data_conclusao()}
       
      
    
    def atualizar_status(self):
      from datetime import datetime
      if self.status is False:
        self.status = True
        hoje = datetime.now()
        self._data_conclusao = f'{hoje.day}{hoje.month}{hoje.year}'
        print(f'Status da Tarefa {self.titulo} alterado para: CONCLUÍDO! No dia {self._formatar_data_conclusao()} ')
      else:
        self._status = False
        self._data_conclusao = 'Nao Informado'
        print(f'Status da Tarefa {self.titulo} alterado para: PENDENTE!')
    
    def atualizar_descricao(self, descricao):
      self.descricao = descricao
      return print("Descrição alterada!")
    
    def atualizar_titulo(self, titulo):
      self.titulo = titulo
      return print(f'Titulo alterado para: {titulo}')
    
    def atualizar_data_conclusao(self, data_conclusao):
      self.data_conclusao = data_conclusao
      return print("Data de Conclusão ATUALIZADA!")
    
    def atualizar_data_criacao(self, data_criacao):
      self.data_criacao = data_criacao
      return print('Data de Criação ATUALIZADA!')
    
class Projeto(Tarefa):
  def __init__(self, titulo, descricao, data_criacao = '', data_conclusao = ''):
    super().__init__(titulo, descricao, data_criacao, data_conclusao)
    self._tarefas_projeto = []
    
  def puxar_tarefa(self, tarefa_do_projeto):
    self._tarefas_projeto.append(tarefa_do_projeto)
    return f'Tarefa alocada ao Projeto {self.titulo}'    
    
  def mostrar_tarefas_no_projeto(self):
    pass  
    
tarefa = Tarefa('foda-se', 'foda-se', '10092024') 
print(f'{tarefa.criar_tarefa()}')
tarefa.atualizar_status()
print(f'{tarefa.criar_tarefa()}')     

projeto = Projeto('foda-se', 'foda-se') 
print(f'{projeto.criar_tarefa()}')
projeto.atualizar_status()
print(f'{projeto.criar_tarefa()}') 