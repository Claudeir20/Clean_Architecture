from core.domain.entities.pedidos import Pedido,ItemPedido
from core.domain.interfaces.pedidos_repository import PedidoRepository
class CriarPedidoUseCase:
    def __init__(self, repo: PedidoRepository):
        self.repo = repo
    
    def executar(self, dados: dict) -> Pedido:
        itens = [
            ItemPedido(
                produto_id=item["produto_id"],
                quantidade=item["quantidade"],
                preco_unitario=item["preco_unitario"]
            )
            for item in dados["itens"]
        ]

        pedido = Pedido(
            cliente_id=dados["cliente_id"],
            itens=itens,
            status=dados.get("status", "pendente")
        )

        self.repo.salvar(pedido)
        return pedido