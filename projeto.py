from tarefa import Tarefa

# Fiz a herança do objeto tarefa para classe projeto. Já que percebi que ambos possuem as mesmas caracteristicas e metodos
# porém o Projeto tem uma coleção de tarefas correspondentes e possui metodos adicionais. Para isso, utilizei o metodo super para
# puxar as caracteristicas da tarefa no projeto 
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
    """
    -> Marca uma tarefa como concluida
    """
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
    """
      -> Atualiza o status do projeto e coloca a data de conclusão após ser marcada como concluida
      """
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