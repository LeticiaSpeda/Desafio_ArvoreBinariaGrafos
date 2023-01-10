class No:
    
  def __init__(self, valor):
    self.valor = valor
    self.esquerda = None
    self.direita = None

class Arvore:
    def __init__(self) -> None:
        self.raiz = None

    def inserir(self, valor):
        novoNo = No(valor)
        
        if self.raiz == None:
            self.raiz=novoNo
        else:
            atual =  self.raiz
        while True:
            pai = atual
            
            if valor < atual.valor:
                atual=atual.esquerda
            if atual==None:
                pai.esquerda=novoNo
                return
                
            else:
                atual = atual.direita
            if atual == None:
                pai.direita = novoNo
                return
            
    def excluir(self, valor):
        if self.raiz == None:
            print("Arvore está vazia")
            return
            
        atual=self.raiz
        while atual.valor != valor:
            
            if valor<atual.valor:
                atual=atual.esquerda
                
            if valor>atual.valor:
                atual=atual.direita
            if atual==None:
                return False

if __name__ == '__main__':
    arvore = Arvore()

    arvore.inserir(1)
    arvore.inserir(2)
    arvore.inserir(3)
    arvore.inserir(4)

    arvore.excluir(4)
    arvore.excluir(3)
    arvore.excluir(2)