'''
request é utilizado para solicitar os dados da internet
json faz a leitura da lista
panda faz a análise estatísticas dos dados
'''
# Informando que as bibliotecas abaixo serão utilizadas na análise de dados
import requests
import json
import pandas

def exportar_tabela(lista_titulo, lista_valores, nome):
    print("Salvando dados da tabela...")
    tabela = pandas.DataFrame({'Moedas':lista_titulo, 'Valores':lista_valores})
    print("Exportando tabela CSV...")
    tabela.to_csv(nome+".csv", index=False, sep=";",decimal=",")
    print("Tabela exportada!")

def chave_acesso(chave="8c95b922799dad2957c180474fd061cd"):
    return "http://data.fixer.io/api/latest?access_key="+chave

def last_update(dia):
    dia = dia[8:10]+"/"+dia[5:7]+"/"+dia[0:4]
    print("Última atualização em ", dia)

def main():
    key = input("Informe a chave de acesso, se não, aperte enter: ")
    url = chave_acesso(key) if len(key) > 0 else chave_acesso()
    print("Obtendo URL...")
    response = requests.get(url)
    if response.status_code == 200:
        print("Acessando base de dados...")
        dados = response.json()
        last_update(dados['date'])
        realDollar = dados['rates']['BRL'] / dados['rates']['USD']
        realBTC = dados['rates']['BRL'] / dados['rates']['BTC']
        moeda = int(input("Digite 1 se quiser saber o valor do Dollar e 2 se quiser saber o valor do Bitcoin ou 3 se quiser saber o valor dos dois: "))
        if moeda == 1:
            exportar_tabela(['Dollar'], [realDollar], 'dollar')
        elif moeda == 2:
            exportar_tabela(['Bitcoin'], [realBTC], 'bitcoin')
        elif moeda == 3:
            exportar_tabela(['Dollar', 'Bitcoin'], [realDollar, realBTC], 'valores')
        else:
            print("Digite um valor válido!")
    else:
        print("Houve algum problema com a conexão com a base de dados")


main()

