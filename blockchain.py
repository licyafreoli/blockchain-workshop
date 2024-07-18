import requests

hash = '00000000000000000000c2cc7cddf5b387529a7e2d7149ace58bb202fbac06af'

url = f'https://blockchain.info/rawblock/{hash}'
resposta = requests.get(url)

dados = reposta.json()
print(f"altura do block: {dados['height']}")
print(f"tempo: {dados['time']}")
print(f"nº de transaçoes: {len(dados['tx'])}")
