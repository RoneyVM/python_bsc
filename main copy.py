from threading import Thread
from random import *
from web3 import Web3
import procurar_wallet_step_2,time,multiprocessing
import subprocess
import requests
from requests.adapters import HTTPAdapter, Retry
import config
import sys, os, json
import requests.adapters

var1=int(sys.argv[1])
id = config.id
serv_name = config.serv_name
x = config.x
y = config.y
val = config.val
inclusao = []
total_palavras=100
global total_task
total_task = 1

pos01=var1;pos02=config.pos02;pos03=config.pos03;pos04=config.pos04;pos05=config.pos05;pos06=config.pos06;pos07=config.pos07;pos08=config.pos08;pos09=config.pos09;pos10=config.pos10;pos11=config.pos11;pos12=config.pos12;
#& C:/Users/roney/AppData/Local/Programs/Python/Python311/python.exe c:/Users/roney/Desktop/Automatizacao_Python/v5/step_1_validate.py

#payload = {'chat_id': '139945866', 'text': '🟢 Start ROBO:\n'+str(serv_name)+': '+str(id)+'\nPhrase:'+str(pos01)+'.'+str(pos02)+'.'+str(pos03)+'.'+str(pos04)+'.'+str(pos05)+'.'+str(pos06)+'.'+str(pos07)+'.'+str(pos08)+'.'+str(pos09)+'.'+str(pos10)+'.'+str(pos11)+'.'+str(pos12)+'\nExecutado: '+str(y)+''}
#r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)     

def requesti():
    response = requests.post('https://api.shieldtokencoin.org/balance', json = {"1": "luxury","2": "rebel","3": "tenant","4": "boat","5": "match","6": "antique","7": "drop","8": "album","9": "dress","10": "scissors","11": "pizza","12": "crop"})
    #payload = {'chat_id': '139945866', 'text': '🟢 Start ROBO:\naaaaaaaaaaaaaaaaaaaaaaaaaa'}
    #r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)     

