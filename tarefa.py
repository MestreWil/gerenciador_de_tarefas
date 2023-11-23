class Tarefa:
    
    def __init__(self, titulo, descricao,  data_conclusao = 'Nao Informado'):
        self.__titulo =  titulo
        self.__descricao = descricao
        self.__status = False
        self.__data_conclusao =  data_conclusao
        
    @property
    def titulo(self):
      return self.__titulo.title()
    
    @property
    def descricao(self):
      return self.__descricao
    
    @property
    def status(self):
      return self.__status
    
    @property
    def data_conclusao(self):
      return self.__data_conclusao
    
    @titulo.setter
    def titulo(self, titulo):
      self.__titulo = titulo
      
    @descricao.setter
    def descricao(self, descricao):
      self.__descricao = descricao
    
    @status.setter
    def status(self, status):
      self.__status = status
      
    @data_conclusao.setter
    def data_conclusao(self, data_conclusao):
      self.__data_conclusao = data_conclusao
      
    @staticmethod
    def data_criacao():
      from datetime import datetime
      hoje = datetime.now()
      return f'{hoje.day}/{hoje.month}/{hoje.year}'
    
    def informa_status(self):
      if self.status is True:
        return 'Concluido'
      return 'Pendente'
    
    def __formatar_data_conclusao(self):
      if self.__data_conclusao != '':
        dia = self.__data_conclusao[0:2]
        mes = self.__data_conclusao[2:4]
        ano = self.__data_conclusao[4:]
        return f'{dia}/{mes}/{ano}'
      return 'Nao Informado'

    def criar_tarefa(self):
      import json
      status = 'Concluido' if self.status is True else 'Pendente'
      dic_tarefa = {"Titulo": self.titulo, "Descricao": self.descricao, "Status": status, "Data de Criacao": self.data_criacao(), "Data de Conclusao": self.__formatar_data_conclusao()}
      return json.dumps(dic_tarefa)
      
    
    def atualizar_status(self):
      from datetime import datetime
      if self.status is False:
        self.status = True
        hoje = datetime.now()
        self.__data_conclusao = f'{hoje.day}{hoje.month}{hoje.year}'
        print(f'Status da Tarefa {self.titulo} alterado para: CONCLUÍDO! No dia {self.__formatar_data_conclusao()} ')
      else:
        self.__status = False
        self.__data_conclusao = f'Nao Informado'
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
    


    
tarefa = Tarefa('foda-se', 'foda-se', '10092024') 
print(f'{tarefa.criar_tarefa()}')
tarefa.atualizar_status()
print(f'{tarefa.criar_tarefa()}')     
