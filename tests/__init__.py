import requests

API_KEY = "e823d114494e33199978c3f7b26a698dc4b3"
lang = "pt_br"
cidade = "rio de janeiro"
endpoint = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang={lang}&units=metric"

def test_validacao_status_api():
    r = requests.get(endpoint)

    assert r.status_code == 200
    #print("Teste concluido!")

def test_validacao_cidades_listadas():
    cidade == "rio de janeiro"
    print("Teste concluido! 2")

test_validacao_status_api()
test_validacao_cidades_listadas()