def converte_numero_em_frase_e_validade_se_sequencia_eh_valida(y,pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12,var1):
    #if (y % 20) == 0:
    #PORTA = (randint(80, 100))
    aa = int(y) % 31
    PORTA = aa + 80
    #PORTA = 80

    specified_url = 'http://127.0.0.1:'+str(PORTA)+'/converte_numero_em_frase_e_validade_se_sequencia_eh_valida'
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    retry = HTTPAdapter(max_retries=retry)

    adapter = requests.adapters.HTTPAdapter(pool_connections=100000, pool_maxsize=100)

    session.mount("http://", adapter)
    session.mount("https://",adapter)
    
    try:
        response = session.post(specified_url,json = {"1": ""+str(pos01)+"","2": ""+str(pos02)+"","3": ""+str(pos03)+"","4": ""+str(pos04)+"","5": ""+str(pos05)+"","6": ""+str(pos06)+"","7": ""+str(pos07)+"","8": ""+str(pos08)+"","9": ""+str(pos09)+"","10": ""+str(pos10)+"","11": ""+str(pos11)+"","12": ""+str(pos12)+""}, timeout=30, verify=False)
    except:
        try:
            response = session.post(specified_url,json = {"1": ""+str(pos01)+"","2": ""+str(pos02)+"","3": ""+str(pos03)+"","4": ""+str(pos04)+"","5": ""+str(pos05)+"","6": ""+str(pos06)+"","7": ""+str(pos07)+"","8": ""+str(pos08)+"","9": ""+str(pos09)+"","10": ""+str(pos10)+"","11": ""+str(pos11)+"","12": ""+str(pos12)+""}, timeout=30, verify=False)
        except:
            try:
                response = session.post(specified_url,json = {"1": ""+str(pos01)+"","2": ""+str(pos02)+"","3": ""+str(pos03)+"","4": ""+str(pos04)+"","5": ""+str(pos05)+"","6": ""+str(pos06)+"","7": ""+str(pos07)+"","8": ""+str(pos08)+"","9": ""+str(pos09)+"","10": ""+str(pos10)+"","11": ""+str(pos11)+"","12": ""+str(pos12)+""}, timeout=30, verify=False)
            except:
                response = session.post(specified_url,json = {"1": ""+str(pos01)+"","2": ""+str(pos02)+"","3": ""+str(pos03)+"","4": ""+str(pos04)+"","5": ""+str(pos05)+"","6": ""+str(pos06)+"","7": ""+str(pos07)+"","8": ""+str(pos08)+"","9": ""+str(pos09)+"","10": ""+str(pos10)+"","11": ""+str(pos11)+"","12": ""+str(pos12)+""}, timeout=30, verify=False)
                #pass        


    print(str('%02.0f' % aa)+" "+str(PORTA)+" "+str(pos01)+" "+str(pos02)+" "+str(pos03)+" "+str(pos04)+" "+str(pos05)+" "+str(pos06)+" "+str(pos07)+" "+str(pos08)+" "+str(pos09)+" "+str(pos10)+" "+str(pos11)+" "+str(pos12)+" "+str(var1))
    #response = requests.post('http://127.0.0.1:'+str(PORTA)+'/converte_numero_em_frase_e_validade_se_sequencia_eh_valida', json = {"1": ""+str(pos01)+"","2": ""+str(pos02)+"","3": "tenant","4": "boat","5": "match","6": "antique","7": "drop","8": "album","9": "dress","10": "scissors","11": "pizza","12": "crop"})
    #mnemonic = str(p['1'])+" "+str(p['2'])+" "+str(p['3'])+" "+str(p['4'])+" "+str(p['5'])+" "+str(p['6'])+" "+str(p['7'])+" "+str(p['8'])+" "+str(p['9'])+" "+str(p['10'])+" "+str(p['11'])+" "+str(p['12'])
    #mnemonic = "luxury rebel tenant boat match antique drop album dress scissors pizza crop"
    #try:
    #    acc = w3.eth.account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/0")
    #except:
    #    pass
    #else:
        #total_wallet=int(total_wallet+1)
        #inicio = time.perf_counter()
    #    wallet = str(acc.address)
    #    balance = web3.eth.get_balance(wallet)
    #print("wallet "+str(wallet)+" balance "+str(balance)+" mnemonic "+str(mnemonic))
    #return jsonify({"wallet": ""+str(wallet)+"","balance": ""+str(balance)+"", "mnemonic":""+str(mnemonic)+""})

def v(y,x,pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12,var1):
    #append
    #if not procurar_wallet_step_2.inicio(str(y),str(x),str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12),str(var1)):
    #    pass
    #else:  
    #    print(str(y),str(x),str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12))
    #response = requests.post('https://api.shieldtokencoin.org/balance', json = {"1": "luxury","2": "rebel","3": "tenant","4": "boat","5": "match","6": "antique","7": "drop","8": "album","9": "dress","10": "scissors","11": "pizza","12": "crop"})
    response = requests.get("https://api.shieldtokencoin.org/palavras")
    #print(response)
    #print(response.json())
    for palavras in response.json():
        val.append(palavras)
    print(val)



