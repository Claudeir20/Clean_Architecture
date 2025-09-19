# Marketplace - Clean Architecture Implementation

Este projeto é uma implementação de um marketplace (sistema de e-commerce) utilizando os princípios da **Arquitetura Limpa (Clean Architecture)** em Python com Django.

## 🏗️ Arquitetura do Projeto

O projeto segue os princípios da Clean Architecture proposta por Robert C. Martin (Uncle Bob), organizando o código em camadas bem definidas e independentes.

### Camadas da Arquitetura

```
┌─────────────────┐
│   Adapters      │  ← Interface com o mundo externo
│   (Django)      │     (Views, Models, URLs)
├─────────────────┤
│  Application    │  ← Casos de uso e lógica de aplicação
│  (Use Cases)    │
├─────────────────┤
│    Domain       │  ← Regras de negócio e entidades
│   (Entities)    │
└─────────────────┘
```

### 1. Domain Layer (`core/domain/`)

**Camada mais interna** - Contém as regras de negócio puras e é independente de qualquer framework ou tecnologia.

#### Entities (`core/domain/entities/`)
- **`Usuario`**: Representa um usuário do sistema
- **`Produto`**: Representa um produto com lógica de estoque
- **`Pedido`** e **`ItemPedido`**: Representam pedidos e seus itens

#### Interfaces (`core/domain/interfaces/`)
- **`UsuarioRepository`**: Contrato para operações de usuário
- **`ProdutoRepository`**: Contrato para operações de produto
- **`PedidoRepository`**: Contrato para operações de pedido

### 2. Application Layer (`core/application/`)

**Camada intermediária** - Contém os casos de uso que orquestram as regras de negócio.

#### Use Cases
- **`CadastrarUsuarioUseCase`**: Lógica para cadastro de usuários
- **`CriarProdutosUseCase`**: Lógica para criação de produtos
- **`CriarPedidoUseCase`**: Lógica para criação de pedidos

### 3. Infrastructure Layer (`adapters/`)

**Camada externa** - Responsável pela implementação das interfaces e comunicação com o mundo externo.

#### Django Apps
- **`adapters.usuarios`**: Implementação Django para usuários
- **`adapters.produtos`**: Implementação Django para produtos
- **`adapters.pedidos`**: Implementação Django para pedidos

## 📁 Estrutura do Projeto

```
market_place3/
├── core/                           # Domain e Application layers
│   ├── domain/
│   │   ├── entities/              # Regras de negócio
│   │   │   ├── usuarios.py
│   │   │   ├── produtos.py
│   │   │   └── pedidos.py
│   │   └── interfaces/            # Contratos de repositório
│   │       ├── usuarios_repository.py
│   │       ├── produtos_repository.py
│   │       └── pedidos_repository.py
│   └── application/
│       └── use_cases/             # Casos de uso
│           ├── cadastrar_usuario.py
│           ├── criar_produtos.py
│           └── pedidos_usecases.py
├── adapters/                      # Infrastructure layer
│   ├── usuarios/
│   │   ├── models.py             # Django models
│   │   ├── views.py              # Django views
│   │   ├── urls.py               # URL routing
│   │   └── repository.py         # Repository implementation
│   ├── produtos/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── repository.py
│   └── pedidos/
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── repository.py
├── project_root/                  # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## 🚀 Funcionalidades

### Usuários
- Cadastro de usuários com diferentes tipos (cliente, vendedor)
- Autenticação via email
- Gerenciamento de perfil

### Produtos
- Cadastro de produtos com controle de estoque
- Associação com vendedores
- Atualização automática de estoque
- Validação de disponibilidade

### Pedidos
- Criação de pedidos com múltiplos itens
- Cálculo automático de totais
- Controle de status do pedido
- Associação com clientes

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Django**: Framework web
- **Django REST Framework**: Para APIs
- **SQLite**: Banco de dados (desenvolvimento)
- **Clean Architecture**: Padrão arquitetural

## 📋 Pré-requisitos

- Python 3.8+
- Django 4.x+
- pip

## 🚀 Instalação e Execução

1. **Clone o repositório**
   ```bash
   git clone <repository-url>
   cd market_place3
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Execute o servidor**
   ```bash
   python manage.py runserver
   ```

6. **Acesse a aplicação**
   - Admin: http://localhost:8000/admin/
   - API: http://localhost:8000/api/

## 🔄 Fluxo de Dados

### Exemplo: Criar um Produto

1. **Request** → `adapters/produtos/views.py`
2. **Controller** → `CriarProdutosUseCase`
3. **Use Case** → `ProdutoRepository`
4. **Repository** → `ProdutoModel` (Django ORM)
5. **Database** → Persistência

### Exemplo: Criar um Pedido

1. **Request** → `adapters/pedidos/views.py`
2. **Controller** → `CriarPedidoUseCase`
3. **Use Case** → Cria `Pedido` e `ItemPedido` entities
4. **Use Case** → `PedidoRepository`
5. **Repository** → `PedidoModel` (Django ORM)

## 🎯 Princípios da Clean Architecture Aplicados

### 1. **Dependência Invertida**
- Camadas externas dependem de camadas internas
- Domain não depende de frameworks
- Interfaces definidas no Domain

### 2. **Independência de Framework**
- Regras de negócio não conhecem Django
- Entities são Puros Python objects
- Use cases independentes de tecnologia

### 3. **Testabilidade**
- Domain pode ser testado sem Django
- Use cases podem ser testados isoladamente
- Repositories podem ser mockados

### 4. **Separação de Responsabilidades**
- Cada camada tem responsabilidade única
- Domain: Regras de negócio
- Application: Fluxo de aplicação
- Infrastructure: Detalhes técnicos

## 🧪 Testes

Para executar os testes:

```bash
python manage.py test
```

## 📝 Padrões de Código

- **PEP 8**: Convenções de estilo Python
- **Type Hints**: Anotações de tipo
- **Docstrings**: Documentação de funções/classes
- **Abstract Base Classes**: Para interfaces

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para detalhes.

## 📞 Contato

Para dúvidas ou sugestões, entre em contato com a equipe de desenvolvimento.

---


