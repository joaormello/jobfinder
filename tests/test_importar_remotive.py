from app.scrapers.remotive import (buscar_vagas_remotive, normalizar_vaga)
from app.services.vaga_service import salvar_vaga

dados = buscar_vagas_remotive()
vagas = dados["jobs"][:10]

for vaga in vagas:
    vaga_normalizada = normalizar_vaga(vaga)
    salvar_vaga(vaga_normalizada)