from abc import ABC, abstractmethod
from core.domain.entities.pedidos import Pedido

class PedidoRepository(ABC):
    @abstractmethod
    def salvar(self, peido: Pedido):
        pass
    @abstractmethod
    def buscar_por_cliente(self, cliente_id: int) -> list[Pedido]:
        pass