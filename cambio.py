'''
request é utilizado para solicitar os dados da internet
json faz a leitura da lista
panda faz a análise estatísticas dos dados
'''
# Informando que as bibliotecas abaixo serão utilizadas na análise de dados
import requests
import json
import pandas

def exportar_tabela(lista_titulos, lista_valores):
    tabela = pandas.DataFrame({'Moedas':lista_titulos, 'Valores':lista_valores})
    print("Exportando tabela CSV...")
    tabela.to_csv("valores.csv", index=False, sep=";",decimal=",")


url = "http://data.fixer.io/api/latest?access_key=8c95b922799dad2957c180474fd061cd"
print("Obtendo URL...")
response = requests.get(url)
if response.status_code == 200:
    print("Acessando base de dados...")
    dados = response.json()
    print(dados['date'])
    dia = dados['date']
    dia = dia[8:10]+"/"+dia[5:7]+"/"+dia[0:4]
    print("Última atualização em ", dia)
    realEuro = dados['rates']['BRL']
    #print("%.3f" % realEuro)
    realDollar = dados['rates']['BRL'] / dados['rates']['USD']
    realDZD = dados['rates']['BRL'] / dados['rates']['DZD']
    realGYD = dados['rates']['BRL'] / dados['rates']['GYD']
    realDJF = dados['rates']['BRL'] / dados['rates']['DJF']
    realBTC = dados['rates']['BRL'] / dados['rates']['BTC']
    #print("%.3f" % realDolar)
    print("Salvando dados da tabela...")

    lista_titulos = ['Euro','Dollar','GYD','DJF','BTC']
    lista_valores = [realEuro, realDollar, realGYD, realDJF, realBTC]
    exportar_tabela(lista_titulos, lista_valores)

    
else:
    print("Houve algum problema com a conexão com a base de dados")