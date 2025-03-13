# Projeto Book Shelf

## Funcionalidades

### Autenticação do usuário

- Cadastro de usuário
- Login de usuário

### CRUD de livros

- Cadastro
- Edição
- Busca
- Listagem
- Remoção

## Estrutura do Projeto



O projeto Book Shelf é organizado em uma estrutura modular para facilitar o desenvolvimento, a manutenção e a escalabilidade. A pasta src serve como o núcleo do código-fonte, abrigando tanto a lógica do servidor (backend) quanto a interface do usuário (frontend).

### Pasta backend



A pasta backend é responsável por toda a lógica do servidor, incluindo a manipulação de dados, APIs e integrações com bancos de dados. Sua estrutura é organizada da seguinte forma:

- constants/: Armazena constantes globais que são usadas em diferentes partes do backend.
- db/: Responsável pela interação com o banco de dados. O frontend não interage diretamente com esta pasta.

- schemas/: Define os esquemas de dados e validações.
- services/: Contém a lógica de negócio e serviços específicos.
- tests/: Inclui testes automatizados para garantir a integridade e funcionalidade do código.

### Pasta frontend

A pasta frontend lida com a interface visual do sistema e a experiência do usuário. Ela é estruturada da seguinte maneira:

- assets/: Contém recursos estáticos, como imagens, ícones e fontes.
- components/: Armazena componentes reutilizáveis da interface.
- constants/: Define constantes globais utilizadas no frontend.
- pages/: Contém as páginas principais do sistema. Deve ser importada na main.
- utils/: Funções auxiliares e utilitárias.

[figma](https://www.figma.com/design/xrLJrHbZujpruzcU3WVu6Q/Biblioteca-de-livro?node-id=0-1&t=uGWfxSLcHEIC9Gh8-1)
