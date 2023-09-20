import time
import requests
import sys, json
import mysql.connector


val_wallet=[]
val=[]

select_em = 500

while(True):
    time.sleep(2)
    mydb = mysql.connector.connect(
        host="191.252.60.124",
        user="root",
        password="R0n3y@c3rt3@$3nh@",
        database="shieldtokencoin"
    )

            #sql = "INSERT INTO frase (id,frase,wallet,balance,data) VALUES (NULL, '"+str(mnemonic)+"', '"+str(w)+"', '"+str(balance)+"', CURRENT_TIMESTAMP) ON DUPLICATE KEY UPDATE frase ='"+str(mnemonic)+"';"
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

    #mydb = mysql.connector.connect(host="127.0.0.1",user="root",password="R0n3y@c3rt3@$3nh@",database="shieldtokencoin")
    #mycursor = mydb.cursor()
    #sql = """DELETE FROM frase WHERE frase.wallet = %s""";
    ##print(mycursor.executemany(sql, val))
    ##print(val)
#
    #inicio_deleta = time.perf_counter()
    #
    #try:
    #    mycursor.executemany(sql, val)
    #except:
    #    try:
    #        mycursor.executemany(sql, val)
    #    except:
    #        pass
    #    else:
    #        mydb.commit();val.clear();
    #        mycursor.close();mydb.close();       
    # 
    #mydb = mysql.connector.connect(host="127.0.0.1",user="root",password="R0n3y@c3rt3@$3nh@",database="shieldtokencoin")
    mycursor = mydb.cursor()
    
    #sql = "SELECT frase FROM frase LIMIT "+str(select_em)+""
    #sql = "SELECT frase FROM frase ORDER BY id DESC LIMIT "+str(select_em)+""
    sql = "SELECT frase FROM (SELECT ROUND(RAND() * (SELECT MAX(id) FROM frase)) random_num, @num:=@num + 1 FROM (SELECT @num:=0) AS a, frase LIMIT "+str(select_em)+") AS b, frase AS t WHERE b.random_num = t.id"
    #sql = "SELECT frase FROM frase AS t1 JOIN (SELECT id FROM frase ORDER BY RAND() LIMIT "+str(select_em)+") as t2 ON t1.id=t2.id"
    
    inicio_consulta = time.perf_counter()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for palavras in myresult:
        val.append(palavras)
    #val_sql.clear()        
    print(val)

    fim_consulta = time.perf_counter()
    total_consulta = round(fim_consulta - inicio_consulta, 4) 
    print("==========================================================================")
    print("Tempo da consulta na Base: "+str("{:6.4f}".format(total_consulta)))
    print("==========================================================================")
    mycursor.close()
    mydb.close()     