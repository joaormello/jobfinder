from app.scrapers.jooble import (buscar_vagas_jooble, normalizar_vaga_jooble)

dados = buscar_vagas_jooble()

vaga = dados["jobs"][0]

print(normalizar_vaga_jooble(vaga))