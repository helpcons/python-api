import requests
import xmltodict
import json
import app

# URL do XML
url = 'https://cdn.lopesrj.com.br/ext/lancamentos.xml'

# Baixa o XML
response = requests.get(url)
xml_data = response.content.decode('utf-8', errors='replace')
xml_data = app.clean_xml(xml_data)

# Converte XML para dicionário
data_dict = xmltodict.parse(xml_data)

# Converte para JSON
json_data = json.dumps(data_dict, indent=2, ensure_ascii=False)

# Salva em um arquivo
with open('imoveis.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

print("Arquivo 'imoveis.json' salvo com sucesso!")
