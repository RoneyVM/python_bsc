# SHELL
# teste_requests_palavras.py
#####################################

####################################
# Implementação Python
# -----------------------------------
# val = []
# retorno = teste_requests_palavras.busca_dados()
# if not retorno:
#     pas
# else:
#     val.append(json.loads(retorno)) 
####################################

import requests

val=[]
def busca_dados():
    response = requests.get("http://191.252.60.124:5000/palavras")
    #print(response)
    #print(response.json())
    for palavras in response.json():
        val.append(palavras)
    print(val)

busca_dados()