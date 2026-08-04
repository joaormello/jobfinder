import os 
import requests 
import re

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("JOOBLE_APP_KEY")


def buscar_vagas_jooble():
    url = f"https://jooble.org/api/{API_KEY}"
    payload = {
        "keywords" : "desenvolvedor",
    }

    response = requests.post(url, json=payload)

    return response.json() 


def normalizar_vaga_jooble(vaga):
    return{
        "titulo":vaga.get("title"),
        "empresa":vaga.get("company"),
        "localizacao":vaga.get("location"),
        "tipo_contrato":vaga.get("type"),
        "salario":vaga.get("salary"),
        "link":vaga.get("link"),
        "fonte":"jooble"
    }


def limpar_link(link):

    resultado = re.search(
        r'https://[^\'"< ]+',
        link
    )

    return resultado.group(0) if resultado else link 