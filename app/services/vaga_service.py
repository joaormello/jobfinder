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