from core.domain.entities.pedidos import Pedido
from core.domain.interfaces.pedidos_repository import PedidoRepository
from .models import PedidoModel

class DjangoPedidoRepository(PedidoRepository):
    def salvar(self, pedido: Pedido):
        PedidoModel.objects.create(
            cliente_id=pedido.cliente_id,
            status=pedido.status,
            total=pedido.total
        )
    
    def buscar_por_cliente(self, cliente_id: int):
        pedidos = PedidoModel.objects.filter(cliente_id=cliente_id)
        return[
            Pedido(
                cliente_id=p.cliente_id,
                itens=[],
                status=p.status
            )
            for p in pedidos
        ]
        