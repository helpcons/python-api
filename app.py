# app.py
from fastapi import FastAPI
import requests
import xmltodict
import re

def clean_xml(xml_str):
    # Remove caracteres de controle inválidos no XML
    return re.sub(r'[^\x09\x0A\x0D\x20-\xFF]|[&]', '', xml_str)

app = FastAPI()

XML_URL = "https://cdn.lopesrj.com.br/ext/lancamentos.xml"  # ⬅️ Substitua pela sua URL real

@app.get("/dados")
def get_dados():
    try:
        response = requests.get(XML_URL)
        response.raise_for_status()
        # xml_data = response.content
        # json_data = xmltodict.parse(xml_data)
        xml_raw = response.content.decode('utf-8', errors='replace')  # ou 'iso-8859-1'
        cleaned_xml = clean_xml(xml_raw)
        json_data = xmltodict.parse(cleaned_xml)

        return json_data
    except Exception as e:
        return {"error": str(e)}
