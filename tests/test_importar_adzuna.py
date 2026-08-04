from app.scrapers.adzuna import (buscar_vagas_adzuna, normalizar_vaga_adzuna)
from app.services.vaga_service import salvar_vaga

dados = buscar_vagas_adzuna()

vagas = dados["results"][:10]

for vaga in vagas:
    vaga_normalizada = normalizar_vaga_adzuna(vaga)
    salvar_vaga(vaga_normalizada)
