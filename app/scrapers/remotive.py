import requests
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def buscar_vagas_remotive():
    url = "https://remotive.com/api/remote-jobs"

    response = requests.get(
        url,
        verify=False
    )
    return response.json()

def normalizar_vaga(vaga):
    return {
        "titulo": vaga.get("title"),
        "empresa": vaga.get("company_name"),
        "localizacao": vaga.get("candidate_required_location"),
        "tipo_contrato": vaga.get("job_type"),
        "salario" : vaga.get("salary"),
        "link" : vaga.get("url"),
        "fonte": vaga.get("url"),
        "fonte" : "remotive"
    }


def limpar_link(link):

    resultado = re.search(
        r'https://[^\'"< ]+',
        link
    )

    return resultado.group(0) if resultado else link 