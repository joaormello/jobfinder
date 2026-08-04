from app.scrapers.jooble import (buscar_vagas_jooble, normalizar_vaga_jooble)
from app.services.vaga_service import salvar_vaga

dados = buscar_vagas_jooble()

for vaga in dados["jobs"]:

    vaga_normalizada = normalizar_vaga_jooble(vaga)
    salvar_vaga(vaga_normalizada)

    