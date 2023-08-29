from web3 import Web3
import sys
import array_palavras
import config, json

var1=int(sys.argv[1])
id = config.id
serv_name = config.serv_name

w3 = Web3()
w3.eth.account.enable_unaudited_hdwallet_features()

def inicio(cont_seq,cont_ord,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,var1):
    #print(str(cont_seq))
    #print(str(array_palavras.p[int(p1)]))
    mnemonic = str(array_palavras.p2[int(p1)])+" "+str(array_palavras.p2[int(p2)])+" "+str(array_palavras.p2[int(p3)])+" "+str(array_palavras.p2[int(p4)])+" "+str(array_palavras.p2[int(p5)])+" "+str(array_palavras.p2[int(p6)])+" "+str(array_palavras.p2[int(p7)])+" "+str(array_palavras.p2[int(p8)])+" "+str(array_palavras.p2[int(p9)])+" "+str(array_palavras.p2[int(p10)])+" "+str(array_palavras.p2[int(p11)])+" "+str(array_palavras.p2[int(p12)])
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
        #print(cont_seq+" "+cont_ord+" "+w+" "+p1+" "+p2+" "+p3+" "+p4+" "+p5+" "+p6+" "+p7+" "+p8+" "+p9+" "+p10+" "+p11+" "+p12+" "+mnemonic)
        value = {"cont_seq": ""+cont_seq+"", "cont_ord": ""+cont_ord+"", "wallet": ""+w+"", "seq": ""+p1+"."+p2+"."+p3+"."+p4+"."+p5+"."+p6+"."+p7+"."+p8+"."+p9+"."+p10+"."+p11+"."+p12+"", "mnemonic": ""+mnemonic+""}
        return json.dumps(value)
        