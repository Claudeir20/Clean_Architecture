from rest_framework.views import APIView
from rest_framework.response import Response
from core.application.use_cases.cadastrar_usuario import CadastrarUsuarioUserCase
from adapters.usuarios.repository import DjangoUsuarioRepository

class CadastrarUsuarioView(APIView):
    def post(self, request):
        use_case = CadastrarUsuarioUserCase(DjangoUsuarioRepository())
        usuario = use_case.executar(request.data)
        return Response({
            "nome": usuario.nome,
            "email": usuario.email,
            "tipo": usuario.tipo
        })
