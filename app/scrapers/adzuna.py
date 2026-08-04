import os 
import requests 
from dotenv import load_dotenv
import re

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")


def buscar_vagas_adzuna():

    url = (
        f"https://api.adzuna.com/v1/api/jobs/br/search/1"
        f"?app_id={APP_ID}"
        f"&app_key={APP_KEY}"
        f"&results_per_page=10"
        f"&what=python"
    )
    response = requests.get(url)
    return response.json() 


def normalizar_vaga_adzuna(vaga):
    return{
        "titulo": vaga.get("title"),
        "empresa": vaga.get("company", {}).get("display_name"),
        "localizacao" : vaga.get("location", {}).get("display_name"),
        "tipo_contrato": None, 
        "salario": None,
        "link": vaga.get("redirect_url"),
        "fonte": "adzuna"
    }

def limpar_link(link):

    resultado = re.search(
        r'https://[^\'"< ]+',
        link
    )

    return resultado.group(0) if resultado else link 