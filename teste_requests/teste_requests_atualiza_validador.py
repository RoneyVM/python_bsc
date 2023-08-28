# SHELL
# teste_atualiza_validador.py teste 1
#####################################

####################################
# Implementação Python
# -----------------------------------
# val = []
# retorno = teste_atualiza_validador.atualiza_validador("teste","1")
# if not retorno:
#     pas
# else:
#     val.append(json.loads(retorno)) 
####################################

import requests,sys

serv_name=str(sys.argv[1])
deleta_em=str(sys.argv[2])

def atualiza_validador(serv_name, deleta_em):
    response = requests.post('http://191.252.60.124:5000/validador', json = {"serv_name": ""+serv_name+"","deleta_em": ""+str(deleta_em)+""})

atualiza_validador(serv_name, deleta_em)