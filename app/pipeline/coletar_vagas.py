from app.scrapers.remotive import(buscar_vagas_remotive, normalizar_vaga)
from app.scrapers.adzuna import (buscar_vagas_adzuna, normalizar_vaga_adzuna)
from app.scrapers.jooble import (buscar_vagas_jooble, normalizar_vaga_jooble)
from app.services.vaga_service import(salvar_vaga, contar_vagas)

def importar_remotive ():
    novas_remotive = 0
    dup_link_remotive = 0 
    dup_conteudo_remotive = 0

    dados = buscar_vagas_remotive()
    vagas = dados["jobs"][:10]
    for vaga in vagas :
        vaga_normalizada = normalizar_vaga(vaga)
        resultado_remotive = salvar_vaga(vaga_normalizada)

        if resultado_remotive == "salva":
            novas_remotive += 1
        elif resultado_remotive == "duplicada_link":
            dup_link_remotive += 1
        elif resultado_remotive == "duplicada_conteudo":
            dup_conteudo_remotive += 1

    print("\nREMOTIVE")
    print(f"Novas: {novas_remotive}")
    print(f"Duplicadas por link: {dup_link_remotive}")
    print(f"Duplicadas por conteúdo: {dup_conteudo_remotive}")  

    

def importar_adzuna():

    novas = 0
    dup_link = 0 
    dup_conteudo = 0

    dados = buscar_vagas_adzuna()
    vagas = dados["results"][:10]

    for vaga in vagas :
        vaga_normalizada = normalizar_vaga(vaga)
        resultado = salvar_vaga(vaga_normalizada)

        if resultado == "salva":
            novas += 1
        elif resultado == "duplicada_link":
            dup_link += 1
        elif resultado == "duplicada_conteudo":
            dup_conteudo += 1

    print("\nADZUNA")
    print(f"Novas: {novas}")
    print(f"Duplicadas por link: {dup_link}")
    print(f"Duplicadas por conteúdo: {dup_conteudo}")  


def importar_jooble():

    novas_jooble = 0
    dup_link_jooble = 0
    dup_conteudo_jooble = 0

    dados = buscar_vagas_jooble()
    vagas = dados["jobs"][:10]

    for vaga in vagas :
        vaga_normalizada = normalizar_vaga_jooble(vaga)
        resultado_jooble = salvar_vaga(vaga_normalizada)

        if resultado_jooble == "salva":
            novas_jooble += 1
        elif resultado_jooble == "duplicada_link":
            dup_link_jooble += 1 
        elif resultado_jooble == "duplicada_conteudo":
            dup_conteudo_jooble += 1

    print("\nJOOBLE")
    print(f"Novas: {novas_jooble}")
    print(f"Duplicadas por link: {dup_link_jooble}")
    print(f"Duplicadas por conteúdo: {dup_conteudo_jooble}")

def executar_pipeline():
    print("Iniciando coleta de vagas...")
    print()

    try:

        importar_remotive()
    except Exception as e :
        print(f"Erro remotive: {e}")
    print()
    try :
        importar_adzuna()
    except Exception as e :
        print(f"Erro Adzuna: {e}")
    print()
    try:
        importar_jooble()
    except Exception as e:
        print(f"Erro Jooble: {e}")
    print()

    print(f"Total de vagas: {contar_vagas()}")

if __name__ == "__main__":
    executar_pipeline()