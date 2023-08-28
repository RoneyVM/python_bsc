from web3 import Web3
import sys
import array_palavras
import config, json

var1=int(sys.argv[1])
id = config.id
serv_name = config.serv_name
#mydb = config.mydb

w3 = Web3()

def inicio(cont_seq,cont_ord,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,var1):
    #print(str(p1))
    #print(str(array_palavras.p[int(p1)]))
    mnemonic = str(array_palavras.p2[int(p1)])+" "+str(array_palavras.p2[int(p2)])+" "+str(array_palavras.p2[int(p3)])+" "+str(array_palavras.p2[int(p4)])+" "+str(array_palavras.p2[int(p5)])+" "+str(array_palavras.p2[int(p6)])+" "+str(array_palavras.p2[int(p7)])+" "+str(array_palavras.p2[int(p8)])+" "+str(array_palavras.p2[int(p9)])+" "+str(array_palavras.p2[int(p10)])+" "+str(array_palavras.p2[int(p11)])+" "+str(array_palavras.p2[int(p12)])
    #print(mnemonic)
    w3.eth.account.enable_unaudited_hdwallet_features()
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
        print(cont_seq+" "+cont_ord+" "+w+" "+p1+" "+p2+" "+p3+" "+p4+" "+p5+" "+p6+" "+p7+" "+p8+" "+p9+" "+p10+" "+p11+" "+p12+" "+mnemonic)
        #teste_wallet2.inicio(str(cont_seq),str(cont_ord),str(w),str(p1),str(p2),str(p3),str(p4),str(p5),str(p6),str(p7),str(p8),str(p9),str(p10),str(p11),str(p12),str(mnemonic))
        #subprocess.Popen(["python", "C:/Users/roney/Desktop/Automatizacao_Python/v5/teste_wallet1.py", str(cont_seq),str(cont_ord),str(w),str(p1),str(p2),str(p3),str(p4),str(p5),str(p6),str(p7),str(p8),str(p9),str(p10),str(p11),str(p12),str(mnemonic)])
        #arquivo = open("c:/Users/roney/Desktop/Automatizacao_Python/v5/wallet_"+str(p1)+".txt", "a")
        #arquivo.write(cont_seq+" "+cont_ord+" "+w+" "+p1+" "+p2+" "+p3+" "+p4+" "+p5+" "+p6+" "+p7+" "+p8+" "+p9+" "+p10+" "+p11+" "+p12+" "+mnemonic+"\n")
        #arquivo = open("c:/Users/roney/Desktop/Automatizacao_Python/v5/insert_wallet"+var1+".sql", "a")
        #arquivo.write("'"+str(mnemonic)+"', '"+p1+"."+p2+"."+p3+"."+p4+"."+p5+"."+p6+"."+p7+"."+p8+"."+p9+"."+p10+"."+p11+"."+p12+"', '"+str(w)+"', '"+str(w)+"'\n")   
        #arquivo.write("'"+str(mnemonic)+"', '"+p1+"."+p2+"."+p3+"."+p4+"."+p5+"."+p6+"."+p7+"."+p8+"."+p9+"."+p10+"."+p11+"."+p12+"', '"+str(w)+"', '"+str(mnemonic)+"'\n")        
        
        #mycursor = mydb.cursor()
        #sql = "INSERT INTO frase (id,frase,seq,wallet,balance,data) VALUES (NULL, '"+str(mnemonic)+"', '"+p1+"."+p2+"."+p3+"."+p4+"."+p5+"."+p6+"."+p7+"."+p8+"."+p9+"."+p10+"."+p11+"."+p12+"', '"+str(w)+"', 'x', CURRENT_TIMESTAMP) ON DUPLICATE KEY UPDATE frase ='"+str(mnemonic)+"';"
        #try:
        #    mycursor.execute(sql)
        #except:
        #    try:
        #        mycursor.execute(sql)
        #    except:
        #        pass
        #    else:
        #        mydb.commit() 
        #else:
        #    mydb.commit() 
    #time.sleep(1)
    #print(str(p1)+" "+str(p2)+" "+str(p3)+" "+str(p4)+" "+str(p5)+" "+str(p6)+" "+str(p7)+" "+str(p8)+" "+str(p9)+" "+str(p10)+" "+str(p11)+" "+str(p12))
    #subprocess.run(["python", "C:/Users/roney/Desktop/Automatizacao_Python/v5/teste.py", str(p1),str(p2),str(p3),str(p4),str(p5),str(p6),str(p7),str(p8),str(p9),str(p10),str(p11),str(p12)],check=True)
    #os.system("python c:/Users/roney/Desktop/Automatizacao_Python/v5/teste.py 1 2 3 4 5 6 7 8 9 10 11 12")
    #subprocess.Popen(["python", "C:/Users/roney/Desktop/Automatizacao_Python/v5/teste.py", str(p1),str(p2),str(p3),str(p4),str(p5),str(p6),str(p7),str(p8),str(p9),str(p10),str(p11),str(p12)])
    #subprocess.Popen(["python", "C:/Users/roney/Desktop/Automatizacao_Python/v5/step3_valida_mnemonic.py", str(p1),str(p2),str(p3),str(p4),str(p5),str(p6),str(p7),str(p8),str(p9),str(p10),str(p11),str(p12)])
        #return ("\"{\""cont_seq"\": \""+cont_seq+"\", \""cont_ord"\": \""+cont_ord+"\", \""wallet"\": \""+w+"\", \""seq"\": \""+p1+"."+p2+"."+p3+"."+p4+"."+p5+"."+p6+"."+p7+"."+p8+"."+p9+"."+p10+"."+p11+"."+p12+"\", \""mnemonic"\": \""+mnemonic+"\"}\"")
        #return("{\"cont_seq\": \""+cont_seq+"\", \"cont_ord\": \""+cont_ord+"\", \"wallet\": \""+w+"\", \"seq\": \""+p1+"."+p2+"."+p3+"."+p4+"."+p5+"."+p6+"."+p7+"."+p8+"."+p9+"."+p10+"."+p11+"."+p12+"\", \"mnemonic\": \""+mnemonic+"\"}")
        value = {"cont_seq": ""+cont_seq+"", "cont_ord": ""+cont_ord+"", "wallet": ""+w+"", "seq": ""+p1+"."+p2+"."+p3+"."+p4+"."+p5+"."+p6+"."+p7+"."+p8+"."+p9+"."+p10+"."+p11+"."+p12+"", "mnemonic": ""+mnemonic+""}
        return json.dumps(value)
        