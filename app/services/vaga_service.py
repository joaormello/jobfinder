from app.database.connection import SessionLocal 
from app.models.vaga import Vaga 

def criar_vaga():
    db = SessionLocal()

    vaga = Vaga(
        titulo = "Desenvolvedor Python",
        empresa = "Enel",
        localizacao = "São Paulo",
        tipo_contrato = "CLT",
        nivel = "Júnior",
        salario = "5000",
        link = "https://exemplo.com/vaga-python"
    )
    db.add(vaga)
    db.commit()

    db.close()
    print("Vaga criada com sucesso !")


def listar_vagas():
    db = SessionLocal()

    try:
        return db.query(Vaga).all()
    finally:
        db.close() 


def buscar_vaga_por_id(vaga_id):
    db = SessionLocal()

    try:
        return db.query(Vaga).filter(
            Vaga.id == vaga_id
            ).first()
    finally:
        db.close()

