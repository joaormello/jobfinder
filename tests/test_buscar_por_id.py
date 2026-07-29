from app.services.vaga_service import buscar_vaga_por_id

vaga = buscar_vaga_por_id(1)

if vaga:
    print(vaga.titulo)
    print(vaga.empresa)
else:
    print("vaga nao encontrada")