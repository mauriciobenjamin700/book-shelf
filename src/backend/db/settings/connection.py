import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
from os.path import abspath, dirname, join

# Certifique-se de que você tenha configurado as credenciais do Firebase.

CONFIGS = abspath(join(dirname(__file__), "book-shelf-79ec4-4b2fbaaa62b3.json"))

cred = credentials.Certificate(CONFIGS)
firebase_admin.initialize_app(cred)

db = firestore.client()

def criar_usuario(id, nome, email, senha):
    """Cria um novo usuário no Firestore."""
    agora = datetime.now().isoformat() # Firestore não aceita datetime diretamente
    db.collection(u'users').document(id).set({
        u'id': id,
        u'nome': nome,
        u'email': email,
        u'senha': senha, # Em produção, nunca armazene senhas diretamente!
        u'created_at': agora,
        u'updated_at': agora
    })


def criar_livro(id, nome, autor, paginas, ano, genero, descricao):
    """Cria um novo livro no Firestore."""
    agora = datetime.now().isoformat()
    db.collection(u'books').document(id).set({
        u'id': id,
        u'nome': nome,
        u'autor': autor,
        u'paginas': paginas,
        u'ano': ano,
        u'genero': genero,
        u'descricao': descricao,
        u'created_at': agora,
        u'updated_at': agora
    })


def criar_favorito(id, livro_id, usuario_id):
    """Cria um novo favorito no Firestore."""
    agora = datetime.now().isoformat()
    db.collection(u'favorites').document(id).set({
        u'id': id,
        u'book_id': livro_id,
        u'user_id': usuario_id,
        u'created_at': agora,
        u'updated_at': agora
    })


# Exemplo de uso:
criar_usuario('123', 'João Silva', 'joao@example.com', 'senha123') # Substitua por senhas seguras!
criar_livro('456', '1984', 'George Orwell', 328, '1949', 'Ficção', 'Uma distopia clássica.')
criar_favorito('789', '456', '123')


# Buscar dados:

# Buscar um usuário
usuario = db.collection(u'users').document('123').get()
print(usuario.to_dict())

# Buscar todos os livros (não é recomendado para conjuntos de dados grandes)
livros = db.collection(u'books').stream()
for livro in livros:
    print(livro.to_dict())

# Buscar favoritos de um usuário específico
favoritos = db.collection(u'favorites').where(u'user_id', u'==', '123').stream()
for favorito in favoritos:
    print(favorito.to_dict())

