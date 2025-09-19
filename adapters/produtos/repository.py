from core.domain.entities.produtos import Produto
from core.domain.interfaces.produtos_repository import ProdutoRepository
from adapters.produtos.models import ProdutoMoedl

class DjangoProdutoRepository(ProdutoRepository):
    def salvar(self, produto: Produto):
        ProdutoMoedl.objects.create(
            nome =produto.nome,
            preco = produto.preco,
            estoque = produto.estoque,
            vendedor_id = produto.vendedor_id
    )