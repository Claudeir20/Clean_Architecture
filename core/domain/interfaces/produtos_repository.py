from abc import ABC, abstractmethod
from core.domain.entities.produtos import Produto

class ProdutoRepository(ABC):
    @abstractmethod
    def salvar(self, produto: Produto): pass