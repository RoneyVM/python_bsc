from web3 import Web3
import sys
import array_palavras
import config, json, time

var1=int(sys.argv[1])
id = config.id
serv_name = config.serv_name

w3 = Web3()
w3.eth.account.enable_unaudited_hdwallet_features()


def inicio(cont_seq,cont_ord,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,var1):
    #print("wwwwwwwwwwwwww",cont_seq,cont_ord,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,var1)
    ##print(str(cont_seq))
    #print(str(p1))
    #print(str(array_palavras.palavra_random[int(p1)]))
    #print(str(array_palavras.palavra_random[int(p2)]))
    #print(str(array_palavras.palavra_random[int(p3)]))
    #print(str(array_palavras.palavra_random[int(p4)]))
    #print(str(array_palavras.palavra_random[int(p5)]))
    #print(str(array_palavras.palavra_random[int(p6)]))
    #print(str(array_palavras.palavra_random[int(p7)]))
    #print(str(array_palavras.palavra_random[int(p8)]))
    #print(str(array_palavras.palavra_random[int(p9)]))
    #print(str(array_palavras.palavra_random[int(p10)]))
    #print(str(array_palavras.palavra_random[int(p11)]))
    #print(str(array_palavras.palavra_random[int(p12)]))
    mnemonic = str(array_palavras.palavra_random[int(p1)])+" "+str(array_palavras.palavra_random[int(p2)])+" "+str(array_palavras.palavra_random[int(p3)])+" "+str(array_palavras.palavra_random[int(p4)])+" "+str(array_palavras.palavra_random[int(p5)])+" "+str(array_palavras.palavra_random[int(p6)])+" "+str(array_palavras.palavra_random[int(p7)])+" "+str(array_palavras.palavra_random[int(p8)])+" "+str(array_palavras.palavra_random[int(p9)])+" "+str(array_palavras.palavra_random[int(p10)])+" "+str(array_palavras.palavra_random[int(p11)])+" "+str(array_palavras.palavra_random[int(p12)])
    #print(mnemonic)
    #mnemonic = "luxury rebel tenant boat match antique drop album dress scissors pizza crop"
    try:
        acc = w3.eth.account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/0")
    except:
        pass
        #print("Erro")
    else:
        for i in range(1):
            acc = w3.eth.account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/{i}")
            #print(f"address{i + 1} = '{acc.address}'")      
        w=str(acc.address)
        #print(cont_seq+" "+cont_ord+" "+w+" "+p1+" "+palavra_random+" "+p3+" "+p4+" "+p5+" "+p6+" "+p7+" "+p8+" "+p9+" "+p10+" "+p11+" "+p12+" "+mnemonic)
        value = {"cont_seq": ""+cont_seq+"", "cont_ord": ""+cont_ord+"", "wallet": ""+w+"", "seq": ""+p1+"."+p2+"."+p3+"."+p4+"."+p5+"."+p6+"."+p7+"."+p8+"."+p9+"."+p10+"."+p11+"."+p12+"", "mnemonic": ""+mnemonic+""}
        return json.dumps(value)
        