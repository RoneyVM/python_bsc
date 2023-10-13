#import jsonify
import mysql.connector
import time
import uuid
idx=uuid.uuid4()
import sys, json, random
global cont, total_palavras
total_palavras = 500

def limpar_tabela():
    mydb = mysql.connector.connect(host="191.252.60.124",user="root",password="R0n3y@c3rt3@$3nh@",database="shieldtokencoin")
    mycursor = mydb.cursor()
    sql = "TRUNCATE servidor"
    mycursor.execute(sql);myresult = mycursor.fetchall();mycursor.close();mydb.close();
    
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

#limpar_tabela()
#time.sleep(30)

def criar_seq():
    x=0
    
    i1=11;i2=10;i3=9;i4=8;i5=7;i6=6;i7=5;i8=4;i9=3;i10=2;i11=1;i12=0;
    p1=11;p2=10;p3=9;p4=8;p5=7;p6=6;p7=5;p8=4;p9=3;p10=2;p11=1;p12=0;
    f1=11;f2=10;f3=9;f4=8;f5=7;f6=6;f7=5;f8=4;f9=3;f10=2;f11=1;f12=0;
    pos01=11;pos02=10;pos03=9;pos04=8;pos05=7;pos06=6;pos07=5;pos08=4;pos09=3;pos10=2;pos11=1;pos12=0;

    while(f12<=total_palavras):
        #print("Count: "+str('%08.0f' % int(y))+" | "+str(pos01),str(pos02),str(pos03),str(pos04),str(pos05),str(pos06),str(pos07),str(pos08),str(pos09),str(pos10),str(pos11),str(pos12))
        x=x+1
        f1=f1+1
        if (f1 > total_palavras): f1=0;f2=f2+1
        if (f1 == total_palavras): f1=0;f2=f2+1
        if (f2 == total_palavras): f2=0;f3=f3+1    
        if (f3 == total_palavras): f3=0;f4=f4+1          
        if (f4 == total_palavras): f4=0;f5=f5+1          
        if (f5 == total_palavras): f5=0;f6=f6+1          
        if (f6 == total_palavras): f6=0;f7=f7+1          
        if (f7 == total_palavras): f7=0;f8=f8+1          
        if (f8 == total_palavras): f8=0;f9=f9+1          
        if (f9 == total_palavras): f9=0;f10=f10+1          
        if (f10 == total_palavras): f10=0;f11=f11+1          
        if (f11 == total_palavras): f11=0;f12=f12+1      

        if (f1 != f2 and f1 != f3 and f1 != f4 and f1 != f5 and f1 != f6 and f1 != f7 and f1 != f8 and f1 != f9 and f1 != f10 and f1 != f11 and f1 != f12):
            if (f2 != f3 and f2 != f4 and f2 != f5 and f2 != f6 and f2 != f7 and f2 != f8 and f2 != f9 and f2 != f10 and f2 != f11 and f2 != f12):
                if (f3 != f4 and f3 != f5 and f3 != f6 and f3 != f7 and f3 != f8 and f3 != f9 and f3 != f10 and f3 != f11 and f3 != f12):            
                    if (f4 != f5 and f4 != f6 and f4 != f7 and f4 != f8 and f4 != f9 and f4 != f10 and f4 != f11 and f4 != f12):            
                        if (f5 != f6 and f5 != f7 and f5 != f8 and f5 != f9 and f5 != f10 and f5 != f11 and f5 != f12):   
                            if (f6 != f7 and f6 != f8 and f6 != f9 and f6 != f10 and f6 != f11 and f6 != f12):            
                                if (f7 != f8 and f7 != f9 and f7 != f10 and f7 != f11 and f7 != f12):            
                                    if (f8 != f9 and f8 != f10 and f8 != f11 and f8 != f12):            
                                        if (f9 != f10 and f9 != f11 and f9 != f12):            
                                            if (f10 != f11 and f10 != f12):            
                                                if (f11 != f12):    
                                                    time.sleep(0.000000001)
                                                    x=x+1
                                                    #time.sleep(1)
                                                    
                                                    if (x % 1000000) == 0:
                                                        #print("INICIO: "+str('%020.0f' % int(x))+"."+str('%04.0f' % int(i1))+"."+str('%04.0f' % int(i2))+"."+str('%04.0f' % int(i3))+"."+str('%04.0f' % int(i4))+"."+str('%04.0f' % int(i5))+"."+str('%04.0f' % int(i6))+"."+str('%04.0f' % int(i7))+"."+str('%04.0f' % int(i8))+"."+str('%04.0f' % int(i9))+"."+str('%04.0f' % int(i10))+"."+str('%04.0f' % int(i11))+"."+str('%04.0f' % int(i12)))   
                                                        #print("FIM   : "+str('%020.0f' % int(x))+"."+str('%04.0f' % int(f1))+"."+str('%04.0f' % int(f2))+"."+str('%04.0f' % int(f3))+"."+str('%04.0f' % int(f4))+"."+str('%04.0f' % int(f5))+"."+str('%04.0f' % int(f6))+"."+str('%04.0f' % int(f7))+"."+str('%04.0f' % int(f8))+"."+str('%04.0f' % int(f9))+"."+str('%04.0f' % int(f10))+"."+str('%04.0f' % int(f11))+"."+str('%04.0f' % int(f12)))    
                                                        print("INICIO: "+str('%020.0f' % int(x))+" "+str(i1)+"."+str(i2)+"."+str(i3)+"."+str(i4)+"."+str(i5)+"."+str(i6)+"."+str(i7)+"."+str(i8)+"."+str(i9)+"."+str(i10)+"."+str(i11)+"."+str(i12))   
                                                        print("FIM   : "+str('%020.0f' % int(x))+" "+str(f1)+"."+str(f2)+"."+str(f3)+"."+str(f4)+"."+str(f5)+"."+str(f6)+"."+str(f7)+"."+str(f8)+"."+str(f9)+"."+str(f10)+"."+str(f11)+"."+str(f12))                          
                                                        print("")

                                                        mydb = mysql.connector.connect(host="191.252.60.124",user="root",password="R0n3y@c3rt3@$3nh@",database="shieldtokencoin")
                                                        mycursor = mydb.cursor()
                                                        sql = "INSERT INTO servidor_job (id, total_palavras, uuid, mnemonic, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, data_alteracao) VALUES (NULL, 200, '', '', "+str(i1)+", "+str(i2)+", "+str(i3)+", "+str(i4)+", "+str(i5)+", "+str(i6)+", "+str(i7)+", "+str(i8)+", "+str(i9)+", "+str(i10)+", "+str(i11)+", "+str(i12)+", "+str(i1)+", "+str(i2)+", "+str(i3)+", "+str(i4)+", "+str(i5)+", "+str(i6)+", "+str(i7)+", "+str(i8)+", "+str(i9)+", "+str(i10)+", "+str(i11)+", "+str(i12)+", "+str(f1)+", "+str(f2)+", "+str(f3)+", "+str(f4)+", "+str(f5)+", "+str(f6)+", "+str(f7)+", "+str(f8)+", "+str(f9)+", "+str(f10)+", "+str(f11)+", "+str(f12)+", now());"
                                                        mycursor.execute(sql);mydb.commit();mycursor.close();mydb.close();


                                                        i1=f1;i2=f2;i3=f3;i4=f4;i5=f5;i6=f6;i7=f7;i8=f8;i9=f9;i10=f10;i11=f11;i12=f12;





criar_seq()

#INSERT INTO servidor_job (id, total_palavras, uuid, mnemonic, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, data_alteracao) VALUES
#(1, 15, '', '\'1\',\'2\',\'3\',\'4\',\'5\',\'6\',\'7\',\'8\',\'9\',\'10\',\'11\',\'12\',\'13\',\'14\',\'15\'', 
# 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 
# 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 
# 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 
# now())

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
    