from app.scrapers.remotive import buscar_vagas_remotive, normalizar_vaga

dados = buscar_vagas_remotive()

vaga = dados["jobs"][0]

print(vaga["url"] == "https://remotive.com/remote-jobs/design/senior-graphic-designer-2091081")

print(vaga["url"])
print(len(vaga["url"]))

for caractere in vaga["url"][:20]:
    print(caractere)