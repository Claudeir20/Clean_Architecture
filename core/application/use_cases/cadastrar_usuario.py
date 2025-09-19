from core.domain.entities.usuarios import Usuario
from core.domain.interfaces.usuarios_repository import UsuarioRepository

class CadastrarUsuarioUserCase:
    def __init__(self, repo: UsuarioRepository):
        self.repo = repo
        
    def executar(self, dados: dict):
        usuario = Usuario(**dados)
        self.repo.salvar(usuario)
        return usuario