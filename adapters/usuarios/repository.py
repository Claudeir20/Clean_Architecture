from core.domain.entities.usuarios import Usuario
from core.domain.interfaces.usuarios_repository import UsuarioRepository
from adapters.usuarios.models import UsuarioModel

class DjangoUsuarioRepository(UsuarioRepository):
    def salvar(self, usuario: Usuario):
        UsuarioModel.objects.create(
            nome=usuario.nome,
            email=usuario.email,
            tipo=usuario.tipo
        )

    def buscar_por_email(self, email: str):
        model = UsuarioModel.objects.get(email=email)
        return Usuario(
            nome=model.nome,
            email=model.email,
            senha=model.password,
            tipo=model.tipo
        )