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


def salvar_vaga(vaga_dados):
    if vaga_ja_existe(vaga_dados["link"]):
        print("Vaga já cadastrada.")
        return
    db = SessionLocal()

    if vaga_ja_existe_por_conteudo(
        vaga["titulo"],
        vaga["empresa"],
        vaga["localizacao"]
    ):
        print("Vaga duplicada entre fontes.")
        return

    try:
        vaga = Vaga(
            titulo = vaga_dados["titulo"],
            empresa = vaga_dados["empresa"],
            localizacao = vaga_dados["localizacao"],
            tipo_contrato = vaga_dados["tipo_contrato"],
            salario = vaga_dados["salario"],
            link = vaga_dados["link"]
        )
        db.add(vaga)
        db.commit()
        print(f"Vaga '{vaga.titulo}' salva com sucesso!")

    finally:
        db.close()



def vaga_ja_existe(link):
    db = SessionLocal()

    try:
        vaga = db.query(Vaga).filter(
            Vaga.link == link
        ).first()
        return vaga is not None
    finally:
        db.close()

def deletar_vaga(vaga_id):
    db = SessionLocal()

    try:
        vaga = db.query(Vaga).filter(
            Vaga.id == vaga_id
        ).first()

        if vaga :
            db.delete(vaga)
            db.commit()

            print("Vaga removida com sucesso !")
        else :
            print("vaga não encontrada !")
    finally:
        db.close()

def contar_vagas():
    db = SessionLocal()

    try :
        return db.query(Vaga).count()

    finally:
        db.close()



def vaga_ja_existe_por_conteudo (
        titulo, 
        empresa, 
        localizacao
):
    db = SessionLocal()

    try :
        return db.query(Vaga).filter(
            Vaga.titulo == titulo, 
            Vaga.empresa == empresa, 
            Vaga.localizacao == localizacao
        ).first()
    finally:
        db.close()