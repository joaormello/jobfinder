from app.scrapers.remotive import(buscar_vagas_remotive, normalizar_vaga)
from app.scrapers.adzuna import (buscar_vagas_adzuna, normalizar_vaga_adzuna)
from app.services.vaga_service import(salvar_vaga, contar_vagas)

def importar_remotive ():
    dados = buscar_vagas_remotive()
    vagas = dados["jobs"][:10]
    for vaga in vagas :
        vaga_normalizada = normalizar_vaga(vaga)
        salvar_vaga(vaga_normalizada)

    print('Importação Remotive finalizada !')

def importar_adzuna():
    dados = buscar_vagas_adzuna()
    vagas = dados["results"][:10]

    for vaga in vagas :
        vaga_normalizada = normalizar_vaga_adzuna(vaga)
        salvar_vaga(vaga_normalizada)
    print("Importação Adzuna finalizada")

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

    print(f"Total de vagas: {contar_vagas()}")

if __name__ == "__main__":
    executar_pipeline()