from abc import ABC, abstractmethod
from core.domain.entities.usuarios import Usuario

class UsuarioRepository(ABC):
    @abstractmethod
    def salvar(self, usuario: Usuario):pass
    
    @abstractmethod
    def buscar_por_email(self, email: str) -> Usuario: pass