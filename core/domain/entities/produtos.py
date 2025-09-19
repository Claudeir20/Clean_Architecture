
class Produto:
    def __init__(self, nome, preco, estoque, vendedor_id):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.vendedor_id = vendedor_id
    
    def atualizar_estoque(self, quantidade):
        if self.estoque + quantidade < 0:
            raise ValueError("Estoque insuficiente")
        self.estoque += quantidade
