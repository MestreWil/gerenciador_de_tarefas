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
    
    def __str__(self):
      return f'Título: {self.titulo} | Descrição: {self.descricao} | Status: {self.informa_status()} | Data de Criação: {self._formatar_data_criacao()} | Data de Conclusão: {self._formatar_data_conclusao()}'
    
    def criar_dicionario(self):
      status = 'Concluido' if self.status is True else 'Pendente'
      return {"Titulo": self.titulo, "Descricao": self.descricao, "Status": status, "Data de Criacao": self._formatar_data_criacao(), "Data de Conclusao": self._formatar_data_conclusao()}
       
    def atualizar_status_tarefa(self):
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
      self.descricao = descricao
      print("Descrição alterada!")
    
    def atualizar_titulo(self, titulo):
      self.titulo = titulo
      print(f'Titulo alterado para: {titulo}')
    
    def atualizar_data_conclusao(self, data_conclusao):
      self.data_conclusao = data_conclusao
      print("Data de Conclusão ATUALIZADA!")
    
    def atualizar_data_criacao(self, data_criacao):
      self.data_criacao = data_criacao
      print('Data de Criação ATUALIZADA!')

class Projeto(Tarefa):
  def __init__(self, titulo, descricao, data_criacao = '', data_conclusao = ''):
    super().__init__(titulo, descricao, data_criacao, data_conclusao)
    self._tarefas_projeto = []
    
  def receber_tarefa(self, tarefa_do_projeto):
    """
    -> Puxa a tarefa para o Projeto
    """
    print(f"Tarefa {tarefa_do_projeto.titulo} alocada ao Projeto {self.titulo}")
    return self._tarefas_projeto.append(tarefa_do_projeto)    
    
  def mostrar_tarefas_no_projeto(self):
    """
    -> Printar a lista tarefa_projeto
    """
    print('-'*30)
    print(f'TAREFAS DO PROJETO {self.titulo}')
    print('-'*30)
    if len(self._tarefas_projeto) == 0:
      print('Nenhuma TAREFA ALOCADA NESSE PROJETO!')
    else:
      num = 0
      for tarefas_alocadas in self._tarefas_projeto:
        num += 1
        print(f'{num} -> {str(tarefas_alocadas)}')
        
  def concluir_tarefa(self):
    if len(self._tarefas_projeto) == 0:
      print(f'Nenhuma TAREFA no Projeto {self.titulo} no momento!')
    else:
      self.mostrar_tarefas_no_projeto()
      tarefa_concluida = int(input('\nQual tarefa foi concluída? (Digite o número da tarefa)')) - 1
      if tarefa_concluida < len(self._tarefas_projeto):
        self._tarefas_projeto[tarefa_concluida].atualizar_status_tarefa()
      else:
        print('Não existe a essa tarefa!')
  
  def atualizar_status_projeto(self):
      from datetime import datetime
      if self.status is False:
        self.status = True
        hoje = datetime.now()
        dia = hoje.day if len(f'{hoje.day}') == 2 else f'0{hoje.day}'
        self._data_conclusao = f'{dia}{hoje.month}{hoje.year}'
        print(f'Status do PROJETO {self.titulo} alterado para: CONCLUÍDO! No dia {self._formatar_data_conclusao()} ')
      else:
        self._status = False
        self._data_conclusao = 'Nao Informado'
        print(f'Status do PROJETO {self.titulo} alterado para: PENDENTE!')
        
        
        
        
  

# projeto = Projeto('foda-se', 'foda-se')
# print(str(projeto))
# projeto.mostrar_tarefas_no_projeto()    
# tarefa = Tarefa('Jogar um CS', 'foda-se', '10092024')
# tarefa2 =  Tarefa('F1', 'Fumar uma erva', '23042025')
# projeto.puxar_tarefa(tarefa)
# projeto.puxar_tarefa(tarefa2)
# projeto.mostrar_tarefas_no_projeto()
# tarefa.atualizar_status_tarefa()
# projeto.mostrar_tarefas_no_projeto()
# tarefa2.atualizar_status_tarefa()     
# projeto.atualizar_status_projeto()
# print(str(projeto)) 