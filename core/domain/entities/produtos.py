from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int
    vendedor_id: int