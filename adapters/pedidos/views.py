from rest_framework.views import APIView
from rest_framework.response import Response
from  core.application.use_cases.pedidos_usecases import CriarPedidoUseCase
from .repository import DjangoPedidoRepository

class CriarPedidoView(APIView):
    def post(self, request):
        use_case = CriarPedidoUseCase(DjangoPedidoRepository())
        pedido = use_case.executar(request.data)
        return Response({
            "cliente_id": pedido.cliente_id,
            "status": pedido.status,
            "total": pedido.total
        })
