from threading import Thread
from web3 import Web3
import time
import requests
import config
import sys, os, json,  random
import array_palavras
import itertools
import f_mnemonic_v2,f_mnemonic_v1
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import socket

hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   

var1=int(sys.argv[1])
var12=int(sys.argv[2])

id = config.id
serv_name = config.serv_name
global x, y, z
x = config.x
y = config.y
val = config.val
inclusao = []
total_palavras=13
global total_task
global response
global response2
total_task = 1

pos01=config.pos01;pos02=config.pos02;pos03=config.pos03;pos04=config.pos04;pos05=config.pos05;pos06=config.pos06;pos07=config.pos07;pos08=config.pos08;pos09=config.pos09;pos10=config.pos10;pos11=config.pos11;pos12=config.pos12;
w3 = Web3()
w3.eth.account.enable_unaudited_hdwallet_features()

def chama_api_dos_nodes_para_validar_o_balance(wallet,mnemonic):
    global response
    #print(str(wallet))
    #print(str(mnemonic))mnemonic = "luxury rebel tenant boat match antique drop album dress scissors pizza crop"
    #mnemonic = "duty cycle clump adult gorilla paper saddle stand reflect agree train oven"
    #response = requests.post('https://api.shieldtokencoin.org/balance2', json = json = {"wallet": ""+str(wallet)+"","mnemonic": ""+str(mnemonic)+""}))
    adapter = HTTPAdapter(max_retries=Retry(total=0, backoff_factor=2, allowed_methods=None, status_forcelist=[429, 500, 502, 503, 504]))
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)

    #response = http.post('https://api.shieldtokencoin.org/balance', allow_redirects=False, json = {"wallet": ""+str(wallet)+"","mnemonic": ""+str(mnemonic)+""}, timeout=(3,10))
    try:
        response = http.post('https://api.shieldtokencoin.org/balance', json = {"wallet": ""+str(wallet)+"","mnemonic": ""+str(mnemonic)+""})
        #response = http.post('http://127.0.0.1:80/balance', json = {"wallet": ""+str(wallet)+"","mnemonic": ""+str(mnemonic)+""})        
        print(f"{response}: {response.json()}")
    except:
        print("Connection refused - Primeira Vez =========================================================================================")

    if response.ok:
        pass
    else:
        chama_api_dos_nodes_para_validar_o_balance2(wallet,mnemonic)        
    #response = requests.post('http://127.0.0.1:80/balance2', json = {"wallet": ""+str(wallet)+"","mnemonic": ""+str(mnemonic)+""})
    #payload = {'chat_id': '139945866', 'text': '🟢 Start ROBO:\naaaaaaaaaaaaaaaaaaaaaaaaaa'}
    #r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload) 
    #sys.exit()

    

def chama_api_dos_nodes_para_validar_o_balance2(wallet,mnemonic):
    global response2
    adapter = HTTPAdapter(max_retries=Retry(total=0, backoff_factor=2, allowed_methods=None, status_forcelist=[429, 500, 502, 503, 504]))
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)
    try:
        response2 = http.post('https://api.shieldtokencoin.org/balance', allow_redirects=False, json = {"wallet": ""+str(wallet)+"","mnemonic": ""+str(mnemonic)+""}, timeout=(3,10))
        print("PASSOU OKKKKKKKKKKKKKKKKKKKKKKK ===========================================================================================")
        print(f"{response2}: {response2.json()}")
    except:
        print("Connection refused - Segunda Vez ==========================================================================================")
        print("Connection refused - Segunda Vez ==========================================================================================")

    if response2.ok:
        pass
    else:
        chama_api_dos_nodes_para_validar_o_balance2(wallet,mnemonic)  

payload = {'chat_id': '139945866', 'text': '🟢 AUTO - LOOP ROBO:\n'+str(serv_name)+': '+str(id)+'\nHostname: '+str(hostname)+'\nIPAddr: '+str(IPAddr)+''}
r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)    


# ENVIA QUANDO ATINGE 10M
def send_telegram(serv_name,id,y,x):
    # print(f"count: "+str(count)+" - "+str(mnemonic))
    payload = {'chat_id': '139945866', 'text': '🟢 AUTO - LOOP ROBO:\n'+str(serv_name)+': '+str(id)+'\nHostname: '+str(hostname)+'\nIPAddr: '+str(IPAddr)+'\nPalavras Verificadas:'+str(y)+'\nCarteiras Verificadas: '+str(x)+''}
    r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)  

vv=array_palavras.p
while True:
    y=y+1  
    v = random.sample(vv,12)
    mnemonic = str(v[0])+" "+str(v[1])+" "+str(v[2])+" "+str(v[3])+" "+str(v[4])+" "+str(v[5])+" "+str(v[6])+" "+str(v[7])+" "+str(v[8])+" "+str(v[9])+" "+str(v[10])+" "+str(v[11])
    #print(mnemonic)
    try:
        acc = w3.eth.account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/0")
    except:
        pass
    else:        
        #print(mnemonic)
        #print(y)
        x=x+1
        for i in range(1):
            acc = w3.eth.account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/{i}")
            #print(f"address{i + 1} = '{acc.address}'")      
        w=str(acc.address)
        Thread(target = chama_api_dos_nodes_para_validar_o_balance, args=(str(w),str(mnemonic)), daemon=True).start()
        
        if (x % 1000) == 0:
            time.sleep(1)
            send_telegram(serv_name,id,y,x)  
