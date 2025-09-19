from core.domain.entities.produtos import Produto
from core.domain.interfaces.produtos_repository import ProdutoRepository

class CriarProdutosUseCase:
    def __init__(self, repo: ProdutoRepository):
        self.repo = repo
    
    def executar(self, dados: dict):
        produto = Produto(**dados)
        self.repo.salvar(produto)
        return produto