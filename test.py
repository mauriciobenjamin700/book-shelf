from src.backend.db.repositories.user import UserRepository
from src.backend.db.models import UserModel
from src.backend.schemas.user import UserLogin, UserRegister


repository = UserRepository()

email = "mauriciobenjamin700@gmail.com"
password = "Aa1234567-"

response = repository.create(
    UserModel(
        username="Mauricio Benjamin",
        password=password,
        email=email
    )
)

print("CREATE: ", response)

# response = repository.get(
#     data=UserLogin(
#         email=email,
#         password=password
#     )
# )

# print("GET: ", response)

# repository.update(
#     UserRegister(
#         username="ROBES",
#         password=password,
#         email=email
#     )
# )


delete = repository.delete(
    UserLogin(
        email=email,
        password=password
    )
)

print("SUMIU? ", delete)