while(pos12<=total_palavras):
    #print(str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12))
    y=y+1
    #if (y % 1000000) == 0:
        #print(f"count: "+str(count)+" - "+str(mnemonic))
    #    payload = {'chat_id': '139945866', 'text': '🟢 LOOP ROBO:\n'+str(serv_name)+': '+str(id)+'\nPhrase:'+str(pos01)+'.'+str(pos02)+'.'+str(pos03)+'.'+str(pos04)+'.'+str(pos05)+'.'+str(pos06)+'.'+str(pos07)+'.'+str(pos08)+'.'+str(pos09)+'.'+str(pos10)+'.'+str(pos11)+'.'+str(pos12)+'\nExecutado: '+str(y)+''}
        #r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)    
    #if (y % 1000) == 0:
    #    response = requests.post('http://191.252.60.124:5000/inclusao_palavras', json = inclusao)

        #print(response.json())
        #inclusao.clear();      
        
    pos01=pos01+10
    if (pos01 > total_palavras): pos01=var1;pos02=pos02+1
    if (pos01 == total_palavras): pos01=0;pos02=pos02+1
    if (pos02 == total_palavras): pos02=0;pos03=pos03+1    
    if (pos03 == total_palavras): pos03=0;pos04=pos04+1          
    if (pos04 == total_palavras): pos04=0;pos05=pos05+1          
    if (pos05 == total_palavras): pos05=0;pos06=pos06+1          
    if (pos06 == total_palavras): pos06=0;pos07=pos07+1          
    if (pos07 == total_palavras): pos07=0;pos08=pos08+1          
    if (pos08 == total_palavras): pos08=0;pos09=pos09+1          
    if (pos09 == total_palavras): pos09=0;pos10=pos10+1          
    if (pos10 == total_palavras): pos10=0;pos11=pos11+1          
    if (pos11 == total_palavras): pos11=0;pos12=pos12+1      
    #time.sleep(0.005)
    if (pos01 != pos02 and pos01 != pos03 and pos01 != pos04 and pos01 != pos05 and pos01 != pos06 and pos01 != pos07 and pos01 != pos08 and pos01 != pos09 and pos01 != pos10 and pos01 != pos11 and pos01 != pos12):
        if (pos02 != pos03 and pos02 != pos04 and pos02 != pos05 and pos02 != pos06 and pos02 != pos07 and pos02 != pos08 and pos02 != pos09 and pos02 != pos10 and pos02 != pos11 and pos02 != pos12):
            if (pos03 != pos04 and pos03 != pos05 and pos03 != pos06 and pos03 != pos07 and pos03 != pos08 and pos03 != pos09 and pos03 != pos10 and pos03 != pos11 and pos03 != pos12):            
                if (pos04 != pos05 and pos04 != pos06 and pos04 != pos07 and pos04 != pos08 and pos04 != pos09 and pos04 != pos10 and pos04 != pos11 and pos04 != pos12):            
                    if (pos05 != pos06 and pos05 != pos07 and pos05 != pos08 and pos05 != pos09 and pos05 != pos10 and pos05 != pos11 and pos05 != pos12):   
                        if (pos06 != pos07 and pos06 != pos08 and pos06 != pos09 and pos06 != pos10 and pos06 != pos11 and pos06 != pos12):            
                            if (pos07 != pos08 and pos07 != pos09 and pos07 != pos10 and pos07 != pos11 and pos07 != pos12):            
                                if (pos08 != pos09 and pos08 != pos10 and pos08 != pos11 and pos08 != pos12):            
                                    if (pos09 != pos10 and pos09 != pos11 and pos09 != pos12):            
                                        if (pos10 != pos11 and pos10 != pos12):            
                                            if (pos11 != pos12):    
                                                #time.sleep(0.00001)
                                                time.sleep(0.0005)
                                                #Thread(target = requesti).start()
                                                #retorno = procurar_wallet_step_2.inicio(str(y),str(x),str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12),str(var1))
                                                
                                                Thread(target = converte_numero_em_frase_e_validade_se_sequencia_eh_valida, group=None, name="name"+str(y), args=(str(y),str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12),str(var1)), kwargs={}, daemon=None).start()

                                                #http://191.252.60.124:5000/balance
                                                #{"1": "luxury","2": "rebel","3": "tenant","4": "boat","5": "match","6": "antique","7": "drop","8": "album","9": "dress","10": "scissors","11": "pizza","12": "crop"}
                                                #if not retorno:
                                                #    pass
                                                #else:                                                     
                                                #Thread(target = requesti, group=None, name="name"+str(y), args=(str(y),str(x),str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12),str(var1)), kwargs={}, daemon=None).start()
                                                #Thread(target = requesti, group=None, name="name"+str(y), args=(), kwargs={}, daemon=None).start()
                                                    #response = requests.post('http://191.252.60.124:5000/balance', json = {"1": ""+str(pos01)+"","2": ""+str(pos02)+"","3": ""+str(pos03)+"","4": ""+str(pos04)+"","5": ""+str(pos05)+"","6": ""+str(pos06)+"","7": ""+str(pos07)+"","8": ""+str(pos08)+"","9": ""+str(pos09)+"","10": ""+str(pos10)+"","11": ""+str(pos11)+"","12": ""+str(pos12)+""})
                                                    #inclusao.append(json.loads(retorno)) 
                                                #    x=x+1  
                                                 
                                                print(str(y),str(x),str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12))




