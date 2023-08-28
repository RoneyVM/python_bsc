from web3 import Web3
import f_server_validadores
import sys,time,random

#####################################################
# REQUEST ------------------------------------------
#    response = requests.post('http://191.252.60.124:5000/delete_wallet', json = val_wallet)
#    print(response.json())
####################################################
# SHELL --------------------------------------------
#/f_send_telegram.py 1 2 3 4 5 6 7 8 9 10 11 12 100 x0aaaa serv1
#{"1": "luxury","2": "rebel","3": "tenant","4": "boat","5": "match","6": "antique","7": "drop","8": "album","9": "dress","10": "scissors","11": "pizza","12": "crop"}
####################################################

mnemonic=str(sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4]+" "+sys.argv[5]+" "+sys.argv[6]+" "+sys.argv[7]+" "+sys.argv[8]+" "+sys.argv[9]+" "+sys.argv[10]+" "+sys.argv[11]+" "+sys.argv[12])
print(mnemonic)
total_wallet=1
count=1
global rand
               
w3 = Web3()
rand = random.randint(0,32)
web3 = Web3(Web3.HTTPProvider(validador_step_2.bsc[int(rand)]))
w3.eth.account.enable_unaudited_hdwallet_features()

def valida_carteira(mnemonic):
    global total_wallet
    global rand
    try:
        acc = w3.eth.account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/0")
    except:
        pass
    else:
        total_wallet=int(total_wallet+1)
        inicio = time.perf_counter()
        w=str(acc.address)
        try:
            balance = web3.eth.get_balance(w)
        except:
            time.sleep(1)
            rand = random.randint(0,32) 
            try:
                balance = web3.eth.get_balance(w)
            except:      
                time.sleep(2)
                rand = random.randint(0,32) 
                try:
                    balance = web3.eth.get_balance(w)
                except:
                    time.sleep(3)
                    rand = random.randint(0,32) 
                    try:
                        balance = web3.eth.get_balance(w)
                    except:
                        time.sleep(4)
                        rand = random.randint(0,32) 
                        try:
                            balance = web3.eth.get_balance(w)
                        except:
                            time.sleep(5)
                            rand = random.randint(0,32) 
                            try:
                                balance = web3.eth.get_balance(w)
                            except:
                                time.sleep(6)
                                rand = random.randint(0,32) 
                                try:
                                    balance = web3.eth.get_balance(w)
                                except:
                                    time.sleep(300)
                                    balance = web3.eth.get_balance(w)   
        fim = time.perf_counter()
        total = round(fim - inicio, 4) 
        if balance == 0:
            print(f"count: "+str('%010.0f' % total_wallet)+"/"+str('%018.0f' % count)+" - time: "+str("{:6.4f}".format(total))+" - "+str(w)+" | "+str(balance)+" | "+str(mnemonic)+" "+str(validador_step_2.bsc[int(rand)]))     
            #val.append((str(w),),)
            #val_wallet.append({"wallet": ""+str(w)+""}) 
            
        else:
            #envia_mensagem(serv_name,mnemonic,balance,w)
            print(f"count: "+str('%010.0f' % total_wallet)+"/"+str('%018.0f' % count)+" - time: "+str("{:6.4f}".format(total))+" - "+str(w)+" | "+str(balance)+" | "+str(mnemonic)+" "+str(validador_step_2.bsc[int(rand)]))     
        if total >= 0.2:
            rand = random.randint(0,32)  

def inicio(mnemonic):
    valida_carteira(mnemonic)

inicio(mnemonic)