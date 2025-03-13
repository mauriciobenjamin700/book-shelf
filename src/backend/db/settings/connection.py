import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


class DatabaseManager:
    def __init__(self):
        self.connection = None
        
        self.connect()
        
    def connect(self):
        if self.connection is None:

            self.connection = db
            
    def disconnect(self):
        if self.connection is not None:
            self.connection = None
    


# Exemplo de uso:
#criar_usuario('123', 'João Silva', 'joao@example.com', 'senha123') # Substitua por senhas seguras!
# criar_livro('456', '1984', 'George Orwell', 328, '1949', 'Ficção', 'Uma distopia clássica.')
# criar_favorito('789', '456', '123')


# # Buscar dados:

# # Buscar um usuário
# usuario = db.collection(u'users').document('123').get()
# print(usuario.to_dict())

# # Buscar todos os livros (não é recomendado para conjuntos de dados grandes)
# livros = db.collection(u'books').stream()
# for livro in livros:
#     print(livro.to_dict())

# # Buscar favoritos de um usuário específico
# favoritos = db.collection(u'favorites').where(u'user_id', u'==', '123').stream()
# for favorito in favoritos:
#     print(favorito.to_dict())

