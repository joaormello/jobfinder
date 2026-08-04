from app.scrapers.remotive import (buscar_vagas_remotive, normalizar_vaga)
from app.services.vaga_service import salvar_vaga


dados = buscar_vagas_remotive()
primeira_vaga = dados["jobs"][0]

vaga_noramlizada = normalizar_vaga(primeira_vaga)
salvar_vaga(vaga_noramlizada)