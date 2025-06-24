import requests
import pandas as pd
from datetime import datetime

# Chave ficticia
API_KEY = "e823d114494e33199978c3f7b26a698dc4b3"
lang = "pt_br"

cidades = ['londres', 'são paulo', 'rio de janeiro', 'santiago', 'montevideo', 'buenos aires']

# Lista para armazenar os registros
registros = []

# Loop pelas cidades
for cidade in cidades:
    endpoint = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang={lang}&units=metric"
    resposta = requests.get(endpoint)
    
    if resposta.status_code == 200:
        data = resposta.json()
        record = {
            'cidade': data['name'],
            'pais': data['sys']['country'],
            'latitude': data['coord']['lat'],
            'longitude': data['coord']['lon'],
            'descricao_clima': data['weather'][0]['description'],
            'temperatura': data['main']['temp'],
            'sensacao_termica': data['main']['feels_like'],
            'temp_min': data['main']['temp_min'],
            'temp_max': data['main']['temp_max'],
            'umidade': data['main']['humidity'],
            'pressao': data['main']['pressure'],
            'visibilidade': data.get('visibility', None),
            'vento_velocidade': data['wind']['speed'],
            'vento_direcao': data['wind'].get('deg', None),
            'nuvens_%': data['clouds']['all'],
            'nascer_sol': datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone']).strftime('%H:%M:%S'),
            'por_sol': datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone']).strftime('%H:%M:%S'),
            'ultima_atualizacao': datetime.utcfromtimestamp(data['dt'] + data['timezone']).strftime('%Y-%m-%d %H:%M:%S'),
            'data_carga': datetime.now().strftime('%Y-%m-%d %H:%M:00')
        }
        registros.append(record)
    else:
        print(f"Erro ao buscar dados para {cidade}: {resposta.status_code}")

# Criando o DataFrame
df = pd.DataFrame(registros)

# Exibindo o DataFrame
#print(df)

# Gerar nome do arquivo com data e hora
nome_arquivo = f"clima_cidades_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# Salvar o DataFrame no CSV
df.to_csv(nome_arquivo, index=False)
print(f"Arquivo salvo como: {nome_arquivo}")
