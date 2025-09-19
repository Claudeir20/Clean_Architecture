# adapters/produtos/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from core.application.use_cases.criar_produtos import CriarProdutosUseCase
from adapters.produtos.repository import DjangoProdutoRepository

class CriarProdutoView(APIView):
    def post(self, request):
        use_case = CriarProdutosUseCase(DjangoProdutoRepository())
        produto = use_case.executar(request.data)
        return Response({
            "nome": produto.nome,
            "preco": produto.preco,
            "estoque": produto.estoque,
            "vendedor_id": produto.vendedor_id
        })
