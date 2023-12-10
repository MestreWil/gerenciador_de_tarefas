class Tarefa:
    
    def __init__(self, titulo, descricao, data_criacao = '',   data_conclusao = ''):
        self._titulo =  titulo
        self._descricao = descricao
        self._status = False
        self._data_criacao = data_criacao
        self._data_conclusao =  data_conclusao
   
   #Definições de Propriedade (getters)     
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
    
    #Setters
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
      """
      -> Formata a data de conclusão
      """
      if self._data_conclusao != '':
        dia = self._data_conclusao[0:2]
        mes = self._data_conclusao[2:4]
        ano = self._data_conclusao[4:]
        return f'{dia}/{mes}/{ano}'
      return 'Nao Informado'

    def _formatar_data_criacao(self):
      """
      -> Formata a data de criação
      """
      if self._data_criacao != '':
        dia = self._data_criacao[0:2]
        mes = self._data_criacao[2:4]
        ano = self._data_criacao[4:]
        return f'{dia}/{mes}/{ano}'
      return 'Nao Informado'
    
    def __str__(self):
      """
      -> Mostra do Objeto em formato string
       """
      return f'Título: {self.titulo} | Descrição: {self.descricao} | Status: {self.informa_status()} | Data de Criação: {self._formatar_data_criacao()} | Data de Conclusão: {self._formatar_data_conclusao()}'
    
    def criar_dicionario(self):
      """
      -> Cria um dicionário com as informações da Tarefa
      """
      status = 'Concluido' if self.status is True else 'Pendente'
      return {"Titulo": self.titulo, "Descricao": self.descricao, "Status": status, "Data de Criacao": self._formatar_data_criacao(), "Data de Conclusao": self._formatar_data_conclusao()}
       
    def atualizar_status_tarefa(self):
      """
      -> Atualiza o status da tarefa e coloca a data de conclusão após ser marcada como concluida
      """
      from datetime import datetime
      if self.status is False:
        self.status = True
        hoje = datetime.now()
        dia = hoje.day if len(f'{hoje.day}') == 2 else f'0{hoje.day}'
        self._data_conclusao = f'{dia}{hoje.month}{hoje.year}'
        print(f'Status da TAREFA {self.titulo} alterado para: CONCLUÍDO! No dia {self._formatar_data_conclusao()} ')
      else:
        self._status = False
        self._data_conclusao = 'Nao Informado'
        print(f'Status da TAREFA {self.titulo} alterado para: PENDENTE!')
    
    def atualizar_descricao(self, descricao):
      """
      -> Atualiza a descrição da tarefa
      """
      self.descricao = descricao
      print("Descrição alterada!")
    
    def atualizar_titulo(self, titulo):
      """
      -> Atualiza o titulo da tarefa
      """
      self.titulo = titulo
      print(f'Titulo alterado para: {titulo}')
    
    def atualizar_data_conclusao(self, data_conclusao):
      """
      -> Atualiza a data de conclusão da tarefa
      """
      self.data_conclusao = data_conclusao
      print("Data de Conclusão ATUALIZADA!")
    
    def atualizar_data_criacao(self, data_criacao):
      """
      -> Atualiza a data de criação da tarefa
      """
      self.data_criacao = data_criacao
      print('Data de Criação ATUALIZADA!')
      
    def carrega_data_criacao(self, data_criacao):
      '''
      -> Faz o carregamento da data de criacao do database.json
      '''
      if data_criacao == 'Nao Informado':
        self._data_criacao = ''
      else:
        data = data_criacao.split('/')
        self._data_criacao = data[0] + data[1] + data[2]
        
    def carrega_status(self, status):
      '''
      -> Faz o carregamento do status de criacao do database.json
      '''
      self._status = status == 'Concluido'
      
    def carrega_data_conclusao(self, data_conclusao):
      '''
      -> Faz o carregamento da data de conclusao do database.json
      '''
      if data_conclusao == 'Nao Informado':
        self._data_conclusao = ''
      else:
       data = data_conclusao.split('/')
       self._data_conclusao = data[0] + data[1] + data[2]
