from app.database.connection import SessionLocal
from app.models.vaga import Vaga

db = SessionLocal()
vagas = db.query(Vaga).all()

for vaga in vagas:
    print(
        f"ID: {vaga.id} |"
        f"Título: {vaga.titulo} |"
        f"Empresa: {vaga.empresa} |"

    )

db.close()