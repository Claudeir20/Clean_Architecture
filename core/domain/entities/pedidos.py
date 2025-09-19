class ItemPedido:
    def __init__(self, produto_id, quantidade, preco_unitario):
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def subtotal(self):
        return self.quantidade * self.preco_unitario


class Pedido:
    def __init__(self, cliente_id, itens, status='pendente'):
        self.cliente_id = cliente_id
        self.itens = itens 
        self.status = status
        self.total = self.calcular_total()

    def calcular_total(self):
        return sum(item.subtotal() for item in self.itens)
