import jsonify
import mysql.connector
import time
import uuid
idx=uuid.uuid4()

def check_server_mysql():    
    mydb = mysql.connector.connect(host="191.252.60.124",user="root",password="R0n3y@c3rt3@$3nh@",database="shieldtokencoin")
    mycursor = mydb.cursor()
    sql = "SELECT id,uuid,nome,ip,data_criacao,data_atualizacao FROM servidor"
    mycursor.execute(sql);myresult = mycursor.fetchall();mycursor.close();mydb.close();
    #print(myresult)
    for x in myresult:
        id=x[0];uuid=x[1]
        nome=x[2];ip=x[3];data_criacao=x[4];data_atualizacao=x[5];
        #print(id,uuid,nome,ip,data_criacao,data_atualizacao)

def update_server_mysql():    
    mydb = mysql.connector.connect(host="191.252.60.124",user="root",password="R0n3y@c3rt3@$3nh@",database="shieldtokencoin")
    mycursor = mydb.cursor()
    sql = "INSERT INTO servidor (id, uuid, nome, ip, data_criacao, data_atualizacao) VALUES (NULL, '"+str(idx)+"', '', '', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) ON DUPLICATE KEY UPDATE uuid='"+str(idx)+"', data_atualizacao=now();"
    mycursor.execute(sql);mydb.commit();mycursor.close();mydb.close();

####################################################################################################################################################################################################################################
def get_server_job():    
    mydb = mysql.connector.connect(host="191.252.60.124",user="root",password="R0n3y@c3rt3@$3nh@",database="shieldtokencoin")
    mycursor = mydb.cursor()
    sql = "SELECT id,total_palavras,uuid,mnemonic,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,data_alteracao FROM servidor_job WHERE  uuid='"+str(idx)+"' ORDER BY data_alteracao DESC LIMIT 1;"
    mycursor.execute(sql);myresult = mycursor.fetchall();mycursor.close();mydb.close();
    #print(myresult)
    for x in myresult:
        id=x[0];uuid=x[1];total_palavras=x[2];mnemonic=x[3];
        i1=x[4];i2=x[5];i3=x[6];i4=x[7];i5=x[8];i6=x[9];i7=x[10];i8=x[11];i9=x[12];i10=x[13];i11=x[14];i12=x[15];
        p1=x[16];p2=x[17];p3=x[18];p4=x[19];p5=x[20];p6=x[21];p7=x[22];p8=x[23];p9=x[24];p10=x[25];p11=x[26];p12=x[27];
        f1=x[28];f2=x[29];f3=x[30];f4=x[31];f5=x[32];f6=x[33];f7=x[34];f8=x[35];f9=x[36];f10=x[37];f11=x[38];f12=x[39];
        data_alteracao=x[40];
        print(id,total_palavras,uuid,mnemonic,data_alteracao,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12)

def update_server_job():    
    mydb = mysql.connector.connect(host="191.252.60.124",user="root",password="R0n3y@c3rt3@$3nh@",database="shieldtokencoin")
    mycursor = mydb.cursor()
    sql = "UPDATE servidor_job SET uuid = '"+str(idx)+"', data_alteracao=now() WHERE uuid='' LIMIT 1;"
    mycursor.execute(sql);mydb.commit();mycursor.close();mydb.close();
####################################################################################################################################################################################################################################


while True:    
    inicio = time.perf_counter()
    

    check_server_mysql()
    time.sleep(2)
    update_server_mysql()

    update_server_job()
    get_server_job()
    
    fim = time.perf_counter()
    total = round(fim - inicio, 4) 
    print("==========================================================================")
    print("Tempo da exclusão na Base: "+str("{:6.4f}".format(total))+" UI:"+str(idx))
    time.sleep(20)
    